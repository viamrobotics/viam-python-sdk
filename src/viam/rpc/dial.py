import ctypes
import pathlib
import re
import socket
import ssl
import sys
import uuid
import warnings
from dataclasses import dataclass
from typing import Callable, Literal, Optional, Tuple, Type, Union

from grpclib.client import Channel, Stream
from grpclib.const import Cardinality
from grpclib.metadata import Deadline, _MetadataLike
from grpclib.protocol import H2Protocol
from grpclib.stream import _RecvType, _SendType
from typing_extensions import Self

from viam import logging
from viam.errors import InsecureConnectionError, ViamError
from viam.proto.rpc.auth import AuthenticateRequest, AuthServiceStub
from viam.proto.rpc.auth import Credentials as PBCredentials
from viam.utils import to_thread

LOGGER = logging.getLogger(__name__)


@dataclass
class Credentials:
    """Credentials to connect to the robot and the Viam app."""

    type: Union[Literal["robot-location-secret"], Literal["robot-secret"], Literal["api-key"]]
    """The type of credential
    """

    payload: str
    """The credential
    """


class DialOptions:
    disable_webrtc: bool
    """Bypass Web RTC and connect directly to the robot.
    """

    auth_entity: Optional[str]
    """The URL to authenticate against. Should be used if the address passed in and FQDN of the server do not match.
    """

    credentials: Optional[Credentials]
    """Credentials for connecting to the robot
    """

    insecure: bool = False
    """Determine if the RPC connection is TLS based. Must be provided to
    establish an insecure connection. Otherwise, a TLS based connection
    will be assumed."""

    allow_insecure_downgrade: bool = False
    """Allow the RPC connection to be downgraded to an insecure connection
    if detected. This is only used when credentials are not present."""

    allow_insecure_with_creds_downgrade: bool = False
    """Allow the RPC connection to be downgraded to an insecure connection
    if detected, even with credentials present. This is generally
    unsafe to use, but can be requested."""

    max_reconnect_attempts: int = 3
    """Max number of times the client attempts to reconnect when connection is lost"""

    timeout: float = 20
    """Number of seconds before the dial connection times out
    Set to 20sec to match _defaultOfferDeadline in goutils/rpc/wrtc_call_queue.go"""

    def __init__(
        self,
        *,
        disable_webrtc: bool = False,
        auth_entity: Optional[str] = None,
        credentials: Optional[Credentials] = None,
        insecure: bool = False,
        allow_insecure_downgrade: bool = False,
        allow_insecure_with_creds_downgrade: bool = False,
        max_reconnect_attempts: int = 3,
        timeout: float = 20,
    ) -> None:
        self.disable_webrtc = disable_webrtc
        self.auth_entity = auth_entity
        self.credentials = credentials
        self.insecure = insecure
        self.allow_insecure_downgrade = allow_insecure_downgrade
        self.allow_insecure_with_creds_downgrade = allow_insecure_with_creds_downgrade
        self.max_reconnect_attempts = max_reconnect_attempts
        self.timeout = timeout

    @classmethod
    def with_api_key(cls, api_key: str, api_key_id: str) -> Self:
        """Create DialOptions with an API key for credentials and default values for other arguments.

        Args:
            api_key (str): your API key
            api_key_id (str): your API key ID. Must be a valid UUID

        Raises:
            ValueError: Raised if the api_key_id is not a valid UUID

        Returns:
            Self: the DialOptions
        """
        try:
            uuid.UUID(api_key_id)
        except ValueError:
            raise ValueError(f"{api_key_id} is not a valid UUID")

        credentials = Credentials(type="api-key", payload=api_key)
        return cls(credentials=credentials, auth_entity=api_key_id)


def _host_port_from_url(url) -> Tuple[Optional[str], Optional[int]]:
    query = "(?:.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*"
    match = re.search(query, url)

    if not match:
        return (None, None)

    host = match.group("host")
    try:
        port = int(match.group("port"))
    except ValueError:
        port = None
    return (host, port)


async def _get_access_token(channel: Channel, address: str, opts: DialOptions) -> str:
    entity = opts.auth_entity if opts.auth_entity else re.sub(r"^(.*:\/\/)/", "", address)
    creds = PBCredentials(
        type=opts.credentials.type if opts.credentials else "", payload=opts.credentials.payload if opts.credentials else ""
    )
    request = AuthenticateRequest(entity=entity, credentials=creds)

    auth_service = AuthServiceStub(channel=channel)
    response = await auth_service.Authenticate(request)
    return response.access_token


class AuthenticatedChannel(Channel):
    _metadata: _MetadataLike

    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        *,
        ssl: Union[None, bool, ssl.SSLContext] = None,
        server_hostname: Optional[str] = None,
    ):
        super().__init__(host, port, ssl=ssl)
        self._server_hostname = server_hostname

    async def _create_connection(self) -> H2Protocol:
        _, protocol = await self._loop.create_connection(
            self._protocol_factory,
            self._host,
            self._port,
            ssl=self._ssl,
            server_hostname=self._server_hostname,
        )
        return protocol

    def request(
        self,
        name: str,
        cardinality: Cardinality,
        request_type: Type[_SendType],
        reply_type: Type[_RecvType],
        *,
        timeout: Optional[float] = None,
        deadline: Optional[Deadline] = None,
        metadata: Optional[_MetadataLike] = None,
    ) -> Stream[_SendType, _RecvType]:
        if not metadata and hasattr(self, "_metadata"):
            metadata = self._metadata
        return super().request(name, cardinality, request_type, reply_type, timeout=timeout, deadline=deadline, metadata=metadata)


@dataclass
class ViamChannel:
    channel: Channel
    release: Callable[[], None]
    _closed: bool = False

    def close(self):
        if not self._closed:
            try:
                self.channel.close()
            except RuntimeError as e:
                # ignore event loop is closed errors - robot is getting shutdown
                if len(e.args) > 0 and e.args[0] == "Event loop is closed":
                    LOGGER.debug("ViamChannel might not have shut down cleanly - Event loop was closed")
                    return
                raise
            finally:
                self.release()
                self._closed = True

    def __del__(self):
        self.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.close()


class _Runtime:
    _lib: ctypes.CDLL
    _ptr: ctypes.c_void_p

    def __init__(self) -> None:
        LOGGER.debug("Creating new viam-rust-utils runtime")
        libname = pathlib.Path(__file__).parent.absolute() / f"libviam_rust_utils.{'dylib' if sys.platform == 'darwin' else 'so'}"
        self._lib = ctypes.CDLL(libname.__str__())
        self._lib.init_rust_runtime.argtypes = ()
        self._lib.init_rust_runtime.restype = ctypes.c_void_p

        self._lib.dial.argtypes = (
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_bool,
            ctypes.c_float,
            ctypes.c_void_p,
        )
        self._lib.dial.restype = ctypes.c_void_p

        self._lib.free_rust_runtime.argtypes = (ctypes.c_void_p,)
        self._lib.free_rust_runtime.restype = None

        self._lib.free_string.argtypes = (ctypes.c_void_p,)
        self._lib.free_string.restype = None

        self._ptr = self._lib.init_rust_runtime()

    async def dial(self, address: str, options: DialOptions) -> Tuple[Optional[str], ctypes.c_void_p]:
        type = options.credentials.type if options.credentials else ""
        payload = options.credentials.payload if options.credentials else ""
        insecure = (
            options.insecure
            or options.allow_insecure_with_creds_downgrade
            or (not type and not payload and options.allow_insecure_downgrade)
        )

        LOGGER.debug(f"Dialing {address} using viam-rust-utils library")
        path_ptr = await to_thread(
            self._lib.dial,
            address.encode("utf-8"),
            options.auth_entity.encode("utf-8") if options.auth_entity else None,
            type.encode("utf-8") if type else None,
            payload.encode("utf-8") if payload else None,
            insecure,
            ctypes.c_float(options.timeout),
            self._ptr,
        )
        path = ctypes.cast(path_ptr, ctypes.c_char_p).value
        path = path.decode("utf-8") if path else ""
        return (path, path_ptr)

    def release(self):
        LOGGER.debug("Freeing viam-rust-utils runtime")
        self._lib.free_rust_runtime(self._ptr)

    def free_str(self, ptr: ctypes.c_void_p):
        LOGGER.debug("Freeing socket string")
        self._lib.free_string(ptr)


async def dial(address: str, options: Optional[DialOptions] = None) -> ViamChannel:
    opts = options if options else DialOptions()
    if opts.disable_webrtc:
        channel = await _dial_direct(address, options)
        return ViamChannel(channel, lambda: None)
    runtime = _Runtime()
    path, path_ptr = await runtime.dial(address, opts)
    if path:
        LOGGER.info(f"Connecting to socket: {path}")
        chan = Channel(path=path, ssl=None)

        def release():
            runtime.free_str(path_ptr)
            runtime.release()

        channel = ViamChannel(chan, release)
        return channel

    runtime.release()
    raise ViamError(f"Unable to establish a connection to {address}")


async def _dial_direct(address: str, options: Optional[DialOptions] = None) -> Channel:
    opts = options if options else DialOptions()
    insecure = opts.insecure

    if pathlib.Path(address).is_socket():
        return Channel(path=address)

    host, port = _host_port_from_url(address)
    if not port:
        port = 80 if insecure else 443
    server_hostname = host

    if insecure:
        ctx = None
    else:
        is_local_host = host is not None and (host.startswith("localhost") or host.startswith("0.0.0.0") or host.startswith("127."))
        if is_local_host:
            ctx = ssl._create_unverified_context(purpose=ssl.Purpose.SERVER_AUTH)
        else:
            ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        ctx.set_ciphers("ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20")
        ctx.set_alpn_protocols(["h2"])

        if (
            options is not None
            and options.auth_entity
            and host != options.auth_entity
            and options.credentials is not None
            and options.credentials.type != "api-key"
        ):
            server_hostname = options.auth_entity

        # Test if downgrade is required.
        downgrade = False
        with socket.create_connection((host, port), timeout=opts.timeout) as sock:
            try:
                with ctx.wrap_socket(sock, server_hostname=server_hostname) as ssock:
                    _ = ssock.version()
            except ssl.SSLError as e:
                if e.reason != "WRONG_VERSION_NUMBER":
                    raise e
                downgrade = True

        if downgrade:
            if opts.credentials:
                if not opts.allow_insecure_with_creds_downgrade:
                    raise InsecureConnectionError(address, authenticated=True)
            elif not opts.allow_insecure_downgrade:
                raise InsecureConnectionError(address)
            ctx = None

    if opts.credentials:
        channel = AuthenticatedChannel(host, port, ssl=ctx, server_hostname=server_hostname)
        access_token = await _get_access_token(channel, address, opts)
        metadata = {"authorization": f"Bearer {access_token}"}
        channel._metadata = metadata
    else:
        channel = Channel(host, port, ssl=ctx)

    return channel


async def dial_direct(address: str, options: Optional[DialOptions] = None) -> Channel:
    warnings.warn("dial_direct is deprecated. Use rpc.dial.dial instead.", DeprecationWarning, stacklevel=2)
    return await _dial_direct(address, options)


async def _dial_app(app_url: str) -> Channel:
    return await _dial_direct(app_url)

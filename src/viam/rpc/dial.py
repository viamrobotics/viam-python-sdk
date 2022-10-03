import ctypes
import pathlib
import re
import socket
import ssl
import sys
import warnings
from dataclasses import dataclass
from typing import Callable, Literal, Optional, Tuple, Type

from grpclib.client import Channel, Stream
from grpclib.const import Cardinality
from grpclib.metadata import Deadline, _MetadataLike
from grpclib.stream import _RecvType, _SendType

from viam import logging
from viam.errors import InsecureConnectionError, ViamError
from viam.proto.rpc.auth import AuthenticateRequest, AuthServiceStub
from viam.proto.rpc.auth import Credentials as PBCredentials

LOGGER = logging.getLogger(__name__)


@dataclass
class Credentials:
    """Credentials to connect to the robot.

    Currently only supports robot location secret.
    """

    type: Literal["robot-location-secret"]
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
    """The URL to authenticate against
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

    def __init__(
        self,
        disable_webrtc: bool = False,
        auth_entity: Optional[str] = None,
        credentials: Optional[Credentials] = None,
        insecure: bool = False,
        allow_insecure_downgrade: bool = False,
        allow_insecure_with_creds_downgrade: bool = False,
    ) -> None:
        self.disable_webrtc = disable_webrtc
        self.auth_entity = auth_entity
        self.credentials = credentials
        self.insecure = insecure
        self.allow_insecure_downgrade = allow_insecure_downgrade
        self.allow_insecure_with_creds_downgrade = allow_insecure_with_creds_downgrade


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
            self.channel.close()
            self.release()
            self._closed = True

    def __del__(self):
        self.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.close()


async def dial(address: str, options: Optional[DialOptions] = None) -> ViamChannel:
    opts = options if options else DialOptions()
    if opts.disable_webrtc:
        channel = await _dial_direct(address, options)
        return ViamChannel(channel, lambda: None)

    creds = opts.credentials.payload if opts.credentials else ""
    insecure = opts.insecure or opts.allow_insecure_with_creds_downgrade or (not creds and opts.allow_insecure_downgrade)

    libname = pathlib.Path(__file__).parent.absolute() / f"libviam.{'dylib' if sys.platform == 'darwin' else 'so'}"
    c_lib = ctypes.CDLL(libname.__str__())
    c_lib.init_rust_runtime.argtypes = ()
    c_lib.init_rust_runtime.restype = ctypes.c_void_p

    c_lib.dial.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool, ctypes.c_void_p)
    c_lib.dial.restype = ctypes.c_void_p

    c_lib.free_rust_runtime.argtypes = (ctypes.c_void_p,)
    c_lib.free_rust_runtime.restype = None

    c_lib.free_string.argtypes = (ctypes.c_void_p,)
    c_lib.free_string.restype = None

    ptr = c_lib.init_rust_runtime()

    path_ptr = c_lib.dial(
        address.encode("utf-8"),
        creds.encode("utf-8") if creds else None,
        insecure,
        ptr,
    )
    path = ctypes.cast(path_ptr, ctypes.c_char_p).value

    if path:
        LOGGER.info(f"Connecting to socket: {path}")
        chan = Channel(path=path.decode("utf-8"), ssl=None)

        def release():
            c_lib.free_string(path_ptr)
            c_lib.free_rust_runtime(ptr)

        channel = ViamChannel(chan, release)
        return channel

    c_lib.free_rust_runtime(ptr)
    raise ViamError(f"Unable to establish a connection to {address}")


async def _dial_direct(address: str, options: Optional[DialOptions] = None) -> Channel:
    opts = options if options else DialOptions()
    insecure = opts.insecure

    host, port = _host_port_from_url(address)
    if not port:
        port = 80 if insecure else 443

    if insecure:
        ctx = None
    else:
        ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        ctx.set_ciphers("ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20")
        ctx.set_alpn_protocols(["h2"])

        # Test if downgrade is required.
        downgrade = False
        with socket.create_connection((host, port)) as sock:
            try:
                with ctx.wrap_socket(sock, server_hostname=host) as ssock:
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
        channel = AuthenticatedChannel(host, port, ssl=ctx)
        access_token = await _get_access_token(channel, address, opts)
        metadata = {"authorization": f"Bearer {access_token}"}
        channel._metadata = metadata
    else:
        channel = Channel(host, port, ssl=ctx)

    return channel


async def dial_direct(address: str, options: Optional[DialOptions] = None) -> Channel:
    warnings.warn("dial_direct is deprecated. Use rpc.dial.dial instead.", DeprecationWarning, stacklevel=2)
    return await _dial_direct(address, options)

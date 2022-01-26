import re
import socket
import ssl
from typing import Optional, Tuple, Type
from grpclib.client import Channel, Stream
from grpclib.const import Cardinality
from grpclib.metadata import _MetadataLike, Deadline
from grpclib.stream import _RecvType, _SendType

from ..gen.proto.rpc.v1.auth_pb2 import AuthenticateRequest
from ..gen.proto.rpc.v1.auth_pb2 import Credentials as PBCredentials
from ..gen.proto.rpc.v1.auth_grpc import AuthServiceStub


class RTCConfiguration:
    pass


class DialWebRTCOptions:
    disable_tricle_ice: bool
    rtc_config: RTCConfiguration


class Credentials:
    type: str
    payload: str

    def __init__(self, type: str, payload: str) -> None:
        self.type = type
        self.payload = payload


class DialOptions:
    auth_entity: str | None
    credentials: Credentials | None
    webrtc_options: DialWebRTCOptions | None
    external_auth_address: str | None

    #: Determine if the RPC connection is TLS based. Must be provided to
    #: establish an insecure connection. Otherwise, a TLS based connection
    #: will be assumed.
    insecure: bool

    #: Allow the RPC connection to be downgraded to an insecure connection
    #: if detected. This is only used when credentials are not present.
    allow_insecure_downgrade: bool

    #: Allow the RPC connection to be downgraded to an insecure connection
    #: if detected, even with credentials present. This is generally
    #: unsafe to use, but can be requested.
    allow_insecure_with_creds_downgrade: bool

    def __init__(
        self,
        auth_entity: str | None = None,
        credentials: Credentials | None = None,
        insecure: bool = False,
        allow_insecure_downgrade: bool = False,
        allow_insecure_with_creds_downgrade=False
    ) -> None:
        self.auth_entity = auth_entity
        self.credentials = credentials
        self.insecure = insecure
        self.allow_insecure_downgrade = allow_insecure_downgrade
        self.allow_insecure_with_creds_downgrade = allow_insecure_with_creds_downgrade  # noqa: E501


def _host_port_from_url(url) -> Tuple[str | None, int | None]:
    query = '(?:.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
    match = re.search(query, url)

    if not match:
        return (None, None)

    host = match.group('host')
    try:
        port = int(match.group('port'))
    except ValueError:
        port = None
    return (host, port)


async def _get_access_token(
    channel: Channel,
    address: str,
    opts: DialOptions
) -> str:
    entity = opts.auth_entity if opts.auth_entity else re.sub(
        r'^(.*:\/\/)/', '', address)
    creds = PBCredentials(
        type=opts.credentials.type if opts.credentials else "",
        payload=opts.credentials.payload if opts.credentials else ""
    )
    request = AuthenticateRequest(
        entity=entity,
        credentials=creds
    )

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
        metadata: Optional[_MetadataLike] = None
    ) -> Stream[_SendType, _RecvType]:
        if not metadata and hasattr(self, '_metadata'):
            metadata = self._metadata
        return super().request(
            name,
            cardinality,
            request_type,
            reply_type,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata
        )


async def dial_direct(
    address: str,
    options: DialOptions = None
) -> Channel:

    insecure = options.insecure if options else False

    host, port = _host_port_from_url(address)
    if not port:
        port = 80 if insecure else 443

    if insecure:
        return Channel(host, port)

    downgrade = False
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    if (
        options
        and (
            options.allow_insecure_downgrade
            or options.allow_insecure_with_creds_downgrade
        )
    ):
        # Test if downgrade is required.
        # Only needed if downgrade is available in options
        with socket.create_connection((host, port)) as sock:
            try:
                with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                    _ = ssock.version()
            except ssl.SSLError as e:
                if e.reason != 'WRONG_VERSION_NUMBER':
                    raise e
                if options.credentials:
                    if options.allow_insecure_with_creds_downgrade:
                        downgrade = True
                elif options.allow_insecure_downgrade:
                    downgrade = True

    if downgrade:
        ctx = None

    if options and options.credentials:
        channel = AuthenticatedChannel(host, port, ssl=ctx)
        access_token = await _get_access_token(channel, address, options)
        metadata = {"authorization": f'Bearer {access_token}'}
        channel._metadata = metadata
    else:
        channel = Channel(host, port, ssl=ctx)

    return channel

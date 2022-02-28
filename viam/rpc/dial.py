from dataclasses import dataclass
import re
import socket
import ssl
from typing import Optional, Tuple, Type
from grpclib.client import Channel, Stream
from grpclib.const import Cardinality
from grpclib.metadata import _MetadataLike, Deadline
from grpclib.stream import _RecvType, _SendType

from viam.proto.rpc.auth import (
    AuthenticateRequest,
    AuthServiceStub,
    Credentials as PBCredentials
)
from viam.errors import InsecureConnectionError


class RTCConfiguration:
    pass


@dataclass
class DialWebRTCOptions:
    disable_tricle_ice: bool
    rtc_config: RTCConfiguration


@dataclass
class Credentials:
    type: str
    payload: str


class DialOptions:
    auth_entity: Optional[str]
    credentials: Optional[Credentials]
    webrtc_options: Optional[DialWebRTCOptions]
    external_auth_address: Optional[str]

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
        auth_entity: Optional[str] = None,
        credentials: Optional[Credentials] = None,
        insecure: bool = False,
        allow_insecure_downgrade: bool = False,
        allow_insecure_with_creds_downgrade=False
    ) -> None:
        self.auth_entity = auth_entity
        self.credentials = credentials
        self.insecure = insecure
        self.allow_insecure_downgrade = allow_insecure_downgrade
        self.allow_insecure_with_creds_downgrade = allow_insecure_with_creds_downgrade  # noqa: E501


def _host_port_from_url(url) -> Tuple[Optional[str], Optional[int]]:
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

    opts = options if options else DialOptions()
    insecure = opts.insecure

    host, port = _host_port_from_url(address)
    if not port:
        port = 80 if insecure else 443

    if insecure:
        ctx = None
    else:
        ctx = ssl.create_default_context(
            purpose=ssl.Purpose.SERVER_AUTH
        )
        ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        ctx.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20')
        ctx.set_alpn_protocols(['h2'])

        # Test if downgrade is required.
        downgrade = False
        with socket.create_connection((host, port)) as sock:
            try:
                with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                    _ = ssock.version()
            except ssl.SSLError as e:
                if e.reason != 'WRONG_VERSION_NUMBER':
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
        metadata = {"authorization": f'Bearer {access_token}'}
        channel._metadata = metadata
    else:
        channel = Channel(host, port, ssl=ctx)

    return channel

import re
from ssl import SSLContext
import ssl
from typing import Optional, Tuple, Type
from grpclib.client import Channel, Stream
from grpclib.const import Cardinality
from grpclib.metadata import _MetadataLike, Deadline
from grpclib.stream import _RecvType, _SendType

from gen.proto.rpc.v1.auth_pb2 import AuthenticateRequest
from gen.proto.rpc.v1.auth_pb2 import Credentials as PBCredentials
from gen.proto.rpc.v1.auth_grpc import AuthServiceStub


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

    def __init__(
        self,
        auth_entity: str | None = None,
        credentials: Credentials | None = None
    ) -> None:
        self.auth_entity = auth_entity
        self.credentials = credentials


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
        if not metadata:
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

    host, port = _host_port_from_url(address)

    if not options or not options.credentials:
        return Channel(host, port)

    ctx = SSLContext(ssl.PROTOCOL_TLSv1_2)
    channel = Channel(host, port, ssl=ctx)
    access_token = await _get_access_token(channel, address, options)
    channel.close()
    metadata = {"authorization": f'Bearer {access_token}'}
    channel = AuthenticatedChannel(host, port, ssl=ctx)
    channel._metadata = metadata

    return channel

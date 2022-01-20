import re
from typing import Tuple
from grpclib.client import Channel


class RTCConfiguration:
    pass


class DialWebRTCOptions:
    disable_tricle_ice: bool
    rtc_config: RTCConfiguration


class Credentials:
    type: str
    payload: str


class DialOptions:
    auth_entity: str | None
    credentials: Credentials | None
    webrtc_options: DialWebRTCOptions | None
    external_auth_address: str | None


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


def dial_direct(
    address: str,
    options: DialOptions = None
) -> Channel:

    host, port = _host_port_from_url(address)

    if not options or not options.credentials:
        return Channel(host, port)

    return Channel(host, port)

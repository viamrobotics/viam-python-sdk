"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class HttpRequest(google.protobuf.message.Message):
    """A common proto for logging HTTP requests. Only contains semantics
    defined by the HTTP specification. Product-specific logging
    information MUST be defined in a separate message.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REQUEST_METHOD_FIELD_NUMBER: builtins.int
    REQUEST_URL_FIELD_NUMBER: builtins.int
    REQUEST_SIZE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RESPONSE_SIZE_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    REMOTE_IP_FIELD_NUMBER: builtins.int
    SERVER_IP_FIELD_NUMBER: builtins.int
    REFERER_FIELD_NUMBER: builtins.int
    LATENCY_FIELD_NUMBER: builtins.int
    CACHE_LOOKUP_FIELD_NUMBER: builtins.int
    CACHE_HIT_FIELD_NUMBER: builtins.int
    CACHE_VALIDATED_WITH_ORIGIN_SERVER_FIELD_NUMBER: builtins.int
    CACHE_FILL_BYTES_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    request_method: typing.Text = ...
    """The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`."""

    request_url: typing.Text = ...
    """The scheme (http, https), the host name, the path and the query
    portion of the URL that was requested.
    Example: `"http://example.com/some/info?color=red"`.
    """

    request_size: builtins.int = ...
    """The size of the HTTP request message in bytes, including the request
    headers and the request body.
    """

    status: builtins.int = ...
    """The response code indicating the status of response.
    Examples: 200, 404.
    """

    response_size: builtins.int = ...
    """The size of the HTTP response message sent back to the client, in bytes,
    including the response headers and the response body.
    """

    user_agent: typing.Text = ...
    """The user agent sent by the client. Example:
    `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET
    CLR 1.0.3705)"`.
    """

    remote_ip: typing.Text = ...
    """The IP address (IPv4 or IPv6) of the client that issued the HTTP
    request. This field can include port information. Examples:
    `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.
    """

    server_ip: typing.Text = ...
    """The IP address (IPv4 or IPv6) of the origin server that the request was
    sent to. This field can include port information. Examples:
    `"192.168.1.1"`, `"10.0.0.1:80"`, `"FE80::0202:B3FF:FE1E:8329"`.
    """

    referer: typing.Text = ...
    """The referer URL of the request, as defined in
    [HTTP/1.1 Header Field
    Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
    """

    @property
    def latency(self) -> google.protobuf.duration_pb2.Duration:
        """The request processing latency on the server, from the time the request was
        received until the response was sent.
        """
        pass
    cache_lookup: builtins.bool = ...
    """Whether or not a cache lookup was attempted."""

    cache_hit: builtins.bool = ...
    """Whether or not an entity was served from cache
    (with or without validation).
    """

    cache_validated_with_origin_server: builtins.bool = ...
    """Whether or not the response was validated with the origin server before
    being served from cache. This field is only meaningful if `cache_hit` is
    True.
    """

    cache_fill_bytes: builtins.int = ...
    """The number of HTTP response bytes inserted into cache. Set only when a
    cache fill was attempted.
    """

    protocol: typing.Text = ...
    """Protocol used for the request. Examples: "HTTP/1.1", "HTTP/2", "websocket" """

    def __init__(self,
        *,
        request_method : typing.Text = ...,
        request_url : typing.Text = ...,
        request_size : builtins.int = ...,
        status : builtins.int = ...,
        response_size : builtins.int = ...,
        user_agent : typing.Text = ...,
        remote_ip : typing.Text = ...,
        server_ip : typing.Text = ...,
        referer : typing.Text = ...,
        latency : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        cache_lookup : builtins.bool = ...,
        cache_hit : builtins.bool = ...,
        cache_validated_with_origin_server : builtins.bool = ...,
        cache_fill_bytes : builtins.int = ...,
        protocol : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["latency",b"latency"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cache_fill_bytes",b"cache_fill_bytes","cache_hit",b"cache_hit","cache_lookup",b"cache_lookup","cache_validated_with_origin_server",b"cache_validated_with_origin_server","latency",b"latency","protocol",b"protocol","referer",b"referer","remote_ip",b"remote_ip","request_method",b"request_method","request_size",b"request_size","request_url",b"request_url","response_size",b"response_size","server_ip",b"server_ip","status",b"status","user_agent",b"user_agent"]) -> None: ...
global___HttpRequest = HttpRequest

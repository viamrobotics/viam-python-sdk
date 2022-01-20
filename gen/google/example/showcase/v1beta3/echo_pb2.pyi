"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _Severity:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _SeverityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Severity.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    UNNECESSARY: Severity.ValueType = ...  # 0
    """The severity is unnecessary."""

    NECESSARY: Severity.ValueType = ...  # 1
    """The severity is necessary."""

    URGENT: Severity.ValueType = ...  # 2
    """Urgent."""

    CRITICAL: Severity.ValueType = ...  # 3
    """Critical."""

class Severity(_Severity, metaclass=_SeverityEnumTypeWrapper):
    """A severity enum used to test enum capabilities in GAPIC surfaces."""
    pass

UNNECESSARY: Severity.ValueType = ...  # 0
"""The severity is unnecessary."""

NECESSARY: Severity.ValueType = ...  # 1
"""The severity is necessary."""

URGENT: Severity.ValueType = ...  # 2
"""Urgent."""

CRITICAL: Severity.ValueType = ...  # 3
"""Critical."""

global___Severity = Severity


class EchoRequest(google.protobuf.message.Message):
    """The request message used for the Echo, Collect and Chat methods.
    If content or opt are set in this message then the request will succeed.
    If status is set in this message then the status will be returned as an
    error.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    SEVERITY_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """The content to be echoed by the server."""

    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """The error to be thrown by the server."""
        pass
    severity: global___Severity.ValueType = ...
    """The severity to be echoed by the server."""

    def __init__(self,
        *,
        content : typing.Text = ...,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        severity : global___Severity.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content",b"content","error",b"error","response",b"response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","error",b"error","response",b"response","severity",b"severity"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["content","error"]]: ...
global___EchoRequest = EchoRequest

class EchoResponse(google.protobuf.message.Message):
    """The response message for the Echo methods."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    SEVERITY_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """The content specified in the request."""

    severity: global___Severity.ValueType = ...
    """The severity specified in the request."""

    def __init__(self,
        *,
        content : typing.Text = ...,
        severity : global___Severity.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","severity",b"severity"]) -> None: ...
global___EchoResponse = EchoResponse

class ExpandRequest(google.protobuf.message.Message):
    """The request message for the Expand method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """The content that will be split into words and returned on the stream."""

    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """The error that is thrown after all words are sent on the stream."""
        pass
    def __init__(self,
        *,
        content : typing.Text = ...,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","error",b"error"]) -> None: ...
global___ExpandRequest = ExpandRequest

class PagedExpandRequest(google.protobuf.message.Message):
    """The request for the PagedExpand method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """Required. The string to expand."""

    page_size: builtins.int = ...
    """The amount of words to returned in each page."""

    page_token: typing.Text = ...
    """The position of the page to be returned."""

    def __init__(self,
        *,
        content : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___PagedExpandRequest = PagedExpandRequest

class PagedExpandResponse(google.protobuf.message.Message):
    """The response for the PagedExpand method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESPONSES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def responses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EchoResponse]:
        """The words that were expanded."""
        pass
    next_page_token: typing.Text = ...
    """The next page token."""

    def __init__(self,
        *,
        responses : typing.Optional[typing.Iterable[global___EchoResponse]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","responses",b"responses"]) -> None: ...
global___PagedExpandResponse = PagedExpandResponse

class WaitRequest(google.protobuf.message.Message):
    """The request for Wait method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    END_TIME_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time that this operation will complete."""
        pass
    @property
    def ttl(self) -> google.protobuf.duration_pb2.Duration:
        """The duration of this operation."""
        pass
    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """The error that will be returned by the server. If this code is specified
        to be the OK rpc code, an empty response will be returned.
        """
        pass
    @property
    def success(self) -> global___WaitResponse:
        """The response to be returned on operation completion."""
        pass
    def __init__(self,
        *,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ttl : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        success : typing.Optional[global___WaitResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end",b"end","end_time",b"end_time","error",b"error","response",b"response","success",b"success","ttl",b"ttl"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end",b"end","end_time",b"end_time","error",b"error","response",b"response","success",b"success","ttl",b"ttl"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["end",b"end"]) -> typing.Optional[typing_extensions.Literal["end_time","ttl"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["error","success"]]: ...
global___WaitRequest = WaitRequest

class WaitResponse(google.protobuf.message.Message):
    """The result of the Wait operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """This content of the result."""

    def __init__(self,
        *,
        content : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content"]) -> None: ...
global___WaitResponse = WaitResponse

class BlockRequest(google.protobuf.message.Message):
    """The request for Block method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ERROR_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    RESPONSE_DELAY_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> google.rpc.status_pb2.Status:
        """The error that will be returned by the server. If this code is specified
        to be the OK rpc code, an empty response will be returned.
        """
        pass
    @property
    def success(self) -> global___BlockResponse:
        """The response to be returned that will signify successful method call."""
        pass
    @property
    def response_delay(self) -> google.protobuf.duration_pb2.Duration:
        """The amount of time to block before returning a response."""
        pass
    def __init__(self,
        *,
        error : typing.Optional[google.rpc.status_pb2.Status] = ...,
        success : typing.Optional[global___BlockResponse] = ...,
        response_delay : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","response",b"response","response_delay",b"response_delay","success",b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","response",b"response","response_delay",b"response_delay","success",b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["error","success"]]: ...
global___BlockRequest = BlockRequest

class BlockResponse(google.protobuf.message.Message):
    """The response for Block method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONTENT_FIELD_NUMBER: builtins.int
    content: typing.Text = ...
    """This content can contain anything, the server will not depend on a value
    here.
    """

    def __init__(self,
        *,
        content : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content"]) -> None: ...
global___BlockResponse = BlockResponse

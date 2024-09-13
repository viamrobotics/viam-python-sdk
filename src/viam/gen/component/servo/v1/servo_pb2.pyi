"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MoveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ANGLE_DEG_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'the name of the servo, as registered'
    angle_deg: builtins.int
    'the degrees by which to rotate the servo.'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., angle_deg: builtins.int=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['angle_deg', b'angle_deg', 'extra', b'extra', 'name', b'name']) -> None:
        ...
global___MoveRequest = MoveRequest

@typing.final
class MoveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___MoveResponse = MoveResponse

@typing.final
class GetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'the name of the servo, as registered'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPositionRequest = GetPositionRequest

@typing.final
class GetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSITION_DEG_FIELD_NUMBER: builtins.int
    position_deg: builtins.int
    'the degrees from neutral by which the servo is currently rotated.'

    def __init__(self, *, position_deg: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['position_deg', b'position_deg']) -> None:
        ...
global___GetPositionResponse = GetPositionResponse

@typing.final
class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a servo'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___StopRequest = StopRequest

@typing.final
class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___StopResponse = StopResponse

@typing.final
class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSITION_DEG_FIELD_NUMBER: builtins.int
    IS_MOVING_FIELD_NUMBER: builtins.int
    position_deg: builtins.int
    is_moving: builtins.bool

    def __init__(self, *, position_deg: builtins.int=..., is_moving: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['is_moving', b'is_moving', 'position_deg', b'position_deg']) -> None:
        ...
global___Status = Status

@typing.final
class IsMovingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___IsMovingRequest = IsMovingRequest

@typing.final
class IsMovingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_MOVING_FIELD_NUMBER: builtins.int
    is_moving: builtins.bool

    def __init__(self, *, is_moving: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['is_moving', b'is_moving']) -> None:
        ...
global___IsMovingResponse = IsMovingResponse
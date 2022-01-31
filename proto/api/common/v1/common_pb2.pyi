"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BoardStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class AnalogsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___AnalogStatus: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___AnalogStatus] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class DigitalInterruptsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___DigitalInterruptStatus: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___DigitalInterruptStatus] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ANALOGS_FIELD_NUMBER: builtins.int
    DIGITAL_INTERRUPTS_FIELD_NUMBER: builtins.int
    @property
    def analogs(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___AnalogStatus]: ...
    @property
    def digital_interrupts(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___DigitalInterruptStatus]: ...
    def __init__(self,
        *,
        analogs : typing.Optional[typing.Mapping[typing.Text, global___AnalogStatus]] = ...,
        digital_interrupts : typing.Optional[typing.Mapping[typing.Text, global___DigitalInterruptStatus]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["analogs",b"analogs","digital_interrupts",b"digital_interrupts"]) -> None: ...
global___BoardStatus = BoardStatus

class AnalogStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int = ...
    def __init__(self,
        *,
        value : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___AnalogStatus = AnalogStatus

class DigitalInterruptStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int = ...
    def __init__(self,
        *,
        value : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___DigitalInterruptStatus = DigitalInterruptStatus

class Pose(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    O_X_FIELD_NUMBER: builtins.int
    O_Y_FIELD_NUMBER: builtins.int
    O_Z_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    x: builtins.float = ...
    """millimeters of the end effector from the base"""

    y: builtins.float = ...
    z: builtins.float = ...
    o_x: builtins.float = ...
    """ox, oy, oz, theta represents an orientation vector
    Structured similarly to an angle axis, an orientation vector works differently. Rather than representing an orientation
    with an arbitrary axis and a rotation around it from an origin, an orientation vector represents orientation
    such that the ox/oy/oz components represent the point on the cartesian unit sphere at which your end effector is pointing
    from the origin, and that unit vector forms an axis around which theta rotates. This means that incrementing/decrementing
    theta will perform an in-line rotation of the end effector.
    Theta is defined as rotation between two planes: the plane defined by the origin, the point (0,0,1), and the rx,ry,rz
    point, and the plane defined by the origin, the rx,ry,rz point, and the new local Z axis. So if theta is kept at
    zero as the north/south pole is circled, the Roll will correct itself to remain in-line.
    Theta in pb.Pose should be degrees. It will be converted to radians in the internal OrientationVec.
    """

    o_y: builtins.float = ...
    o_z: builtins.float = ...
    theta: builtins.float = ...
    def __init__(self,
        *,
        x : builtins.float = ...,
        y : builtins.float = ...,
        z : builtins.float = ...,
        o_x : builtins.float = ...,
        o_y : builtins.float = ...,
        o_z : builtins.float = ...,
        theta : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["o_x",b"o_x","o_y",b"o_y","o_z",b"o_z","theta",b"theta","x",b"x","y",b"y","z",b"z"]) -> None: ...
global___Pose = Pose

class Vector3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float = ...
    y: builtins.float = ...
    z: builtins.float = ...
    def __init__(self,
        *,
        x : builtins.float = ...,
        y : builtins.float = ...,
        z : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x",b"x","y",b"y","z",b"z"]) -> None: ...
global___Vector3 = Vector3

class BoxGeometry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WIDTH_MM_FIELD_NUMBER: builtins.int
    LENGTH_MM_FIELD_NUMBER: builtins.int
    DEPTH_MM_FIELD_NUMBER: builtins.int
    width_mm: builtins.float = ...
    length_mm: builtins.float = ...
    depth_mm: builtins.float = ...
    def __init__(self,
        *,
        width_mm : builtins.float = ...,
        length_mm : builtins.float = ...,
        depth_mm : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["depth_mm",b"depth_mm","length_mm",b"length_mm","width_mm",b"width_mm"]) -> None: ...
global___BoxGeometry = BoxGeometry

class GeoPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    latitude: builtins.float = ...
    longitude: builtins.float = ...
    def __init__(self,
        *,
        latitude : builtins.float = ...,
        longitude : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["latitude",b"latitude","longitude",b"longitude"]) -> None: ...
global___GeoPoint = GeoPoint

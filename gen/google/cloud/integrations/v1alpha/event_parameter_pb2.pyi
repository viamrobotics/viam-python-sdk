"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.integrations.v1alpha.value_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class EventParameter(google.protobuf.message.Message):
    """This message is used for processing and persisting (when applicable) key
    value pair parameters for each event in the event bus.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: typing.Text = ...
    """Key is used to retrieve the corresponding parameter value. This should be
    unique for a given fired event. These parameters must be predefined in the
    integration definition.
    """

    @property
    def value(self) -> google.cloud.integrations.v1alpha.value_type_pb2.ValueType:
        """Values for the defined keys. Each value can either be string, int, double
        or any proto message.
        """
        pass
    def __init__(self,
        *,
        key : typing.Text = ...,
        value : typing.Optional[google.cloud.integrations.v1alpha.value_type_pb2.ValueType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...
global___EventParameter = EventParameter

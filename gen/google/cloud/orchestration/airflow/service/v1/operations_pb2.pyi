"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OperationMetadata(google.protobuf.message.Message):
    """Metadata describing an operation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _State:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        STATE_UNSPECIFIED: OperationMetadata.State.ValueType = ...  # 0
        """Unused."""

        PENDING: OperationMetadata.State.ValueType = ...  # 1
        """The operation has been created but is not yet started."""

        RUNNING: OperationMetadata.State.ValueType = ...  # 2
        """The operation is underway."""

        SUCCEEDED: OperationMetadata.State.ValueType = ...  # 3
        """The operation completed successfully."""

        SUCCESSFUL: OperationMetadata.State.ValueType = ...  # 3
        FAILED: OperationMetadata.State.ValueType = ...  # 4
        """The operation is no longer running but did not succeed."""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """An enum describing the overall state of an operation."""
        pass

    STATE_UNSPECIFIED: OperationMetadata.State.ValueType = ...  # 0
    """Unused."""

    PENDING: OperationMetadata.State.ValueType = ...  # 1
    """The operation has been created but is not yet started."""

    RUNNING: OperationMetadata.State.ValueType = ...  # 2
    """The operation is underway."""

    SUCCEEDED: OperationMetadata.State.ValueType = ...  # 3
    """The operation completed successfully."""

    SUCCESSFUL: OperationMetadata.State.ValueType = ...  # 3
    FAILED: OperationMetadata.State.ValueType = ...  # 4
    """The operation is no longer running but did not succeed."""


    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNSPECIFIED: OperationMetadata.Type.ValueType = ...  # 0
        """Unused."""

        CREATE: OperationMetadata.Type.ValueType = ...  # 1
        """A resource creation operation."""

        DELETE: OperationMetadata.Type.ValueType = ...  # 2
        """A resource deletion operation."""

        UPDATE: OperationMetadata.Type.ValueType = ...  # 3
        """A resource update operation."""

        CHECK: OperationMetadata.Type.ValueType = ...  # 4
        """A resource check operation."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """Type of longrunning operation."""
        pass

    TYPE_UNSPECIFIED: OperationMetadata.Type.ValueType = ...  # 0
    """Unused."""

    CREATE: OperationMetadata.Type.ValueType = ...  # 1
    """A resource creation operation."""

    DELETE: OperationMetadata.Type.ValueType = ...  # 2
    """A resource deletion operation."""

    UPDATE: OperationMetadata.Type.ValueType = ...  # 3
    """A resource update operation."""

    CHECK: OperationMetadata.Type.ValueType = ...  # 4
    """A resource check operation."""


    STATE_FIELD_NUMBER: builtins.int
    OPERATION_TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    RESOURCE_UUID_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    state: global___OperationMetadata.State.ValueType = ...
    """Output only. The current operation state."""

    operation_type: global___OperationMetadata.Type.ValueType = ...
    """Output only. The type of operation being performed."""

    resource: typing.Text = ...
    """Output only. The resource being operated on, as a [relative resource name](
    /apis/design/resource_names#relative_resource_name).
    """

    resource_uuid: typing.Text = ...
    """Output only. The UUID of the resource being operated on."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the operation was submitted to the server."""
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the operation terminated, regardless of its success.
        This field is unset if the operation is still ongoing.
        """
        pass
    def __init__(self,
        *,
        state : global___OperationMetadata.State.ValueType = ...,
        operation_type : global___OperationMetadata.Type.ValueType = ...,
        resource : typing.Text = ...,
        resource_uuid : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","end_time",b"end_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","end_time",b"end_time","operation_type",b"operation_type","resource",b"resource","resource_uuid",b"resource_uuid","state",b"state"]) -> None: ...
global___OperationMetadata = OperationMetadata

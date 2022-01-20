"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SystemTimestamps(google.protobuf.message.Message):
    """Timestamps associated with this resource in a particular system."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    EXPIRE_TIME_FIELD_NUMBER: builtins.int
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation timestamp of the resource within the given system."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp of the last modification of the resource or its metadata within
        a given system.

        Note: Depending on the source system, not every modification updates this
        timestamp.
        For example, BigQuery timestamps every metadata modification but not data
        or permission changes.
        """
        pass
    @property
    def expire_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Expiration timestamp of the resource within the given system.

        Currently only applicable to BigQuery resources.
        """
        pass
    def __init__(self,
        *,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        expire_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","expire_time",b"expire_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","expire_time",b"expire_time","update_time",b"update_time"]) -> None: ...
global___SystemTimestamps = SystemTimestamps

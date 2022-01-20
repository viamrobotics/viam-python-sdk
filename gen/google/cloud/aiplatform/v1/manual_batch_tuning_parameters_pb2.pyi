"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ManualBatchTuningParameters(google.protobuf.message.Message):
    """Manual batch tuning parameters."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BATCH_SIZE_FIELD_NUMBER: builtins.int
    batch_size: builtins.int = ...
    """Immutable. The number of the records (e.g. instances) of the operation given in
    each batch to a machine replica. Machine type, and size of a single
    record should be considered when setting this parameter, higher value
    speeds up the batch operation's execution, but too high value will result
    in a whole batch not fitting in a machine's memory, and the whole
    operation will fail.
    The default value is 4.
    """

    def __init__(self,
        *,
        batch_size : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["batch_size",b"batch_size"]) -> None: ...
global___ManualBatchTuningParameters = ManualBatchTuningParameters

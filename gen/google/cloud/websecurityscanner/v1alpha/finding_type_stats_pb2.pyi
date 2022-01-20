"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.websecurityscanner.v1alpha.finding_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FindingTypeStats(google.protobuf.message.Message):
    """A FindingTypeStats resource represents stats regarding a specific FindingType
    of Findings under a given ScanRun.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FINDING_TYPE_FIELD_NUMBER: builtins.int
    FINDING_COUNT_FIELD_NUMBER: builtins.int
    finding_type: google.cloud.websecurityscanner.v1alpha.finding_pb2.Finding.FindingType.ValueType = ...
    """The finding type associated with the stats."""

    finding_count: builtins.int = ...
    """The count of findings belonging to this finding type."""

    def __init__(self,
        *,
        finding_type : google.cloud.websecurityscanner.v1alpha.finding_pb2.Finding.FindingType.ValueType = ...,
        finding_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["finding_count",b"finding_count","finding_type",b"finding_type"]) -> None: ...
global___FindingTypeStats = FindingTypeStats

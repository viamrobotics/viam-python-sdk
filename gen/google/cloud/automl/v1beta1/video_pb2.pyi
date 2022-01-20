"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import google.protobuf.descriptor
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class VideoClassificationDatasetMetadata(google.protobuf.message.Message):
    """Dataset metadata specific to video classification.
    All Video Classification datasets are treated as multi label.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___VideoClassificationDatasetMetadata = VideoClassificationDatasetMetadata

class VideoObjectTrackingDatasetMetadata(google.protobuf.message.Message):
    """Dataset metadata specific to video object tracking."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___VideoObjectTrackingDatasetMetadata = VideoObjectTrackingDatasetMetadata

class VideoClassificationModelMetadata(google.protobuf.message.Message):
    """Model metadata specific to video classification."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___VideoClassificationModelMetadata = VideoClassificationModelMetadata

class VideoObjectTrackingModelMetadata(google.protobuf.message.Message):
    """Model metadata specific to video object tracking."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___VideoObjectTrackingModelMetadata = VideoObjectTrackingModelMetadata

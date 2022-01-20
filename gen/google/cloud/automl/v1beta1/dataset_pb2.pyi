"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1beta1.image_pb2
import google.cloud.automl.v1beta1.tables_pb2
import google.cloud.automl.v1beta1.text_pb2
import google.cloud.automl.v1beta1.translation_pb2
import google.cloud.automl.v1beta1.video_pb2
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Dataset(google.protobuf.message.Message):
    """A workspace for solving a single, particular machine learning (ML) problem.
    A workspace contains examples that may be annotated.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSLATION_DATASET_METADATA_FIELD_NUMBER: builtins.int
    IMAGE_CLASSIFICATION_DATASET_METADATA_FIELD_NUMBER: builtins.int
    TEXT_CLASSIFICATION_DATASET_METADATA_FIELD_NUMBER: builtins.int
    IMAGE_OBJECT_DETECTION_DATASET_METADATA_FIELD_NUMBER: builtins.int
    VIDEO_CLASSIFICATION_DATASET_METADATA_FIELD_NUMBER: builtins.int
    VIDEO_OBJECT_TRACKING_DATASET_METADATA_FIELD_NUMBER: builtins.int
    TEXT_EXTRACTION_DATASET_METADATA_FIELD_NUMBER: builtins.int
    TEXT_SENTIMENT_DATASET_METADATA_FIELD_NUMBER: builtins.int
    TABLES_DATASET_METADATA_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXAMPLE_COUNT_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    @property
    def translation_dataset_metadata(self) -> google.cloud.automl.v1beta1.translation_pb2.TranslationDatasetMetadata:
        """Metadata for a dataset used for translation."""
        pass
    @property
    def image_classification_dataset_metadata(self) -> google.cloud.automl.v1beta1.image_pb2.ImageClassificationDatasetMetadata:
        """Metadata for a dataset used for image classification."""
        pass
    @property
    def text_classification_dataset_metadata(self) -> google.cloud.automl.v1beta1.text_pb2.TextClassificationDatasetMetadata:
        """Metadata for a dataset used for text classification."""
        pass
    @property
    def image_object_detection_dataset_metadata(self) -> google.cloud.automl.v1beta1.image_pb2.ImageObjectDetectionDatasetMetadata:
        """Metadata for a dataset used for image object detection."""
        pass
    @property
    def video_classification_dataset_metadata(self) -> google.cloud.automl.v1beta1.video_pb2.VideoClassificationDatasetMetadata:
        """Metadata for a dataset used for video classification."""
        pass
    @property
    def video_object_tracking_dataset_metadata(self) -> google.cloud.automl.v1beta1.video_pb2.VideoObjectTrackingDatasetMetadata:
        """Metadata for a dataset used for video object tracking."""
        pass
    @property
    def text_extraction_dataset_metadata(self) -> google.cloud.automl.v1beta1.text_pb2.TextExtractionDatasetMetadata:
        """Metadata for a dataset used for text extraction."""
        pass
    @property
    def text_sentiment_dataset_metadata(self) -> google.cloud.automl.v1beta1.text_pb2.TextSentimentDatasetMetadata:
        """Metadata for a dataset used for text sentiment."""
        pass
    @property
    def tables_dataset_metadata(self) -> google.cloud.automl.v1beta1.tables_pb2.TablesDatasetMetadata:
        """Metadata for a dataset used for Tables."""
        pass
    name: typing.Text = ...
    """Output only. The resource name of the dataset.
    Form: `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`
    """

    display_name: typing.Text = ...
    """Required. The name of the dataset to show in the interface. The name can be
    up to 32 characters long and can consist only of ASCII Latin letters A-Z
    and a-z, underscores
    (_), and ASCII digits 0-9.
    """

    description: typing.Text = ...
    """User-provided description of the dataset. The description can be up to
    25000 characters long.
    """

    example_count: builtins.int = ...
    """Output only. The number of examples in the dataset."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Timestamp when this dataset was created."""
        pass
    etag: typing.Text = ...
    """Used to perform consistent read-modify-write updates. If not set, a blind
    "overwrite" update happens.
    """

    def __init__(self,
        *,
        translation_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.translation_pb2.TranslationDatasetMetadata] = ...,
        image_classification_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.image_pb2.ImageClassificationDatasetMetadata] = ...,
        text_classification_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.text_pb2.TextClassificationDatasetMetadata] = ...,
        image_object_detection_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.image_pb2.ImageObjectDetectionDatasetMetadata] = ...,
        video_classification_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.video_pb2.VideoClassificationDatasetMetadata] = ...,
        video_object_tracking_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.video_pb2.VideoObjectTrackingDatasetMetadata] = ...,
        text_extraction_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.text_pb2.TextExtractionDatasetMetadata] = ...,
        text_sentiment_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.text_pb2.TextSentimentDatasetMetadata] = ...,
        tables_dataset_metadata : typing.Optional[google.cloud.automl.v1beta1.tables_pb2.TablesDatasetMetadata] = ...,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        description : typing.Text = ...,
        example_count : builtins.int = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        etag : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","dataset_metadata",b"dataset_metadata","image_classification_dataset_metadata",b"image_classification_dataset_metadata","image_object_detection_dataset_metadata",b"image_object_detection_dataset_metadata","tables_dataset_metadata",b"tables_dataset_metadata","text_classification_dataset_metadata",b"text_classification_dataset_metadata","text_extraction_dataset_metadata",b"text_extraction_dataset_metadata","text_sentiment_dataset_metadata",b"text_sentiment_dataset_metadata","translation_dataset_metadata",b"translation_dataset_metadata","video_classification_dataset_metadata",b"video_classification_dataset_metadata","video_object_tracking_dataset_metadata",b"video_object_tracking_dataset_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","dataset_metadata",b"dataset_metadata","description",b"description","display_name",b"display_name","etag",b"etag","example_count",b"example_count","image_classification_dataset_metadata",b"image_classification_dataset_metadata","image_object_detection_dataset_metadata",b"image_object_detection_dataset_metadata","name",b"name","tables_dataset_metadata",b"tables_dataset_metadata","text_classification_dataset_metadata",b"text_classification_dataset_metadata","text_extraction_dataset_metadata",b"text_extraction_dataset_metadata","text_sentiment_dataset_metadata",b"text_sentiment_dataset_metadata","translation_dataset_metadata",b"translation_dataset_metadata","video_classification_dataset_metadata",b"video_classification_dataset_metadata","video_object_tracking_dataset_metadata",b"video_object_tracking_dataset_metadata"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["dataset_metadata",b"dataset_metadata"]) -> typing.Optional[typing_extensions.Literal["translation_dataset_metadata","image_classification_dataset_metadata","text_classification_dataset_metadata","image_object_detection_dataset_metadata","video_classification_dataset_metadata","video_object_tracking_dataset_metadata","text_extraction_dataset_metadata","text_sentiment_dataset_metadata","tables_dataset_metadata"]]: ...
global___Dataset = Dataset

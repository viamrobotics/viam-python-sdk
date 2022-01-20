"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1.classification_pb2
import google.cloud.automl.v1.detection_pb2
import google.cloud.automl.v1.text_extraction_pb2
import google.cloud.automl.v1.text_sentiment_pb2
import google.cloud.automl.v1.translation_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AnnotationPayload(google.protobuf.message.Message):
    """Contains annotation information that is relevant to AutoML."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSLATION_FIELD_NUMBER: builtins.int
    CLASSIFICATION_FIELD_NUMBER: builtins.int
    IMAGE_OBJECT_DETECTION_FIELD_NUMBER: builtins.int
    TEXT_EXTRACTION_FIELD_NUMBER: builtins.int
    TEXT_SENTIMENT_FIELD_NUMBER: builtins.int
    ANNOTATION_SPEC_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    @property
    def translation(self) -> google.cloud.automl.v1.translation_pb2.TranslationAnnotation:
        """Annotation details for translation."""
        pass
    @property
    def classification(self) -> google.cloud.automl.v1.classification_pb2.ClassificationAnnotation:
        """Annotation details for content or image classification."""
        pass
    @property
    def image_object_detection(self) -> google.cloud.automl.v1.detection_pb2.ImageObjectDetectionAnnotation:
        """Annotation details for image object detection."""
        pass
    @property
    def text_extraction(self) -> google.cloud.automl.v1.text_extraction_pb2.TextExtractionAnnotation:
        """Annotation details for text extraction."""
        pass
    @property
    def text_sentiment(self) -> google.cloud.automl.v1.text_sentiment_pb2.TextSentimentAnnotation:
        """Annotation details for text sentiment."""
        pass
    annotation_spec_id: typing.Text = ...
    """Output only . The resource ID of the annotation spec that
    this annotation pertains to. The annotation spec comes from either an
    ancestor dataset, or the dataset that was used to train the model in use.
    """

    display_name: typing.Text = ...
    """Output only. The value of
    [display_name][google.cloud.automl.v1.AnnotationSpec.display_name]
    when the model was trained. Because this field returns a value at model
    training time, for different models trained using the same dataset, the
    returned value could be different as model owner could update the
    `display_name` between any two model training.
    """

    def __init__(self,
        *,
        translation : typing.Optional[google.cloud.automl.v1.translation_pb2.TranslationAnnotation] = ...,
        classification : typing.Optional[google.cloud.automl.v1.classification_pb2.ClassificationAnnotation] = ...,
        image_object_detection : typing.Optional[google.cloud.automl.v1.detection_pb2.ImageObjectDetectionAnnotation] = ...,
        text_extraction : typing.Optional[google.cloud.automl.v1.text_extraction_pb2.TextExtractionAnnotation] = ...,
        text_sentiment : typing.Optional[google.cloud.automl.v1.text_sentiment_pb2.TextSentimentAnnotation] = ...,
        annotation_spec_id : typing.Text = ...,
        display_name : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["classification",b"classification","detail",b"detail","image_object_detection",b"image_object_detection","text_extraction",b"text_extraction","text_sentiment",b"text_sentiment","translation",b"translation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotation_spec_id",b"annotation_spec_id","classification",b"classification","detail",b"detail","display_name",b"display_name","image_object_detection",b"image_object_detection","text_extraction",b"text_extraction","text_sentiment",b"text_sentiment","translation",b"translation"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["detail",b"detail"]) -> typing.Optional[typing_extensions.Literal["translation","classification","image_object_detection","text_extraction","text_sentiment"]]: ...
global___AnnotationPayload = AnnotationPayload

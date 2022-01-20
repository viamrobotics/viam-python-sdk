"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.automl.v1beta1.text_segment_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TextExtractionAnnotation(google.protobuf.message.Message):
    """Annotation for identifying spans of text."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TEXT_SEGMENT_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    @property
    def text_segment(self) -> google.cloud.automl.v1beta1.text_segment_pb2.TextSegment:
        """An entity annotation will set this, which is the part of the original
        text to which the annotation pertains.
        """
        pass
    score: builtins.float = ...
    """Output only. A confidence estimate between 0.0 and 1.0. A higher value
    means greater confidence in correctness of the annotation.
    """

    def __init__(self,
        *,
        text_segment : typing.Optional[google.cloud.automl.v1beta1.text_segment_pb2.TextSegment] = ...,
        score : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["annotation",b"annotation","text_segment",b"text_segment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotation",b"annotation","score",b"score","text_segment",b"text_segment"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["annotation",b"annotation"]) -> typing.Optional[typing_extensions.Literal["text_segment"]]: ...
global___TextExtractionAnnotation = TextExtractionAnnotation

class TextExtractionEvaluationMetrics(google.protobuf.message.Message):
    """Model evaluation metrics for text extraction problems."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ConfidenceMetricsEntry(google.protobuf.message.Message):
        """Metrics for a single confidence threshold."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        CONFIDENCE_THRESHOLD_FIELD_NUMBER: builtins.int
        RECALL_FIELD_NUMBER: builtins.int
        PRECISION_FIELD_NUMBER: builtins.int
        F1_SCORE_FIELD_NUMBER: builtins.int
        confidence_threshold: builtins.float = ...
        """Output only. The confidence threshold value used to compute the metrics.
        Only annotations with score of at least this threshold are considered to
        be ones the model would return.
        """

        recall: builtins.float = ...
        """Output only. Recall under the given confidence threshold."""

        precision: builtins.float = ...
        """Output only. Precision under the given confidence threshold."""

        f1_score: builtins.float = ...
        """Output only. The harmonic mean of recall and precision."""

        def __init__(self,
            *,
            confidence_threshold : builtins.float = ...,
            recall : builtins.float = ...,
            precision : builtins.float = ...,
            f1_score : builtins.float = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["confidence_threshold",b"confidence_threshold","f1_score",b"f1_score","precision",b"precision","recall",b"recall"]) -> None: ...

    AU_PRC_FIELD_NUMBER: builtins.int
    CONFIDENCE_METRICS_ENTRIES_FIELD_NUMBER: builtins.int
    au_prc: builtins.float = ...
    """Output only. The Area under precision recall curve metric."""

    @property
    def confidence_metrics_entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TextExtractionEvaluationMetrics.ConfidenceMetricsEntry]:
        """Output only. Metrics that have confidence thresholds.
        Precision-recall curve can be derived from it.
        """
        pass
    def __init__(self,
        *,
        au_prc : builtins.float = ...,
        confidence_metrics_entries : typing.Optional[typing.Iterable[global___TextExtractionEvaluationMetrics.ConfidenceMetricsEntry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["au_prc",b"au_prc","confidence_metrics_entries",b"confidence_metrics_entries"]) -> None: ...
global___TextExtractionEvaluationMetrics = TextExtractionEvaluationMetrics

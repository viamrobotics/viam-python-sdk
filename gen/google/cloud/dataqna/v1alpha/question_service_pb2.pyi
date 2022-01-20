"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.dataqna.v1alpha.question_pb2
import google.cloud.dataqna.v1alpha.user_feedback_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetQuestionRequest(google.protobuf.message.Message):
    """A request to get a previously created question."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    READ_MASK_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The unique identifier for the question.
    Example: `projects/foo/locations/bar/questions/1234`
    """

    @property
    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The list of fields to be retrieved."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        read_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","read_mask",b"read_mask"]) -> None: ...
global___GetQuestionRequest = GetQuestionRequest

class CreateQuestionRequest(google.protobuf.message.Message):
    """Request to create a question resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    QUESTION_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the project this data source reference belongs to.
    Example: `projects/foo/locations/bar`
    """

    @property
    def question(self) -> google.cloud.dataqna.v1alpha.question_pb2.Question:
        """Required. The question to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        question : typing.Optional[google.cloud.dataqna.v1alpha.question_pb2.Question] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["question",b"question"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","question",b"question"]) -> None: ...
global___CreateQuestionRequest = CreateQuestionRequest

class ExecuteQuestionRequest(google.protobuf.message.Message):
    """Request to execute an interpretation."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    INTERPRETATION_INDEX_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The unique identifier for the question.
    Example: `projects/foo/locations/bar/questions/1234`
    """

    interpretation_index: builtins.int = ...
    """Required. Index of the interpretation to execute."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        interpretation_index : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["interpretation_index",b"interpretation_index","name",b"name"]) -> None: ...
global___ExecuteQuestionRequest = ExecuteQuestionRequest

class GetUserFeedbackRequest(google.protobuf.message.Message):
    """Request to get user feedback."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The unique identifier for the user feedback.
    User feedback is a singleton resource on a Question.
    Example: `projects/foo/locations/bar/questions/1234/userFeedback`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetUserFeedbackRequest = GetUserFeedbackRequest

class UpdateUserFeedbackRequest(google.protobuf.message.Message):
    """Request to updates user feedback."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_FEEDBACK_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def user_feedback(self) -> google.cloud.dataqna.v1alpha.user_feedback_pb2.UserFeedback:
        """Required. The user feedback to update. This can be called even if there is no
        user feedback so far.
        The feedback's name field is used to identify the user feedback (and the
        corresponding question) to update.
        """
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The list of fields to be updated."""
        pass
    def __init__(self,
        *,
        user_feedback : typing.Optional[google.cloud.dataqna.v1alpha.user_feedback_pb2.UserFeedback] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask","user_feedback",b"user_feedback"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["update_mask",b"update_mask","user_feedback",b"user_feedback"]) -> None: ...
global___UpdateUserFeedbackRequest = UpdateUserFeedbackRequest

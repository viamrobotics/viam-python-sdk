"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.api.label_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class LogDescriptor(google.protobuf.message.Message):
    """A description of a log type. Example in YAML format:

        - name: library.googleapis.com/activity_history
          description: The history of borrowing and returning library items.
          display_name: Activity
          labels:
          - key: /customer_id
            description: Identifier of a library customer
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the log. It must be less than 512 characters long and can
    include the following characters: upper- and lower-case alphanumeric
    characters [A-Za-z0-9], and punctuation characters including
    slash, underscore, hyphen, period [/_-.].
    """

    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.api.label_pb2.LabelDescriptor]:
        """The set of labels that are available to describe a specific log entry.
        Runtime requests that contain labels not specified here are
        considered invalid.
        """
        pass
    description: typing.Text = ...
    """A human-readable description of this log. This information appears in
    the documentation and can contain details.
    """

    display_name: typing.Text = ...
    """The human-readable name for this log. This information appears on
    the user interface and should be concise.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        labels : typing.Optional[typing.Iterable[google.api.label_pb2.LabelDescriptor]] = ...,
        description : typing.Text = ...,
        display_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","display_name",b"display_name","labels",b"labels","name",b"name"]) -> None: ...
global___LogDescriptor = LogDescriptor

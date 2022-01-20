"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v7.enums.shared_set_status_pb2
import google.ads.googleads.v7.enums.shared_set_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SharedSet(google.protobuf.message.Message):
    """Proto file describing the SharedSet resource.

    SharedSets are used for sharing criterion exclusions across multiple
    campaigns.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MEMBER_COUNT_FIELD_NUMBER: builtins.int
    REFERENCE_COUNT_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. The resource name of the shared set.
    Shared set resource names have the form:

    `customers/{customer_id}/sharedSets/{shared_set_id}`
    """

    id: builtins.int = ...
    """Output only. The ID of this shared set. Read only."""

    type: google.ads.googleads.v7.enums.shared_set_type_pb2.SharedSetTypeEnum.SharedSetType.ValueType = ...
    """Immutable. The type of this shared set: each shared set holds only a single kind
    of resource. Required. Immutable.
    """

    name: typing.Text = ...
    """The name of this shared set. Required.
    Shared Sets must have names that are unique among active shared sets of
    the same type.
    The length of this string should be between 1 and 255 UTF-8 bytes,
    inclusive.
    """

    status: google.ads.googleads.v7.enums.shared_set_status_pb2.SharedSetStatusEnum.SharedSetStatus.ValueType = ...
    """Output only. The status of this shared set. Read only."""

    member_count: builtins.int = ...
    """Output only. The number of shared criteria within this shared set. Read only."""

    reference_count: builtins.int = ...
    """Output only. The number of campaigns associated with this shared set. Read only."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        id : typing.Optional[builtins.int] = ...,
        type : google.ads.googleads.v7.enums.shared_set_type_pb2.SharedSetTypeEnum.SharedSetType.ValueType = ...,
        name : typing.Optional[typing.Text] = ...,
        status : google.ads.googleads.v7.enums.shared_set_status_pb2.SharedSetStatusEnum.SharedSetStatus.ValueType = ...,
        member_count : typing.Optional[builtins.int] = ...,
        reference_count : typing.Optional[builtins.int] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_id",b"_id","_member_count",b"_member_count","_name",b"_name","_reference_count",b"_reference_count","id",b"id","member_count",b"member_count","name",b"name","reference_count",b"reference_count"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_id",b"_id","_member_count",b"_member_count","_name",b"_name","_reference_count",b"_reference_count","id",b"id","member_count",b"member_count","name",b"name","reference_count",b"reference_count","resource_name",b"resource_name","status",b"status","type",b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_id",b"_id"]) -> typing.Optional[typing_extensions.Literal["id"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_member_count",b"_member_count"]) -> typing.Optional[typing_extensions.Literal["member_count"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_reference_count",b"_reference_count"]) -> typing.Optional[typing_extensions.Literal["reference_count"]]: ...
global___SharedSet = SharedSet

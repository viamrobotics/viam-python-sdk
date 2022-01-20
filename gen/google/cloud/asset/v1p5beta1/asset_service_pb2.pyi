"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.asset.v1p5beta1.assets_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _ContentType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ContentTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ContentType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    CONTENT_TYPE_UNSPECIFIED: ContentType.ValueType = ...  # 0
    """Unspecified content type."""

    RESOURCE: ContentType.ValueType = ...  # 1
    """Resource metadata."""

    IAM_POLICY: ContentType.ValueType = ...  # 2
    """The actual IAM policy set on a resource."""

    ORG_POLICY: ContentType.ValueType = ...  # 4
    """The Cloud Organization Policy set on an asset."""

    ACCESS_POLICY: ContentType.ValueType = ...  # 5
    """The Cloud Access context mananger Policy set on an asset."""

class ContentType(_ContentType, metaclass=_ContentTypeEnumTypeWrapper):
    """Asset content type."""
    pass

CONTENT_TYPE_UNSPECIFIED: ContentType.ValueType = ...  # 0
"""Unspecified content type."""

RESOURCE: ContentType.ValueType = ...  # 1
"""Resource metadata."""

IAM_POLICY: ContentType.ValueType = ...  # 2
"""The actual IAM policy set on a resource."""

ORG_POLICY: ContentType.ValueType = ...  # 4
"""The Cloud Organization Policy set on an asset."""

ACCESS_POLICY: ContentType.ValueType = ...  # 5
"""The Cloud Access context mananger Policy set on an asset."""

global___ContentType = ContentType


class ListAssetsRequest(google.protobuf.message.Message):
    """ListAssets request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    READ_TIME_FIELD_NUMBER: builtins.int
    ASSET_TYPES_FIELD_NUMBER: builtins.int
    CONTENT_TYPE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. Name of the organization or project the assets belong to. Format:
    "organizations/[organization-number]" (such as "organizations/123"),
    "projects/[project-number]" (such as "projects/my-project-id"), or
    "projects/[project-id]" (such as "projects/12345").
    """

    @property
    def read_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp to take an asset snapshot. This can only be set to a timestamp
        between 2018-10-02 UTC (inclusive) and the current time. If not specified,
        the current time will be used. Due to delays in resource data collection
        and indexing, there is a volatile window during which running the same
        query may get different results.
        """
        pass
    @property
    def asset_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A list of asset types of which to take a snapshot for. For  example:
        "compute.googleapis.com/Disk". If specified, only matching assets will be
        returned. See [Introduction to Cloud Asset
        Inventory](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview)
        for all supported asset types.
        """
        pass
    content_type: global___ContentType.ValueType = ...
    """Asset content type. If not specified, no content but the asset name will
    be returned.
    """

    page_size: builtins.int = ...
    """The maximum number of assets to be returned in a single response. Default
    is 100, minimum is 1, and maximum is 1000.
    """

    page_token: typing.Text = ...
    """The `next_page_token` returned from the previous `ListAssetsResponse`, or
    unspecified for the first `ListAssetsRequest`. It is a continuation of a
    prior `ListAssets` call, and the API should return the next page of assets.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        read_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        asset_types : typing.Optional[typing.Iterable[typing.Text]] = ...,
        content_type : global___ContentType.ValueType = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_time",b"read_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_types",b"asset_types","content_type",b"content_type","page_size",b"page_size","page_token",b"page_token","parent",b"parent","read_time",b"read_time"]) -> None: ...
global___ListAssetsRequest = ListAssetsRequest

class ListAssetsResponse(google.protobuf.message.Message):
    """ListAssets response."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    READ_TIME_FIELD_NUMBER: builtins.int
    ASSETS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def read_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time the snapshot was taken."""
        pass
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.asset.v1p5beta1.assets_pb2.Asset]:
        """Assets."""
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results. Set to empty if there are no
    remaining results.
    """

    def __init__(self,
        *,
        read_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        assets : typing.Optional[typing.Iterable[google.cloud.asset.v1p5beta1.assets_pb2.Asset]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["read_time",b"read_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets",b"assets","next_page_token",b"next_page_token","read_time",b"read_time"]) -> None: ...
global___ListAssetsResponse = ListAssetsResponse

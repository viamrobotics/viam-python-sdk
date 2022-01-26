"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SqlTiersListRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROJECT_FIELD_NUMBER: builtins.int
    project: typing.Text = ...
    """Project ID of the project for which to list tiers."""

    def __init__(self,
        *,
        project : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["project",b"project"]) -> None: ...
global___SqlTiersListRequest = SqlTiersListRequest

class TiersListResponse(google.protobuf.message.Message):
    """Tiers list response."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KIND_FIELD_NUMBER: builtins.int
    ITEMS_FIELD_NUMBER: builtins.int
    kind: typing.Text = ...
    """This is always `sql#tiersList`."""

    @property
    def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Tier]:
        """List of tiers."""
        pass
    def __init__(self,
        *,
        kind : typing.Text = ...,
        items : typing.Optional[typing.Iterable[global___Tier]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["items",b"items","kind",b"kind"]) -> None: ...
global___TiersListResponse = TiersListResponse

class Tier(google.protobuf.message.Message):
    """A Google Cloud SQL service tier resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIER_FIELD_NUMBER: builtins.int
    RAM_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    DISK_QUOTA_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    tier: typing.Text = ...
    """An identifier for the machine type, for example, `db-custom-1-3840`. For
    related information, see [Pricing](/sql/pricing).
    """

    RAM: builtins.int = ...
    """The maximum RAM usage of this tier in bytes."""

    kind: typing.Text = ...
    """This is always `sql#tier`."""

    Disk_Quota: builtins.int = ...
    """The maximum disk size of this tier in bytes."""

    @property
    def region(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The applicable regions for this tier."""
        pass
    def __init__(self,
        *,
        tier : typing.Text = ...,
        RAM : builtins.int = ...,
        kind : typing.Text = ...,
        Disk_Quota : builtins.int = ...,
        region : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["Disk_Quota",b"Disk_Quota","RAM",b"RAM","kind",b"kind","region",b"region","tier",b"tier"]) -> None: ...
global___Tier = Tier

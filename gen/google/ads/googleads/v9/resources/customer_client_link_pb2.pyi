"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v9.enums.manager_link_status_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CustomerClientLink(google.protobuf.message.Message):
    """Proto file describing the CustomerClientLink resource.

    Represents customer client link relationship.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CLIENT_CUSTOMER_FIELD_NUMBER: builtins.int
    MANAGER_LINK_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    HIDDEN_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. Name of the resource.
    CustomerClientLink resource names have the form:
    `customers/{customer_id}/customerClientLinks/{client_customer_id}~{manager_link_id}`
    """

    client_customer: typing.Text = ...
    """Immutable. The client customer linked to this customer."""

    manager_link_id: builtins.int = ...
    """Output only. This is uniquely identifies a customer client link. Read only."""

    status: google.ads.googleads.v9.enums.manager_link_status_pb2.ManagerLinkStatusEnum.ManagerLinkStatus.ValueType = ...
    """This is the status of the link between client and manager."""

    hidden: builtins.bool = ...
    """The visibility of the link. Users can choose whether or not to see hidden
    links in the Google Ads UI.
    Default value is false
    """

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        client_customer : typing.Optional[typing.Text] = ...,
        manager_link_id : typing.Optional[builtins.int] = ...,
        status : google.ads.googleads.v9.enums.manager_link_status_pb2.ManagerLinkStatusEnum.ManagerLinkStatus.ValueType = ...,
        hidden : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_client_customer",b"_client_customer","_hidden",b"_hidden","_manager_link_id",b"_manager_link_id","client_customer",b"client_customer","hidden",b"hidden","manager_link_id",b"manager_link_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_client_customer",b"_client_customer","_hidden",b"_hidden","_manager_link_id",b"_manager_link_id","client_customer",b"client_customer","hidden",b"hidden","manager_link_id",b"manager_link_id","resource_name",b"resource_name","status",b"status"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_client_customer",b"_client_customer"]) -> typing.Optional[typing_extensions.Literal["client_customer"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_hidden",b"_hidden"]) -> typing.Optional[typing_extensions.Literal["hidden"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_manager_link_id",b"_manager_link_id"]) -> typing.Optional[typing_extensions.Literal["manager_link_id"]]: ...
global___CustomerClientLink = CustomerClientLink

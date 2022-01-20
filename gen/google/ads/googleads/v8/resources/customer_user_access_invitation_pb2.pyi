"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.googleads.v8.enums.access_invitation_status_pb2
import google.ads.googleads.v8.enums.access_role_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CustomerUserAccessInvitation(google.protobuf.message.Message):
    """Proto file describing the CustomerUserAccessInvitation resource.

    Represent an invitation to a new user on this customer account.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    INVITATION_ID_FIELD_NUMBER: builtins.int
    ACCESS_ROLE_FIELD_NUMBER: builtins.int
    EMAIL_ADDRESS_FIELD_NUMBER: builtins.int
    CREATION_DATE_TIME_FIELD_NUMBER: builtins.int
    INVITATION_STATUS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    """Immutable. Name of the resource.
    Resource names have the form:
    `customers/{customer_id}/customerUserAccessInvitations/{invitation_id}`
    """

    invitation_id: builtins.int = ...
    """Output only. The ID of the invitation.
    This field is read-only.
    """

    access_role: google.ads.googleads.v8.enums.access_role_pb2.AccessRoleEnum.AccessRole.ValueType = ...
    """Immutable. Access role of the user."""

    email_address: typing.Text = ...
    """Immutable. Email address the invitation was sent to.
    This can differ from the email address of the account
    that accepts the invite.
    """

    creation_date_time: typing.Text = ...
    """Output only. Time invitation was created.
    This field is read-only.
    The format is "YYYY-MM-DD HH:MM:SS".
    Examples: "2018-03-05 09:15:00" or "2018-02-01 14:34:30"
    """

    invitation_status: google.ads.googleads.v8.enums.access_invitation_status_pb2.AccessInvitationStatusEnum.AccessInvitationStatus.ValueType = ...
    """Output only. Invitation status of the user."""

    def __init__(self,
        *,
        resource_name : typing.Text = ...,
        invitation_id : builtins.int = ...,
        access_role : google.ads.googleads.v8.enums.access_role_pb2.AccessRoleEnum.AccessRole.ValueType = ...,
        email_address : typing.Text = ...,
        creation_date_time : typing.Text = ...,
        invitation_status : google.ads.googleads.v8.enums.access_invitation_status_pb2.AccessInvitationStatusEnum.AccessInvitationStatus.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_role",b"access_role","creation_date_time",b"creation_date_time","email_address",b"email_address","invitation_id",b"invitation_id","invitation_status",b"invitation_status","resource_name",b"resource_name"]) -> None: ...
global___CustomerUserAccessInvitation = CustomerUserAccessInvitation

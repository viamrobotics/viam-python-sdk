"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _EnrollmentLevel:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _EnrollmentLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnrollmentLevel.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ENROLLMENT_LEVEL_UNSPECIFIED: EnrollmentLevel.ValueType = ...  # 0
    """Default value for proto, shouldn't be used."""

    BLOCK_ALL: EnrollmentLevel.ValueType = ...  # 1
    """Service is enrolled in Access Approval for all requests"""

class EnrollmentLevel(_EnrollmentLevel, metaclass=_EnrollmentLevelEnumTypeWrapper):
    """Represents the type of enrollment for a given service to Access Approval."""
    pass

ENROLLMENT_LEVEL_UNSPECIFIED: EnrollmentLevel.ValueType = ...  # 0
"""Default value for proto, shouldn't be used."""

BLOCK_ALL: EnrollmentLevel.ValueType = ...  # 1
"""Service is enrolled in Access Approval for all requests"""

global___EnrollmentLevel = EnrollmentLevel


class AccessLocations(google.protobuf.message.Message):
    """Home office and physical location of the principal."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRINCIPAL_OFFICE_COUNTRY_FIELD_NUMBER: builtins.int
    PRINCIPAL_PHYSICAL_LOCATION_COUNTRY_FIELD_NUMBER: builtins.int
    principal_office_country: typing.Text = ...
    """The "home office" location of the principal. A two-letter country code
    (ISO 3166-1 alpha-2), such as "US", "DE" or "GB" or a region code. In some
    limited situations Google systems may refer refer to a region code instead
    of a country code.
    Possible Region Codes:

    - ASI: Asia
    - EUR: Europe
    - OCE: Oceania
    - AFR: Africa
    - NAM: North America
    - SAM: South America
    - ANT: Antarctica
    - ANY: Any location
    """

    principal_physical_location_country: typing.Text = ...
    """Physical location of the principal at the time of the access. A
    two-letter country code (ISO 3166-1 alpha-2), such as "US", "DE" or "GB" or
    a region code. In some limited situations Google systems may refer refer to
    a region code instead of a country code.
    Possible Region Codes:

    - ASI: Asia
    - EUR: Europe
    - OCE: Oceania
    - AFR: Africa
    - NAM: North America
    - SAM: South America
    - ANT: Antarctica
    - ANY: Any location
    """

    def __init__(self,
        *,
        principal_office_country : typing.Text = ...,
        principal_physical_location_country : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["principal_office_country",b"principal_office_country","principal_physical_location_country",b"principal_physical_location_country"]) -> None: ...
global___AccessLocations = AccessLocations

class AccessReason(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNSPECIFIED: AccessReason.Type.ValueType = ...  # 0
        """Default value for proto, shouldn't be used."""

        CUSTOMER_INITIATED_SUPPORT: AccessReason.Type.ValueType = ...  # 1
        """Customer made a request or raised an issue that required the principal to
        access customer data. `detail` is of the form ("#####" is the issue ID):

        - "Feedback Report: #####"
        - "Case Number: #####"
        - "Case ID: #####"
        - "E-PIN Reference: #####"
        - "Google-#####"
        - "T-#####"
        """

        GOOGLE_INITIATED_SERVICE: AccessReason.Type.ValueType = ...  # 2
        """The principal accessed customer data in order to diagnose or resolve a
        suspected issue in services or a known outage. Often this access is used
        to confirm that customers are not affected by a suspected service issue
        or to remediate a reversible system issue.
        """

        GOOGLE_INITIATED_REVIEW: AccessReason.Type.ValueType = ...  # 3
        """Google initiated service for security, fraud, abuse, or compliance
        purposes.
        """

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """Type of access justification."""
        pass

    TYPE_UNSPECIFIED: AccessReason.Type.ValueType = ...  # 0
    """Default value for proto, shouldn't be used."""

    CUSTOMER_INITIATED_SUPPORT: AccessReason.Type.ValueType = ...  # 1
    """Customer made a request or raised an issue that required the principal to
    access customer data. `detail` is of the form ("#####" is the issue ID):

    - "Feedback Report: #####"
    - "Case Number: #####"
    - "Case ID: #####"
    - "E-PIN Reference: #####"
    - "Google-#####"
    - "T-#####"
    """

    GOOGLE_INITIATED_SERVICE: AccessReason.Type.ValueType = ...  # 2
    """The principal accessed customer data in order to diagnose or resolve a
    suspected issue in services or a known outage. Often this access is used
    to confirm that customers are not affected by a suspected service issue
    or to remediate a reversible system issue.
    """

    GOOGLE_INITIATED_REVIEW: AccessReason.Type.ValueType = ...  # 3
    """Google initiated service for security, fraud, abuse, or compliance
    purposes.
    """


    TYPE_FIELD_NUMBER: builtins.int
    DETAIL_FIELD_NUMBER: builtins.int
    type: global___AccessReason.Type.ValueType = ...
    """Type of access justification."""

    detail: typing.Text = ...
    """More detail about certain reason types. See comments for each type above."""

    def __init__(self,
        *,
        type : global___AccessReason.Type.ValueType = ...,
        detail : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["detail",b"detail","type",b"type"]) -> None: ...
global___AccessReason = AccessReason

class ApproveDecision(google.protobuf.message.Message):
    """A decision that has been made to approve access to a resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    APPROVE_TIME_FIELD_NUMBER: builtins.int
    EXPIRE_TIME_FIELD_NUMBER: builtins.int
    @property
    def approve_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time at which approval was granted."""
        pass
    @property
    def expire_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time at which the approval expires."""
        pass
    def __init__(self,
        *,
        approve_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        expire_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["approve_time",b"approve_time","expire_time",b"expire_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["approve_time",b"approve_time","expire_time",b"expire_time"]) -> None: ...
global___ApproveDecision = ApproveDecision

class DismissDecision(google.protobuf.message.Message):
    """A decision that has been made to dismiss an approval request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DISMISS_TIME_FIELD_NUMBER: builtins.int
    @property
    def dismiss_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time at which the approval request was dismissed."""
        pass
    def __init__(self,
        *,
        dismiss_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dismiss_time",b"dismiss_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dismiss_time",b"dismiss_time"]) -> None: ...
global___DismissDecision = DismissDecision

class ResourceProperties(google.protobuf.message.Message):
    """The properties associated with the resource of the request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXCLUDES_DESCENDANTS_FIELD_NUMBER: builtins.int
    excludes_descendants: builtins.bool = ...
    """Whether an approval will exclude the descendants of the resource being
    requested.
    """

    def __init__(self,
        *,
        excludes_descendants : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["excludes_descendants",b"excludes_descendants"]) -> None: ...
global___ResourceProperties = ResourceProperties

class ApprovalRequest(google.protobuf.message.Message):
    """A request for the customer to approve access to a resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    REQUESTED_RESOURCE_NAME_FIELD_NUMBER: builtins.int
    REQUESTED_RESOURCE_PROPERTIES_FIELD_NUMBER: builtins.int
    REQUESTED_REASON_FIELD_NUMBER: builtins.int
    REQUESTED_LOCATIONS_FIELD_NUMBER: builtins.int
    REQUEST_TIME_FIELD_NUMBER: builtins.int
    REQUESTED_EXPIRATION_FIELD_NUMBER: builtins.int
    APPROVE_FIELD_NUMBER: builtins.int
    DISMISS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name of the request. Format is
    "{projects|folders|organizations}/{id}/approvalRequests/{approval_request_id}".
    """

    requested_resource_name: typing.Text = ...
    """The resource for which approval is being requested. The format of the
    resource name is defined at
    https://cloud.google.com/apis/design/resource_names. The resource name here
    may either be a "full" resource name (e.g.
    "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative"
    resource name (e.g. "shelves/shelf1/books/book2") as described in the
    resource name specification.
    """

    @property
    def requested_resource_properties(self) -> global___ResourceProperties:
        """Properties related to the resource represented by requested_resource_name."""
        pass
    @property
    def requested_reason(self) -> global___AccessReason:
        """The justification for which approval is being requested."""
        pass
    @property
    def requested_locations(self) -> global___AccessLocations:
        """The locations for which approval is being requested."""
        pass
    @property
    def request_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The time at which approval was requested."""
        pass
    @property
    def requested_expiration(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The requested expiration for the approval. If the request is approved,
        access will be granted from the time of approval until the expiration time.
        """
        pass
    @property
    def approve(self) -> global___ApproveDecision:
        """Access was approved."""
        pass
    @property
    def dismiss(self) -> global___DismissDecision:
        """The request was dismissed."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        requested_resource_name : typing.Text = ...,
        requested_resource_properties : typing.Optional[global___ResourceProperties] = ...,
        requested_reason : typing.Optional[global___AccessReason] = ...,
        requested_locations : typing.Optional[global___AccessLocations] = ...,
        request_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        requested_expiration : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        approve : typing.Optional[global___ApproveDecision] = ...,
        dismiss : typing.Optional[global___DismissDecision] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["approve",b"approve","decision",b"decision","dismiss",b"dismiss","request_time",b"request_time","requested_expiration",b"requested_expiration","requested_locations",b"requested_locations","requested_reason",b"requested_reason","requested_resource_properties",b"requested_resource_properties"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["approve",b"approve","decision",b"decision","dismiss",b"dismiss","name",b"name","request_time",b"request_time","requested_expiration",b"requested_expiration","requested_locations",b"requested_locations","requested_reason",b"requested_reason","requested_resource_name",b"requested_resource_name","requested_resource_properties",b"requested_resource_properties"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["decision",b"decision"]) -> typing.Optional[typing_extensions.Literal["approve","dismiss"]]: ...
global___ApprovalRequest = ApprovalRequest

class EnrolledService(google.protobuf.message.Message):
    """Represents the enrollment of a cloud resource into a specific service."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLOUD_PRODUCT_FIELD_NUMBER: builtins.int
    ENROLLMENT_LEVEL_FIELD_NUMBER: builtins.int
    cloud_product: typing.Text = ...
    """The product for which Access Approval will be enrolled. Allowed values are
    listed below (case-sensitive):

    - all
    - appengine.googleapis.com
    - bigquery.googleapis.com
    - bigtable.googleapis.com
    - cloudkms.googleapis.com
    - compute.googleapis.com
    - dataflow.googleapis.com
    - iam.googleapis.com
    - pubsub.googleapis.com
    - storage.googleapis.com
    """

    enrollment_level: global___EnrollmentLevel.ValueType = ...
    """The enrollment level of the service."""

    def __init__(self,
        *,
        cloud_product : typing.Text = ...,
        enrollment_level : global___EnrollmentLevel.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cloud_product",b"cloud_product","enrollment_level",b"enrollment_level"]) -> None: ...
global___EnrolledService = EnrolledService

class AccessApprovalSettings(google.protobuf.message.Message):
    """Settings on a Project/Folder/Organization related to Access Approval."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NOTIFICATION_EMAILS_FIELD_NUMBER: builtins.int
    ENROLLED_SERVICES_FIELD_NUMBER: builtins.int
    ENROLLED_ANCESTOR_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name of the settings. Format is one of:

    - "projects/{project_id}/accessApprovalSettings"
    - "folders/{folder_id}/accessApprovalSettings"
    - "organizations/{organization_id}/accessApprovalSettings"
    """

    @property
    def notification_emails(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """A list of email addresses to which notifications relating to approval
        requests should be sent. Notifications relating to a resource will be sent
        to all emails in the settings of ancestor resources of that resource. A
        maximum of 50 email addresses are allowed.
        """
        pass
    @property
    def enrolled_services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EnrolledService]:
        """A list of Google Cloud Services for which the given resource has Access
        Approval enrolled. Access requests for the resource given by name against
        any of these services contained here will be required to have explicit
        approval. If name refers to an organization, enrollment can be done for
        individual services. If name refers to a folder or project, enrollment can
        only be done on an all or nothing basis.

        If a cloud_product is repeated in this list, the first entry will be
        honored and all following entries will be discarded. A maximum of 10
        enrolled services will be enforced, to be expanded as the set of supported
        services is expanded.
        """
        pass
    enrolled_ancestor: builtins.bool = ...
    """Output only. This field is read only (not settable via
    UpdateAccessAccessApprovalSettings method). If the field is true, that
    indicates that at least one service is enrolled for Access Approval in one
    or more ancestors of the Project or Folder (this field will always be
    unset for the organization since organizations do not have ancestors).
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        notification_emails : typing.Optional[typing.Iterable[typing.Text]] = ...,
        enrolled_services : typing.Optional[typing.Iterable[global___EnrolledService]] = ...,
        enrolled_ancestor : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["enrolled_ancestor",b"enrolled_ancestor","enrolled_services",b"enrolled_services","name",b"name","notification_emails",b"notification_emails"]) -> None: ...
global___AccessApprovalSettings = AccessApprovalSettings

class ListApprovalRequestsMessage(google.protobuf.message.Message):
    """Request to list approval requests."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """The parent resource. This may be "projects/{project_id}",
    "folders/{folder_id}", or "organizations/{organization_id}".
    """

    filter: typing.Text = ...
    """A filter on the type of approval requests to retrieve. Must be one of the
    following values:

    - [not set]: Requests that are pending or have active approvals.
    - ALL: All requests.
    - PENDING: Only pending requests.
    - ACTIVE: Only active (i.e. currently approved) requests.
    - DISMISSED: Only dismissed (including expired) requests.
    """

    page_size: builtins.int = ...
    """Requested page size."""

    page_token: typing.Text = ...
    """A token identifying the page of results to return."""

    def __init__(self,
        *,
        parent : typing.Text = ...,
        filter : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListApprovalRequestsMessage = ListApprovalRequestsMessage

class ListApprovalRequestsResponse(google.protobuf.message.Message):
    """Response to listing of ApprovalRequest objects."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    APPROVAL_REQUESTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def approval_requests(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApprovalRequest]:
        """Approval request details."""
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results, or empty if there are no more."""

    def __init__(self,
        *,
        approval_requests : typing.Optional[typing.Iterable[global___ApprovalRequest]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["approval_requests",b"approval_requests","next_page_token",b"next_page_token"]) -> None: ...
global___ListApprovalRequestsResponse = ListApprovalRequestsResponse

class GetApprovalRequestMessage(google.protobuf.message.Message):
    """Request to get an approval request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the approval request to retrieve."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetApprovalRequestMessage = GetApprovalRequestMessage

class ApproveApprovalRequestMessage(google.protobuf.message.Message):
    """Request to approve an ApprovalRequest."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    EXPIRE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the approval request to approve."""

    @property
    def expire_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The expiration time of this approval."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        expire_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expire_time",b"expire_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expire_time",b"expire_time","name",b"name"]) -> None: ...
global___ApproveApprovalRequestMessage = ApproveApprovalRequestMessage

class DismissApprovalRequestMessage(google.protobuf.message.Message):
    """Request to dismiss an approval request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the ApprovalRequest to dismiss."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DismissApprovalRequestMessage = DismissApprovalRequestMessage

class GetAccessApprovalSettingsMessage(google.protobuf.message.Message):
    """Request to get access approval settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the AccessApprovalSettings to retrieve."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetAccessApprovalSettingsMessage = GetAccessApprovalSettingsMessage

class UpdateAccessApprovalSettingsMessage(google.protobuf.message.Message):
    """Request to update access approval settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SETTINGS_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def settings(self) -> global___AccessApprovalSettings:
        """The new AccessApprovalSettings."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The update mask applies to the settings. Only the top level fields of
        AccessApprovalSettings (notification_emails & enrolled_services) are
        supported. For each field, if it is included, the currently stored value
        will be entirely overwritten with the value of the field passed in this
        request.

        For the `FieldMask` definition, see
        https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
        If this field is left unset, only the notification_emails field will be
        updated.
        """
        pass
    def __init__(self,
        *,
        settings : typing.Optional[global___AccessApprovalSettings] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["settings",b"settings","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["settings",b"settings","update_mask",b"update_mask"]) -> None: ...
global___UpdateAccessApprovalSettingsMessage = UpdateAccessApprovalSettingsMessage

class DeleteAccessApprovalSettingsMessage(google.protobuf.message.Message):
    """Request to delete access approval settings."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the AccessApprovalSettings to delete."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteAccessApprovalSettingsMessage = DeleteAccessApprovalSettingsMessage

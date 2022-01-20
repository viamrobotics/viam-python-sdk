"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.osconfig.v1alpha.os_policy_pb2
import google.cloud.osconfig.v1alpha.osconfig_common_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OSPolicyAssignment(google.protobuf.message.Message):
    """OS policy assignment is an API resource that is used to
    apply a set of OS policies to a dynamically targeted group of Compute Engine
    VM instances.

    An OS policy is used to define the desired state configuration for a
    Compute Engine VM instance through a set of configuration resources that
    provide capabilities such as installing or removing software packages, or
    executing a script.

    For more information, see [OS policy and OS policy
    assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _RolloutState:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RolloutStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RolloutState.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ROLLOUT_STATE_UNSPECIFIED: OSPolicyAssignment.RolloutState.ValueType = ...  # 0
        """Invalid value"""

        IN_PROGRESS: OSPolicyAssignment.RolloutState.ValueType = ...  # 1
        """The rollout is in progress."""

        CANCELLING: OSPolicyAssignment.RolloutState.ValueType = ...  # 2
        """The rollout is being cancelled."""

        CANCELLED: OSPolicyAssignment.RolloutState.ValueType = ...  # 3
        """The rollout is cancelled."""

        SUCCEEDED: OSPolicyAssignment.RolloutState.ValueType = ...  # 4
        """The rollout has completed successfully."""

    class RolloutState(_RolloutState, metaclass=_RolloutStateEnumTypeWrapper):
        """OS policy assignment rollout state"""
        pass

    ROLLOUT_STATE_UNSPECIFIED: OSPolicyAssignment.RolloutState.ValueType = ...  # 0
    """Invalid value"""

    IN_PROGRESS: OSPolicyAssignment.RolloutState.ValueType = ...  # 1
    """The rollout is in progress."""

    CANCELLING: OSPolicyAssignment.RolloutState.ValueType = ...  # 2
    """The rollout is being cancelled."""

    CANCELLED: OSPolicyAssignment.RolloutState.ValueType = ...  # 3
    """The rollout is cancelled."""

    SUCCEEDED: OSPolicyAssignment.RolloutState.ValueType = ...  # 4
    """The rollout has completed successfully."""


    class LabelSet(google.protobuf.message.Message):
        """Message representing label set.
        * A label is a key value pair set for a VM.
        * A LabelSet is a set of labels.
        * Labels within a LabelSet are ANDed. In other words, a LabelSet is
          applicable for a VM only if it matches all the labels in the
          LabelSet.
        * Example: A LabelSet with 2 labels: `env=prod` and `type=webserver` will
                   only be applicable for those VMs with both labels
                   present.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class LabelsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...
            def __init__(self,
                *,
                key : typing.Text = ...,
                value : typing.Text = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        LABELS_FIELD_NUMBER: builtins.int
        @property
        def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
            """Labels are identified by key/value pairs in this map.
            A VM should contain all the key/value pairs specified in this
            map to be selected.
            """
            pass
        def __init__(self,
            *,
            labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["labels",b"labels"]) -> None: ...

    class InstanceFilter(google.protobuf.message.Message):
        """Message to represent the filters to select VMs for an assignment"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ALL_FIELD_NUMBER: builtins.int
        OS_SHORT_NAMES_FIELD_NUMBER: builtins.int
        INCLUSION_LABELS_FIELD_NUMBER: builtins.int
        EXCLUSION_LABELS_FIELD_NUMBER: builtins.int
        all: builtins.bool = ...
        """Target all VMs in the project. If true, no other criteria is
        permitted.
        """

        @property
        def os_short_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            """A VM is included if it's OS short name matches with any of the
            values provided in this list.
            """
            pass
        @property
        def inclusion_labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OSPolicyAssignment.LabelSet]:
            """List of label sets used for VM inclusion.

            If the list has more than one `LabelSet`, the VM is included if any
            of the label sets are applicable for the VM.
            """
            pass
        @property
        def exclusion_labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OSPolicyAssignment.LabelSet]:
            """List of label sets used for VM exclusion.

            If the list has more than one label set, the VM is excluded if any
            of the label sets are applicable for the VM.

            This filter is applied last in the filtering chain and therefore a
            VM is guaranteed to be excluded if it satisfies one of the below
            label sets.
            """
            pass
        def __init__(self,
            *,
            all : builtins.bool = ...,
            os_short_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
            inclusion_labels : typing.Optional[typing.Iterable[global___OSPolicyAssignment.LabelSet]] = ...,
            exclusion_labels : typing.Optional[typing.Iterable[global___OSPolicyAssignment.LabelSet]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["all",b"all","exclusion_labels",b"exclusion_labels","inclusion_labels",b"inclusion_labels","os_short_names",b"os_short_names"]) -> None: ...

    class Rollout(google.protobuf.message.Message):
        """Message to configure the rollout at the zonal level for the OS policy
        assignment.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        DISRUPTION_BUDGET_FIELD_NUMBER: builtins.int
        MIN_WAIT_DURATION_FIELD_NUMBER: builtins.int
        @property
        def disruption_budget(self) -> google.cloud.osconfig.v1alpha.osconfig_common_pb2.FixedOrPercent:
            """Required. The maximum number (or percentage) of VMs per zone to disrupt at
            any given moment.
            """
            pass
        @property
        def min_wait_duration(self) -> google.protobuf.duration_pb2.Duration:
            """Required. This determines the minimum duration of time to wait after the
            configuration changes are applied through the current rollout. A
            VM continues to count towards the `disruption_budget` at least
            until this duration of time has passed after configuration changes are
            applied.
            """
            pass
        def __init__(self,
            *,
            disruption_budget : typing.Optional[google.cloud.osconfig.v1alpha.osconfig_common_pb2.FixedOrPercent] = ...,
            min_wait_duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["disruption_budget",b"disruption_budget","min_wait_duration",b"min_wait_duration"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["disruption_budget",b"disruption_budget","min_wait_duration",b"min_wait_duration"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OS_POLICIES_FIELD_NUMBER: builtins.int
    INSTANCE_FILTER_FIELD_NUMBER: builtins.int
    ROLLOUT_FIELD_NUMBER: builtins.int
    REVISION_ID_FIELD_NUMBER: builtins.int
    REVISION_CREATE_TIME_FIELD_NUMBER: builtins.int
    ROLLOUT_STATE_FIELD_NUMBER: builtins.int
    BASELINE_FIELD_NUMBER: builtins.int
    DELETED_FIELD_NUMBER: builtins.int
    RECONCILING_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Resource name.

    Format:
    `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id}`

    This field is ignored when you create an OS policy assignment.
    """

    description: typing.Text = ...
    """OS policy assignment description.
    Length of the description is limited to 1024 characters.
    """

    @property
    def os_policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.osconfig.v1alpha.os_policy_pb2.OSPolicy]:
        """Required. List of OS policies to be applied to the VMs."""
        pass
    @property
    def instance_filter(self) -> global___OSPolicyAssignment.InstanceFilter:
        """Required. Filter to select VMs."""
        pass
    @property
    def rollout(self) -> global___OSPolicyAssignment.Rollout:
        """Required. Rollout to deploy the OS policy assignment.
        A rollout is triggered in the following situations:
        1) OSPolicyAssignment is created.
        2) OSPolicyAssignment is updated and the update contains changes to one of
        the following fields:
           - instance_filter
           - os_policies
        3) OSPolicyAssignment is deleted.
        """
        pass
    revision_id: typing.Text = ...
    """Output only. The assignment revision ID
    A new revision is committed whenever a rollout is triggered for a OS policy
    assignment
    """

    @property
    def revision_create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The timestamp that the revision was created."""
        pass
    rollout_state: global___OSPolicyAssignment.RolloutState.ValueType = ...
    """Output only. OS policy assignment rollout state"""

    baseline: builtins.bool = ...
    """Output only. Indicates that this revision has been successfully rolled out in this zone
    and new VMs will be assigned OS policies from this revision.

    For a given OS policy assignment, there is only one revision with a value
    of `true` for this field.
    """

    deleted: builtins.bool = ...
    """Output only. Indicates that this revision deletes the OS policy assignment."""

    reconciling: builtins.bool = ...
    """Output only. Indicates that reconciliation is in progress for the revision.
    This value is `true` when the `rollout_state` is one of:
    * IN_PROGRESS
    * CANCELLING
    """

    uid: typing.Text = ...
    """Output only. Server generated unique id for the OS policy assignment resource."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        os_policies : typing.Optional[typing.Iterable[google.cloud.osconfig.v1alpha.os_policy_pb2.OSPolicy]] = ...,
        instance_filter : typing.Optional[global___OSPolicyAssignment.InstanceFilter] = ...,
        rollout : typing.Optional[global___OSPolicyAssignment.Rollout] = ...,
        revision_id : typing.Text = ...,
        revision_create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        rollout_state : global___OSPolicyAssignment.RolloutState.ValueType = ...,
        baseline : builtins.bool = ...,
        deleted : builtins.bool = ...,
        reconciling : builtins.bool = ...,
        uid : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["instance_filter",b"instance_filter","revision_create_time",b"revision_create_time","rollout",b"rollout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["baseline",b"baseline","deleted",b"deleted","description",b"description","instance_filter",b"instance_filter","name",b"name","os_policies",b"os_policies","reconciling",b"reconciling","revision_create_time",b"revision_create_time","revision_id",b"revision_id","rollout",b"rollout","rollout_state",b"rollout_state","uid",b"uid"]) -> None: ...
global___OSPolicyAssignment = OSPolicyAssignment

class OSPolicyAssignmentOperationMetadata(google.protobuf.message.Message):
    """OS policy assignment operation metadata provided by OS policy assignment API
    methods that return long running operations.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _APIMethod:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _APIMethodEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_APIMethod.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        API_METHOD_UNSPECIFIED: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 0
        """Invalid value"""

        CREATE: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 1
        """Create OS policy assignment API method"""

        UPDATE: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 2
        """Update OS policy assignment API method"""

        DELETE: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 3
        """Delete OS policy assignment API method"""

    class APIMethod(_APIMethod, metaclass=_APIMethodEnumTypeWrapper):
        """The OS policy assignment API method."""
        pass

    API_METHOD_UNSPECIFIED: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 0
    """Invalid value"""

    CREATE: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 1
    """Create OS policy assignment API method"""

    UPDATE: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 2
    """Update OS policy assignment API method"""

    DELETE: OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...  # 3
    """Delete OS policy assignment API method"""


    class _RolloutState:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _RolloutStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RolloutState.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ROLLOUT_STATE_UNSPECIFIED: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 0
        """Invalid value"""

        IN_PROGRESS: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 1
        """The rollout is in progress."""

        CANCELLING: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 2
        """The rollout is being cancelled."""

        CANCELLED: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 3
        """The rollout is cancelled."""

        SUCCEEDED: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 4
        """The rollout has completed successfully."""

    class RolloutState(_RolloutState, metaclass=_RolloutStateEnumTypeWrapper):
        """State of the rollout"""
        pass

    ROLLOUT_STATE_UNSPECIFIED: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 0
    """Invalid value"""

    IN_PROGRESS: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 1
    """The rollout is in progress."""

    CANCELLING: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 2
    """The rollout is being cancelled."""

    CANCELLED: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 3
    """The rollout is cancelled."""

    SUCCEEDED: OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...  # 4
    """The rollout has completed successfully."""


    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: builtins.int
    API_METHOD_FIELD_NUMBER: builtins.int
    ROLLOUT_STATE_FIELD_NUMBER: builtins.int
    ROLLOUT_START_TIME_FIELD_NUMBER: builtins.int
    ROLLOUT_UPDATE_TIME_FIELD_NUMBER: builtins.int
    os_policy_assignment: typing.Text = ...
    """Reference to the `OSPolicyAssignment` API resource.

    Format:
    `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}`
    """

    api_method: global___OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...
    """The OS policy assignment API method."""

    rollout_state: global___OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...
    """State of the rollout"""

    @property
    def rollout_start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Rollout start time"""
        pass
    @property
    def rollout_update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Rollout update time"""
        pass
    def __init__(self,
        *,
        os_policy_assignment : typing.Text = ...,
        api_method : global___OSPolicyAssignmentOperationMetadata.APIMethod.ValueType = ...,
        rollout_state : global___OSPolicyAssignmentOperationMetadata.RolloutState.ValueType = ...,
        rollout_start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        rollout_update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["rollout_start_time",b"rollout_start_time","rollout_update_time",b"rollout_update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_method",b"api_method","os_policy_assignment",b"os_policy_assignment","rollout_start_time",b"rollout_start_time","rollout_state",b"rollout_state","rollout_update_time",b"rollout_update_time"]) -> None: ...
global___OSPolicyAssignmentOperationMetadata = OSPolicyAssignmentOperationMetadata

class CreateOSPolicyAssignmentRequest(google.protobuf.message.Message):
    """A request message to create an OS policy assignment"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: builtins.int
    OS_POLICY_ASSIGNMENT_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent resource name in the form:
    projects/{project}/locations/{location}
    """

    @property
    def os_policy_assignment(self) -> global___OSPolicyAssignment:
        """Required. The OS policy assignment to be created."""
        pass
    os_policy_assignment_id: typing.Text = ...
    """Required. The logical name of the OS policy assignment in the project
    with the following restrictions:

    * Must contain only lowercase letters, numbers, and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.
    * Must be unique within the project.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        os_policy_assignment : typing.Optional[global___OSPolicyAssignment] = ...,
        os_policy_assignment_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["os_policy_assignment",b"os_policy_assignment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["os_policy_assignment",b"os_policy_assignment","os_policy_assignment_id",b"os_policy_assignment_id","parent",b"parent"]) -> None: ...
global___CreateOSPolicyAssignmentRequest = CreateOSPolicyAssignmentRequest

class UpdateOSPolicyAssignmentRequest(google.protobuf.message.Message):
    """A request message to update an OS policy assignment"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OS_POLICY_ASSIGNMENT_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def os_policy_assignment(self) -> global___OSPolicyAssignment:
        """Required. The updated OS policy assignment."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. Field mask that controls which fields of the assignment should be updated."""
        pass
    def __init__(self,
        *,
        os_policy_assignment : typing.Optional[global___OSPolicyAssignment] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["os_policy_assignment",b"os_policy_assignment","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["os_policy_assignment",b"os_policy_assignment","update_mask",b"update_mask"]) -> None: ...
global___UpdateOSPolicyAssignmentRequest = UpdateOSPolicyAssignmentRequest

class GetOSPolicyAssignmentRequest(google.protobuf.message.Message):
    """A request message to get an OS policy assignment"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of OS policy assignment.

    Format:
    `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetOSPolicyAssignmentRequest = GetOSPolicyAssignmentRequest

class ListOSPolicyAssignmentsRequest(google.protobuf.message.Message):
    """A request message to list OS policy assignments for a parent resource"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent resource name."""

    page_size: builtins.int = ...
    """The maximum number of assignments to return."""

    page_token: typing.Text = ...
    """A pagination token returned from a previous call to
    `ListOSPolicyAssignments` that indicates where this listing should continue
    from.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListOSPolicyAssignmentsRequest = ListOSPolicyAssignmentsRequest

class ListOSPolicyAssignmentsResponse(google.protobuf.message.Message):
    """A response message for listing all assignments under given parent."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OS_POLICY_ASSIGNMENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def os_policy_assignments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OSPolicyAssignment]:
        """The list of assignments"""
        pass
    next_page_token: typing.Text = ...
    """The pagination token to retrieve the next page of OS policy assignments."""

    def __init__(self,
        *,
        os_policy_assignments : typing.Optional[typing.Iterable[global___OSPolicyAssignment]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","os_policy_assignments",b"os_policy_assignments"]) -> None: ...
global___ListOSPolicyAssignmentsResponse = ListOSPolicyAssignmentsResponse

class ListOSPolicyAssignmentRevisionsRequest(google.protobuf.message.Message):
    """A request message to list revisions for a OS policy assignment"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the OS policy assignment to list revisions for."""

    page_size: builtins.int = ...
    """The maximum number of revisions to return."""

    page_token: typing.Text = ...
    """A pagination token returned from a previous call to
    `ListOSPolicyAssignmentRevisions` that indicates where this listing should
    continue from.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___ListOSPolicyAssignmentRevisionsRequest = ListOSPolicyAssignmentRevisionsRequest

class ListOSPolicyAssignmentRevisionsResponse(google.protobuf.message.Message):
    """A response message for listing all revisions for a OS policy assignment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OS_POLICY_ASSIGNMENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def os_policy_assignments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OSPolicyAssignment]:
        """The OS policy assignment revisions"""
        pass
    next_page_token: typing.Text = ...
    """The pagination token to retrieve the next page of OS policy assignment
    revisions.
    """

    def __init__(self,
        *,
        os_policy_assignments : typing.Optional[typing.Iterable[global___OSPolicyAssignment]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","os_policy_assignments",b"os_policy_assignments"]) -> None: ...
global___ListOSPolicyAssignmentRevisionsResponse = ListOSPolicyAssignmentRevisionsResponse

class DeleteOSPolicyAssignmentRequest(google.protobuf.message.Message):
    """A request message for deleting a OS policy assignment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the OS policy assignment to be deleted"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteOSPolicyAssignmentRequest = DeleteOSPolicyAssignmentRequest

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _OSPolicyComplianceState:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _OSPolicyComplianceStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OSPolicyComplianceState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED: OSPolicyComplianceState.ValueType = ...  # 0
    """Default value. This value is unused."""

    COMPLIANT: OSPolicyComplianceState.ValueType = ...  # 1
    """Compliant state."""

    NON_COMPLIANT: OSPolicyComplianceState.ValueType = ...  # 2
    """Non-compliant state"""

    UNKNOWN: OSPolicyComplianceState.ValueType = ...  # 3
    """Unknown compliance state."""

    NO_OS_POLICIES_APPLICABLE: OSPolicyComplianceState.ValueType = ...  # 4
    """No applicable OS policies were found for the instance.
    This state is only applicable to the instance.
    """

class OSPolicyComplianceState(_OSPolicyComplianceState, metaclass=_OSPolicyComplianceStateEnumTypeWrapper):
    """Supported OSPolicy compliance states."""
    pass

OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED: OSPolicyComplianceState.ValueType = ...  # 0
"""Default value. This value is unused."""

COMPLIANT: OSPolicyComplianceState.ValueType = ...  # 1
"""Compliant state."""

NON_COMPLIANT: OSPolicyComplianceState.ValueType = ...  # 2
"""Non-compliant state"""

UNKNOWN: OSPolicyComplianceState.ValueType = ...  # 3
"""Unknown compliance state."""

NO_OS_POLICIES_APPLICABLE: OSPolicyComplianceState.ValueType = ...  # 4
"""No applicable OS policies were found for the instance.
This state is only applicable to the instance.
"""

global___OSPolicyComplianceState = OSPolicyComplianceState


class OSPolicyResourceConfigStep(google.protobuf.message.Message):
    """Step performed by the OS Config agent for configuring an `OSPolicyResource`
    to its desired state.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Type:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNSPECIFIED: OSPolicyResourceConfigStep.Type.ValueType = ...  # 0
        """Default value. This value is unused."""

        VALIDATION: OSPolicyResourceConfigStep.Type.ValueType = ...  # 1
        """Validation to detect resource conflicts, schema errors, etc."""

        DESIRED_STATE_CHECK: OSPolicyResourceConfigStep.Type.ValueType = ...  # 2
        """Check the current desired state status of the resource."""

        DESIRED_STATE_ENFORCEMENT: OSPolicyResourceConfigStep.Type.ValueType = ...  # 3
        """Enforce the desired state for a resource that is not in desired state."""

        DESIRED_STATE_CHECK_POST_ENFORCEMENT: OSPolicyResourceConfigStep.Type.ValueType = ...  # 4
        """Re-check desired state status for a resource after enforcement of all
        resources in the current configuration run.

        This step is used to determine the final desired state status for the
        resource. It accounts for any resources that might have drifted from
        their desired state due to side effects from configuring other resources
        during the current configuration run.
        """

    class Type(_Type, metaclass=_TypeEnumTypeWrapper):
        """Supported configuration step types"""
        pass

    TYPE_UNSPECIFIED: OSPolicyResourceConfigStep.Type.ValueType = ...  # 0
    """Default value. This value is unused."""

    VALIDATION: OSPolicyResourceConfigStep.Type.ValueType = ...  # 1
    """Validation to detect resource conflicts, schema errors, etc."""

    DESIRED_STATE_CHECK: OSPolicyResourceConfigStep.Type.ValueType = ...  # 2
    """Check the current desired state status of the resource."""

    DESIRED_STATE_ENFORCEMENT: OSPolicyResourceConfigStep.Type.ValueType = ...  # 3
    """Enforce the desired state for a resource that is not in desired state."""

    DESIRED_STATE_CHECK_POST_ENFORCEMENT: OSPolicyResourceConfigStep.Type.ValueType = ...  # 4
    """Re-check desired state status for a resource after enforcement of all
    resources in the current configuration run.

    This step is used to determine the final desired state status for the
    resource. It accounts for any resources that might have drifted from
    their desired state due to side effects from configuring other resources
    during the current configuration run.
    """


    class _Outcome:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _OutcomeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Outcome.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        OUTCOME_UNSPECIFIED: OSPolicyResourceConfigStep.Outcome.ValueType = ...  # 0
        """Default value. This value is unused."""

        SUCCEEDED: OSPolicyResourceConfigStep.Outcome.ValueType = ...  # 1
        """The step succeeded."""

        FAILED: OSPolicyResourceConfigStep.Outcome.ValueType = ...  # 2
        """The step failed."""

    class Outcome(_Outcome, metaclass=_OutcomeEnumTypeWrapper):
        """Supported outcomes for a configuration step."""
        pass

    OUTCOME_UNSPECIFIED: OSPolicyResourceConfigStep.Outcome.ValueType = ...  # 0
    """Default value. This value is unused."""

    SUCCEEDED: OSPolicyResourceConfigStep.Outcome.ValueType = ...  # 1
    """The step succeeded."""

    FAILED: OSPolicyResourceConfigStep.Outcome.ValueType = ...  # 2
    """The step failed."""


    TYPE_FIELD_NUMBER: builtins.int
    OUTCOME_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    type: global___OSPolicyResourceConfigStep.Type.ValueType = ...
    """Configuration step type."""

    outcome: global___OSPolicyResourceConfigStep.Outcome.ValueType = ...
    """Outcome of the configuration step."""

    error_message: typing.Text = ...
    """An error message recorded during the execution of this step.
    Only populated when outcome is FAILED.
    """

    def __init__(self,
        *,
        type : global___OSPolicyResourceConfigStep.Type.ValueType = ...,
        outcome : global___OSPolicyResourceConfigStep.Outcome.ValueType = ...,
        error_message : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message",b"error_message","outcome",b"outcome","type",b"type"]) -> None: ...
global___OSPolicyResourceConfigStep = OSPolicyResourceConfigStep

class OSPolicyResourceCompliance(google.protobuf.message.Message):
    """Compliance data for an OS policy resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ExecResourceOutput(google.protobuf.message.Message):
        """ExecResource specific output."""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        ENFORCEMENT_OUTPUT_FIELD_NUMBER: builtins.int
        enforcement_output: builtins.bytes = ...
        """Output from Enforcement phase output file (if run).
        Output size is limited to 100K bytes.
        """

        def __init__(self,
            *,
            enforcement_output : builtins.bytes = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["enforcement_output",b"enforcement_output"]) -> None: ...

    OS_POLICY_RESOURCE_ID_FIELD_NUMBER: builtins.int
    CONFIG_STEPS_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    EXEC_RESOURCE_OUTPUT_FIELD_NUMBER: builtins.int
    os_policy_resource_id: typing.Text = ...
    """The id of the OS policy resource."""

    @property
    def config_steps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OSPolicyResourceConfigStep]:
        """Ordered list of configuration steps taken by the agent for the OS policy
        resource.
        """
        pass
    state: global___OSPolicyComplianceState.ValueType = ...
    """Compliance state of the OS policy resource."""

    @property
    def exec_resource_output(self) -> global___OSPolicyResourceCompliance.ExecResourceOutput:
        """ExecResource specific output."""
        pass
    def __init__(self,
        *,
        os_policy_resource_id : typing.Text = ...,
        config_steps : typing.Optional[typing.Iterable[global___OSPolicyResourceConfigStep]] = ...,
        state : global___OSPolicyComplianceState.ValueType = ...,
        exec_resource_output : typing.Optional[global___OSPolicyResourceCompliance.ExecResourceOutput] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exec_resource_output",b"exec_resource_output","output",b"output"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config_steps",b"config_steps","exec_resource_output",b"exec_resource_output","os_policy_resource_id",b"os_policy_resource_id","output",b"output","state",b"state"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["output",b"output"]) -> typing.Optional[typing_extensions.Literal["exec_resource_output"]]: ...
global___OSPolicyResourceCompliance = OSPolicyResourceCompliance

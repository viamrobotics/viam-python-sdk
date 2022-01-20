"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _JobState:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _JobStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobState.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    JOB_STATE_UNSPECIFIED: JobState.ValueType = ...  # 0
    """The job state is unspecified."""

    JOB_STATE_QUEUED: JobState.ValueType = ...  # 1
    """The job has been just created or resumed and processing has not yet begun."""

    JOB_STATE_PENDING: JobState.ValueType = ...  # 2
    """The service is preparing to run the job."""

    JOB_STATE_RUNNING: JobState.ValueType = ...  # 3
    """The job is in progress."""

    JOB_STATE_SUCCEEDED: JobState.ValueType = ...  # 4
    """The job completed successfully."""

    JOB_STATE_FAILED: JobState.ValueType = ...  # 5
    """The job failed."""

    JOB_STATE_CANCELLING: JobState.ValueType = ...  # 6
    """The job is being cancelled. From this state the job may only go to
    either `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
    """

    JOB_STATE_CANCELLED: JobState.ValueType = ...  # 7
    """The job has been cancelled."""

    JOB_STATE_PAUSED: JobState.ValueType = ...  # 8
    """The job has been stopped, and can be resumed."""

    JOB_STATE_EXPIRED: JobState.ValueType = ...  # 9
    """The job has expired."""

class JobState(_JobState, metaclass=_JobStateEnumTypeWrapper):
    """Describes the state of a job."""
    pass

JOB_STATE_UNSPECIFIED: JobState.ValueType = ...  # 0
"""The job state is unspecified."""

JOB_STATE_QUEUED: JobState.ValueType = ...  # 1
"""The job has been just created or resumed and processing has not yet begun."""

JOB_STATE_PENDING: JobState.ValueType = ...  # 2
"""The service is preparing to run the job."""

JOB_STATE_RUNNING: JobState.ValueType = ...  # 3
"""The job is in progress."""

JOB_STATE_SUCCEEDED: JobState.ValueType = ...  # 4
"""The job completed successfully."""

JOB_STATE_FAILED: JobState.ValueType = ...  # 5
"""The job failed."""

JOB_STATE_CANCELLING: JobState.ValueType = ...  # 6
"""The job is being cancelled. From this state the job may only go to
either `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.
"""

JOB_STATE_CANCELLED: JobState.ValueType = ...  # 7
"""The job has been cancelled."""

JOB_STATE_PAUSED: JobState.ValueType = ...  # 8
"""The job has been stopped, and can be resumed."""

JOB_STATE_EXPIRED: JobState.ValueType = ...  # 9
"""The job has expired."""

global___JobState = JobState


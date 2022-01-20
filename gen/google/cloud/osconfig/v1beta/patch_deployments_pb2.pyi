"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.osconfig.v1beta.patch_jobs_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.type.datetime_pb2
import google.type.dayofweek_pb2
import google.type.timeofday_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PatchDeployment(google.protobuf.message.Message):
    """Patch deployments are configurations that individual patch jobs use to
    complete a patch. These configurations include instance filter, package
    repository settings, and a schedule. For more information about creating and
    managing patch deployments, see [Scheduling patch
    jobs](/compute/docs/os-patch-management/schedule-patch-jobs).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    INSTANCE_FILTER_FIELD_NUMBER: builtins.int
    PATCH_CONFIG_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    ONE_TIME_SCHEDULE_FIELD_NUMBER: builtins.int
    RECURRING_SCHEDULE_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    LAST_EXECUTE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Unique name for the patch deployment resource in a project. The patch
    deployment name is in the form:
    `projects/{project_id}/patchDeployments/{patch_deployment_id}`.
    This field is ignored when you create a new patch deployment.
    """

    description: typing.Text = ...
    """Optional. Description of the patch deployment. Length of the description is limited
    to 1024 characters.
    """

    @property
    def instance_filter(self) -> google.cloud.osconfig.v1beta.patch_jobs_pb2.PatchInstanceFilter:
        """Required. VM instances to patch."""
        pass
    @property
    def patch_config(self) -> google.cloud.osconfig.v1beta.patch_jobs_pb2.PatchConfig:
        """Optional. Patch configuration that is applied."""
        pass
    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """Optional. Duration of the patch. After the duration ends, the patch times out."""
        pass
    @property
    def one_time_schedule(self) -> global___OneTimeSchedule:
        """Required. Schedule a one-time execution."""
        pass
    @property
    def recurring_schedule(self) -> global___RecurringSchedule:
        """Required. Schedule recurring executions."""
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Time the patch deployment was created. Timestamp is in
        <a href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC3339</a>
        text format.
        """
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. Time the patch deployment was last updated. Timestamp is in
        <a href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC3339</a>
        text format.
        """
        pass
    @property
    def last_execute_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last time a patch job was started by this deployment.
        Timestamp is in
        <a href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC3339</a>
        text format.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        instance_filter : typing.Optional[google.cloud.osconfig.v1beta.patch_jobs_pb2.PatchInstanceFilter] = ...,
        patch_config : typing.Optional[google.cloud.osconfig.v1beta.patch_jobs_pb2.PatchConfig] = ...,
        duration : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        one_time_schedule : typing.Optional[global___OneTimeSchedule] = ...,
        recurring_schedule : typing.Optional[global___RecurringSchedule] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_execute_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","duration",b"duration","instance_filter",b"instance_filter","last_execute_time",b"last_execute_time","one_time_schedule",b"one_time_schedule","patch_config",b"patch_config","recurring_schedule",b"recurring_schedule","schedule",b"schedule","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","description",b"description","duration",b"duration","instance_filter",b"instance_filter","last_execute_time",b"last_execute_time","name",b"name","one_time_schedule",b"one_time_schedule","patch_config",b"patch_config","recurring_schedule",b"recurring_schedule","schedule",b"schedule","update_time",b"update_time"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["schedule",b"schedule"]) -> typing.Optional[typing_extensions.Literal["one_time_schedule","recurring_schedule"]]: ...
global___PatchDeployment = PatchDeployment

class OneTimeSchedule(google.protobuf.message.Message):
    """Sets the time for a one time patch deployment. Timestamp is in
    <a href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC3339</a>
    text format.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXECUTE_TIME_FIELD_NUMBER: builtins.int
    @property
    def execute_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Required. The desired patch job execution time."""
        pass
    def __init__(self,
        *,
        execute_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["execute_time",b"execute_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["execute_time",b"execute_time"]) -> None: ...
global___OneTimeSchedule = OneTimeSchedule

class RecurringSchedule(google.protobuf.message.Message):
    """Sets the time for recurring patch deployments."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Frequency:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _FrequencyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Frequency.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        FREQUENCY_UNSPECIFIED: RecurringSchedule.Frequency.ValueType = ...  # 0
        """Invalid. A frequency must be specified."""

        WEEKLY: RecurringSchedule.Frequency.ValueType = ...  # 1
        """Indicates that the frequency should be expressed in terms of
        weeks.
        """

        MONTHLY: RecurringSchedule.Frequency.ValueType = ...  # 2
        """Indicates that the frequency should be expressed in terms of
        months.
        """

        DAILY: RecurringSchedule.Frequency.ValueType = ...  # 3
        """Indicates that the frequency should be expressed in terms of
        days.
        """

    class Frequency(_Frequency, metaclass=_FrequencyEnumTypeWrapper):
        """Specifies the frequency of the recurring patch deployments."""
        pass

    FREQUENCY_UNSPECIFIED: RecurringSchedule.Frequency.ValueType = ...  # 0
    """Invalid. A frequency must be specified."""

    WEEKLY: RecurringSchedule.Frequency.ValueType = ...  # 1
    """Indicates that the frequency should be expressed in terms of
    weeks.
    """

    MONTHLY: RecurringSchedule.Frequency.ValueType = ...  # 2
    """Indicates that the frequency should be expressed in terms of
    months.
    """

    DAILY: RecurringSchedule.Frequency.ValueType = ...  # 3
    """Indicates that the frequency should be expressed in terms of
    days.
    """


    TIME_ZONE_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    TIME_OF_DAY_FIELD_NUMBER: builtins.int
    FREQUENCY_FIELD_NUMBER: builtins.int
    WEEKLY_FIELD_NUMBER: builtins.int
    MONTHLY_FIELD_NUMBER: builtins.int
    LAST_EXECUTE_TIME_FIELD_NUMBER: builtins.int
    NEXT_EXECUTE_TIME_FIELD_NUMBER: builtins.int
    @property
    def time_zone(self) -> google.type.datetime_pb2.TimeZone:
        """Required. Defines the time zone that `time_of_day` is relative to.
        The rules for daylight saving time are determined by the chosen time zone.
        """
        pass
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Optional. The time that the recurring schedule becomes effective.
        Defaults to `create_time` of the patch deployment.
        """
        pass
    @property
    def end_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Optional. The end time at which a recurring patch deployment schedule is no longer
        active.
        """
        pass
    @property
    def time_of_day(self) -> google.type.timeofday_pb2.TimeOfDay:
        """Required. Time of the day to run a recurring deployment."""
        pass
    frequency: global___RecurringSchedule.Frequency.ValueType = ...
    """Required. The frequency unit of this recurring schedule."""

    @property
    def weekly(self) -> global___WeeklySchedule:
        """Required. Schedule with weekly executions."""
        pass
    @property
    def monthly(self) -> global___MonthlySchedule:
        """Required. Schedule with monthly executions."""
        pass
    @property
    def last_execute_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the last patch job ran successfully."""
        pass
    @property
    def next_execute_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time the next patch job is scheduled to run."""
        pass
    def __init__(self,
        *,
        time_zone : typing.Optional[google.type.datetime_pb2.TimeZone] = ...,
        start_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        time_of_day : typing.Optional[google.type.timeofday_pb2.TimeOfDay] = ...,
        frequency : global___RecurringSchedule.Frequency.ValueType = ...,
        weekly : typing.Optional[global___WeeklySchedule] = ...,
        monthly : typing.Optional[global___MonthlySchedule] = ...,
        last_execute_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        next_execute_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_time",b"end_time","last_execute_time",b"last_execute_time","monthly",b"monthly","next_execute_time",b"next_execute_time","schedule_config",b"schedule_config","start_time",b"start_time","time_of_day",b"time_of_day","time_zone",b"time_zone","weekly",b"weekly"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_time",b"end_time","frequency",b"frequency","last_execute_time",b"last_execute_time","monthly",b"monthly","next_execute_time",b"next_execute_time","schedule_config",b"schedule_config","start_time",b"start_time","time_of_day",b"time_of_day","time_zone",b"time_zone","weekly",b"weekly"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["schedule_config",b"schedule_config"]) -> typing.Optional[typing_extensions.Literal["weekly","monthly"]]: ...
global___RecurringSchedule = RecurringSchedule

class WeeklySchedule(google.protobuf.message.Message):
    """Represents a weekly schedule."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DAY_OF_WEEK_FIELD_NUMBER: builtins.int
    day_of_week: google.type.dayofweek_pb2.DayOfWeek.ValueType = ...
    """Required. Day of the week."""

    def __init__(self,
        *,
        day_of_week : google.type.dayofweek_pb2.DayOfWeek.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["day_of_week",b"day_of_week"]) -> None: ...
global___WeeklySchedule = WeeklySchedule

class MonthlySchedule(google.protobuf.message.Message):
    """Represents a monthly schedule. An example of a valid monthly schedule is
    "on the third Tuesday of the month" or "on the 15th of the month".
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WEEK_DAY_OF_MONTH_FIELD_NUMBER: builtins.int
    MONTH_DAY_FIELD_NUMBER: builtins.int
    @property
    def week_day_of_month(self) -> global___WeekDayOfMonth:
        """Required. Week day in a month."""
        pass
    month_day: builtins.int = ...
    """Required. One day of the month. 1-31 indicates the 1st to the 31st day. -1
    indicates the last day of the month.
    Months without the target day will be skipped. For example, a schedule to
    run "every month on the 31st" will not run in February, April, June, etc.
    """

    def __init__(self,
        *,
        week_day_of_month : typing.Optional[global___WeekDayOfMonth] = ...,
        month_day : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["day_of_month",b"day_of_month","month_day",b"month_day","week_day_of_month",b"week_day_of_month"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["day_of_month",b"day_of_month","month_day",b"month_day","week_day_of_month",b"week_day_of_month"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["day_of_month",b"day_of_month"]) -> typing.Optional[typing_extensions.Literal["week_day_of_month","month_day"]]: ...
global___MonthlySchedule = MonthlySchedule

class WeekDayOfMonth(google.protobuf.message.Message):
    """Represents one week day in a month. An example is "the 4th Sunday"."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WEEK_ORDINAL_FIELD_NUMBER: builtins.int
    DAY_OF_WEEK_FIELD_NUMBER: builtins.int
    week_ordinal: builtins.int = ...
    """Required. Week number in a month. 1-4 indicates the 1st to 4th week of the month. -1
    indicates the last week of the month.
    """

    day_of_week: google.type.dayofweek_pb2.DayOfWeek.ValueType = ...
    """Required. A day of the week."""

    def __init__(self,
        *,
        week_ordinal : builtins.int = ...,
        day_of_week : google.type.dayofweek_pb2.DayOfWeek.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["day_of_week",b"day_of_week","week_ordinal",b"week_ordinal"]) -> None: ...
global___WeekDayOfMonth = WeekDayOfMonth

class CreatePatchDeploymentRequest(google.protobuf.message.Message):
    """A request message for creating a patch deployment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PATCH_DEPLOYMENT_ID_FIELD_NUMBER: builtins.int
    PATCH_DEPLOYMENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The project to apply this patch deployment to in the form `projects/*`."""

    patch_deployment_id: typing.Text = ...
    """Required. A name for the patch deployment in the project. When creating a name
    the following rules apply:
    * Must contain only lowercase letters, numbers, and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.
    * Must be unique within the project.
    """

    @property
    def patch_deployment(self) -> global___PatchDeployment:
        """Required. The patch deployment to create."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        patch_deployment_id : typing.Text = ...,
        patch_deployment : typing.Optional[global___PatchDeployment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["patch_deployment",b"patch_deployment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","patch_deployment",b"patch_deployment","patch_deployment_id",b"patch_deployment_id"]) -> None: ...
global___CreatePatchDeploymentRequest = CreatePatchDeploymentRequest

class GetPatchDeploymentRequest(google.protobuf.message.Message):
    """A request message for retrieving a patch deployment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the patch deployment in the form
    `projects/*/patchDeployments/*`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetPatchDeploymentRequest = GetPatchDeploymentRequest

class ListPatchDeploymentsRequest(google.protobuf.message.Message):
    """A request message for listing patch deployments."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The resource name of the parent in the form `projects/*`."""

    page_size: builtins.int = ...
    """Optional. The maximum number of patch deployments to return. Default is 100."""

    page_token: typing.Text = ...
    """Optional. A pagination token returned from a previous call to ListPatchDeployments
    that indicates where this listing should continue from.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListPatchDeploymentsRequest = ListPatchDeploymentsRequest

class ListPatchDeploymentsResponse(google.protobuf.message.Message):
    """A response message for listing patch deployments."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATCH_DEPLOYMENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def patch_deployments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PatchDeployment]:
        """The list of patch deployments."""
        pass
    next_page_token: typing.Text = ...
    """A pagination token that can be used to get the next page of patch
    deployments.
    """

    def __init__(self,
        *,
        patch_deployments : typing.Optional[typing.Iterable[global___PatchDeployment]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","patch_deployments",b"patch_deployments"]) -> None: ...
global___ListPatchDeploymentsResponse = ListPatchDeploymentsResponse

class DeletePatchDeploymentRequest(google.protobuf.message.Message):
    """A request message for deleting a patch deployment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the patch deployment in the form
    `projects/*/patchDeployments/*`.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeletePatchDeploymentRequest = DeletePatchDeploymentRequest

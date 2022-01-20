"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.talent.v4beta1.common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import google.type.date_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Application(google.protobuf.message.Message):
    """Resource that represents a job application record of a candidate."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ApplicationState:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ApplicationStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ApplicationState.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        APPLICATION_STATE_UNSPECIFIED: Application.ApplicationState.ValueType = ...  # 0
        """Default value."""

        IN_PROGRESS: Application.ApplicationState.ValueType = ...  # 1
        """The current stage is in progress or pending, for example, interviews in
        progress.
        """

        CANDIDATE_WITHDREW: Application.ApplicationState.ValueType = ...  # 2
        """The current stage was terminated by a candidate decision."""

        EMPLOYER_WITHDREW: Application.ApplicationState.ValueType = ...  # 3
        """The current stage was terminated by an employer or agency decision."""

        COMPLETED: Application.ApplicationState.ValueType = ...  # 4
        """The current stage is successfully completed, but the next stage (if
        applicable) has not begun.
        """

        CLOSED: Application.ApplicationState.ValueType = ...  # 5
        """The current stage was closed without an exception, or terminated for
        reasons unrealated to the candidate.
        """

    class ApplicationState(_ApplicationState, metaclass=_ApplicationStateEnumTypeWrapper):
        """Enum that represents the application status."""
        pass

    APPLICATION_STATE_UNSPECIFIED: Application.ApplicationState.ValueType = ...  # 0
    """Default value."""

    IN_PROGRESS: Application.ApplicationState.ValueType = ...  # 1
    """The current stage is in progress or pending, for example, interviews in
    progress.
    """

    CANDIDATE_WITHDREW: Application.ApplicationState.ValueType = ...  # 2
    """The current stage was terminated by a candidate decision."""

    EMPLOYER_WITHDREW: Application.ApplicationState.ValueType = ...  # 3
    """The current stage was terminated by an employer or agency decision."""

    COMPLETED: Application.ApplicationState.ValueType = ...  # 4
    """The current stage is successfully completed, but the next stage (if
    applicable) has not begun.
    """

    CLOSED: Application.ApplicationState.ValueType = ...  # 5
    """The current stage was closed without an exception, or terminated for
    reasons unrealated to the candidate.
    """


    class _ApplicationStage:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ApplicationStageEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ApplicationStage.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        APPLICATION_STAGE_UNSPECIFIED: Application.ApplicationStage.ValueType = ...  # 0
        """Default value."""

        NEW: Application.ApplicationStage.ValueType = ...  # 1
        """Candidate has applied or a recruiter put candidate into consideration but
        candidate is not yet screened / no decision has been made to move or not
        move the candidate to the next stage.
        """

        SCREEN: Application.ApplicationStage.ValueType = ...  # 2
        """A recruiter decided to screen the candidate for this role."""

        HIRING_MANAGER_REVIEW: Application.ApplicationStage.ValueType = ...  # 3
        """Candidate is being / was sent to the customer / hiring manager for
        detailed review.
        """

        INTERVIEW: Application.ApplicationStage.ValueType = ...  # 4
        """Candidate was approved by the client / hiring manager and is being / was
        interviewed for the role.
        """

        OFFER_EXTENDED: Application.ApplicationStage.ValueType = ...  # 5
        """Candidate will be / has been given an offer of employment."""

        OFFER_ACCEPTED: Application.ApplicationStage.ValueType = ...  # 6
        """Candidate has accepted their offer of employment."""

        STARTED: Application.ApplicationStage.ValueType = ...  # 7
        """Candidate has begun (or completed) their employment or assignment with
        the employer.
        """

    class ApplicationStage(_ApplicationStage, metaclass=_ApplicationStageEnumTypeWrapper):
        """The stage of the application."""
        pass

    APPLICATION_STAGE_UNSPECIFIED: Application.ApplicationStage.ValueType = ...  # 0
    """Default value."""

    NEW: Application.ApplicationStage.ValueType = ...  # 1
    """Candidate has applied or a recruiter put candidate into consideration but
    candidate is not yet screened / no decision has been made to move or not
    move the candidate to the next stage.
    """

    SCREEN: Application.ApplicationStage.ValueType = ...  # 2
    """A recruiter decided to screen the candidate for this role."""

    HIRING_MANAGER_REVIEW: Application.ApplicationStage.ValueType = ...  # 3
    """Candidate is being / was sent to the customer / hiring manager for
    detailed review.
    """

    INTERVIEW: Application.ApplicationStage.ValueType = ...  # 4
    """Candidate was approved by the client / hiring manager and is being / was
    interviewed for the role.
    """

    OFFER_EXTENDED: Application.ApplicationStage.ValueType = ...  # 5
    """Candidate will be / has been given an offer of employment."""

    OFFER_ACCEPTED: Application.ApplicationStage.ValueType = ...  # 6
    """Candidate has accepted their offer of employment."""

    STARTED: Application.ApplicationStage.ValueType = ...  # 7
    """Candidate has begun (or completed) their employment or assignment with
    the employer.
    """


    NAME_FIELD_NUMBER: builtins.int
    EXTERNAL_ID_FIELD_NUMBER: builtins.int
    PROFILE_FIELD_NUMBER: builtins.int
    JOB_FIELD_NUMBER: builtins.int
    COMPANY_FIELD_NUMBER: builtins.int
    APPLICATION_DATE_FIELD_NUMBER: builtins.int
    STAGE_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    INTERVIEWS_FIELD_NUMBER: builtins.int
    REFERRAL_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    OUTCOME_NOTES_FIELD_NUMBER: builtins.int
    OUTCOME_FIELD_NUMBER: builtins.int
    IS_MATCH_FIELD_NUMBER: builtins.int
    JOB_TITLE_SNIPPET_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required during application update.

    Resource name assigned to an application by the API.

    The format is
    "projects/{project_id}/tenants/{tenant_id}/profiles/{profile_id}/applications/{application_id}".
    For example, "projects/foo/tenants/bar/profiles/baz/applications/qux".
    """

    external_id: typing.Text = ...
    """Required. Client side application identifier, used to uniquely identify the
    application.

    The maximum number of allowed characters is 255.
    """

    profile: typing.Text = ...
    """Output only. Resource name of the candidate of this application.

    The format is
    "projects/{project_id}/tenants/{tenant_id}/profiles/{profile_id}".
    For example, "projects/foo/tenants/bar/profiles/baz".
    """

    job: typing.Text = ...
    """Required. Resource name of the job which the candidate applied for.

    The format is
    "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}". For example,
    "projects/foo/tenants/bar/jobs/baz".
    """

    company: typing.Text = ...
    """Resource name of the company which the candidate applied for.

    The format is
    "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}".
    For example, "projects/foo/tenants/bar/companies/baz".
    """

    @property
    def application_date(self) -> google.type.date_pb2.Date:
        """The application date."""
        pass
    stage: global___Application.ApplicationStage.ValueType = ...
    """Required. What is the most recent stage of the application (that is, new,
    screen, send cv, hired, finished work)?  This field is intentionally not
    comprehensive of every possible status, but instead, represents statuses
    that would be used to indicate to the ML models good / bad matches.
    """

    state: global___Application.ApplicationState.ValueType = ...
    """The application state."""

    @property
    def interviews(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.talent.v4beta1.common_pb2.Interview]:
        """All interviews (screen, onsite, and so on) conducted as part of this
        application (includes details such as user conducting the interview,
        timestamp, feedback, and so on).
        """
        pass
    @property
    def referral(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """If the candidate is referred by a employee."""
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Required. Reflects the time that the application was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The last update timestamp."""
        pass
    outcome_notes: typing.Text = ...
    """Free text reason behind the recruitement outcome (for example, reason for
    withdraw / reject, reason for an unsuccessful finish, and so on).

    Number of characters allowed is 100.
    """

    outcome: google.cloud.talent.v4beta1.common_pb2.Outcome.ValueType = ...
    """Outcome positiveness shows how positive the outcome is."""

    @property
    def is_match(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Output only. Indicates whether this job application is a match to
        application related filters. This value is only applicable in profile
        search response.
        """
        pass
    job_title_snippet: typing.Text = ...
    """Output only. Job title snippet shows how the job title is related to a
    search query. It's empty if the job title isn't related to the search
    query.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        external_id : typing.Text = ...,
        profile : typing.Text = ...,
        job : typing.Text = ...,
        company : typing.Text = ...,
        application_date : typing.Optional[google.type.date_pb2.Date] = ...,
        stage : global___Application.ApplicationStage.ValueType = ...,
        state : global___Application.ApplicationState.ValueType = ...,
        interviews : typing.Optional[typing.Iterable[google.cloud.talent.v4beta1.common_pb2.Interview]] = ...,
        referral : typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        outcome_notes : typing.Text = ...,
        outcome : google.cloud.talent.v4beta1.common_pb2.Outcome.ValueType = ...,
        is_match : typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        job_title_snippet : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["application_date",b"application_date","create_time",b"create_time","is_match",b"is_match","referral",b"referral","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_date",b"application_date","company",b"company","create_time",b"create_time","external_id",b"external_id","interviews",b"interviews","is_match",b"is_match","job",b"job","job_title_snippet",b"job_title_snippet","name",b"name","outcome",b"outcome","outcome_notes",b"outcome_notes","profile",b"profile","referral",b"referral","stage",b"stage","state",b"state","update_time",b"update_time"]) -> None: ...
global___Application = Application

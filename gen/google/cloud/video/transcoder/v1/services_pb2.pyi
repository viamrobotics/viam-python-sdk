"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.cloud.video.transcoder.v1.resources_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateJobRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.CreateJob`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    JOB_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent location to create and process this job.
    Format: `projects/{project}/locations/{location}`
    """

    @property
    def job(self) -> google.cloud.video.transcoder.v1.resources_pb2.Job:
        """Required. Parameters for creating transcoding job."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        job : typing.Optional[google.cloud.video.transcoder.v1.resources_pb2.Job] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job",b"job"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["job",b"job","parent",b"parent"]) -> None: ...
global___CreateJobRequest = CreateJobRequest

class ListJobsRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.ListJobs`.
    The parent location from which to retrieve the collection of jobs.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. Format: `projects/{project}/locations/{location}`"""

    page_size: builtins.int = ...
    """The maximum number of items to return."""

    page_token: typing.Text = ...
    """The `next_page_token` value returned from a previous List request, if
    any.
    """

    filter: typing.Text = ...
    """The filter expression, following the syntax outlined in
    https://google.aip.dev/160.
    """

    order_by: typing.Text = ...
    """One or more fields to compare and use to sort the output.
    See https://google.aip.dev/132#ordering.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        filter : typing.Text = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListJobsRequest = ListJobsRequest

class GetJobRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.GetJob`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the job to retrieve.
    Format: `projects/{project}/locations/{location}/jobs/{job}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetJobRequest = GetJobRequest

class DeleteJobRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.DeleteJob`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the job to delete.
    Format: `projects/{project}/locations/{location}/jobs/{job}`
    """

    allow_missing: builtins.bool = ...
    """If set to true, and the job is not found, the request will succeed but no
    action will be taken on the server.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        allow_missing : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_missing",b"allow_missing","name",b"name"]) -> None: ...
global___DeleteJobRequest = DeleteJobRequest

class ListJobsResponse(google.protobuf.message.Message):
    """Response message for `TranscoderService.ListJobs`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JOBS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    UNREACHABLE_FIELD_NUMBER: builtins.int
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.video.transcoder.v1.resources_pb2.Job]:
        """List of jobs in the specified region."""
        pass
    next_page_token: typing.Text = ...
    """The pagination token."""

    @property
    def unreachable(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of regions that could not be reached."""
        pass
    def __init__(self,
        *,
        jobs : typing.Optional[typing.Iterable[google.cloud.video.transcoder.v1.resources_pb2.Job]] = ...,
        next_page_token : typing.Text = ...,
        unreachable : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jobs",b"jobs","next_page_token",b"next_page_token","unreachable",b"unreachable"]) -> None: ...
global___ListJobsResponse = ListJobsResponse

class CreateJobTemplateRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.CreateJobTemplate`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    JOB_TEMPLATE_FIELD_NUMBER: builtins.int
    JOB_TEMPLATE_ID_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent location to create this job template.
    Format: `projects/{project}/locations/{location}`
    """

    @property
    def job_template(self) -> google.cloud.video.transcoder.v1.resources_pb2.JobTemplate:
        """Required. Parameters for creating job template."""
        pass
    job_template_id: typing.Text = ...
    """Required. The ID to use for the job template, which will become the final component
    of the job template's resource name.

    This value should be 4-63 characters, and valid characters must match the
    regular expression `[a-zA-Z][a-zA-Z0-9_-]*`.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        job_template : typing.Optional[google.cloud.video.transcoder.v1.resources_pb2.JobTemplate] = ...,
        job_template_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job_template",b"job_template"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_template",b"job_template","job_template_id",b"job_template_id","parent",b"parent"]) -> None: ...
global___CreateJobTemplateRequest = CreateJobTemplateRequest

class ListJobTemplatesRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.ListJobTemplates`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The parent location from which to retrieve the collection of job templates.
    Format: `projects/{project}/locations/{location}`
    """

    page_size: builtins.int = ...
    """The maximum number of items to return."""

    page_token: typing.Text = ...
    """The `next_page_token` value returned from a previous List request, if
    any.
    """

    filter: typing.Text = ...
    """The filter expression, following the syntax outlined in
    https://google.aip.dev/160.
    """

    order_by: typing.Text = ...
    """One or more fields to compare and use to sort the output.
    See https://google.aip.dev/132#ordering.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        filter : typing.Text = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","order_by",b"order_by","page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListJobTemplatesRequest = ListJobTemplatesRequest

class GetJobTemplateRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.GetJobTemplate`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the job template to retrieve.
    Format:
    `projects/{project}/locations/{location}/jobTemplates/{job_template}`
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetJobTemplateRequest = GetJobTemplateRequest

class DeleteJobTemplateRequest(google.protobuf.message.Message):
    """Request message for `TranscoderService.DeleteJobTemplate`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    ALLOW_MISSING_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the job template to delete.
    `projects/{project}/locations/{location}/jobTemplates/{job_template}`
    """

    allow_missing: builtins.bool = ...
    """If set to true, and the job template is not found, the request will succeed
    but no action will be taken on the server.
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        allow_missing : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_missing",b"allow_missing","name",b"name"]) -> None: ...
global___DeleteJobTemplateRequest = DeleteJobTemplateRequest

class ListJobTemplatesResponse(google.protobuf.message.Message):
    """Response message for `TranscoderService.ListJobTemplates`."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    JOB_TEMPLATES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    UNREACHABLE_FIELD_NUMBER: builtins.int
    @property
    def job_templates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.cloud.video.transcoder.v1.resources_pb2.JobTemplate]:
        """List of job templates in the specified region."""
        pass
    next_page_token: typing.Text = ...
    """The pagination token."""

    @property
    def unreachable(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List of regions that could not be reached."""
        pass
    def __init__(self,
        *,
        job_templates : typing.Optional[typing.Iterable[google.cloud.video.transcoder.v1.resources_pb2.JobTemplate]] = ...,
        next_page_token : typing.Text = ...,
        unreachable : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_templates",b"job_templates","next_page_token",b"next_page_token","unreachable",b"unreachable"]) -> None: ...
global___ListJobTemplatesResponse = ListJobTemplatesResponse

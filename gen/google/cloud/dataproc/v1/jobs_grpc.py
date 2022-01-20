# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dataproc/v1/jobs.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.dataproc.v1.jobs_pb2


class JobControllerBase(abc.ABC):

    @abc.abstractmethod
    async def SubmitJob(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.SubmitJobRequest, google.cloud.dataproc.v1.jobs_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def SubmitJobAsOperation(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.SubmitJobRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetJob(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.GetJobRequest, google.cloud.dataproc.v1.jobs_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def ListJobs(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.ListJobsRequest, google.cloud.dataproc.v1.jobs_pb2.ListJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateJob(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.UpdateJobRequest, google.cloud.dataproc.v1.jobs_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def CancelJob(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.CancelJobRequest, google.cloud.dataproc.v1.jobs_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteJob(self, stream: 'grpclib.server.Stream[google.cloud.dataproc.v1.jobs_pb2.DeleteJobRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dataproc.v1.JobController/SubmitJob': grpclib.const.Handler(
                self.SubmitJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.SubmitJobRequest,
                google.cloud.dataproc.v1.jobs_pb2.Job,
            ),
            '/google.cloud.dataproc.v1.JobController/SubmitJobAsOperation': grpclib.const.Handler(
                self.SubmitJobAsOperation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.SubmitJobRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dataproc.v1.JobController/GetJob': grpclib.const.Handler(
                self.GetJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.GetJobRequest,
                google.cloud.dataproc.v1.jobs_pb2.Job,
            ),
            '/google.cloud.dataproc.v1.JobController/ListJobs': grpclib.const.Handler(
                self.ListJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.ListJobsRequest,
                google.cloud.dataproc.v1.jobs_pb2.ListJobsResponse,
            ),
            '/google.cloud.dataproc.v1.JobController/UpdateJob': grpclib.const.Handler(
                self.UpdateJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.UpdateJobRequest,
                google.cloud.dataproc.v1.jobs_pb2.Job,
            ),
            '/google.cloud.dataproc.v1.JobController/CancelJob': grpclib.const.Handler(
                self.CancelJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.CancelJobRequest,
                google.cloud.dataproc.v1.jobs_pb2.Job,
            ),
            '/google.cloud.dataproc.v1.JobController/DeleteJob': grpclib.const.Handler(
                self.DeleteJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dataproc.v1.jobs_pb2.DeleteJobRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class JobControllerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SubmitJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/SubmitJob',
            google.cloud.dataproc.v1.jobs_pb2.SubmitJobRequest,
            google.cloud.dataproc.v1.jobs_pb2.Job,
        )
        self.SubmitJobAsOperation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/SubmitJobAsOperation',
            google.cloud.dataproc.v1.jobs_pb2.SubmitJobRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/GetJob',
            google.cloud.dataproc.v1.jobs_pb2.GetJobRequest,
            google.cloud.dataproc.v1.jobs_pb2.Job,
        )
        self.ListJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/ListJobs',
            google.cloud.dataproc.v1.jobs_pb2.ListJobsRequest,
            google.cloud.dataproc.v1.jobs_pb2.ListJobsResponse,
        )
        self.UpdateJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/UpdateJob',
            google.cloud.dataproc.v1.jobs_pb2.UpdateJobRequest,
            google.cloud.dataproc.v1.jobs_pb2.Job,
        )
        self.CancelJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/CancelJob',
            google.cloud.dataproc.v1.jobs_pb2.CancelJobRequest,
            google.cloud.dataproc.v1.jobs_pb2.Job,
        )
        self.DeleteJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dataproc.v1.JobController/DeleteJob',
            google.cloud.dataproc.v1.jobs_pb2.DeleteJobRequest,
            google.protobuf.empty_pb2.Empty,
        )

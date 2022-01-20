# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/ml/v1/job_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.auth_pb2
import google.protobuf.empty_pb2
import google.protobuf.timestamp_pb2
import google.cloud.ml.v1.job_service_pb2


class JobServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateJob(self, stream: 'grpclib.server.Stream[google.cloud.ml.v1.job_service_pb2.CreateJobRequest, google.cloud.ml.v1.job_service_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def ListJobs(self, stream: 'grpclib.server.Stream[google.cloud.ml.v1.job_service_pb2.ListJobsRequest, google.cloud.ml.v1.job_service_pb2.ListJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetJob(self, stream: 'grpclib.server.Stream[google.cloud.ml.v1.job_service_pb2.GetJobRequest, google.cloud.ml.v1.job_service_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def CancelJob(self, stream: 'grpclib.server.Stream[google.cloud.ml.v1.job_service_pb2.CancelJobRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.ml.v1.JobService/CreateJob': grpclib.const.Handler(
                self.CreateJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.ml.v1.job_service_pb2.CreateJobRequest,
                google.cloud.ml.v1.job_service_pb2.Job,
            ),
            '/google.cloud.ml.v1.JobService/ListJobs': grpclib.const.Handler(
                self.ListJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.ml.v1.job_service_pb2.ListJobsRequest,
                google.cloud.ml.v1.job_service_pb2.ListJobsResponse,
            ),
            '/google.cloud.ml.v1.JobService/GetJob': grpclib.const.Handler(
                self.GetJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.ml.v1.job_service_pb2.GetJobRequest,
                google.cloud.ml.v1.job_service_pb2.Job,
            ),
            '/google.cloud.ml.v1.JobService/CancelJob': grpclib.const.Handler(
                self.CancelJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.ml.v1.job_service_pb2.CancelJobRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class JobServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.ml.v1.JobService/CreateJob',
            google.cloud.ml.v1.job_service_pb2.CreateJobRequest,
            google.cloud.ml.v1.job_service_pb2.Job,
        )
        self.ListJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.ml.v1.JobService/ListJobs',
            google.cloud.ml.v1.job_service_pb2.ListJobsRequest,
            google.cloud.ml.v1.job_service_pb2.ListJobsResponse,
        )
        self.GetJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.ml.v1.JobService/GetJob',
            google.cloud.ml.v1.job_service_pb2.GetJobRequest,
            google.cloud.ml.v1.job_service_pb2.Job,
        )
        self.CancelJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.ml.v1.JobService/CancelJob',
            google.cloud.ml.v1.job_service_pb2.CancelJobRequest,
            google.protobuf.empty_pb2.Empty,
        )

# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/osconfig/v1/osconfig_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.resource_pb2
import google.cloud.osconfig.v1.patch_deployments_pb2
import google.cloud.osconfig.v1.patch_jobs_pb2
import google.protobuf.empty_pb2
import google.cloud.osconfig.v1.osconfig_service_pb2


class OsConfigServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ExecutePatchJob(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_jobs_pb2.ExecutePatchJobRequest, google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob]') -> None:
        pass

    @abc.abstractmethod
    async def GetPatchJob(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_jobs_pb2.GetPatchJobRequest, google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob]') -> None:
        pass

    @abc.abstractmethod
    async def CancelPatchJob(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_jobs_pb2.CancelPatchJobRequest, google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob]') -> None:
        pass

    @abc.abstractmethod
    async def ListPatchJobs(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobsRequest, google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListPatchJobInstanceDetails(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobInstanceDetailsRequest, google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobInstanceDetailsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreatePatchDeployment(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_deployments_pb2.CreatePatchDeploymentRequest, google.cloud.osconfig.v1.patch_deployments_pb2.PatchDeployment]') -> None:
        pass

    @abc.abstractmethod
    async def GetPatchDeployment(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_deployments_pb2.GetPatchDeploymentRequest, google.cloud.osconfig.v1.patch_deployments_pb2.PatchDeployment]') -> None:
        pass

    @abc.abstractmethod
    async def ListPatchDeployments(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_deployments_pb2.ListPatchDeploymentsRequest, google.cloud.osconfig.v1.patch_deployments_pb2.ListPatchDeploymentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeletePatchDeployment(self, stream: 'grpclib.server.Stream[google.cloud.osconfig.v1.patch_deployments_pb2.DeletePatchDeploymentRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.osconfig.v1.OsConfigService/ExecutePatchJob': grpclib.const.Handler(
                self.ExecutePatchJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_jobs_pb2.ExecutePatchJobRequest,
                google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/GetPatchJob': grpclib.const.Handler(
                self.GetPatchJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_jobs_pb2.GetPatchJobRequest,
                google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/CancelPatchJob': grpclib.const.Handler(
                self.CancelPatchJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_jobs_pb2.CancelPatchJobRequest,
                google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/ListPatchJobs': grpclib.const.Handler(
                self.ListPatchJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobsRequest,
                google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobsResponse,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/ListPatchJobInstanceDetails': grpclib.const.Handler(
                self.ListPatchJobInstanceDetails,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobInstanceDetailsRequest,
                google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobInstanceDetailsResponse,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/CreatePatchDeployment': grpclib.const.Handler(
                self.CreatePatchDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_deployments_pb2.CreatePatchDeploymentRequest,
                google.cloud.osconfig.v1.patch_deployments_pb2.PatchDeployment,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/GetPatchDeployment': grpclib.const.Handler(
                self.GetPatchDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_deployments_pb2.GetPatchDeploymentRequest,
                google.cloud.osconfig.v1.patch_deployments_pb2.PatchDeployment,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/ListPatchDeployments': grpclib.const.Handler(
                self.ListPatchDeployments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_deployments_pb2.ListPatchDeploymentsRequest,
                google.cloud.osconfig.v1.patch_deployments_pb2.ListPatchDeploymentsResponse,
            ),
            '/google.cloud.osconfig.v1.OsConfigService/DeletePatchDeployment': grpclib.const.Handler(
                self.DeletePatchDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.osconfig.v1.patch_deployments_pb2.DeletePatchDeploymentRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class OsConfigServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ExecutePatchJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/ExecutePatchJob',
            google.cloud.osconfig.v1.patch_jobs_pb2.ExecutePatchJobRequest,
            google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob,
        )
        self.GetPatchJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/GetPatchJob',
            google.cloud.osconfig.v1.patch_jobs_pb2.GetPatchJobRequest,
            google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob,
        )
        self.CancelPatchJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/CancelPatchJob',
            google.cloud.osconfig.v1.patch_jobs_pb2.CancelPatchJobRequest,
            google.cloud.osconfig.v1.patch_jobs_pb2.PatchJob,
        )
        self.ListPatchJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/ListPatchJobs',
            google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobsRequest,
            google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobsResponse,
        )
        self.ListPatchJobInstanceDetails = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/ListPatchJobInstanceDetails',
            google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobInstanceDetailsRequest,
            google.cloud.osconfig.v1.patch_jobs_pb2.ListPatchJobInstanceDetailsResponse,
        )
        self.CreatePatchDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/CreatePatchDeployment',
            google.cloud.osconfig.v1.patch_deployments_pb2.CreatePatchDeploymentRequest,
            google.cloud.osconfig.v1.patch_deployments_pb2.PatchDeployment,
        )
        self.GetPatchDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/GetPatchDeployment',
            google.cloud.osconfig.v1.patch_deployments_pb2.GetPatchDeploymentRequest,
            google.cloud.osconfig.v1.patch_deployments_pb2.PatchDeployment,
        )
        self.ListPatchDeployments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/ListPatchDeployments',
            google.cloud.osconfig.v1.patch_deployments_pb2.ListPatchDeploymentsRequest,
            google.cloud.osconfig.v1.patch_deployments_pb2.ListPatchDeploymentsResponse,
        )
        self.DeletePatchDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.osconfig.v1.OsConfigService/DeletePatchDeployment',
            google.cloud.osconfig.v1.patch_deployments_pb2.DeletePatchDeploymentRequest,
            google.protobuf.empty_pb2.Empty,
        )

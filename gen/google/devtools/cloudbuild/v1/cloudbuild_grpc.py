# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/devtools/cloudbuild/v1/cloudbuild.proto
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
import google.api.httpbody_pb2
import google.api.resource_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.devtools.cloudbuild.v1.cloudbuild_pb2


class CloudBuildBase(abc.ABC):

    @abc.abstractmethod
    async def CreateBuild(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateBuildRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetBuild(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.GetBuildRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.Build]') -> None:
        pass

    @abc.abstractmethod
    async def ListBuilds(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildsRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CancelBuild(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.CancelBuildRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.Build]') -> None:
        pass

    @abc.abstractmethod
    async def RetryBuild(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.RetryBuildRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ApproveBuild(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.ApproveBuildRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateBuildTrigger(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateBuildTriggerRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger]') -> None:
        pass

    @abc.abstractmethod
    async def GetBuildTrigger(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.GetBuildTriggerRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger]') -> None:
        pass

    @abc.abstractmethod
    async def ListBuildTriggers(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildTriggersRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildTriggersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBuildTrigger(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.DeleteBuildTriggerRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateBuildTrigger(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.UpdateBuildTriggerRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger]') -> None:
        pass

    @abc.abstractmethod
    async def RunBuildTrigger(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.RunBuildTriggerRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ReceiveTriggerWebhook(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.ReceiveTriggerWebhookRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.ReceiveTriggerWebhookResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateWorkerPool(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateWorkerPoolRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetWorkerPool(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.GetWorkerPoolRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.WorkerPool]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteWorkerPool(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.DeleteWorkerPoolRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateWorkerPool(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.UpdateWorkerPoolRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListWorkerPools(self, stream: 'grpclib.server.Stream[google.devtools.cloudbuild.v1.cloudbuild_pb2.ListWorkerPoolsRequest, google.devtools.cloudbuild.v1.cloudbuild_pb2.ListWorkerPoolsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.devtools.cloudbuild.v1.CloudBuild/CreateBuild': grpclib.const.Handler(
                self.CreateBuild,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateBuildRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/GetBuild': grpclib.const.Handler(
                self.GetBuild,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.GetBuildRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.Build,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/ListBuilds': grpclib.const.Handler(
                self.ListBuilds,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildsRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildsResponse,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/CancelBuild': grpclib.const.Handler(
                self.CancelBuild,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.CancelBuildRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.Build,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/RetryBuild': grpclib.const.Handler(
                self.RetryBuild,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.RetryBuildRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/ApproveBuild': grpclib.const.Handler(
                self.ApproveBuild,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ApproveBuildRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/CreateBuildTrigger': grpclib.const.Handler(
                self.CreateBuildTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateBuildTriggerRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/GetBuildTrigger': grpclib.const.Handler(
                self.GetBuildTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.GetBuildTriggerRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/ListBuildTriggers': grpclib.const.Handler(
                self.ListBuildTriggers,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildTriggersRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildTriggersResponse,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/DeleteBuildTrigger': grpclib.const.Handler(
                self.DeleteBuildTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.DeleteBuildTriggerRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/UpdateBuildTrigger': grpclib.const.Handler(
                self.UpdateBuildTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.UpdateBuildTriggerRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/RunBuildTrigger': grpclib.const.Handler(
                self.RunBuildTrigger,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.RunBuildTriggerRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/ReceiveTriggerWebhook': grpclib.const.Handler(
                self.ReceiveTriggerWebhook,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ReceiveTriggerWebhookRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ReceiveTriggerWebhookResponse,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/CreateWorkerPool': grpclib.const.Handler(
                self.CreateWorkerPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateWorkerPoolRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/GetWorkerPool': grpclib.const.Handler(
                self.GetWorkerPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.GetWorkerPoolRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.WorkerPool,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/DeleteWorkerPool': grpclib.const.Handler(
                self.DeleteWorkerPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.DeleteWorkerPoolRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/UpdateWorkerPool': grpclib.const.Handler(
                self.UpdateWorkerPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.UpdateWorkerPoolRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.devtools.cloudbuild.v1.CloudBuild/ListWorkerPools': grpclib.const.Handler(
                self.ListWorkerPools,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ListWorkerPoolsRequest,
                google.devtools.cloudbuild.v1.cloudbuild_pb2.ListWorkerPoolsResponse,
            ),
        }


class CloudBuildStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateBuild = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/CreateBuild',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateBuildRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetBuild = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/GetBuild',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.GetBuildRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.Build,
        )
        self.ListBuilds = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/ListBuilds',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildsRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildsResponse,
        )
        self.CancelBuild = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/CancelBuild',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.CancelBuildRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.Build,
        )
        self.RetryBuild = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/RetryBuild',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.RetryBuildRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ApproveBuild = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/ApproveBuild',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ApproveBuildRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateBuildTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/CreateBuildTrigger',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateBuildTriggerRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger,
        )
        self.GetBuildTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/GetBuildTrigger',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.GetBuildTriggerRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger,
        )
        self.ListBuildTriggers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/ListBuildTriggers',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildTriggersRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ListBuildTriggersResponse,
        )
        self.DeleteBuildTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/DeleteBuildTrigger',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.DeleteBuildTriggerRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.UpdateBuildTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/UpdateBuildTrigger',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.UpdateBuildTriggerRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.BuildTrigger,
        )
        self.RunBuildTrigger = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/RunBuildTrigger',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.RunBuildTriggerRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ReceiveTriggerWebhook = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/ReceiveTriggerWebhook',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ReceiveTriggerWebhookRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ReceiveTriggerWebhookResponse,
        )
        self.CreateWorkerPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/CreateWorkerPool',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.CreateWorkerPoolRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetWorkerPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/GetWorkerPool',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.GetWorkerPoolRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.WorkerPool,
        )
        self.DeleteWorkerPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/DeleteWorkerPool',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.DeleteWorkerPoolRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateWorkerPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/UpdateWorkerPool',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.UpdateWorkerPoolRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListWorkerPools = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.devtools.cloudbuild.v1.CloudBuild/ListWorkerPools',
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ListWorkerPoolsRequest,
            google.devtools.cloudbuild.v1.cloudbuild_pb2.ListWorkerPoolsResponse,
        )

# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/assuredworkloads/v1/assuredworkloads.proto
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
import google.api.resource_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.assuredworkloads.v1.assuredworkloads_pb2


class AssuredWorkloadsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateWorkload(self, stream: 'grpclib.server.Stream[google.cloud.assuredworkloads.v1.assuredworkloads_pb2.CreateWorkloadRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateWorkload(self, stream: 'grpclib.server.Stream[google.cloud.assuredworkloads.v1.assuredworkloads_pb2.UpdateWorkloadRequest, google.cloud.assuredworkloads.v1.assuredworkloads_pb2.Workload]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteWorkload(self, stream: 'grpclib.server.Stream[google.cloud.assuredworkloads.v1.assuredworkloads_pb2.DeleteWorkloadRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetWorkload(self, stream: 'grpclib.server.Stream[google.cloud.assuredworkloads.v1.assuredworkloads_pb2.GetWorkloadRequest, google.cloud.assuredworkloads.v1.assuredworkloads_pb2.Workload]') -> None:
        pass

    @abc.abstractmethod
    async def ListWorkloads(self, stream: 'grpclib.server.Stream[google.cloud.assuredworkloads.v1.assuredworkloads_pb2.ListWorkloadsRequest, google.cloud.assuredworkloads.v1.assuredworkloads_pb2.ListWorkloadsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/CreateWorkload': grpclib.const.Handler(
                self.CreateWorkload,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.CreateWorkloadRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/UpdateWorkload': grpclib.const.Handler(
                self.UpdateWorkload,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.UpdateWorkloadRequest,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.Workload,
            ),
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/DeleteWorkload': grpclib.const.Handler(
                self.DeleteWorkload,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.DeleteWorkloadRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/GetWorkload': grpclib.const.Handler(
                self.GetWorkload,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.GetWorkloadRequest,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.Workload,
            ),
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/ListWorkloads': grpclib.const.Handler(
                self.ListWorkloads,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.ListWorkloadsRequest,
                google.cloud.assuredworkloads.v1.assuredworkloads_pb2.ListWorkloadsResponse,
            ),
        }


class AssuredWorkloadsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateWorkload = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/CreateWorkload',
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.CreateWorkloadRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateWorkload = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/UpdateWorkload',
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.UpdateWorkloadRequest,
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.Workload,
        )
        self.DeleteWorkload = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/DeleteWorkload',
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.DeleteWorkloadRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetWorkload = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/GetWorkload',
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.GetWorkloadRequest,
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.Workload,
        )
        self.ListWorkloads = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.assuredworkloads.v1.AssuredWorkloadsService/ListWorkloads',
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.ListWorkloadsRequest,
            google.cloud.assuredworkloads.v1.assuredworkloads_pb2.ListWorkloadsResponse,
        )

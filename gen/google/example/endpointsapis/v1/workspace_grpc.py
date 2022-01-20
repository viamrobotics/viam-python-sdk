# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/example/endpointsapis/v1/workspace.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.protobuf.empty_pb2
import google.example.endpointsapis.v1.workspace_pb2


class WorkspacesBase(abc.ABC):

    @abc.abstractmethod
    async def ListWorkspaces(self, stream: 'grpclib.server.Stream[google.example.endpointsapis.v1.workspace_pb2.ListWorkspacesRequest, google.example.endpointsapis.v1.workspace_pb2.ListWorkspacesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetWorkspace(self, stream: 'grpclib.server.Stream[google.example.endpointsapis.v1.workspace_pb2.GetWorkspaceRequest, google.example.endpointsapis.v1.workspace_pb2.Workspace]') -> None:
        pass

    @abc.abstractmethod
    async def CreateWorkspace(self, stream: 'grpclib.server.Stream[google.example.endpointsapis.v1.workspace_pb2.CreateWorkspaceRequest, google.example.endpointsapis.v1.workspace_pb2.Workspace]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateWorkspace(self, stream: 'grpclib.server.Stream[google.example.endpointsapis.v1.workspace_pb2.UpdateWorkspaceRequest, google.example.endpointsapis.v1.workspace_pb2.Workspace]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteWorkspace(self, stream: 'grpclib.server.Stream[google.example.endpointsapis.v1.workspace_pb2.DeleteWorkspaceRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.example.endpointsapis.v1.Workspaces/ListWorkspaces': grpclib.const.Handler(
                self.ListWorkspaces,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.endpointsapis.v1.workspace_pb2.ListWorkspacesRequest,
                google.example.endpointsapis.v1.workspace_pb2.ListWorkspacesResponse,
            ),
            '/google.example.endpointsapis.v1.Workspaces/GetWorkspace': grpclib.const.Handler(
                self.GetWorkspace,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.endpointsapis.v1.workspace_pb2.GetWorkspaceRequest,
                google.example.endpointsapis.v1.workspace_pb2.Workspace,
            ),
            '/google.example.endpointsapis.v1.Workspaces/CreateWorkspace': grpclib.const.Handler(
                self.CreateWorkspace,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.endpointsapis.v1.workspace_pb2.CreateWorkspaceRequest,
                google.example.endpointsapis.v1.workspace_pb2.Workspace,
            ),
            '/google.example.endpointsapis.v1.Workspaces/UpdateWorkspace': grpclib.const.Handler(
                self.UpdateWorkspace,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.endpointsapis.v1.workspace_pb2.UpdateWorkspaceRequest,
                google.example.endpointsapis.v1.workspace_pb2.Workspace,
            ),
            '/google.example.endpointsapis.v1.Workspaces/DeleteWorkspace': grpclib.const.Handler(
                self.DeleteWorkspace,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.endpointsapis.v1.workspace_pb2.DeleteWorkspaceRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class WorkspacesStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListWorkspaces = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.endpointsapis.v1.Workspaces/ListWorkspaces',
            google.example.endpointsapis.v1.workspace_pb2.ListWorkspacesRequest,
            google.example.endpointsapis.v1.workspace_pb2.ListWorkspacesResponse,
        )
        self.GetWorkspace = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.endpointsapis.v1.Workspaces/GetWorkspace',
            google.example.endpointsapis.v1.workspace_pb2.GetWorkspaceRequest,
            google.example.endpointsapis.v1.workspace_pb2.Workspace,
        )
        self.CreateWorkspace = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.endpointsapis.v1.Workspaces/CreateWorkspace',
            google.example.endpointsapis.v1.workspace_pb2.CreateWorkspaceRequest,
            google.example.endpointsapis.v1.workspace_pb2.Workspace,
        )
        self.UpdateWorkspace = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.endpointsapis.v1.Workspaces/UpdateWorkspace',
            google.example.endpointsapis.v1.workspace_pb2.UpdateWorkspaceRequest,
            google.example.endpointsapis.v1.workspace_pb2.Workspace,
        )
        self.DeleteWorkspace = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.endpointsapis.v1.Workspaces/DeleteWorkspace',
            google.example.endpointsapis.v1.workspace_pb2.DeleteWorkspaceRequest,
            google.protobuf.empty_pb2.Empty,
        )

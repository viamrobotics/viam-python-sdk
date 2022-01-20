# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/gaming/v1/game_server_clusters_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.cloud.gaming.v1.game_server_clusters_pb2
import google.longrunning.operations_pb2
import google.cloud.gaming.v1.game_server_clusters_service_pb2


class GameServerClustersServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListGameServerClusters(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.ListGameServerClustersRequest, google.cloud.gaming.v1.game_server_clusters_pb2.ListGameServerClustersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.GetGameServerClusterRequest, google.cloud.gaming.v1.game_server_clusters_pb2.GameServerCluster]') -> None:
        pass

    @abc.abstractmethod
    async def CreateGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.CreateGameServerClusterRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PreviewCreateGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.PreviewCreateGameServerClusterRequest, google.cloud.gaming.v1.game_server_clusters_pb2.PreviewCreateGameServerClusterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.DeleteGameServerClusterRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PreviewDeleteGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.PreviewDeleteGameServerClusterRequest, google.cloud.gaming.v1.game_server_clusters_pb2.PreviewDeleteGameServerClusterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.UpdateGameServerClusterRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PreviewUpdateGameServerCluster(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_clusters_pb2.PreviewUpdateGameServerClusterRequest, google.cloud.gaming.v1.game_server_clusters_pb2.PreviewUpdateGameServerClusterResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.gaming.v1.GameServerClustersService/ListGameServerClusters': grpclib.const.Handler(
                self.ListGameServerClusters,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.ListGameServerClustersRequest,
                google.cloud.gaming.v1.game_server_clusters_pb2.ListGameServerClustersResponse,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/GetGameServerCluster': grpclib.const.Handler(
                self.GetGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.GetGameServerClusterRequest,
                google.cloud.gaming.v1.game_server_clusters_pb2.GameServerCluster,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/CreateGameServerCluster': grpclib.const.Handler(
                self.CreateGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.CreateGameServerClusterRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/PreviewCreateGameServerCluster': grpclib.const.Handler(
                self.PreviewCreateGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.PreviewCreateGameServerClusterRequest,
                google.cloud.gaming.v1.game_server_clusters_pb2.PreviewCreateGameServerClusterResponse,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/DeleteGameServerCluster': grpclib.const.Handler(
                self.DeleteGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.DeleteGameServerClusterRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/PreviewDeleteGameServerCluster': grpclib.const.Handler(
                self.PreviewDeleteGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.PreviewDeleteGameServerClusterRequest,
                google.cloud.gaming.v1.game_server_clusters_pb2.PreviewDeleteGameServerClusterResponse,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/UpdateGameServerCluster': grpclib.const.Handler(
                self.UpdateGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.UpdateGameServerClusterRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerClustersService/PreviewUpdateGameServerCluster': grpclib.const.Handler(
                self.PreviewUpdateGameServerCluster,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_clusters_pb2.PreviewUpdateGameServerClusterRequest,
                google.cloud.gaming.v1.game_server_clusters_pb2.PreviewUpdateGameServerClusterResponse,
            ),
        }


class GameServerClustersServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListGameServerClusters = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/ListGameServerClusters',
            google.cloud.gaming.v1.game_server_clusters_pb2.ListGameServerClustersRequest,
            google.cloud.gaming.v1.game_server_clusters_pb2.ListGameServerClustersResponse,
        )
        self.GetGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/GetGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.GetGameServerClusterRequest,
            google.cloud.gaming.v1.game_server_clusters_pb2.GameServerCluster,
        )
        self.CreateGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/CreateGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.CreateGameServerClusterRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PreviewCreateGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/PreviewCreateGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.PreviewCreateGameServerClusterRequest,
            google.cloud.gaming.v1.game_server_clusters_pb2.PreviewCreateGameServerClusterResponse,
        )
        self.DeleteGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/DeleteGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.DeleteGameServerClusterRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PreviewDeleteGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/PreviewDeleteGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.PreviewDeleteGameServerClusterRequest,
            google.cloud.gaming.v1.game_server_clusters_pb2.PreviewDeleteGameServerClusterResponse,
        )
        self.UpdateGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/UpdateGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.UpdateGameServerClusterRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PreviewUpdateGameServerCluster = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerClustersService/PreviewUpdateGameServerCluster',
            google.cloud.gaming.v1.game_server_clusters_pb2.PreviewUpdateGameServerClusterRequest,
            google.cloud.gaming.v1.game_server_clusters_pb2.PreviewUpdateGameServerClusterResponse,
        )

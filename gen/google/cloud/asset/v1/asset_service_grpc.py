# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/asset/v1/asset_service.proto
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
import google.cloud.asset.v1.assets_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.type.expr_pb2
import google.cloud.asset.v1.asset_service_pb2


class AssetServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ExportAssets(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.ExportAssetsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListAssets(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.ListAssetsRequest, google.cloud.asset.v1.asset_service_pb2.ListAssetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BatchGetAssetsHistory(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.BatchGetAssetsHistoryRequest, google.cloud.asset.v1.asset_service_pb2.BatchGetAssetsHistoryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateFeed(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.CreateFeedRequest, google.cloud.asset.v1.asset_service_pb2.Feed]') -> None:
        pass

    @abc.abstractmethod
    async def GetFeed(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.GetFeedRequest, google.cloud.asset.v1.asset_service_pb2.Feed]') -> None:
        pass

    @abc.abstractmethod
    async def ListFeeds(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.ListFeedsRequest, google.cloud.asset.v1.asset_service_pb2.ListFeedsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateFeed(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.UpdateFeedRequest, google.cloud.asset.v1.asset_service_pb2.Feed]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteFeed(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.DeleteFeedRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SearchAllResources(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.SearchAllResourcesRequest, google.cloud.asset.v1.asset_service_pb2.SearchAllResourcesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchAllIamPolicies(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.SearchAllIamPoliciesRequest, google.cloud.asset.v1.asset_service_pb2.SearchAllIamPoliciesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AnalyzeIamPolicy(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyRequest, google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AnalyzeIamPolicyLongrunning(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyLongrunningRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def AnalyzeMove(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1.asset_service_pb2.AnalyzeMoveRequest, google.cloud.asset.v1.asset_service_pb2.AnalyzeMoveResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.asset.v1.AssetService/ExportAssets': grpclib.const.Handler(
                self.ExportAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.ExportAssetsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.asset.v1.AssetService/ListAssets': grpclib.const.Handler(
                self.ListAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.ListAssetsRequest,
                google.cloud.asset.v1.asset_service_pb2.ListAssetsResponse,
            ),
            '/google.cloud.asset.v1.AssetService/BatchGetAssetsHistory': grpclib.const.Handler(
                self.BatchGetAssetsHistory,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.BatchGetAssetsHistoryRequest,
                google.cloud.asset.v1.asset_service_pb2.BatchGetAssetsHistoryResponse,
            ),
            '/google.cloud.asset.v1.AssetService/CreateFeed': grpclib.const.Handler(
                self.CreateFeed,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.CreateFeedRequest,
                google.cloud.asset.v1.asset_service_pb2.Feed,
            ),
            '/google.cloud.asset.v1.AssetService/GetFeed': grpclib.const.Handler(
                self.GetFeed,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.GetFeedRequest,
                google.cloud.asset.v1.asset_service_pb2.Feed,
            ),
            '/google.cloud.asset.v1.AssetService/ListFeeds': grpclib.const.Handler(
                self.ListFeeds,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.ListFeedsRequest,
                google.cloud.asset.v1.asset_service_pb2.ListFeedsResponse,
            ),
            '/google.cloud.asset.v1.AssetService/UpdateFeed': grpclib.const.Handler(
                self.UpdateFeed,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.UpdateFeedRequest,
                google.cloud.asset.v1.asset_service_pb2.Feed,
            ),
            '/google.cloud.asset.v1.AssetService/DeleteFeed': grpclib.const.Handler(
                self.DeleteFeed,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.DeleteFeedRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.asset.v1.AssetService/SearchAllResources': grpclib.const.Handler(
                self.SearchAllResources,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.SearchAllResourcesRequest,
                google.cloud.asset.v1.asset_service_pb2.SearchAllResourcesResponse,
            ),
            '/google.cloud.asset.v1.AssetService/SearchAllIamPolicies': grpclib.const.Handler(
                self.SearchAllIamPolicies,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.SearchAllIamPoliciesRequest,
                google.cloud.asset.v1.asset_service_pb2.SearchAllIamPoliciesResponse,
            ),
            '/google.cloud.asset.v1.AssetService/AnalyzeIamPolicy': grpclib.const.Handler(
                self.AnalyzeIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyRequest,
                google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyResponse,
            ),
            '/google.cloud.asset.v1.AssetService/AnalyzeIamPolicyLongrunning': grpclib.const.Handler(
                self.AnalyzeIamPolicyLongrunning,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyLongrunningRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.asset.v1.AssetService/AnalyzeMove': grpclib.const.Handler(
                self.AnalyzeMove,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1.asset_service_pb2.AnalyzeMoveRequest,
                google.cloud.asset.v1.asset_service_pb2.AnalyzeMoveResponse,
            ),
        }


class AssetServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ExportAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/ExportAssets',
            google.cloud.asset.v1.asset_service_pb2.ExportAssetsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/ListAssets',
            google.cloud.asset.v1.asset_service_pb2.ListAssetsRequest,
            google.cloud.asset.v1.asset_service_pb2.ListAssetsResponse,
        )
        self.BatchGetAssetsHistory = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/BatchGetAssetsHistory',
            google.cloud.asset.v1.asset_service_pb2.BatchGetAssetsHistoryRequest,
            google.cloud.asset.v1.asset_service_pb2.BatchGetAssetsHistoryResponse,
        )
        self.CreateFeed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/CreateFeed',
            google.cloud.asset.v1.asset_service_pb2.CreateFeedRequest,
            google.cloud.asset.v1.asset_service_pb2.Feed,
        )
        self.GetFeed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/GetFeed',
            google.cloud.asset.v1.asset_service_pb2.GetFeedRequest,
            google.cloud.asset.v1.asset_service_pb2.Feed,
        )
        self.ListFeeds = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/ListFeeds',
            google.cloud.asset.v1.asset_service_pb2.ListFeedsRequest,
            google.cloud.asset.v1.asset_service_pb2.ListFeedsResponse,
        )
        self.UpdateFeed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/UpdateFeed',
            google.cloud.asset.v1.asset_service_pb2.UpdateFeedRequest,
            google.cloud.asset.v1.asset_service_pb2.Feed,
        )
        self.DeleteFeed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/DeleteFeed',
            google.cloud.asset.v1.asset_service_pb2.DeleteFeedRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SearchAllResources = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/SearchAllResources',
            google.cloud.asset.v1.asset_service_pb2.SearchAllResourcesRequest,
            google.cloud.asset.v1.asset_service_pb2.SearchAllResourcesResponse,
        )
        self.SearchAllIamPolicies = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/SearchAllIamPolicies',
            google.cloud.asset.v1.asset_service_pb2.SearchAllIamPoliciesRequest,
            google.cloud.asset.v1.asset_service_pb2.SearchAllIamPoliciesResponse,
        )
        self.AnalyzeIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/AnalyzeIamPolicy',
            google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyRequest,
            google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyResponse,
        )
        self.AnalyzeIamPolicyLongrunning = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/AnalyzeIamPolicyLongrunning',
            google.cloud.asset.v1.asset_service_pb2.AnalyzeIamPolicyLongrunningRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.AnalyzeMove = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1.AssetService/AnalyzeMove',
            google.cloud.asset.v1.asset_service_pb2.AnalyzeMoveRequest,
            google.cloud.asset.v1.asset_service_pb2.AnalyzeMoveResponse,
        )

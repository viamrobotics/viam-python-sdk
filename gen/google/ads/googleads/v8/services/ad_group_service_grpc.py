# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/ad_group_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.ad_group_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.ad_group_service_pb2


class AdGroupServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAdGroup(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.ad_group_service_pb2.GetAdGroupRequest, google.ads.googleads.v8.resources.ad_group_pb2.AdGroup]') -> None:
        pass

    @abc.abstractmethod
    async def MutateAdGroups(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.ad_group_service_pb2.MutateAdGroupsRequest, google.ads.googleads.v8.services.ad_group_service_pb2.MutateAdGroupsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.AdGroupService/GetAdGroup': grpclib.const.Handler(
                self.GetAdGroup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.ad_group_service_pb2.GetAdGroupRequest,
                google.ads.googleads.v8.resources.ad_group_pb2.AdGroup,
            ),
            '/google.ads.googleads.v8.services.AdGroupService/MutateAdGroups': grpclib.const.Handler(
                self.MutateAdGroups,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.ad_group_service_pb2.MutateAdGroupsRequest,
                google.ads.googleads.v8.services.ad_group_service_pb2.MutateAdGroupsResponse,
            ),
        }


class AdGroupServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAdGroup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.AdGroupService/GetAdGroup',
            google.ads.googleads.v8.services.ad_group_service_pb2.GetAdGroupRequest,
            google.ads.googleads.v8.resources.ad_group_pb2.AdGroup,
        )
        self.MutateAdGroups = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.AdGroupService/MutateAdGroups',
            google.ads.googleads.v8.services.ad_group_service_pb2.MutateAdGroupsRequest,
            google.ads.googleads.v8.services.ad_group_service_pb2.MutateAdGroupsResponse,
        )

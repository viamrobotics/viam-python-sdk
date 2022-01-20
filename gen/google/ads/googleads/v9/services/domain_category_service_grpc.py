# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/domain_category_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.domain_category_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.domain_category_service_pb2


class DomainCategoryServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetDomainCategory(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.domain_category_service_pb2.GetDomainCategoryRequest, google.ads.googleads.v9.resources.domain_category_pb2.DomainCategory]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.DomainCategoryService/GetDomainCategory': grpclib.const.Handler(
                self.GetDomainCategory,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.domain_category_service_pb2.GetDomainCategoryRequest,
                google.ads.googleads.v9.resources.domain_category_pb2.DomainCategory,
            ),
        }


class DomainCategoryServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetDomainCategory = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.DomainCategoryService/GetDomainCategory',
            google.ads.googleads.v9.services.domain_category_service_pb2.GetDomainCategoryRequest,
            google.ads.googleads.v9.resources.domain_category_pb2.DomainCategory,
        )

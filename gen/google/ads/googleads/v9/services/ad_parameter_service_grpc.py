# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/ad_parameter_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.ad_parameter_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.ad_parameter_service_pb2


class AdParameterServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAdParameter(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.ad_parameter_service_pb2.GetAdParameterRequest, google.ads.googleads.v9.resources.ad_parameter_pb2.AdParameter]') -> None:
        pass

    @abc.abstractmethod
    async def MutateAdParameters(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.ad_parameter_service_pb2.MutateAdParametersRequest, google.ads.googleads.v9.services.ad_parameter_service_pb2.MutateAdParametersResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.AdParameterService/GetAdParameter': grpclib.const.Handler(
                self.GetAdParameter,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.ad_parameter_service_pb2.GetAdParameterRequest,
                google.ads.googleads.v9.resources.ad_parameter_pb2.AdParameter,
            ),
            '/google.ads.googleads.v9.services.AdParameterService/MutateAdParameters': grpclib.const.Handler(
                self.MutateAdParameters,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.ad_parameter_service_pb2.MutateAdParametersRequest,
                google.ads.googleads.v9.services.ad_parameter_service_pb2.MutateAdParametersResponse,
            ),
        }


class AdParameterServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAdParameter = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.AdParameterService/GetAdParameter',
            google.ads.googleads.v9.services.ad_parameter_service_pb2.GetAdParameterRequest,
            google.ads.googleads.v9.resources.ad_parameter_pb2.AdParameter,
        )
        self.MutateAdParameters = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.AdParameterService/MutateAdParameters',
            google.ads.googleads.v9.services.ad_parameter_service_pb2.MutateAdParametersRequest,
            google.ads.googleads.v9.services.ad_parameter_service_pb2.MutateAdParametersResponse,
        )

# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/conversion_upload_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.common.offline_user_data_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.conversion_upload_service_pb2


class ConversionUploadServiceBase(abc.ABC):

    @abc.abstractmethod
    async def UploadClickConversions(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadClickConversionsRequest, google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadClickConversionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UploadCallConversions(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadCallConversionsRequest, google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadCallConversionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.ConversionUploadService/UploadClickConversions': grpclib.const.Handler(
                self.UploadClickConversions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadClickConversionsRequest,
                google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadClickConversionsResponse,
            ),
            '/google.ads.googleads.v9.services.ConversionUploadService/UploadCallConversions': grpclib.const.Handler(
                self.UploadCallConversions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadCallConversionsRequest,
                google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadCallConversionsResponse,
            ),
        }


class ConversionUploadServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UploadClickConversions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.ConversionUploadService/UploadClickConversions',
            google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadClickConversionsRequest,
            google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadClickConversionsResponse,
        )
        self.UploadCallConversions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.ConversionUploadService/UploadCallConversions',
            google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadCallConversionsRequest,
            google.ads.googleads.v9.services.conversion_upload_service_pb2.UploadCallConversionsResponse,
        )

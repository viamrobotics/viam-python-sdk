# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/conversion_adjustment_upload_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.enums.conversion_adjustment_type_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.rpc.status_pb2
import google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2


class ConversionAdjustmentUploadServiceBase(abc.ABC):

    @abc.abstractmethod
    async def UploadConversionAdjustments(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsRequest, google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.ConversionAdjustmentUploadService/UploadConversionAdjustments': grpclib.const.Handler(
                self.UploadConversionAdjustments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsRequest,
                google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsResponse,
            ),
        }


class ConversionAdjustmentUploadServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UploadConversionAdjustments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.ConversionAdjustmentUploadService/UploadConversionAdjustments',
            google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsRequest,
            google.ads.googleads.v7.services.conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsResponse,
        )

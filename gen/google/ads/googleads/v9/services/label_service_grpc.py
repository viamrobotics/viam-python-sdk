# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/label_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.label_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.label_service_pb2


class LabelServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetLabel(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.label_service_pb2.GetLabelRequest, google.ads.googleads.v9.resources.label_pb2.Label]') -> None:
        pass

    @abc.abstractmethod
    async def MutateLabels(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.label_service_pb2.MutateLabelsRequest, google.ads.googleads.v9.services.label_service_pb2.MutateLabelsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.LabelService/GetLabel': grpclib.const.Handler(
                self.GetLabel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.label_service_pb2.GetLabelRequest,
                google.ads.googleads.v9.resources.label_pb2.Label,
            ),
            '/google.ads.googleads.v9.services.LabelService/MutateLabels': grpclib.const.Handler(
                self.MutateLabels,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.label_service_pb2.MutateLabelsRequest,
                google.ads.googleads.v9.services.label_service_pb2.MutateLabelsResponse,
            ),
        }


class LabelServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetLabel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.LabelService/GetLabel',
            google.ads.googleads.v9.services.label_service_pb2.GetLabelRequest,
            google.ads.googleads.v9.resources.label_pb2.Label,
        )
        self.MutateLabels = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.LabelService/MutateLabels',
            google.ads.googleads.v9.services.label_service_pb2.MutateLabelsRequest,
            google.ads.googleads.v9.services.label_service_pb2.MutateLabelsResponse,
        )

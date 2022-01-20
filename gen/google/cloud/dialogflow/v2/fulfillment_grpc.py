# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2/fulfillment.proto
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
import google.protobuf.field_mask_pb2
import google.cloud.dialogflow.v2.fulfillment_pb2


class FulfillmentsBase(abc.ABC):

    @abc.abstractmethod
    async def GetFulfillment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.fulfillment_pb2.GetFulfillmentRequest, google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateFulfillment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.fulfillment_pb2.UpdateFulfillmentRequest, google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2.Fulfillments/GetFulfillment': grpclib.const.Handler(
                self.GetFulfillment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.fulfillment_pb2.GetFulfillmentRequest,
                google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment,
            ),
            '/google.cloud.dialogflow.v2.Fulfillments/UpdateFulfillment': grpclib.const.Handler(
                self.UpdateFulfillment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.fulfillment_pb2.UpdateFulfillmentRequest,
                google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment,
            ),
        }


class FulfillmentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetFulfillment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Fulfillments/GetFulfillment',
            google.cloud.dialogflow.v2.fulfillment_pb2.GetFulfillmentRequest,
            google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment,
        )
        self.UpdateFulfillment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Fulfillments/UpdateFulfillment',
            google.cloud.dialogflow.v2.fulfillment_pb2.UpdateFulfillmentRequest,
            google.cloud.dialogflow.v2.fulfillment_pb2.Fulfillment,
        )

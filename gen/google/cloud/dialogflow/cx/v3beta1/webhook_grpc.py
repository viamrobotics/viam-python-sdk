# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/cx/v3beta1/webhook.proto
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
import google.cloud.dialogflow.cx.v3beta1.response_message_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.cloud.dialogflow.cx.v3beta1.webhook_pb2


class WebhooksBase(abc.ABC):

    @abc.abstractmethod
    async def ListWebhooks(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.webhook_pb2.ListWebhooksRequest, google.cloud.dialogflow.cx.v3beta1.webhook_pb2.ListWebhooksResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetWebhook(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.webhook_pb2.GetWebhookRequest, google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook]') -> None:
        pass

    @abc.abstractmethod
    async def CreateWebhook(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.webhook_pb2.CreateWebhookRequest, google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateWebhook(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.webhook_pb2.UpdateWebhookRequest, google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteWebhook(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.webhook_pb2.DeleteWebhookRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/ListWebhooks': grpclib.const.Handler(
                self.ListWebhooks,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.ListWebhooksRequest,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.ListWebhooksResponse,
            ),
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/GetWebhook': grpclib.const.Handler(
                self.GetWebhook,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.GetWebhookRequest,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook,
            ),
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/CreateWebhook': grpclib.const.Handler(
                self.CreateWebhook,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.CreateWebhookRequest,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook,
            ),
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/UpdateWebhook': grpclib.const.Handler(
                self.UpdateWebhook,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.UpdateWebhookRequest,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook,
            ),
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/DeleteWebhook': grpclib.const.Handler(
                self.DeleteWebhook,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.webhook_pb2.DeleteWebhookRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class WebhooksStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListWebhooks = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/ListWebhooks',
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.ListWebhooksRequest,
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.ListWebhooksResponse,
        )
        self.GetWebhook = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/GetWebhook',
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.GetWebhookRequest,
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook,
        )
        self.CreateWebhook = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/CreateWebhook',
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.CreateWebhookRequest,
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook,
        )
        self.UpdateWebhook = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/UpdateWebhook',
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.UpdateWebhookRequest,
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.Webhook,
        )
        self.DeleteWebhook = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Webhooks/DeleteWebhook',
            google.cloud.dialogflow.cx.v3beta1.webhook_pb2.DeleteWebhookRequest,
            google.protobuf.empty_pb2.Empty,
        )

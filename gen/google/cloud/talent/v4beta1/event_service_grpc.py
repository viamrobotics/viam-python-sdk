# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/talent/v4beta1/event_service.proto
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
import google.cloud.talent.v4beta1.event_pb2
import google.cloud.talent.v4beta1.event_service_pb2


class EventServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateClientEvent(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4beta1.event_service_pb2.CreateClientEventRequest, google.cloud.talent.v4beta1.event_pb2.ClientEvent]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.talent.v4beta1.EventService/CreateClientEvent': grpclib.const.Handler(
                self.CreateClientEvent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4beta1.event_service_pb2.CreateClientEventRequest,
                google.cloud.talent.v4beta1.event_pb2.ClientEvent,
            ),
        }


class EventServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateClientEvent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4beta1.EventService/CreateClientEvent',
            google.cloud.talent.v4beta1.event_service_pb2.CreateClientEventRequest,
            google.cloud.talent.v4beta1.event_pb2.ClientEvent,
        )

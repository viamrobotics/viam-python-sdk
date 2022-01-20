# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/firebase/fcm/connection/v1alpha1/connection_api.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.protobuf.timestamp_pb2
import google.firebase.fcm.connection.v1alpha1.connection_api_pb2


class ConnectionApiBase(abc.ABC):

    @abc.abstractmethod
    async def Connect(self, stream: 'grpclib.server.Stream[google.firebase.fcm.connection.v1alpha1.connection_api_pb2.UpstreamRequest, google.firebase.fcm.connection.v1alpha1.connection_api_pb2.DownstreamResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.firebase.fcm.connection.v1alpha1.ConnectionApi/Connect': grpclib.const.Handler(
                self.Connect,
                grpclib.const.Cardinality.STREAM_STREAM,
                google.firebase.fcm.connection.v1alpha1.connection_api_pb2.UpstreamRequest,
                google.firebase.fcm.connection.v1alpha1.connection_api_pb2.DownstreamResponse,
            ),
        }


class ConnectionApiStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Connect = grpclib.client.StreamStreamMethod(
            channel,
            '/google.firebase.fcm.connection.v1alpha1.ConnectionApi/Connect',
            google.firebase.fcm.connection.v1alpha1.connection_api_pb2.UpstreamRequest,
            google.firebase.fcm.connection.v1alpha1.connection_api_pb2.DownstreamResponse,
        )

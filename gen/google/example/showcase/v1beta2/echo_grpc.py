# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/example/showcase/v1beta2/echo.proto
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
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.example.showcase.v1beta2.echo_pb2


class EchoBase(abc.ABC):

    @abc.abstractmethod
    async def Echo(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.EchoRequest, google.example.showcase.v1beta2.echo_pb2.EchoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Expand(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.ExpandRequest, google.example.showcase.v1beta2.echo_pb2.EchoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Collect(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.EchoRequest, google.example.showcase.v1beta2.echo_pb2.EchoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Chat(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.EchoRequest, google.example.showcase.v1beta2.echo_pb2.EchoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PagedExpand(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.PagedExpandRequest, google.example.showcase.v1beta2.echo_pb2.PagedExpandResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Wait(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.WaitRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def Block(self, stream: 'grpclib.server.Stream[google.example.showcase.v1beta2.echo_pb2.BlockRequest, google.example.showcase.v1beta2.echo_pb2.BlockResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.example.showcase.v1beta2.Echo/Echo': grpclib.const.Handler(
                self.Echo,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.echo_pb2.EchoRequest,
                google.example.showcase.v1beta2.echo_pb2.EchoResponse,
            ),
            '/google.example.showcase.v1beta2.Echo/Expand': grpclib.const.Handler(
                self.Expand,
                grpclib.const.Cardinality.UNARY_STREAM,
                google.example.showcase.v1beta2.echo_pb2.ExpandRequest,
                google.example.showcase.v1beta2.echo_pb2.EchoResponse,
            ),
            '/google.example.showcase.v1beta2.Echo/Collect': grpclib.const.Handler(
                self.Collect,
                grpclib.const.Cardinality.STREAM_UNARY,
                google.example.showcase.v1beta2.echo_pb2.EchoRequest,
                google.example.showcase.v1beta2.echo_pb2.EchoResponse,
            ),
            '/google.example.showcase.v1beta2.Echo/Chat': grpclib.const.Handler(
                self.Chat,
                grpclib.const.Cardinality.STREAM_STREAM,
                google.example.showcase.v1beta2.echo_pb2.EchoRequest,
                google.example.showcase.v1beta2.echo_pb2.EchoResponse,
            ),
            '/google.example.showcase.v1beta2.Echo/PagedExpand': grpclib.const.Handler(
                self.PagedExpand,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.echo_pb2.PagedExpandRequest,
                google.example.showcase.v1beta2.echo_pb2.PagedExpandResponse,
            ),
            '/google.example.showcase.v1beta2.Echo/Wait': grpclib.const.Handler(
                self.Wait,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.echo_pb2.WaitRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.example.showcase.v1beta2.Echo/Block': grpclib.const.Handler(
                self.Block,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.example.showcase.v1beta2.echo_pb2.BlockRequest,
                google.example.showcase.v1beta2.echo_pb2.BlockResponse,
            ),
        }


class EchoStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Echo = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/Echo',
            google.example.showcase.v1beta2.echo_pb2.EchoRequest,
            google.example.showcase.v1beta2.echo_pb2.EchoResponse,
        )
        self.Expand = grpclib.client.UnaryStreamMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/Expand',
            google.example.showcase.v1beta2.echo_pb2.ExpandRequest,
            google.example.showcase.v1beta2.echo_pb2.EchoResponse,
        )
        self.Collect = grpclib.client.StreamUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/Collect',
            google.example.showcase.v1beta2.echo_pb2.EchoRequest,
            google.example.showcase.v1beta2.echo_pb2.EchoResponse,
        )
        self.Chat = grpclib.client.StreamStreamMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/Chat',
            google.example.showcase.v1beta2.echo_pb2.EchoRequest,
            google.example.showcase.v1beta2.echo_pb2.EchoResponse,
        )
        self.PagedExpand = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/PagedExpand',
            google.example.showcase.v1beta2.echo_pb2.PagedExpandRequest,
            google.example.showcase.v1beta2.echo_pb2.PagedExpandResponse,
        )
        self.Wait = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/Wait',
            google.example.showcase.v1beta2.echo_pb2.WaitRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.Block = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.example.showcase.v1beta2.Echo/Block',
            google.example.showcase.v1beta2.echo_pb2.BlockRequest,
            google.example.showcase.v1beta2.echo_pb2.BlockResponse,
        )

import abc
import typing
import grpclib.const
import grpclib.exceptions
if typing.TYPE_CHECKING:
    import grpclib.server
from ...... import proto
from .echoresource_grpc import EchoResourceServiceBase as _EchoResourceServiceBase

class UnimplementedEchoResourceServiceBase(_EchoResourceServiceBase):

    async def EchoResource(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoResourceMultiple(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceMultipleResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def EchoResourceBiDi(self, stream: 'grpclib.server.Stream[proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiRequest, proto.rpc.examples.echoresource.v1.echoresource_pb2.EchoResourceBiDiResponse]') -> None:
        raise grpclib.exceptions.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
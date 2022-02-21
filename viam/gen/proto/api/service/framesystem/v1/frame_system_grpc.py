import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class FrameSystemServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Config(self, stream: 'grpclib.server.Stream[proto.api.service.framesystem.v1.frame_system_pb2.ConfigRequest, proto.api.service.framesystem.v1.frame_system_pb2.ConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.service.framesystem.v1.FrameSystemService/Config': grpclib.const.Handler(self.Config, grpclib.const.Cardinality.UNARY_UNARY, proto.api.service.framesystem.v1.frame_system_pb2.ConfigRequest, proto.api.service.framesystem.v1.frame_system_pb2.ConfigResponse)}

class FrameSystemServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Config = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.service.framesystem.v1.FrameSystemService/Config', proto.api.service.framesystem.v1.frame_system_pb2.ConfigRequest, proto.api.service.framesystem.v1.frame_system_pb2.ConfigResponse)
import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto
from ...... import proto

class ArmServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetEndPosition(self, stream: 'grpclib.server.Stream[proto.api.component.arm.v1.arm_pb2.GetEndPositionRequest, proto.api.component.arm.v1.arm_pb2.GetEndPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToPosition(self, stream: 'grpclib.server.Stream[proto.api.component.arm.v1.arm_pb2.MoveToPositionRequest, proto.api.component.arm.v1.arm_pb2.MoveToPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetJointPositions(self, stream: 'grpclib.server.Stream[proto.api.component.arm.v1.arm_pb2.GetJointPositionsRequest, proto.api.component.arm.v1.arm_pb2.GetJointPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToJointPositions(self, stream: 'grpclib.server.Stream[proto.api.component.arm.v1.arm_pb2.MoveToJointPositionsRequest, proto.api.component.arm.v1.arm_pb2.MoveToJointPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[proto.api.component.arm.v1.arm_pb2.StopRequest, proto.api.component.arm.v1.arm_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.arm.v1.ArmService/GetEndPosition': grpclib.const.Handler(self.GetEndPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.arm.v1.arm_pb2.GetEndPositionRequest, proto.api.component.arm.v1.arm_pb2.GetEndPositionResponse), '/proto.api.component.arm.v1.ArmService/MoveToPosition': grpclib.const.Handler(self.MoveToPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.arm.v1.arm_pb2.MoveToPositionRequest, proto.api.component.arm.v1.arm_pb2.MoveToPositionResponse), '/proto.api.component.arm.v1.ArmService/GetJointPositions': grpclib.const.Handler(self.GetJointPositions, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.arm.v1.arm_pb2.GetJointPositionsRequest, proto.api.component.arm.v1.arm_pb2.GetJointPositionsResponse), '/proto.api.component.arm.v1.ArmService/MoveToJointPositions': grpclib.const.Handler(self.MoveToJointPositions, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.arm.v1.arm_pb2.MoveToJointPositionsRequest, proto.api.component.arm.v1.arm_pb2.MoveToJointPositionsResponse), '/proto.api.component.arm.v1.ArmService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.arm.v1.arm_pb2.StopRequest, proto.api.component.arm.v1.arm_pb2.StopResponse)}

class ArmServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetEndPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.arm.v1.ArmService/GetEndPosition', proto.api.component.arm.v1.arm_pb2.GetEndPositionRequest, proto.api.component.arm.v1.arm_pb2.GetEndPositionResponse)
        self.MoveToPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.arm.v1.ArmService/MoveToPosition', proto.api.component.arm.v1.arm_pb2.MoveToPositionRequest, proto.api.component.arm.v1.arm_pb2.MoveToPositionResponse)
        self.GetJointPositions = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.arm.v1.ArmService/GetJointPositions', proto.api.component.arm.v1.arm_pb2.GetJointPositionsRequest, proto.api.component.arm.v1.arm_pb2.GetJointPositionsResponse)
        self.MoveToJointPositions = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.arm.v1.ArmService/MoveToJointPositions', proto.api.component.arm.v1.arm_pb2.MoveToJointPositionsRequest, proto.api.component.arm.v1.arm_pb2.MoveToJointPositionsResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.arm.v1.ArmService/Stop', proto.api.component.arm.v1.arm_pb2.StopRequest, proto.api.component.arm.v1.arm_pb2.StopResponse)
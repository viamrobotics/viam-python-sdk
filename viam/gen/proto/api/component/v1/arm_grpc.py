import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto
from ..... import proto

class ArmServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetEndPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.arm_pb2.ArmServiceGetEndPositionRequest, proto.api.component.v1.arm_pb2.ArmServiceGetEndPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToPosition(self, stream: 'grpclib.server.Stream[proto.api.component.v1.arm_pb2.ArmServiceMoveToPositionRequest, proto.api.component.v1.arm_pb2.ArmServiceMoveToPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetJointPositions(self, stream: 'grpclib.server.Stream[proto.api.component.v1.arm_pb2.ArmServiceGetJointPositionsRequest, proto.api.component.v1.arm_pb2.ArmServiceGetJointPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def MoveToJointPositions(self, stream: 'grpclib.server.Stream[proto.api.component.v1.arm_pb2.ArmServiceMoveToJointPositionsRequest, proto.api.component.v1.arm_pb2.ArmServiceMoveToJointPositionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.ArmService/GetEndPosition': grpclib.const.Handler(self.GetEndPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.arm_pb2.ArmServiceGetEndPositionRequest, proto.api.component.v1.arm_pb2.ArmServiceGetEndPositionResponse), '/proto.api.component.v1.ArmService/MoveToPosition': grpclib.const.Handler(self.MoveToPosition, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.arm_pb2.ArmServiceMoveToPositionRequest, proto.api.component.v1.arm_pb2.ArmServiceMoveToPositionResponse), '/proto.api.component.v1.ArmService/GetJointPositions': grpclib.const.Handler(self.GetJointPositions, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.arm_pb2.ArmServiceGetJointPositionsRequest, proto.api.component.v1.arm_pb2.ArmServiceGetJointPositionsResponse), '/proto.api.component.v1.ArmService/MoveToJointPositions': grpclib.const.Handler(self.MoveToJointPositions, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.arm_pb2.ArmServiceMoveToJointPositionsRequest, proto.api.component.v1.arm_pb2.ArmServiceMoveToJointPositionsResponse)}

class ArmServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetEndPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ArmService/GetEndPosition', proto.api.component.v1.arm_pb2.ArmServiceGetEndPositionRequest, proto.api.component.v1.arm_pb2.ArmServiceGetEndPositionResponse)
        self.MoveToPosition = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ArmService/MoveToPosition', proto.api.component.v1.arm_pb2.ArmServiceMoveToPositionRequest, proto.api.component.v1.arm_pb2.ArmServiceMoveToPositionResponse)
        self.GetJointPositions = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ArmService/GetJointPositions', proto.api.component.v1.arm_pb2.ArmServiceGetJointPositionsRequest, proto.api.component.v1.arm_pb2.ArmServiceGetJointPositionsResponse)
        self.MoveToJointPositions = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.ArmService/MoveToJointPositions', proto.api.component.v1.arm_pb2.ArmServiceMoveToJointPositionsRequest, proto.api.component.v1.arm_pb2.ArmServiceMoveToJointPositionsResponse)
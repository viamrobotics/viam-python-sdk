import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from .... import component

class GripperServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Open(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Grab(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.gripper.v1.GripperService/Open': grpclib.const.Handler(self.Open, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse), '/viam.component.gripper.v1.GripperService/Grab': grpclib.const.Handler(self.Grab, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse), '/viam.component.gripper.v1.GripperService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse)}

class GripperServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Open = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/Open', component.gripper.v1.gripper_pb2.OpenRequest, component.gripper.v1.gripper_pb2.OpenResponse)
        self.Grab = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/Grab', component.gripper.v1.gripper_pb2.GrabRequest, component.gripper.v1.gripper_pb2.GrabResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.gripper.v1.GripperService/Stop', component.gripper.v1.gripper_pb2.StopRequest, component.gripper.v1.gripper_pb2.StopResponse)
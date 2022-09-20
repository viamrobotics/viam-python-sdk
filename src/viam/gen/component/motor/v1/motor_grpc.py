import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
import google.protobuf.struct_pb2
from .... import component

class MotorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SetPower(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.SetPowerRequest, component.motor.v1.motor_pb2.SetPowerResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoFor(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GoForRequest, component.motor.v1.motor_pb2.GoForResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GoTo(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GoToRequest, component.motor.v1.motor_pb2.GoToResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetZeroPosition(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.ResetZeroPositionRequest, component.motor.v1.motor_pb2.ResetZeroPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetPosition(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GetPositionRequest, component.motor.v1.motor_pb2.GetPositionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetProperties(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.GetPropertiesRequest, component.motor.v1.motor_pb2.GetPropertiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Stop(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.StopRequest, component.motor.v1.motor_pb2.StopResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IsPowered(self, stream: 'grpclib.server.Stream[component.motor.v1.motor_pb2.IsPoweredRequest, component.motor.v1.motor_pb2.IsPoweredResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/viam.component.motor.v1.MotorService/SetPower': grpclib.const.Handler(self.SetPower, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.SetPowerRequest, component.motor.v1.motor_pb2.SetPowerResponse), '/viam.component.motor.v1.MotorService/GoFor': grpclib.const.Handler(self.GoFor, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.GoForRequest, component.motor.v1.motor_pb2.GoForResponse), '/viam.component.motor.v1.MotorService/GoTo': grpclib.const.Handler(self.GoTo, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.GoToRequest, component.motor.v1.motor_pb2.GoToResponse), '/viam.component.motor.v1.MotorService/ResetZeroPosition': grpclib.const.Handler(self.ResetZeroPosition, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.ResetZeroPositionRequest, component.motor.v1.motor_pb2.ResetZeroPositionResponse), '/viam.component.motor.v1.MotorService/GetPosition': grpclib.const.Handler(self.GetPosition, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.GetPositionRequest, component.motor.v1.motor_pb2.GetPositionResponse), '/viam.component.motor.v1.MotorService/GetProperties': grpclib.const.Handler(self.GetProperties, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.GetPropertiesRequest, component.motor.v1.motor_pb2.GetPropertiesResponse), '/viam.component.motor.v1.MotorService/Stop': grpclib.const.Handler(self.Stop, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.StopRequest, component.motor.v1.motor_pb2.StopResponse), '/viam.component.motor.v1.MotorService/IsPowered': grpclib.const.Handler(self.IsPowered, grpclib.const.Cardinality.UNARY_UNARY, component.motor.v1.motor_pb2.IsPoweredRequest, component.motor.v1.motor_pb2.IsPoweredResponse)}

class MotorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetPower = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/SetPower', component.motor.v1.motor_pb2.SetPowerRequest, component.motor.v1.motor_pb2.SetPowerResponse)
        self.GoFor = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/GoFor', component.motor.v1.motor_pb2.GoForRequest, component.motor.v1.motor_pb2.GoForResponse)
        self.GoTo = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/GoTo', component.motor.v1.motor_pb2.GoToRequest, component.motor.v1.motor_pb2.GoToResponse)
        self.ResetZeroPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/ResetZeroPosition', component.motor.v1.motor_pb2.ResetZeroPositionRequest, component.motor.v1.motor_pb2.ResetZeroPositionResponse)
        self.GetPosition = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/GetPosition', component.motor.v1.motor_pb2.GetPositionRequest, component.motor.v1.motor_pb2.GetPositionResponse)
        self.GetProperties = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/GetProperties', component.motor.v1.motor_pb2.GetPropertiesRequest, component.motor.v1.motor_pb2.GetPropertiesResponse)
        self.Stop = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/Stop', component.motor.v1.motor_pb2.StopRequest, component.motor.v1.motor_pb2.StopResponse)
        self.IsPowered = grpclib.client.UnaryUnaryMethod(channel, '/viam.component.motor.v1.MotorService/IsPowered', component.motor.v1.motor_pb2.IsPoweredRequest, component.motor.v1.motor_pb2.IsPoweredResponse)
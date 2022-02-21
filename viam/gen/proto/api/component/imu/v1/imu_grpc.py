import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ...... import proto

class IMUServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ReadAngularVelocity(self, stream: 'grpclib.server.Stream[proto.api.component.imu.v1.imu_pb2.ReadAngularVelocityRequest, proto.api.component.imu.v1.imu_pb2.ReadAngularVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadOrientation(self, stream: 'grpclib.server.Stream[proto.api.component.imu.v1.imu_pb2.ReadOrientationRequest, proto.api.component.imu.v1.imu_pb2.ReadOrientationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadAcceleration(self, stream: 'grpclib.server.Stream[proto.api.component.imu.v1.imu_pb2.ReadAccelerationRequest, proto.api.component.imu.v1.imu_pb2.ReadAccelerationResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.imu.v1.IMUService/ReadAngularVelocity': grpclib.const.Handler(self.ReadAngularVelocity, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.imu.v1.imu_pb2.ReadAngularVelocityRequest, proto.api.component.imu.v1.imu_pb2.ReadAngularVelocityResponse), '/proto.api.component.imu.v1.IMUService/ReadOrientation': grpclib.const.Handler(self.ReadOrientation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.imu.v1.imu_pb2.ReadOrientationRequest, proto.api.component.imu.v1.imu_pb2.ReadOrientationResponse), '/proto.api.component.imu.v1.IMUService/ReadAcceleration': grpclib.const.Handler(self.ReadAcceleration, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.imu.v1.imu_pb2.ReadAccelerationRequest, proto.api.component.imu.v1.imu_pb2.ReadAccelerationResponse)}

class IMUServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReadAngularVelocity = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.imu.v1.IMUService/ReadAngularVelocity', proto.api.component.imu.v1.imu_pb2.ReadAngularVelocityRequest, proto.api.component.imu.v1.imu_pb2.ReadAngularVelocityResponse)
        self.ReadOrientation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.imu.v1.IMUService/ReadOrientation', proto.api.component.imu.v1.imu_pb2.ReadOrientationRequest, proto.api.component.imu.v1.imu_pb2.ReadOrientationResponse)
        self.ReadAcceleration = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.imu.v1.IMUService/ReadAcceleration', proto.api.component.imu.v1.imu_pb2.ReadAccelerationRequest, proto.api.component.imu.v1.imu_pb2.ReadAccelerationResponse)
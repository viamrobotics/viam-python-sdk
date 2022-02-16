import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
import google.api.annotations_pb2
from ..... import proto

class IMUServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ReadAngularVelocity(self, stream: 'grpclib.server.Stream[proto.api.component.v1.imu_pb2.IMUServiceReadAngularVelocityRequest, proto.api.component.v1.imu_pb2.IMUServiceReadAngularVelocityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadOrientation(self, stream: 'grpclib.server.Stream[proto.api.component.v1.imu_pb2.IMUServiceReadOrientationRequest, proto.api.component.v1.imu_pb2.IMUServiceReadOrientationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ReadAcceleration(self, stream: 'grpclib.server.Stream[proto.api.component.v1.imu_pb2.IMUServiceReadAccelerationRequest, proto.api.component.v1.imu_pb2.IMUServiceReadAccelerationResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/proto.api.component.v1.IMUService/ReadAngularVelocity': grpclib.const.Handler(self.ReadAngularVelocity, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.imu_pb2.IMUServiceReadAngularVelocityRequest, proto.api.component.v1.imu_pb2.IMUServiceReadAngularVelocityResponse), '/proto.api.component.v1.IMUService/ReadOrientation': grpclib.const.Handler(self.ReadOrientation, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.imu_pb2.IMUServiceReadOrientationRequest, proto.api.component.v1.imu_pb2.IMUServiceReadOrientationResponse), '/proto.api.component.v1.IMUService/ReadAcceleration': grpclib.const.Handler(self.ReadAcceleration, grpclib.const.Cardinality.UNARY_UNARY, proto.api.component.v1.imu_pb2.IMUServiceReadAccelerationRequest, proto.api.component.v1.imu_pb2.IMUServiceReadAccelerationResponse)}

class IMUServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReadAngularVelocity = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.IMUService/ReadAngularVelocity', proto.api.component.v1.imu_pb2.IMUServiceReadAngularVelocityRequest, proto.api.component.v1.imu_pb2.IMUServiceReadAngularVelocityResponse)
        self.ReadOrientation = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.IMUService/ReadOrientation', proto.api.component.v1.imu_pb2.IMUServiceReadOrientationRequest, proto.api.component.v1.imu_pb2.IMUServiceReadOrientationResponse)
        self.ReadAcceleration = grpclib.client.UnaryUnaryMethod(channel, '/proto.api.component.v1.IMUService/ReadAcceleration', proto.api.component.v1.imu_pb2.IMUServiceReadAccelerationRequest, proto.api.component.v1.imu_pb2.IMUServiceReadAccelerationResponse)
from grpclib.server import Stream

from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.base import (
    BaseServiceBase,
    MoveStraightRequest, MoveStraightResponse,
    MoveArcRequest, MoveArcResponse,
    SpinRequest, SpinResponse,
    StopRequest, StopResponse,
)

from .base import BaseBase


class BaseService(BaseServiceBase, ComponentServiceBase[BaseBase]):
    """
    gRPC service for a robotic Base
    """

    RESOURCE_TYPE = BaseBase

    async def MoveStraight(
        self,
        stream: Stream[MoveStraightRequest, MoveStraightResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await base.move_straight(
            distance=request.distance_mm,
            velocity=request.mm_per_sec,
            blocking=request.block
        )
        response = MoveStraightResponse()
        await stream.send_message(response)

    async def MoveArc(
        self,
        stream: Stream[MoveArcRequest, MoveArcResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await base.move_arc(
            distance=request.distance_mm,
            velocity=request.mm_per_sec,
            angle=request.angle_deg,
            blocking=request.block
        )
        response = MoveArcResponse()
        await stream.send_message(response)

    async def Spin(
        self,
        stream: Stream[SpinRequest, SpinResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await base.spin(
            angle=request.angle_deg,
            velocity=request.degs_per_sec,
            blocking=request.block
        )
        response = SpinResponse()
        await stream.send_message(response)

    async def Stop(
        self,
        stream: Stream[StopRequest, StopResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            base = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await base.stop()
        response = StopResponse()
        await stream.send_message(response)

from grpclib.server import Stream
from viam.components.base import ComponentServiceBase
from viam.components.registry import RegistryManager
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.servo import (
    ServoServiceBase,
    MoveRequest, MoveResponse,
    GetPositionRequest, GetPositionResponse
)

from .servo import ServoBase


class ServoService(ServoServiceBase, ComponentServiceBase):
    """
    gRPC Service for a Servo
    """

    manager: RegistryManager

    def get_servo(self, name: str) -> ServoBase:
        """
        Get the servo with the given name if it exists in the registry.
        If the servo does not exist in the registry,
        this function will raise an error

        Args:
            name (str): _description_

        Raises:
            ComponentNotFoundError

        Returns:
            ServoBase: The servo
        """
        return self.manager.get_component(ServoBase, name)

    async def Move(
        self,
        stream: Stream[MoveRequest, MoveResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_servo(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await servo.move(request.angle_deg)
        await stream.send_message(MoveResponse())

    async def GetPosition(
        self,
        stream: Stream[GetPositionRequest, GetPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            servo = self.get_servo(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        position = await servo.get_position()
        resp = GetPositionResponse(position_deg=position)
        await stream.send_message(resp)

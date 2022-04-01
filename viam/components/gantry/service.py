from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.gantry import (GantryServiceBase,
                                             GetLengthsRequest,
                                             GetLengthsResponse,
                                             GetPositionRequest,
                                             GetPositionResponse,
                                             MoveToPositionRequest,
                                             MoveToPositionResponse)

from .gantry import Gantry


class GantryService(GantryServiceBase, ComponentServiceBase[Gantry]):
    """
    gRPC Service for an Gantry
    """

    RESOURCE_TYPE = Gantry

    async def GetPosition(
        self,
        stream: Stream[GetPositionRequest, GetPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        position = await gantry.get_position()
        response = GetPositionResponse(positions_mm=position)
        await stream.send_message(response)

    async def MoveToPosition(
        self,
        stream: Stream[MoveToPositionRequest, MoveToPositionResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        await gantry.move_to_position(
            list(request.positions_mm),
            request.world_state
        )
        response = MoveToPositionResponse()
        await stream.send_message(response)

    async def GetLengths(
        self,
        stream: Stream[GetLengthsRequest, GetLengthsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            gantry = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        lengths = await gantry.get_lengths()
        response = GetLengthsResponse(lengths_mm=lengths)
        await stream.send_message(response)

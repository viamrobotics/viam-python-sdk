import asyncio

from viam.proto.component.board import Status as BoardStatus
from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .board import Board, Tick, TickStream
from .client import BoardClient
from .service import BoardRPCService

__all__ = ["Board"]


async def create_status(component: Board) -> Status:
    analogs, digital_interrupts = {}, {}
    s = BoardStatus(analogs=analogs, digital_interrupts=digital_interrupts)
    return Status(name=Board.get_resource_name(component.name), status=message_to_struct(s))


Registry.register_subtype(ResourceRegistration(Board, BoardRPCService, lambda name, channel: BoardClient(name, channel), create_status))

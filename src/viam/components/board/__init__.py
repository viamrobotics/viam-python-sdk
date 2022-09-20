from viam.proto.robot import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .board import Board
from .client import BoardClient
from .service import BoardService

__all__ = [
    "Board",
]


async def create_status(component: Board) -> Status:
    return Status(name=Board.get_resource_name(component.name), status=message_to_struct(await component.status()))


Registry.register(ComponentRegistration(Board, "board", BoardService, lambda name, channel: BoardClient(name, channel), create_status))

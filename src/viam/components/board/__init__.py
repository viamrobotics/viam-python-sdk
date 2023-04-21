from viam.proto.robot import Status
from viam.resource.registry import Registry, ResourceRegistration
from viam.utils import message_to_struct

from .board import Board
from .client import BoardClient
from .service import BoardService

__all__ = [
    "Board",
]


async def create_status(component: Board) -> Status:
    return Status(name=Board.get_resource_name(component.name), status=message_to_struct(await component.status()))


Registry.register_subtype(ResourceRegistration(Board, BoardService, lambda name, channel: BoardClient(name, channel), create_status))

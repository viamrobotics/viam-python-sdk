import asyncio
from viam.proto.component.gantry import Status as GantryStatus
from viam.proto.robot import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import GantryClient
from .gantry import Gantry
from .service import GantryService

__all__ = [
    "Gantry",
]


async def create_status(component: Gantry) -> Status:
    (positions_mm, lengths_mm, is_moving) = await asyncio.gather(component.get_position(), component.get_lengths(), component.is_moving())
    s = GantryStatus(positions_mm=positions_mm, lengths_mm=lengths_mm, is_moving=is_moving)
    return Status(name=Gantry.get_resource_name(component.name), status=message_to_struct(s))


Registry.register(ComponentRegistration(Gantry, "gantry", GantryService, lambda name, channel: GantryClient(name, channel), create_status))

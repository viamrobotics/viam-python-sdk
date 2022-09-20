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
    s = GantryStatus(
        positions_mm=await component.get_position(), lengths_mm=await component.get_lengths(), is_moving=await component.is_moving()
    )
    return Status(name=Gantry.get_resource_name(component.name), status=message_to_struct(s))


Registry.register(ComponentRegistration(Gantry, "gantry", GantryService, lambda name, channel: GantryClient(name, channel), create_status))

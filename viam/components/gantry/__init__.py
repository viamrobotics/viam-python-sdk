from viam.proto.api.component.gantry import Status as GantryStatus
from viam.proto.api.service.status import Status
from viam.registry import ComponentRegistration, Registry
from viam.utils import message_to_struct

from .client import GantryClient
from .gantry import Gantry
from .service import GantryService

__all__ = [
    'Gantry',
    'GantryClient',
]


async def create_status(component: Gantry) -> Status:
    s = GantryStatus(
        positions_mm=await component.get_position(),
        lengths_mm=await component.get_lengths()
    )
    return Status(
        name=Gantry.get_resource_name(component.name),
        status=message_to_struct(s)
    )

Registry.register(
    ComponentRegistration(
        Gantry,
        'gantry',
        GantryService,
        lambda name, channel: GantryClient(name, channel),
        create_status
    )
)

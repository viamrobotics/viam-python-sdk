from viam.resource.registry import ResourceRegistration, Registry

from .client import MovementSensorClient
from .movement_sensor import GeoPoint, MovementSensor, Orientation, Vector3
from .service import MovementSensorService

__all__ = [
    "MovementSensor",
    "GeoPoint",
    "Orientation",
    "Vector3",
]

Registry.register_subtype(
    ResourceRegistration(
        MovementSensor,
        MovementSensorService,
        lambda name, channel: MovementSensorClient(name, channel),
    )
)

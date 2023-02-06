from viam.resource.registry import ComponentRegistration, Registry

from .client import MovementSensorClient
from .movement_sensor import GeoPoint, MovementSensor, Orientation, Vector3
from .service import MovementSensorService

__all__ = [
    "MovementSensor",
    "GeoPoint",
    "Orientation",
    "Vector3",
]

Registry.register(
    ComponentRegistration(
        MovementSensor,
        MovementSensorService,
        lambda name, channel: MovementSensorClient(name, channel),
    )
)

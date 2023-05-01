from viam.resource.registry import Registry, ResourceRegistration

from .client import MovementSensorClient
from .movement_sensor import GeoPoint, MovementSensor, Orientation, Vector3
from .service import MovementSensorRPCService

__all__ = [
    "MovementSensor",
    "GeoPoint",
    "Orientation",
    "Vector3",
]

Registry.register_subtype(
    ResourceRegistration(
        MovementSensor,
        MovementSensorRPCService,
        lambda name, channel: MovementSensorClient(name, channel),
    )
)

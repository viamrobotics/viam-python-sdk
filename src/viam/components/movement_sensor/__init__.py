from viam.proto.common import GeoPoint, Orientation, Vector3
from viam.resource.registry import Registry, ResourceRegistration

from .client import MovementSensorClient
from .movement_sensor import MovementSensor
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

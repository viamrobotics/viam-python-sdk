from viam.proto.common import Geometry
from viam.resource.registry import Registry, ResourceRegistration

from .client import PowerSensorClient
from .power_sensor import PowerSensor
from .service import PowerSensorRPCService

__all__ = [
    "PowerSensor",
    "Geometry",
]

Registry.register_subtype(
    ResourceRegistration(
        PowerSensor,
        PowerSensorRPCService,
        lambda name, channel: PowerSensorClient(name, channel),
    )
)

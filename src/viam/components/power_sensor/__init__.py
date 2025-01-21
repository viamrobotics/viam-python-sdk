from viam.resource.registry import Registry, ResourceRegistration

from .client import PowerSensorClient
from .power_sensor import PowerSensor
from .service import PowerSensorRPCService

__all__ = [
    "PowerSensor",
]

Registry.register_api(
    ResourceRegistration(
        PowerSensor,
        PowerSensorRPCService,
        lambda name, channel: PowerSensorClient(name, channel),
    )
)

from viam.resource.registry import Registry, ResourceRegistration

from .client import SensorClient
from .sensor import Sensor
from .service import SensorRPCService

__all__ = [
    "Sensor",
]

Registry.register_subtype(
    ResourceRegistration(
        Sensor,
        SensorRPCService,
        lambda name, channel: SensorClient(name, channel),
    )
)

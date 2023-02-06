from viam.resource.registry import ComponentRegistration, Registry

from .client import SensorClient
from .sensor import Sensor
from .service import SensorService

__all__ = [
    "Sensor",
]

Registry.register(
    ComponentRegistration(
        Sensor,
        SensorService,
        lambda name, channel: SensorClient(name, channel),
    )
)

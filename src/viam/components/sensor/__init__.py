import viam.gen.component.sensor.v1.sensor_pb2  # Need this import for Sensor service descriptors to resolve
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

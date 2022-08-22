from typing import Generic, Type, TypeVar

from grpclib.client import Channel
from viam.proto.api.common import ResourceName
from viam.services.motion import MotionServiceClient
from viam.services.sensors import SensorsServiceClient
from viam.services.vision import VisionServiceClient

Service = TypeVar("Service")


class ServiceType(Generic[Service]):
    @classmethod
    @property
    def MOTION(cls):
        return ServiceType("motion", MotionServiceClient)

    @classmethod
    @property
    def VISION(cls):
        return ServiceType("vision", VisionServiceClient)

    @classmethod
    @property
    def SENSORS(cls):
        return ServiceType("sensor", SensorsServiceClient)

    def __init__(self, name: str, cls: Type[Service]):
        self.resource_name = ResourceName(namespace="rdk", type="service", subtype=name, name=name)
        self._cls = cls

    @property
    def name(self):
        return self.resource_name.name

    def with_channel(self, channel: Channel) -> Service:
        return self._cls(channel)

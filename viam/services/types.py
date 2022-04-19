from typing import Generic, Type, TypeVar

from grpclib.client import Channel
from viam.proto.api.common import ResourceName
from viam.services.frame_system import FrameSystemClient
from viam.services.metadata.client import MetadataClient
from viam.services.motion import MotionClient
from viam.services.object_segmentation import ObjectSegmentationClient
from viam.services.status.client import StatusClient

Service = TypeVar('Service')


class ServiceType(Generic[Service]):

    @classmethod
    @property
    def METADATA(cls):
        return ServiceType('metadata', MetadataClient)

    @classmethod
    @property
    def STATUS(cls):
        return ServiceType('status', StatusClient)

    @classmethod
    @property
    def FRAME_SYSTEM(cls):
        return ServiceType('frame_system', FrameSystemClient)

    @classmethod
    @property
    def MOTION(cls):
        return ServiceType('motion', MotionClient)

    @classmethod
    @property
    def OBJECT_SEGMENTATION(cls):
        return ServiceType('object_segmentation', ObjectSegmentationClient)

    def __init__(self, name: str, cls: Type[Service]):
        self.resource_name = ResourceName(
            namespace='rdk',
            type='service',
            subtype=name,
            name=name
        )
        self._cls = cls

    @property
    def name(self):
        return self.resource_name.name

    def with_channel(self, channel: Channel) -> Service:
        return self._cls(channel)

from viam.proto.common import Pose
from viam.proto.service.slam import MappingMode, SensorInfo
from viam.resource.registry import Registry, ResourceRegistration

from .client import SLAMClient
from .service import SLAMRPCService
from .slam import SLAM

__all__ = [
    "Pose",
    "MappingMode",
    "SensorInfo",
    "SLAMClient",
    "SLAM",
]

Registry.register_subtype(ResourceRegistration(SLAM, SLAMRPCService, lambda name, channel: SLAMClient(name, channel)))

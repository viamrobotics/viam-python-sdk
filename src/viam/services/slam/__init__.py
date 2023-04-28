from viam.proto.common import Pose
from viam.resource.registry import Registry, ResourceRegistration

from .client import SLAMServiceClient
from .service import SLAMServiceRPCService
from .slam import SLAM

__all__ = [
    "Pose",
    "SLAMServiceClient",
    "SLAM",
]

Registry.register_subtype(ResourceRegistration(SLAM, SLAMServiceRPCService, lambda name, channel: SLAMServiceClient(name, channel)))

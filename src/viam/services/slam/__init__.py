from viam.proto.common import Pose
from viam.resource.registry import Registry, ResourceRegistration

from .client import SLAMServiceClient
from .service import SLAMServiceRPCService
from .slam import SLAMService

__all__ = [
    "Pose",
    "SLAMServiceClient",
    "SLAMService",
]

Registry.register_subtype(ResourceRegistration(SLAMService, SLAMServiceRPCService, lambda name, channel: SLAMServiceClient(name, channel)))

from viam.proto.service.motion import Constraints, GetPlanResponse, ListPlanStatusesResponse, MotionConfiguration
from viam.resource.registry import Registry, ResourceRegistration

from .client import MotionClient
from .motion import Motion
from .service import MotionRPCService

__all__ = ["MotionClient", "MotionConfiguration", "Constraints", "GetPlanResponse", "ListPlanStatusesResponse"]


Registry.register_subtype(
    ResourceRegistration(
        Motion,
        MotionRPCService,
        lambda name, channel: MotionClient(name, channel),
    )
)

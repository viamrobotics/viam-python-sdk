from viam.resource.registry import Registry, ResourceRegistration

from .client import PoseTrackerClient
from .pose_tracker import PoseTracker
from .service import PoseTrackerRPCService

__all__ = [
    "PoseTracker",
]

Registry.register_subtype(
    ResourceRegistration(
        PoseTracker,
        PoseTrackerRPCService,
        lambda name, channel: PoseTrackerClient(name, channel),
    )
)

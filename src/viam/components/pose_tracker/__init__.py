from viam.resource.registry import ResourceRegistration, Registry

from .client import PoseTrackerClient
from .pose_tracker import PoseTracker
from .service import PoseTrackerService

__all__ = [
    "PoseTracker",
]

Registry.register_subtype(
    ResourceRegistration(
        PoseTracker,
        PoseTrackerService,
        lambda name, channel: PoseTrackerClient(name, channel),
    )
)

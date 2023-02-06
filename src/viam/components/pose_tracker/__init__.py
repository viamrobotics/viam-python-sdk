from viam.resource.registry import ComponentRegistration, Registry

from .client import PoseTrackerClient
from .pose_tracker import PoseTracker
from .service import PoseTrackerService

__all__ = [
    "PoseTracker",
]

Registry.register(
    ComponentRegistration(
        PoseTracker,
        PoseTrackerService,
        lambda name, channel: PoseTrackerClient(name, channel),
    )
)

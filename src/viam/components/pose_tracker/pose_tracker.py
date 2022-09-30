import abc
from typing import Dict, List

from viam.proto.common import PoseInFrame

from ..component_base import ComponentBase


class PoseTracker(ComponentBase):
    """
    PoseTracker represents a physical pose or motion tracking device.

    This acts as an abstract base class for any drivers representing specific
    pose tracker implementations. This cannot be used on its own. If the `__init__()` function is
    overridden, it must call the `super().__init__()` function.
    """

    @abc.abstractmethod
    async def get_poses(self, body_names: List[str], **kwargs) -> Dict[str, PoseInFrame]:
        """
        Returns the current pose of each body tracked by the pose tracker.

        Args:
            body_names (List[str]): Names of the bodies whose poses are being
                requested. In the event this parameter is not supplied or is
                an empty list, all available poses are returned.
        """
        ...

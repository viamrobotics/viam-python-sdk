import abc
from typing import Any, Dict, Final, List, Mapping, Optional

from viam.proto.common import PoseInFrame
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class PoseTracker(ComponentBase):
    """
    PoseTracker represents a physical pose or motion tracking device.

    This acts as an abstract base class for any drivers representing specific
    pose tracker implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "pose_tracker"
    )

    @abc.abstractmethod
    async def get_poses(
        self,
        body_names: List[str],
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Dict[str, PoseInFrame]:
        """
        Returns the current pose of each body tracked by the pose tracker.

        Args:
            body_names (List[str]): Names of the bodies whose poses are being
                requested. In the event this parameter is not supplied or is
                an empty list, all available poses are returned.
        """
        ...

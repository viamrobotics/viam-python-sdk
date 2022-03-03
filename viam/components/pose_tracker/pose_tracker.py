import abc
from typing import Dict, List

from viam.proto.api.common import PoseInFrame

from ..component_base import ComponentBase


class PoseTrackerBase(ComponentBase):

    @abc.abstractmethod
    async def get_poses(self, body_names: List[str]) -> Dict[str, PoseInFrame]:
        """returns the current pose of each body tracked by the pose tracker

        Args:
            body_names (List[str]): Names of the bodies whose poses are being 
                requested. In the event this parameter is not supplied or is 
                an empty list, all available poses are returned 
        """
        ...

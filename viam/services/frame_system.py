from typing import List
from grpclib.client import Channel
from viam.proto.api.common import PoseInFrame
from viam.proto.api.service.framesystem import (Config, ConfigRequest,
                                                ConfigResponse,
                                                FrameSystemServiceStub,
                                                TransformPoseRequest,
                                                TransformPoseResponse)


class FrameSystemClient:
    """
    FrameSystem is Viam service that handles tracking and trasforming the reference frames of observations made by different components of
    a robot.

    """

    def __init__(self, channel: Channel) -> None:
        self.client = FrameSystemServiceStub(channel)

    async def config(self) -> List[Config]:
        """
        Get the configuration of the frame system of a given robot.

        Returns: The configuration of a given robot's frame system
        """
        request = ConfigRequest()
        response: ConfigResponse = await self.client.Config(request)
        return list(response.frame_system_configs)

    async def transform_pose(
        self,
        source: PoseInFrame,
        destination: str
    ) -> PoseInFrame:
        """
        Transforms a given pose from the reference frame to a new specified reference frame.

        Args:

            source (Pose): The pose that needs to be transformed
            destination : The reference frame to transform the given pose to

        """
        request = TransformPoseRequest(source=source, destination=destination)
        response: TransformPoseResponse = \
            await self.client.TransformPose(request)
        return response.pose

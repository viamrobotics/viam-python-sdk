from typing import List
from grpclib.client import Channel
from viam.proto.api.common import PoseInFrame
from viam.proto.api.service.framesystem import (Config, ConfigRequest,
                                                ConfigResponse,
                                                FrameSystemServiceStub,
                                                TransformPoseRequest,
                                                TransformPoseResponse)


class FrameSystemClient:

    def __init__(self, channel: Channel) -> None:
        self.client = FrameSystemServiceStub(channel)

    async def config(self) -> List[Config]:
        request = ConfigRequest()
        response: ConfigResponse = await self.client.Config(request)
        return list(response.frame_system_configs)

    async def transform_pose(
        self,
        source: PoseInFrame,
        destination: str
    ) -> PoseInFrame:
        request = TransformPoseRequest(source=source, destination=destination)
        response: TransformPoseResponse = \
            await self.client.TransformPose(request)
        return response.pose

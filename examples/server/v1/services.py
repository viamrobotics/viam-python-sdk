from typing import List
from viam.services.slam import Pose, SLAM
from tests.mocks.services import INTERNAL_STATE_CHUNKS, POINT_CLOUD_PCD_CHUNKS, POSITION


class ExampleSLAM(SLAM):
    def __init__(self, name: str):
        self.position = POSITION
        self.internal_chunks = INTERNAL_STATE_CHUNKS
        self.point_cloud_chunks = POINT_CLOUD_PCD_CHUNKS
        super().__init__(name)

    async def get_internal_state(self, **kwargs) -> List[bytes]:
        return self.internal_chunks

    async def get_point_cloud_map(self, **kwargs) -> List[bytes]:
        return self.point_cloud_chunks

    async def get_position(self, **kwargs) -> Pose:
        return self.position

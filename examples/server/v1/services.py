from typing import List
from viam.services.slam import Pose, SLAM
from tests.mocks.services import MockSLAM


class ExampleSLAM(SLAM):
    def __init__(self, name: str):
        self.position = MockSLAM.POSITION
        self.internal_chunks = MockSLAM.INTERNAL_STATE_CHUNKS
        self.point_cloud_chunks = MockSLAM.POINT_CLOUD_PCD_CHUNKS
        super().__init__(name)

    async def get_internal_state(self, **kwargs) -> List[bytes]:
        return self.internal_chunks

    async def get_point_cloud_map(self, **kwargs) -> List[bytes]:
        return self.point_cloud_chunks

    async def get_position(self, **kwargs) -> Pose:
        return self.position

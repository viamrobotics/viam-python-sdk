from typing import List
from viam.services.slam import Pose, SLAMService


class ExampleSLAMService(SLAMService):
    def __init__(self, name: str):
        self.position = Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)
        self.internal_chunks = [bytes(5), bytes(2)]
        self.point_cloud_chunks = [bytes(3), bytes(2)]
        super().__init__(name)

    async def get_internal_state(self, **kwargs) -> List[bytes]:
        return self.internal_chunks

    async def get_point_cloud_map(self, **kwargs) -> List[bytes]:
        return self.point_cloud_chunks

    async def get_position(self, **kwargs) -> Pose:
        return self.position

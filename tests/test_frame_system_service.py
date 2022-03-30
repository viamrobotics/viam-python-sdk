import pytest
from grpclib.testing import ChannelFor
from viam.proto.api.service.framesystem import Config
from viam.proto.api.common import Pose, PoseInFrame
from viam.services.frame_system import FrameSystemClient

from .mocks.services import MockFrameSystemService

CONFIG_RESPONSE = [
    Config(
        name='config0',
        pose_in_parent_frame=PoseInFrame(
            reference_frame='reference0',
            pose=Pose(
                x=1,
                y=2,
                z=3,
                o_x=2,
                o_y=3,
                o_z=4,
                theta=20
            )
        ),
        model_json=b'some fake json'
    ),
    Config(
        name='config1',
        pose_in_parent_frame=PoseInFrame(
            reference_frame='reference1',
            pose=Pose(
                x=2,
                y=3,
                z=4,
                o_x=3,
                o_y=4,
                o_z=5,
                theta=21
            )
        ),
        model_json=b'some fake json part 2'
    ),
]
TRANSFORM_RESPONSE = PoseInFrame(
    reference_frame='arm',
    pose=Pose(
        x=1,
        y=2,
        z=3,
        o_x=2,
        o_y=3,
        o_z=4,
        theta=20
    )
)


@pytest.fixture(scope='function')
def service() -> MockFrameSystemService:
    return MockFrameSystemService(
        config_response=CONFIG_RESPONSE,
        transform_response=TRANSFORM_RESPONSE
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_config(self, service: MockFrameSystemService):
        async with ChannelFor([service]) as channel:
            client = FrameSystemClient(channel)
            configs = await client.config()
            assert configs == CONFIG_RESPONSE

    @pytest.mark.asyncio
    async def test_transform_pose(self, service: MockFrameSystemService):
        async with ChannelFor([service]) as channel:
            client = FrameSystemClient(channel)
            pose = await client.transform_pose(PoseInFrame(), 'some dest')
            assert pose == TRANSFORM_RESPONSE

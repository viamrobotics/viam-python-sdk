from io import BytesIO
import pytest
from google.api.httpbody_pb2 import HttpBody
from grpclib.testing import ChannelFor
from PIL import Image
from viam.components.camera import Camera, CameraClient
from viam.components.camera.service import CameraService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.camera import (CameraServiceStub,
                                             GetFrameRequest, GetFrameResponse,
                                             GetPointCloudRequest,
                                             GetPointCloudResponse,
                                             RenderFrameRequest)
from viam.components.types import CameraMimeType

from .mocks.components import MockCamera


@pytest.fixture(scope='function')
def image() -> Image.Image:
    return Image.new('RGBA', (100, 100), '#AABBCCDD')


@pytest.fixture(scope='function')
def point_cloud() -> bytes:
    return b'THIS IS A POINT CLOUD'


@pytest.fixture(scope='function')
def camera() -> Camera:
    return MockCamera(name='camera')


@pytest.fixture(scope='function')
def service(camera: Camera) -> CameraService:
    rm = ResourceManager([camera])
    return CameraService(rm)


class TestCamera:

    @pytest.mark.asyncio
    async def test_get_frame(self, camera: Camera, image: Image.Image):
        img = await camera.get_frame()
        assert img == image

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: Camera, point_cloud: bytes):
        pc, _ = await camera.get_point_cloud()
        assert pc == point_cloud


class TestService:

    @pytest.mark.asyncio
    async def test_get_frame(
        self,
        service: CameraService,
        image: Image.Image
    ):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetFrameRequest(name='camera')
            response: GetFrameResponse = await client.GetFrame(request)
            img = Image.frombytes(
                'RGBA',
                (response.width_px, response.height_px),
                response.image,
                'raw'
            )
            assert img == image

    @pytest.mark.asyncio
    async def test_render_frame(
        self,
        service: CameraService,
        image: Image.Image
    ):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = RenderFrameRequest(
                name='camera', mime_type=CameraMimeType.PNG)
            response: HttpBody = await client.RenderFrame(request)
            assert response.content_type == CameraMimeType.PNG
            buf = BytesIO(response.data)
            img = Image.open(buf, formats=['JPEG', 'PNG'])
            assert img.tobytes() == image.tobytes()

    @pytest.mark.asyncio
    async def test_get_point_cloud(
        self,
        service: CameraService,
        point_cloud: bytes
    ):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(
                name='camera', mime_type=CameraMimeType.PCD)
            response: GetPointCloudResponse = \
                await client.GetPointCloud(request)
            assert response.point_cloud == point_cloud


class TestClient:

    @pytest.mark.asyncio
    async def test_get_frame(
        self,
        service: CameraService,
        image: Image.Image
    ):
        async with ChannelFor([service]) as channel:
            camera = CameraClient('camera', channel)
            img = await camera.get_frame()
            assert img == image

    @pytest.mark.asyncio
    async def test_get_point_cloud(
        self,
        service: CameraService,
        point_cloud: bytes
    ):
        async with ChannelFor([service]) as channel:
            camera = CameraClient('camera', channel)
            pc, _ = await camera.get_point_cloud()
            assert pc == point_cloud

from io import BytesIO
from grpclib import GRPCError
import pytest
from google.api.httpbody_pb2 import HttpBody
from grpclib.testing import ChannelFor
from PIL import Image
from viam.components.camera import Camera, CameraClient, CameraService
from viam.components.resource_manager import ResourceManager
from viam.proto.api.component.camera import (CameraServiceStub,
                                             GetFrameRequest, GetFrameResponse,
                                             GetPointCloudRequest,
                                             GetPointCloudResponse,
                                             RenderFrameRequest)
from viam.utils import CameraMimeType

from .mocks.components import MockCamera


@pytest.fixture(scope='function')
def camera() -> Camera:
    return MockCamera(name='camera')


@pytest.fixture()
def image() -> Image.Image:
    return Image.new('RGBA', (100, 100), '#AABBCCDD')


@pytest.fixture()
def service(camera: Camera) -> CameraService:
    rm = ResourceManager([camera])
    return CameraService(rm)


class TestCamera:

    @pytest.mark.asyncio
    async def test_next(self, camera: Camera, image: Image.Image):
        img = await camera.next()
        assert img == image

    @pytest.mark.asyncio
    async def test_next_point_cloud(self, camera: Camera):
        with pytest.raises(NotImplementedError):
            await camera.next_point_cloud()


class TestService:

    @pytest.mark.asyncio
    async def test_get_frame(
        self, service: CameraService,
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
                name='camera', mime_type=CameraMimeType.PNG.value)
            response: HttpBody = await client.RenderFrame(request)
            assert response.content_type == CameraMimeType.PNG.value
            buf = BytesIO(response.data)
            img = Image.open(buf, formats=['JPEG', 'PNG'])
            assert img.tobytes() == image.tobytes()

    @pytest.mark.asyncio
    async def test_get_point_cloud(
        self,
        service: CameraService,
    ):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(
                name='camera', mime_type=CameraMimeType.PCD.value)
            with pytest.raises(GRPCError):
                await client.GetPointCloud(request)


class TestClient:

    @pytest.mark.asyncio
    async def test_next(
        self,
        service: CameraService,
        image: Image.Image
    ):
        async with ChannelFor([service]) as channel:
            camera = CameraClient('camera', channel)
            img = await camera.next()
            assert img == image

    @pytest.mark.asyncio
    async def test_next_point_cloud(
        self,
        service: CameraService
    ):
        async with ChannelFor([service]) as channel:
            camera = CameraClient('camera', channel)
            with pytest.raises(GRPCError):
                await camera.next_point_cloud()

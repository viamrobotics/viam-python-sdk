from io import BytesIO

import pytest
from google.api.httpbody_pb2 import HttpBody
from grpclib.testing import ChannelFor
from PIL import Image
from viam.components.camera import Camera, CameraClient
from viam.components.camera.service import CameraService
from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.components.types import CameraMimeType, RawImage
from viam.proto.api.component.camera import (
    CameraServiceStub,
    GetFrameRequest,
    GetFrameResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    IntrinsicParameters,
    RenderFrameRequest,
)

from .mocks.components import MockCamera

# ################################ NB ################################# #
#   These test values have to be fixtures and must match the values in  #
#  MockCamera because there are some weird PIL errors if you pass these #
#   fixtures in the initializer to seed the mock with expected values   #
# ##################################################################### #


@pytest.fixture(scope="function")
def image() -> Image.Image:
    return Image.new("RGBA", (100, 100), "#AABBCCDD")


@pytest.fixture(scope="function")
def point_cloud() -> bytes:
    return b"THIS IS A POINT CLOUD"


@pytest.fixture(scope="function")
def properties() -> IntrinsicParameters:
    return IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6)


@pytest.fixture(scope="function")
def camera() -> Camera:
    return MockCamera("camera")


@pytest.fixture(scope="function")
def service(camera: Camera) -> CameraService:
    rm = ResourceManager([camera])
    return CameraService(rm)


@pytest.fixture(scope="function")
def generic_service(camera: Camera) -> GenericService:
    manager = ResourceManager([camera])
    return GenericService(manager)


class TestCamera:
    @pytest.mark.asyncio
    async def test_get_frame(self, camera: Camera, image: Image.Image):
        img = await camera.get_frame(CameraMimeType.PNG)
        assert img == image

        img = await camera.get_frame(CameraMimeType.RAW)
        assert isinstance(img, RawImage)

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: Camera, point_cloud: bytes):
        pc, _ = await camera.get_point_cloud()
        assert pc == point_cloud

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: Camera, properties: IntrinsicParameters):
        props = await camera.get_properties()
        assert props == properties

    @pytest.mark.asyncio
    async def test_do(self, camera: Camera):
        with pytest.raises(NotImplementedError):
            await camera.do({"command": "args"})


class TestService:
    @pytest.mark.asyncio
    async def test_get_frame(self, service: CameraService, image: Image.Image):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            # Test known mime type
            request = GetFrameRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: GetFrameResponse = await client.GetFrame(request)
            img = Image.open(BytesIO(response.image), formats=["PNG"])
            assert img.tobytes() == image.tobytes()

            # Test raw mime type
            request = GetFrameRequest(name="camera", mime_type=CameraMimeType.RAW)
            response: GetFrameResponse = await client.GetFrame(request)
            img = Image.frombytes("RGBA", (response.width_px, response.height_px), response.image, "raw")
            assert img == image
            assert response.mime_type == CameraMimeType.RAW

            # Test unknown mime type
            request = GetFrameRequest(name="camera", mime_type="unknown")
            response: GetFrameResponse = await client.GetFrame(request)
            img = Image.frombytes("RGBA", (response.width_px, response.height_px), response.image, "raw")
            assert img == image
            assert response.mime_type == "unknown"

    @pytest.mark.asyncio
    async def test_render_frame(self, service: CameraService, image: Image.Image):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = RenderFrameRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: HttpBody = await client.RenderFrame(request)
            assert response.content_type == CameraMimeType.PNG
            buf = BytesIO(response.data)
            img = Image.open(buf, formats=["JPEG", "PNG"])
            assert img.tobytes() == image.tobytes()

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, service: CameraService, point_cloud: bytes):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(name="camera", mime_type=CameraMimeType.PCD)
            response: GetPointCloudResponse = await client.GetPointCloud(request)
            assert response.point_cloud == point_cloud

    @pytest.mark.asyncio
    async def test_get_properties(self, service: CameraService, properties: IntrinsicParameters):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPropertiesRequest(name="camera")
            response: GetPropertiesResponse = await client.GetProperties(request)
            assert response.intrinsic_parameters == properties


class TestClient:
    @pytest.mark.asyncio
    async def test_get_frame(self, service: CameraService, image: Image.Image):
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            # Test known mime type
            img = await client.get_frame()
            assert isinstance(img, Image.Image)
            assert img.convert("RGBA") == image.convert("RGBA")
            assert img.tobytes() == image.tobytes()

            # Test raw mime type
            img = await client.get_frame(CameraMimeType.RAW)
            assert isinstance(img, RawImage)
            assert img.data == image.tobytes()
            assert img.width == image.width
            assert img.height == image.height
            assert img.mime_type == CameraMimeType.RAW

            # Test unknown mime type
            img = await client.get_frame("unknown")
            assert isinstance(img, RawImage)
            assert img.data == image.tobytes()
            assert img.width == image.width
            assert img.height == image.height
            assert img.mime_type == "unknown"

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, service: CameraService, point_cloud: bytes):
        async with ChannelFor([service]) as channel:
            camera = CameraClient("camera", channel)
            pc, _ = await camera.get_point_cloud()
            assert pc == point_cloud

    @pytest.mark.asyncio
    async def test_get_properties(self, service: CameraService, properties: IntrinsicParameters):
        async with ChannelFor([service]) as channel:
            camera = CameraClient("camera", channel)
            props = await camera.get_properties()
            assert props == properties

    @pytest.mark.asyncio
    async def test_do(self, service: CameraService, generic_service: GenericService):
        async with ChannelFor([service, generic_service]) as channel:
            client = CameraClient("camera", channel)
            with pytest.raises(NotImplementedError):
                await client.do({"command": "args"})

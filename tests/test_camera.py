from io import BytesIO

import pytest
from google.api.httpbody_pb2 import HttpBody
from grpclib.testing import ChannelFor

from PIL import Image

from viam.components.camera import Camera, CameraClient
from viam.components.camera.service import CameraService
from viam.components.generic.service import GenericService
from viam.components.resource_manager import ResourceManager
from viam.media.video import CameraMimeType, RawImage, LIBRARY_SUPPORTED_FORMATS
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.camera import (
    CameraServiceStub,
    DistortionParameters,
    GetImageRequest,
    GetImageResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    IntrinsicParameters,
    RenderFrameRequest,
)
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
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
def properties() -> Camera.Properties:
    return Camera.Properties(
        True,
        IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
        DistortionParameters(model="no_distortion"),
    )


@pytest.fixture(scope="function")
def camera() -> MockCamera:
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
        img = await camera.get_image(CameraMimeType.PNG)
        assert img == image

        img = await camera.get_image(CameraMimeType.VIAM_RGBA)
        assert isinstance(img, Image.Image)

        img = await camera.get_image(CameraMimeType.PNG.with_lazy_suffix)
        assert isinstance(img, RawImage)

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: Camera, point_cloud: bytes):
        pc, _ = await camera.get_point_cloud()
        assert pc == point_cloud

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: Camera, properties: Camera.Properties):
        props = await camera.get_properties()
        assert props == properties

    @pytest.mark.asyncio
    async def test_do(self, camera: Camera):
        resp = await camera.do_command({"command": "args"})
        assert resp == {"hello": "world"}

    @pytest.mark.asyncio
    async def test_timeout(self, camera: MockCamera):
        assert camera.timeout is None

        await camera.get_image(timeout=1.82)
        assert camera.timeout == loose_approx(1.82)

        await camera.get_point_cloud(timeout=4.4)
        assert camera.timeout == loose_approx(4.4)

        await camera.get_properties(timeout=7.86)
        assert camera.timeout == loose_approx(7.86)


class TestService:
    @pytest.mark.asyncio
    async def test_get_frame(self, camera: MockCamera, service: CameraService, image: Image.Image):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            # Test known mime type
            request = GetImageRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: GetImageResponse = await client.GetImage(request, timeout=18.2)
            img = Image.open(BytesIO(response.image), formats=["PNG"])
            assert img.tobytes() == image.tobytes()
            assert camera.timeout == loose_approx(18.2)

            # Test raw mime type
            request = GetImageRequest(name="camera", mime_type=CameraMimeType.VIAM_RGBA)
            response: GetImageResponse = await client.GetImage(request)
            img = Image.open(BytesIO(response.image), formats=["VIAM_RGBA"])
            assert img.tobytes() == image.tobytes()
            assert response.mime_type == CameraMimeType.VIAM_RGBA

            # Test unknown mime type
            request = GetImageRequest(name="camera", mime_type="unknown")
            response: GetImageResponse = await client.GetImage(request)
            img = Image.frombytes("RGBA", (100, 100), response.image, "raw")
            assert img == image
            assert response.mime_type == "unknown"

    @pytest.mark.asyncio
    async def test_render_frame(self, camera: MockCamera, service: CameraService, image: Image.Image):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = RenderFrameRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: HttpBody = await client.RenderFrame(request, timeout=4.4)
            assert response.content_type == CameraMimeType.PNG
            buf = BytesIO(response.data)
            img = Image.open(buf, formats=LIBRARY_SUPPORTED_FORMATS)
            assert img.tobytes() == image.tobytes()
            assert camera.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: MockCamera, service: CameraService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(name="camera", mime_type=CameraMimeType.PCD)
            response: GetPointCloudResponse = await client.GetPointCloud(request, timeout=7.86)
            assert response.point_cloud == point_cloud
            assert camera.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: MockCamera, service: CameraService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPropertiesRequest(name="camera")
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=5.43)
            assert response.supports_pcd == properties.supports_pcd
            assert response.intrinsic_parameters == properties.intrinsic_parameters
            assert camera.timeout == loose_approx(5.43)


class TestClient:
    @pytest.mark.asyncio
    async def test_get_frame(self, camera: MockCamera, service: CameraService, image: Image.Image):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            # Test known mime type
            png_img = await client.get_image(timeout=1.82, mime_type=CameraMimeType.PNG)
            assert isinstance(png_img, Image.Image)
            assert png_img.tobytes() == image.tobytes()
            assert camera.timeout == loose_approx(1.82)

            # Test raw mime type
            rgba_img = await client.get_image(CameraMimeType.VIAM_RGBA)
            assert isinstance(rgba_img, Image.Image)
            rgba_bytes = rgba_img.tobytes()
            assert rgba_bytes == image.copy().convert("RGBA").tobytes()

            # Test lazy mime type
            raw_img = await client.get_image(CameraMimeType.PNG.with_lazy_suffix)
            assert isinstance(raw_img, RawImage)
            assert raw_img.data == image.tobytes()
            assert raw_img.mime_type == CameraMimeType.PNG

            # Test unknown mime type
            raw_img = await client.get_image("unknown")
            assert isinstance(raw_img, RawImage)
            assert raw_img.data == image.tobytes()
            assert raw_img.mime_type == "unknown"

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: MockCamera, service: CameraService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            pc, _ = await client.get_point_cloud(timeout=4.4)
            assert pc == point_cloud
            assert camera.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: MockCamera, service: CameraService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            props = await client.get_properties(timeout=7.86)
            assert props == properties
            assert camera.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_do(self, service: CameraService):
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            resp = await client.do_command({"command": "args"})
            assert resp == {"hello": "world"}

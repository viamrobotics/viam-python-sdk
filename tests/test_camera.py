from datetime import datetime

import pytest
from google.api.httpbody_pb2 import HttpBody
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor
from PIL import Image

from viam.components.camera import Camera, CameraClient
from viam.components.camera.service import CameraRPCService
from viam.components.generic.service import GenericRPCService
from viam.media.video import CameraMimeType, NamedImage, ViamImage
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse, ResponseMetadata
from viam.proto.component.camera import (
    CameraServiceStub,
    DistortionParameters,
    Format,
    GetImageRequest,
    GetImageResponse,
    GetImagesRequest,
    GetImagesResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    IntrinsicParameters,
    RenderFrameRequest,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import GEOMETRIES, MockCamera

# ################################ NB ################################# #
#   These test values have to be fixtures and must match the values in  #
#  MockCamera because there are some weird PIL errors if you pass these #
#   fixtures in the initializer to seed the mock with expected values   #
# ##################################################################### #


@pytest.fixture(scope="function")
def image() -> Image.Image:
    return Image.new("RGBA", (100, 100), "#AABBCCDD")


@pytest.fixture(scope="function")
def metadata() -> ResponseMetadata:
    ts = Timestamp()
    ts.FromDatetime(datetime(1970, 1, 1))
    return ResponseMetadata(captured_at=ts)


@pytest.fixture(scope="function")
def point_cloud() -> bytes:
    return b"THIS IS A POINT CLOUD"


@pytest.fixture(scope="function")
def properties() -> Camera.Properties:
    return Camera.Properties(
        supports_pcd=False,
        intrinsic_parameters=IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
        distortion_parameters=DistortionParameters(model="no_distortion"),
    )


@pytest.fixture(scope="function")
def camera() -> MockCamera:
    return MockCamera("camera")


@pytest.fixture(scope="function")
def service(camera: Camera) -> CameraRPCService:
    rm = ResourceManager([camera])
    return CameraRPCService(rm)


@pytest.fixture(scope="function")
def generic_service(camera: Camera) -> GenericRPCService:
    manager = ResourceManager([camera])
    return GenericRPCService(manager)


class TestCamera:
    @pytest.mark.asyncio
    async def test_get_image(self, camera: MockCamera, image: Image.Image):
        img = await camera.get_image(CameraMimeType.PNG)
        assert img.data == CameraMimeType.PNG.encode_image(image)
        assert img.mime_type == CameraMimeType.PNG

        img = await camera.get_image(CameraMimeType.PNG, {"1": 1})
        assert camera.extra == {"1": 1}

        img = await camera.get_image(CameraMimeType.VIAM_RGBA)
        assert img.data == CameraMimeType.VIAM_RGBA.encode_image(image)
        assert img.mime_type == CameraMimeType.VIAM_RGBA

    @pytest.mark.asyncio
    async def test_get_images(self, camera: Camera, image: Image.Image, metadata: ResponseMetadata):
        imgs, md = await camera.get_images()
        assert isinstance(imgs[0], NamedImage)
        assert imgs[0].name == camera.name
        assert imgs[0].data == CameraMimeType.VIAM_RGBA.encode_image(image)
        assert md == metadata

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: MockCamera, point_cloud: bytes):
        pc, _ = await camera.get_point_cloud()
        assert pc == point_cloud

        await camera.get_point_cloud(extra={"1": 1})
        assert camera.extra == {"1": 1}

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: Camera, properties: Camera.Properties):
        props = await camera.get_properties()
        assert props == properties

    @pytest.mark.asyncio
    async def test_do(self, camera: Camera):
        command = {"command": "args"}
        resp = await camera.do_command(command)
        assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_timeout(self, camera: MockCamera):
        assert camera.timeout is None

        await camera.get_image(timeout=1.82)
        assert camera.timeout == loose_approx(1.82)

        await camera.get_point_cloud(timeout=4.4)
        assert camera.timeout == loose_approx(4.4)

        await camera.get_properties(timeout=7.86)
        assert camera.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_get_geometries(self, camera: MockCamera):
        geometries = await camera.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    @pytest.mark.asyncio
    async def test_get_image(self, camera: MockCamera, service: CameraRPCService, image: Image.Image):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            # Test known mime type
            request = GetImageRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: GetImageResponse = await client.GetImage(request, timeout=18.2)
            assert response.image == CameraMimeType.PNG.encode_image(image)
            assert camera.timeout == loose_approx(18.2)

            # Test raw mime type
            request = GetImageRequest(name="camera", mime_type=CameraMimeType.VIAM_RGBA)
            response: GetImageResponse = await client.GetImage(request)
            assert response.image == CameraMimeType.VIAM_RGBA.encode_image(image)
            assert response.mime_type == CameraMimeType.VIAM_RGBA

            # Test unknown mime type
            request = GetImageRequest(name="camera", mime_type="unknown")
            response: GetImageResponse = await client.GetImage(request)
            assert response.image == image.convert("RGBA").tobytes("raw", "RGBA")
            assert response.mime_type == "unknown"

            # Test empty mime type. Empty mime type should default to JPEG for non-depth cameras
            request = GetImageRequest(name="camera")
            response: GetImageResponse = await client.GetImage(request)
            assert service._camera_mime_types["camera"] == CameraMimeType.JPEG

    @pytest.mark.asyncio
    async def test_get_images(self, camera: MockCamera, service: CameraRPCService, metadata: ResponseMetadata):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            request = GetImagesRequest(name="camera")
            response: GetImagesResponse = await client.GetImages(request, timeout=18.2)
            raw_img = response.images[0]
            assert raw_img.format == Format.FORMAT_RAW_RGBA
            assert raw_img.source_name == camera.name
            assert response.response_metadata == metadata
            assert camera.timeout == loose_approx(18.2)

    @pytest.mark.asyncio
    async def test_render_frame(self, camera: MockCamera, service: CameraRPCService, image: Image.Image):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = RenderFrameRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: HttpBody = await client.RenderFrame(request, timeout=4.4)
            assert response.content_type == CameraMimeType.PNG
            assert response.data == CameraMimeType.PNG.encode_image(image)
            assert camera.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: MockCamera, service: CameraRPCService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(name="camera", mime_type=CameraMimeType.PCD)
            response: GetPointCloudResponse = await client.GetPointCloud(request, timeout=7.86)
            assert response.point_cloud == point_cloud
            assert camera.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: MockCamera, service: CameraRPCService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPropertiesRequest(name="camera")
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=5.43)
            assert response.supports_pcd == properties.supports_pcd
            assert response.intrinsic_parameters == properties.intrinsic_parameters
            assert camera.timeout == loose_approx(5.43)

    @pytest.mark.asyncio
    async def test_do(self, camera: MockCamera, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=camera.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self, camera: MockCamera, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetGeometriesRequest(name=camera.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    @pytest.mark.asyncio
    async def test_get_image(self, camera: MockCamera, service: CameraRPCService, image: Image.Image):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            # Test known mime type
            png_img = await client.get_image(timeout=1.82, mime_type=CameraMimeType.PNG)
            assert png_img.data == CameraMimeType.PNG.encode_image(image)
            assert isinstance(png_img.image, Image.Image)
            assert png_img.image.tobytes() == image.tobytes()
            assert camera.timeout == loose_approx(1.82)

            # Test raw mime type
            rgba_img = await client.get_image(CameraMimeType.VIAM_RGBA)
            assert isinstance(rgba_img.image, Image.Image)
            rgba_bytes = rgba_img.image.tobytes()
            assert rgba_bytes == image.copy().convert("RGBA").tobytes()

            # Test lazy mime type
            raw_img = await client.get_image(CameraMimeType.PNG.with_lazy_suffix)
            assert isinstance(raw_img, ViamImage)
            assert raw_img.image is None
            assert raw_img.data == image.tobytes()
            assert raw_img.mime_type == CameraMimeType.PNG

            # Test unknown mime type
            raw_img = await client.get_image("unknown")
            assert isinstance(raw_img, ViamImage)
            assert raw_img.image is None
            assert raw_img.mime_type == CameraMimeType.UNSUPPORTED

    @pytest.mark.asyncio
    async def test_get_images(self, camera: MockCamera, service: CameraRPCService, image: Image.Image, metadata: ResponseMetadata):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            imgs, md = await client.get_images(timeout=1.82)
            assert isinstance(imgs[0], NamedImage)
            assert imgs[0].name == camera.name
            assert imgs[0].image is not None
            assert imgs[0].image.tobytes() == image.tobytes()
            assert md == metadata
            assert camera.timeout == loose_approx(1.82)

    @pytest.mark.asyncio
    async def test_get_point_cloud(self, camera: MockCamera, service: CameraRPCService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            pc, _ = await client.get_point_cloud(timeout=4.4)
            assert pc == point_cloud
            assert camera.timeout == loose_approx(4.4)

    @pytest.mark.asyncio
    async def test_get_properties(self, camera: MockCamera, service: CameraRPCService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            props = await client.get_properties(timeout=7.86)
            assert props == properties
            assert camera.timeout == loose_approx(7.86)

    @pytest.mark.asyncio
    async def test_do(self, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    @pytest.mark.asyncio
    async def test_get_geometries(self, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES

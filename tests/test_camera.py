from datetime import datetime

import pytest
from google.api.httpbody_pb2 import HttpBody
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

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
    Image
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
def image() -> ViamImage:
    return ViamImage(b"data", CameraMimeType.PNG)


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
        mime_types=[CameraMimeType.PNG, CameraMimeType.JPEG],
        frame_rate=10.0,
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
    async def test_get_image(self, camera: MockCamera, image: ViamImage):
        img = await camera.get_image(CameraMimeType.PNG)
        assert img.data == image.data
        assert img.mime_type == image.mime_type

        img = await camera.get_image(CameraMimeType.PNG, {"1": 1})
        assert camera.extra == {"1": 1}

    async def test_get_images(self, camera: Camera, image: ViamImage, metadata: ResponseMetadata):
        imgs, md = await camera.get_images(filter_source_names=["cam1", "cam2"])
        assert isinstance(imgs[0], NamedImage)
        assert imgs[0].name == camera.name
        assert imgs[0].data == image.data
        assert md == metadata
        assert camera.filter_source_names == ["cam1", "cam2"]

    async def test_get_point_cloud(self, camera: MockCamera, point_cloud: bytes):
        pc, _ = await camera.get_point_cloud()
        assert pc == point_cloud

        await camera.get_point_cloud(extra={"1": 1})
        assert camera.extra == {"1": 1}

    async def test_get_properties(self, camera: Camera, properties: Camera.Properties):
        props = await camera.get_properties()
        assert props == properties

    async def test_do(self, camera: Camera):
        command = {"command": "args"}
        resp = await camera.do_command(command)
        assert resp == {"command": command}

    async def test_timeout(self, camera: MockCamera):
        assert camera.timeout is None

        await camera.get_image(timeout=1.82)
        assert camera.timeout == loose_approx(1.82)

        await camera.get_point_cloud(timeout=4.4)
        assert camera.timeout == loose_approx(4.4)

        await camera.get_properties(timeout=7.86)
        assert camera.timeout == loose_approx(7.86)

    async def test_get_geometries(self, camera: MockCamera):
        geometries = await camera.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    async def test_get_image(self, camera: MockCamera, service: CameraRPCService, image: ViamImage):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            # Test known mime type
            request = GetImageRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: GetImageResponse = await client.GetImage(request, timeout=18.1)
            assert response.image == image.data
            assert camera.timeout == loose_approx(18.1)

            # Test empty mime type. Empty mime type should default to response mime type
            request = GetImageRequest(name="camera")
            response: GetImageResponse = await client.GetImage(request)
            assert response.image == image.data
            assert response.mime_type == image.mime_type

    async def test_get_images(self, camera: MockCamera, service: CameraRPCService, metadata: ResponseMetadata):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            request = GetImagesRequest(name="camera", filter_source_names=["cam1", "cam2"])
            response: GetImagesResponse = await client.GetImages(request, timeout=18.1)
            raw_img = response.images[0]
            assert raw_img.format == Format.FORMAT_PNG
            assert raw_img.source_name == camera.name
            assert raw_img.mime_type == CameraMimeType.PNG
            assert response.response_metadata == metadata
            assert camera.timeout == loose_approx(18.1)
            assert camera.filter_source_names == ["cam1", "cam2"]

    async def test_render_frame(self, camera: MockCamera, service: CameraRPCService, image: ViamImage):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = RenderFrameRequest(name="camera", mime_type=CameraMimeType.PNG)
            response: HttpBody = await client.RenderFrame(request, timeout=4.4)
            assert response.content_type == CameraMimeType.PNG
            assert response.data == image.data
            assert camera.timeout == loose_approx(4.4)

    async def test_get_point_cloud(self, camera: MockCamera, service: CameraRPCService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(name="camera", mime_type=CameraMimeType.PCD)
            response: GetPointCloudResponse = await client.GetPointCloud(request, timeout=7.86)
            assert response.point_cloud == point_cloud
            assert camera.timeout == loose_approx(7.86)

    async def test_get_properties(self, camera: MockCamera, service: CameraRPCService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPropertiesRequest(name="camera")
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=5.43)
            assert response.supports_pcd == properties.supports_pcd
            assert response.intrinsic_parameters == properties.intrinsic_parameters
            assert response.mime_types == properties.mime_types
            assert response.frame_rate == properties.frame_rate
            assert camera.timeout == loose_approx(5.43)

    async def test_do(self, camera: MockCamera, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=camera.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}

    async def test_get_geometries(self, camera: MockCamera, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetGeometriesRequest(name=camera.name)
            response: GetGeometriesResponse = await client.GetGeometries(request)
            assert [geometry for geometry in response.geometries] == GEOMETRIES


class TestClient:
    async def test_get_image(self, camera: MockCamera, service: CameraRPCService, image: ViamImage):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            img = await client.get_image(timeout=1.82, mime_type=CameraMimeType.PNG)
            assert img.data == image.data
            assert img.mime_type == image.mime_type

    async def test_get_images(self, camera: MockCamera, service: CameraRPCService, image: ViamImage, metadata: ResponseMetadata):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            imgs, md = await client.get_images(timeout=1.82, filter_source_names=["cam1", "cam2"])
            assert isinstance(imgs[0], NamedImage)
            assert imgs[0].name == camera.name
            assert imgs[0].data == image.data
            assert md == metadata
            assert camera.timeout == loose_approx(1.82)
            assert camera.filter_source_names == ["cam1", "cam2"]

    async def test_get_point_cloud(self, camera: MockCamera, service: CameraRPCService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            pc, _ = await client.get_point_cloud(timeout=4.4)
            assert pc == point_cloud
            assert camera.timeout == loose_approx(4.4)

    async def test_get_properties(self, camera: MockCamera, service: CameraRPCService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            props = await client.get_properties(timeout=7.86)
            assert props == properties
            assert camera.timeout == loose_approx(7.86)

    async def test_do(self, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

    async def test_get_geometries(self, service: CameraRPCService):
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            geometries = await client.get_geometries()
            assert geometries == GEOMETRIES

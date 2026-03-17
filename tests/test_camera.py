from datetime import datetime
from typing import Optional

import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.components.camera import Camera, CameraClient
from viam.components.camera.service import CameraRPCService
from viam.components.generic.service import GenericRPCService
from viam.media.video import CameraMimeType, NamedImage, ViamImage
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GetGeometriesRequest,
    GetGeometriesResponse,
    Orientation,
    ResponseMetadata,
    Vector3,
)
from viam.proto.component.camera import (
    CameraServiceStub,
    DistortionParameters,
    ExtrinsicParameters,
    GetImagesRequest,
    GetImagesResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    IntrinsicParameters,
)
from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import expected_grpc_timeout
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
def properties_with_extrinsic() -> Camera.Properties:
    return Camera.Properties(
        supports_pcd=False,
        intrinsic_parameters=IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
        distortion_parameters=DistortionParameters(model="no_distortion"),
        mime_types=[CameraMimeType.PNG, CameraMimeType.JPEG],
        frame_rate=10.0,
        extrinsic_parameters=ExtrinsicParameters(
            translation=Vector3(x=1.0, y=2.0, z=3.0), orientation=Orientation(o_x=0.0, o_y=0.0, o_z=0.0, theta=0.0)
        ),
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
    async def test_get_images(self, camera: Camera, image: ViamImage, metadata: ResponseMetadata):
        imgs, md = await camera.get_images()
        assert isinstance(imgs[0], NamedImage)
        assert imgs[0].name == camera.name
        assert imgs[0].data == image.data
        assert md == metadata

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

        await camera.get_point_cloud(timeout=4.4)
        assert camera.timeout == expected_grpc_timeout(4.4)

        await camera.get_properties(timeout=7.86)
        assert camera.timeout == expected_grpc_timeout(7.86)

    async def test_get_geometries(self, camera: MockCamera):
        geometries = await camera.get_geometries()
        assert geometries == GEOMETRIES


class TestService:
    async def test_get_images(self, camera: MockCamera, service: CameraRPCService, metadata: ResponseMetadata):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)

            request = GetImagesRequest(name="camera")
            response: GetImagesResponse = await client.GetImages(request, timeout=18.1)
            raw_img = response.images[0]
            assert raw_img.mime_type == CameraMimeType.PNG
            assert raw_img.source_name == camera.name
            assert response.response_metadata == metadata
            assert camera.timeout == expected_grpc_timeout(18.1)

    async def test_get_images_uses_source_name_not_resource_name(self):
        class MockCameraWithCustomSource(MockCamera):
            def __init__(self, name: str, source_name: str):
                super().__init__(name)
                self._source_name = source_name

            async def get_images(self, timeout: Optional[float] = None, **kwargs):
                self.timeout = timeout
                return [NamedImage(self._source_name, self.image.data, self.image.mime_type)], self.metadata

        custom_camera = MockCameraWithCustomSource("camera", "the_source")
        rm = ResourceManager([custom_camera])
        service = CameraRPCService(rm)

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetImagesRequest(name="camera")
            response: GetImagesResponse = await client.GetImages(request)
            assert response.images[0].source_name == "the_source"

    async def test_get_point_cloud(self, camera: MockCamera, service: CameraRPCService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(name="camera", mime_type=CameraMimeType.PCD)
            response: GetPointCloudResponse = await client.GetPointCloud(request, timeout=7.86)
            assert response.point_cloud == point_cloud
            assert camera.timeout == expected_grpc_timeout(7.86)

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
            assert camera.timeout == expected_grpc_timeout(5.43)

    async def test_get_properties_with_extrinsic(self, properties_with_extrinsic: Camera.Properties):
        class MockCameraWithExtrinsic(MockCamera):
            def __init__(self, name: str):
                super().__init__(name)
                self.props = properties_with_extrinsic

            async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Camera.Properties:
                self.timeout = timeout
                return self.props

        camera = MockCameraWithExtrinsic("camera")
        rm = ResourceManager([camera])
        service = CameraRPCService(rm)

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPropertiesRequest(name="camera")
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=5.43)
            assert response.supports_pcd == properties_with_extrinsic.supports_pcd
            assert response.intrinsic_parameters == properties_with_extrinsic.intrinsic_parameters
            assert response.mime_types == properties_with_extrinsic.mime_types
            assert response.frame_rate == properties_with_extrinsic.frame_rate
            assert response.extrinsic_parameters == properties_with_extrinsic.extrinsic_parameters
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
    async def test_get_images(self, camera: MockCamera, service: CameraRPCService, image: ViamImage, metadata: ResponseMetadata):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)

            imgs, md = await client.get_images(timeout=1.82)
            assert isinstance(imgs[0], NamedImage)
            assert imgs[0].name == camera.name
            assert imgs[0].data == image.data
            assert md == metadata
            assert camera.timeout == expected_grpc_timeout(1.82)

    async def test_get_point_cloud(self, camera: MockCamera, service: CameraRPCService, point_cloud: bytes):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            pc, _ = await client.get_point_cloud(timeout=4.4)
            assert pc == point_cloud
            assert camera.timeout == expected_grpc_timeout(4.4)

    async def test_get_properties(self, camera: MockCamera, service: CameraRPCService, properties: Camera.Properties):
        assert camera.timeout is None
        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            props = await client.get_properties(timeout=7.86)
            assert props == properties
            assert camera.timeout == expected_grpc_timeout(7.86)

    async def test_get_properties_with_extrinsic(self, properties_with_extrinsic: Camera.Properties):
        class MockCameraWithExtrinsic(MockCamera):
            def __init__(self, name: str):
                super().__init__(name)
                self.props = properties_with_extrinsic

            async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Camera.Properties:
                self.timeout = timeout
                return self.props

        camera = MockCameraWithExtrinsic("camera")
        rm = ResourceManager([camera])
        service = CameraRPCService(rm)

        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            props = await client.get_properties(timeout=7.86)
            assert props == properties_with_extrinsic
            assert props.extrinsic_parameters.translation.x == 1.0
            assert props.extrinsic_parameters.translation.y == 2.0
            assert props.extrinsic_parameters.translation.z == 3.0
            assert props.extrinsic_parameters.orientation.o_x == 0.0
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

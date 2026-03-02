from datetime import datetime
from typing import cast
from unittest.mock import AsyncMock

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
from viam.resource.rpc_client_base import ResourceRPCClientBase
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks import create_mock_subclass
from .mocks.components import GEOMETRIES


@pytest.fixture(scope="function")
def camera() -> Camera:
    mc = create_mock_subclass(Camera)
    return mc(name="camera")


@pytest.fixture(scope="function")
def service(camera: Camera) -> CameraRPCService:
    manager = ResourceManager([camera])
    return CameraRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(camera: Camera) -> GenericRPCService:
    manager = ResourceManager([camera])
    return GenericRPCService(manager)


DEFAULT_EXTRA = {"a": "b"}
DEFAULT_EXTRA_STRUCT = dict_to_struct(DEFAULT_EXTRA)
DEFAULT_TIMEOUT = 1.82
DEFAULT_TIMEOUT_APPROX = loose_approx(DEFAULT_TIMEOUT)
DEFAULT_METADATA = ResourceRPCClientBase.Metadata()
DEFAULT_METADATA.enable_debug_logging


class TestService:
    async def test_get_images(self, camera: Camera, service: CameraRPCService):
        ts = Timestamp()
        ts.FromDatetime(datetime.now())
        metadata = ResponseMetadata(captured_at=ts)
        image = ViamImage(b"data", CameraMimeType.PNG)

        cast(AsyncMock, camera.get_images).return_value = (
            [NamedImage(camera.name, image.data, image.mime_type)],
            metadata,
        )

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetImagesRequest(name="camera", extra=DEFAULT_EXTRA_STRUCT)
            response: GetImagesResponse = await client.GetImages(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            raw_img = response.images[0]
            assert raw_img.mime_type == CameraMimeType.PNG
            assert raw_img.source_name == camera.name
            assert response.response_metadata == metadata
            cast(AsyncMock, camera.get_images).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata, filter_source_names=[]
            )

    async def test_get_point_cloud(self, camera: Camera, service: CameraRPCService):
        point_cloud = b"THIS IS A POINT CLOUD"
        cast(AsyncMock, camera.get_point_cloud).return_value = (point_cloud, CameraMimeType.PCD)

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPointCloudRequest(name="camera", mime_type=CameraMimeType.PCD, extra=DEFAULT_EXTRA_STRUCT)
            response: GetPointCloudResponse = await client.GetPointCloud(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            assert response.point_cloud == point_cloud
            cast(AsyncMock, camera.get_point_cloud).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_properties(self, camera: Camera, service: CameraRPCService):
        properties = Camera.Properties(
            supports_pcd=False,
            intrinsic_parameters=IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
            distortion_parameters=DistortionParameters(model="no_distortion"),
            mime_types=[CameraMimeType.PNG, CameraMimeType.JPEG],
            frame_rate=10.0,
            extrinsic_parameters=ExtrinsicParameters(
                translation=Vector3(x=1.0, y=2.0, z=3.0), orientation=Orientation(o_x=0.0, o_y=0.0, o_z=0.0, theta=0.0)
            ),
        )
        cast(AsyncMock, camera.get_properties).return_value = properties

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetPropertiesRequest(name="camera")
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            assert response.supports_pcd == properties.supports_pcd
            assert response.intrinsic_parameters == properties.intrinsic_parameters
            assert response.mime_types == properties.mime_types
            assert response.frame_rate == properties.frame_rate
            assert response.extrinsic_parameters == properties.extrinsic_parameters
            cast(AsyncMock, camera.get_properties).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_do(self, camera: Camera, service: CameraRPCService):
        command = {"command": "args"}
        cast(AsyncMock, camera.do_command).return_value = {"command": command}

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = DoCommandRequest(name=camera.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            result = struct_to_dict(response.result)
            assert result == {"command": command}
            cast(AsyncMock, camera.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_geometries(self, camera: Camera, service: CameraRPCService):
        cast(AsyncMock, camera.get_geometries).return_value = GEOMETRIES

        async with ChannelFor([service]) as channel:
            client = CameraServiceStub(channel)
            request = GetGeometriesRequest(name=camera.name, extra=DEFAULT_EXTRA_STRUCT)
            response: GetGeometriesResponse = await client.GetGeometries(request, timeout=DEFAULT_TIMEOUT)
            assert [geometry for geometry in response.geometries] == GEOMETRIES
            cast(AsyncMock, camera.get_geometries).assert_called_once_with(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX)


class TestClient:
    async def test_get_images(self, camera: Camera, service: CameraRPCService):
        ts = Timestamp()
        ts.FromDatetime(datetime.now())
        metadata = ResponseMetadata(captured_at=ts)
        image = ViamImage(b"data", CameraMimeType.PNG)

        cast(AsyncMock, camera.get_images).return_value = (
            [NamedImage(camera.name, image.data, image.mime_type)],
            metadata,
        )

        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            imgs, md = await client.get_images(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            assert isinstance(imgs[0], NamedImage)
            assert imgs[0].name == camera.name
            assert imgs[0].data == image.data
            assert md == metadata
            cast(AsyncMock, camera.get_images).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata, filter_source_names=[]
            )

    async def test_get_point_cloud(self, camera: Camera, service: CameraRPCService):
        point_cloud = b"THIS IS A POINT CLOUD"
        cast(AsyncMock, camera.get_point_cloud).return_value = (point_cloud, CameraMimeType.PCD)

        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            pc, mime = await client.get_point_cloud(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            assert pc == point_cloud
            assert mime == CameraMimeType.PCD
            cast(AsyncMock, camera.get_point_cloud).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_properties(self, camera: Camera, service: CameraRPCService):
        properties = Camera.Properties(
            supports_pcd=False,
            intrinsic_parameters=IntrinsicParameters(width_px=1, height_px=2, focal_x_px=3, focal_y_px=4, center_x_px=5, center_y_px=6),
            distortion_parameters=DistortionParameters(model="no_distortion"),
            mime_types=[CameraMimeType.PNG, CameraMimeType.JPEG],
            frame_rate=10.0,
            extrinsic_parameters=ExtrinsicParameters(
                translation=Vector3(x=1.0, y=2.0, z=3.0), orientation=Orientation(o_x=0.0, o_y=0.0, o_z=0.0, theta=0.0)
            ),
        )
        cast(AsyncMock, camera.get_properties).return_value = properties

        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            props = await client.get_properties(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            assert props == properties
            cast(AsyncMock, camera.get_properties).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_do(self, camera: Camera, service: CameraRPCService):
        command = {"command": "args"}
        cast(AsyncMock, camera.do_command).return_value = {"command": command}

        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            resp = await client.do_command(command, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            assert resp == {"command": command}
            cast(AsyncMock, camera.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_geometries(self, camera: Camera, service: CameraRPCService):
        cast(AsyncMock, camera.get_geometries).return_value = GEOMETRIES

        async with ChannelFor([service]) as channel:
            client = CameraClient("camera", channel)
            geometries = await client.get_geometries(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            assert geometries == GEOMETRIES
            cast(AsyncMock, camera.get_geometries).assert_called_once_with(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX)

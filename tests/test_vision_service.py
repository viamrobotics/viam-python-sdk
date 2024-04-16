from random import random

import pytest
from grpclib.testing import ChannelFor
from PIL import Image

from viam.media.pil import pil_to_viam_image
from viam.media.video import CameraMimeType
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeometriesInFrame,
    Geometry,
    PointCloudObject,
    Pose,
    RectangularPrism,
    Vector3,
)
from viam.proto.service.vision import (
    GetClassificationsFromCameraRequest,
    GetClassificationsFromCameraResponse,
    GetClassificationsRequest,
    GetClassificationsResponse,
    GetDetectionsFromCameraRequest,
    GetDetectionsFromCameraResponse,
    GetDetectionsRequest,
    GetDetectionsResponse,
    GetObjectPointCloudsRequest,
    GetObjectPointCloudsResponse,
    VisionServiceStub,
)
from viam.resource.manager import ResourceManager
from viam.services.vision import Classification, Detection, VisionClient
from viam.services.vision.service import VisionRPCService
from viam.utils import dict_to_struct, struct_to_dict

from .mocks.services import MockVision

i = Image.new("RGBA", (100, 100), "#AABBCCDD")
IMAGE = pil_to_viam_image(i, CameraMimeType.JPEG)
DETECTORS = [
    "detector-0",
    "detector-1",
]
DETECTIONS = [
    Detection(
        x_min=0,
        y_min=1,
        x_max=10,
        y_max=11,
        confidence=random(),
        class_name="test-detection-class",
    ),
    Detection(
        x_min=100,
        y_min=200,
        x_max=300,
        y_max=400,
        confidence=random(),
        class_name="test-detection-class",
    ),
]
CLASSIFIERS = [
    "classifier-0",
    "classifier-1",
]
CLASSIFICATIONS = [
    Classification(class_name="test-detection-class", confidence=0.1),
    Classification(class_name="test-detection-class", confidence=0.82),
]
SEGMENTERS = [
    "segmenter-0",
    "segmenter-1",
]

POINT_CLOUDS = [
    PointCloudObject(
        point_cloud=b"THIS IS A POINT CLOUD",
        geometries=GeometriesInFrame(
            reference_frame="depth1",
            geometries=[
                Geometry(
                    center=Pose(x=282.45238095238096, y=241.66666666666666, z=902.8809523809524, o_z=1.0),
                    box=RectangularPrism(dims_mm=Vector3(x=13, y=7, z=11)),
                )
            ],
        ),
    ),
    PointCloudObject(
        point_cloud=b"THIS IS A POINT CLOUD",
        geometries=GeometriesInFrame(
            reference_frame="depth1",
            geometries=[
                Geometry(
                    center=Pose(x=-129.84615384615384, y=165.53846153846155, z=511.46153846153845, o_z=1.0),
                    box=RectangularPrism(dims_mm=Vector3(x=5.0, y=4.0, z=7.0)),
                )
            ],
        ),
    ),
]

VISION_SERVICE_NAME = "vision1"


@pytest.fixture(scope="function")
def vision() -> MockVision:
    return MockVision(
        VISION_SERVICE_NAME,
        detectors=DETECTORS,
        detections=DETECTIONS,
        classifiers=CLASSIFIERS,
        classifications=CLASSIFICATIONS,
        segmenters=SEGMENTERS,
        point_clouds=POINT_CLOUDS,
    )


@pytest.fixture(scope="function")
def service(vision: MockVision) -> VisionRPCService:
    rm = ResourceManager([vision])
    return VisionRPCService(rm)


class TestVision:
    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, vision: MockVision):
        extra = {"foo": "get_detections_from_camera"}
        response = await vision.get_detections_from_camera("fake-camera", extra=extra)
        assert response == DETECTIONS
        assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_detections(self, vision: MockVision):
        extra = {"foo": "get_detections"}
        response = await vision.get_detections(IMAGE, extra=extra)
        assert response == DETECTIONS
        assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications_from_camera(self, vision: MockVision):
        extra = {"foo": "get_classifications_from_camera"}
        response = await vision.get_classifications_from_camera("fake-camera", 1, extra=extra)
        assert response == CLASSIFICATIONS
        assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications(self, vision: MockVision):
        extra = {"foo": "get_classifications"}
        response = await vision.get_classifications(IMAGE, 1, extra=extra)
        assert response == CLASSIFICATIONS
        assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, vision: MockVision):
        extra = {"foo": "get_object_point_clouds"}
        response = await vision.get_object_point_clouds("camera", extra=extra)
        assert response == POINT_CLOUDS
        assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_do(self, vision: MockVision):
        command = {"command": "args"}
        response = await vision.do_command(command)
        assert response["cmd"] == command


class TestService:
    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_detections_from_camera"}
            request = GetDetectionsFromCameraRequest(name=vision.name, camera_name="fake-camera", extra=dict_to_struct(extra))
            response: GetDetectionsFromCameraResponse = await client.GetDetectionsFromCamera(request)
            assert response.detections == DETECTIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_detections(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_detections"}
            request = GetDetectionsRequest(
                name=vision.name,
                image=IMAGE.data,
                width=100,
                height=100,
                mime_type=CameraMimeType.JPEG,
                extra=dict_to_struct(extra),
            )
            response: GetDetectionsResponse = await client.GetDetections(request)
            assert response.detections == DETECTIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications_from_camera(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_classifications_from_camera"}
            request = GetClassificationsFromCameraRequest(name=vision.name, camera_name="fake-camera", n=1, extra=dict_to_struct(extra))
            response: GetClassificationsFromCameraResponse = await client.GetClassificationsFromCamera(request)
            assert response.classifications == CLASSIFICATIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_classifications"}
            request = GetClassificationsRequest(
                name=vision.name,
                image=IMAGE.data,
                width=100,
                height=100,
                mime_type=CameraMimeType.JPEG,
                n=1,
                extra=dict_to_struct(extra),
            )
            response: GetClassificationsResponse = await client.GetClassifications(request)
            assert response.classifications == CLASSIFICATIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_object_point_clouds"}
            request = GetObjectPointCloudsRequest(
                name=vision.name,
                camera_name="camera",
                mime_type=CameraMimeType.PCD,
                extra=dict_to_struct(extra),
            )
            response: GetObjectPointCloudsResponse = await client.GetObjectPointClouds(request)
            assert response.objects == POINT_CLOUDS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_do(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=vision.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            assert struct_to_dict(response.result)["cmd"] == command


class TestClient:
    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detections_from_camera"}
            response = await client.get_detections_from_camera("fake-camera", extra=extra)
            assert response == DETECTIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_detections(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detections"}
            response = await client.get_detections(IMAGE, extra=extra)
            assert response == DETECTIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications_from_camera(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifications_from_camera"}
            response = await client.get_classifications_from_camera("fake-camera", 1, extra=extra)
            assert response == CLASSIFICATIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifications"}
            response = await client.get_classifications(IMAGE, 1, extra=extra)
            assert response == CLASSIFICATIONS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_object_point_clouds"}
            response = await client.get_object_point_clouds("camera", extra=extra)
            assert response == POINT_CLOUDS
            assert vision.extra == extra

    @pytest.mark.asyncio
    async def test_do(self, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response["cmd"] == command

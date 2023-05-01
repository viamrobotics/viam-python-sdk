from random import random

import pytest
from grpclib.testing import ChannelFor
from PIL import Image

from viam.proto.common import (
    GeometriesInFrame,
    Geometry,
    PointCloudObject,
    Pose,
    RectangularPrism,
    Vector3,
)
from viam.services.vision import (
    Detection,
    Classification,
    VisionServiceClient,
)

from .mocks.services import MockVision

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
def service() -> MockVision:
    return MockVision(
        detectors=DETECTORS,
        detections=DETECTIONS,
        classifiers=CLASSIFIERS,
        classifications=CLASSIFICATIONS,
        segmenters=SEGMENTERS,
        point_clouds=POINT_CLOUDS,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detections_from_camera"}
            response = await client.get_detections_from_camera("fake-camera", extra=extra)
            assert response == DETECTIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_detections(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            extra = {"foo": "get_detections"}
            response = await client.get_detections(image, extra=extra)
            assert response == DETECTIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications_from_camera(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifications_from_camera"}
            response = await client.get_classifications_from_camera("fake-camera", 1, extra=extra)
            assert response == CLASSIFICATIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            extra = {"foo": "get_classifications"}
            response = await client.get_classifications(image, 1, extra=extra)
            assert response == CLASSIFICATIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_object_point_clouds"}
            response = await client.get_object_point_clouds("camera", extra=extra)
            assert response == POINT_CLOUDS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_do(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == command

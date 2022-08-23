from random import random
from typing import Dict, List, Tuple

import pytest
from grpclib.testing import ChannelFor
from PIL import Image

from viam.proto.api.common import (
    GeometriesInFrame,
    Geometry,
    PointCloudObject,
    Pose,
    RectangularPrism,
    Vector3,
)
from viam.proto.api.service.vision import VisionServiceBase
from viam.services.vision import (
    Detection,
    DetectorConfig,
    DetectorType,
    VisionServiceClient,
)

from .mocks.services import MockVisionService

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
SEGMENTERS = [
    "segmenter-0",
    "segmenter-1",
]
PARAMETERS: Dict[str, List[Tuple[str, str]]] = {
    "segmenter-0": [
        ("parameter-0", "float64"),
        ("parameter-1", "string"),
    ],
    "segmenter-1": [
        ("parameter-0", "int"),
        ("parameter-1", "float64"),
    ],
}
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


@pytest.fixture(scope="function")
def service() -> VisionServiceBase:
    return MockVisionService(
        detectors=DETECTORS, detections=DETECTIONS, segmenters=SEGMENTERS, parameters=PARAMETERS, point_clouds=POINT_CLOUDS
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_detectors(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            response = await client.get_detector_names()
            assert response == DETECTORS

    @pytest.mark.asyncio
    async def test_add_detectors(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            await client.add_detector(DetectorConfig("detector-2", DetectorType.TENSORFLOW, {"foo": "bar"}))
            response = await client.get_detector_names()
            assert response[-1] == "detector-2"

    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            response = await client.get_detections_from_camera("fake-camera", "fake-detector")
            assert response == DETECTIONS

    @pytest.mark.asyncio
    async def test_get_detections(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            response = await client.get_detections(image, "fake-detector")
            assert response == DETECTIONS

    @pytest.mark.asyncio
    async def test_get_segmenters(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            response = await client.get_segmenter_names()
            assert response == SEGMENTERS

    @pytest.mark.asyncio
    async def test_get_segmenter_parameters(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            response = await client.get_segmenter_parameters("segmenter-0")
            assert response == PARAMETERS["segmenter-0"]

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(channel)
            response = await client.get_object_point_clouds("camera", "segmenter", {})
            assert response == POINT_CLOUDS

from random import random
from typing import Dict, Mapping, Sequence, Union

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
from viam.proto.service.vision import VisionServiceBase
from viam.services.vision import (
    Detection,
    Classification,
    VisModelConfig,
    VisModelType,
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
MODEL_SCHEMA: Dict[str, Mapping[str, Union[str, int, float, bool, Sequence, Mapping]]] = {
    VisModelType.CLASSIFIER_TENSORFLOW: {
        "parameter-0": "float64",
        "parameter-1": "string",
    },
    VisModelType.CLASSIFIER_TFLITE: {
        "parameter-0": "int",
        "parameter-1": "string",
    },
    VisModelType.DETECTOR_COLOR: {
        "parameter-0": "int",
        "parameter-1": "float64",
    },
    VisModelType.DETECTOR_TENSORFLOW: {
        "parameter-0": "string",
        "parameter-1": "string",
    },
    VisModelType.DETECTOR_TF_LITE: {
        "parameter-0": "string",
        "parameter-1": "float64",
    },
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

VISION_SERVICE_NAME = "vision1"


@pytest.fixture(scope="function")
def service() -> VisionServiceBase:
    return MockVisionService(
        detectors=DETECTORS,
        detections=DETECTIONS,
        classifiers=CLASSIFIERS,
        classifications=CLASSIFICATIONS,
        segmenters=SEGMENTERS,
        point_clouds=POINT_CLOUDS,
        model_schema=MODEL_SCHEMA,
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_detectors(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_detector_names()
            assert response == DETECTORS

    @pytest.mark.asyncio
    async def test_add_detector(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            await client.add_detector(VisModelConfig("detector-2", VisModelType.DETECTOR_TENSORFLOW, {"foo": "bar"}))
            response = await client.get_detector_names()
            assert response[-1] == "detector-2"

    @pytest.mark.asyncio
    async def test_remove_detector(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            await client.remove_detector("detector-1")
            response = await client.get_detector_names()
            assert "detector-1" not in response

    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_detections_from_camera("fake-camera", "fake-detector")
            assert response == DETECTIONS

    @pytest.mark.asyncio
    async def test_get_detections(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            response = await client.get_detections(image, "fake-detector")
            assert response == DETECTIONS

    @pytest.mark.asyncio
    async def test_get_classifiers(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_classifier_names()
            assert response == CLASSIFIERS

    @pytest.mark.asyncio
    async def test_add_classifier(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            await client.add_classifier(VisModelConfig("classifier-2", VisModelType.DETECTOR_TENSORFLOW, {"foo": "bar"}))
            response = await client.get_classifier_names()
            assert response[-1] == "classifier-2"

    @pytest.mark.asyncio
    async def test_remove_classifier(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            await client.remove_classifier("classifier-1")
            response = await client.get_classifier_names()
            assert "classifier-1" not in response

    @pytest.mark.asyncio
    async def test_get_classifications_from_camera(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_classifications_from_camera("fake-camera", "fake-classifier", 1)
            assert response == CLASSIFICATIONS

    @pytest.mark.asyncio
    async def test_get_classifications(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            response = await client.get_classifications(image, "fake-classifier")
            assert response == CLASSIFICATIONS

    @pytest.mark.asyncio
    async def test_get_segmenters(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_segmenter_names()
            assert response == SEGMENTERS

    @pytest.mark.asyncio
    async def test_add_segmenter(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            await client.add_segmenter(VisModelConfig("segmenter-2", VisModelType.DETECTOR_TENSORFLOW, {"foo": "bar"}))
            response = await client.get_segmenter_names()
            assert response[-1] == "segmenter-2"

    @pytest.mark.asyncio
    async def test_remove_segmenter(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            await client.remove_segmenter("segmenter-1")
            response = await client.get_segmenter_names()
            assert "segmenter-1" not in response

    @pytest.mark.asyncio
    async def test_get_model_parameters_schema(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_model_parameters_schema(VisModelType.DETECTOR_COLOR)
            assert response == MODEL_SCHEMA[VisModelType.DETECTOR_COLOR]

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, service: VisionServiceBase):
        async with ChannelFor([service]) as channel:
            client = VisionServiceClient(VISION_SERVICE_NAME, channel)
            response = await client.get_object_point_clouds("camera", "segmenter", {})
            assert response == POINT_CLOUDS

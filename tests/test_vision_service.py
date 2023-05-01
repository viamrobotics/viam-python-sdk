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
from viam.services.vision import (
    Detection,
    Classification,
    VisModelConfig,
    VisModelType,
    VisionClient,
)

from . import loose_approx
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
def service() -> MockVision:
    return MockVision(
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
    async def test_get_detectors(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detectors"}
            assert service.timeout is None
            timeout = 1.3
            response = await client.get_detector_names(extra=extra, timeout=timeout)
            assert response == DETECTORS
            assert service.extra == extra
            assert service.timeout == loose_approx(timeout)

    @pytest.mark.asyncio
    async def test_add_detector(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "add_detector"}
            await client.add_detector(VisModelConfig("detector-2", VisModelType.DETECTOR_TENSORFLOW, {"foo": "bar"}), extra=extra)
            assert service.extra == extra
            response = await client.get_detector_names()
            assert response[-1] == "detector-2"
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_remove_detector(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "remove_detector"}
            await client.remove_detector("detector-1", extra=extra)
            assert service.extra == extra
            response = await client.get_detector_names()
            assert "detector-1" not in response
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_get_detections_from_camera(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detections_from_camera"}
            response = await client.get_detections_from_camera("fake-camera", "fake-detector", extra=extra)
            assert response == DETECTIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_detections(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            extra = {"foo": "get_detections"}
            response = await client.get_detections(image, "fake-detector", extra=extra)
            assert response == DETECTIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifiers(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifiers"}
            response = await client.get_classifier_names(extra=extra)
            assert response == CLASSIFIERS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_add_classifier(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "add_classifier"}
            await client.add_classifier(VisModelConfig("classifier-2", VisModelType.DETECTOR_TENSORFLOW, {"foo": "bar"}), extra=extra)
            assert service.extra == extra
            response = await client.get_classifier_names()
            assert response[-1] == "classifier-2"
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_remove_classifier(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "remove_classifier"}
            await client.remove_classifier("classifier-1", extra=extra)
            assert service.extra == extra
            response = await client.get_classifier_names()
            assert "classifier-1" not in response
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_get_classifications_from_camera(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifications_from_camera"}
            response = await client.get_classifications_from_camera("fake-camera", "fake-classifier", 1, extra=extra)
            assert response == CLASSIFICATIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_classifications(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            image = Image.new("RGB", (100, 100), "#AABBCCDD")
            extra = {"foo": "get_classifications"}
            response = await client.get_classifications(image, "fake-classifier", extra=extra)
            assert response == CLASSIFICATIONS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_segmenters(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_segmenter_names"}
            response = await client.get_segmenter_names(extra=extra)
            assert response == SEGMENTERS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_add_segmenter(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "add_segmenter"}
            await client.add_segmenter(VisModelConfig("segmenter-2", VisModelType.DETECTOR_TENSORFLOW, {"foo": "bar"}), extra=extra)
            assert service.extra == extra
            response = await client.get_segmenter_names()
            assert response[-1] == "segmenter-2"
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_remove_segmenter(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "remove_segmenter"}
            await client.remove_segmenter("segmenter-1", extra=extra)
            assert service.extra == extra
            response = await client.get_segmenter_names()
            assert "segmenter-1" not in response
            assert service.extra == {}

    @pytest.mark.asyncio
    async def test_get_model_parameters_schema(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_model_parameters_schema"}
            response = await client.get_model_parameters_schema(VisModelType.DETECTOR_COLOR, extra=extra)
            assert response == MODEL_SCHEMA[VisModelType.DETECTOR_COLOR]
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_object_point_clouds"}
            response = await client.get_object_point_clouds("camera", "segmenter", extra=extra)
            assert response == POINT_CLOUDS
            assert service.extra == extra

    @pytest.mark.asyncio
    async def test_do(self, service: MockVision):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response == command

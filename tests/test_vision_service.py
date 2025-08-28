from random import random

import pytest
from grpclib.testing import ChannelFor
from PIL import Image

from viam.media.utils.pil import pil_to_viam_image
from viam.media.video import CameraMimeType, ViamImage
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
    CaptureAllFromCameraRequest,
    CaptureAllFromCameraResponse,
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
    GetPropertiesRequest,
    GetPropertiesResponse,
    VisionServiceStub,
)
from viam.resource.manager import ResourceManager
from viam.services.vision import Classification, Detection, Vision, VisionClient
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
                    center=Pose(
                        x=282.45238095238096,
                        y=241.66666666666666,
                        z=902.8809523809524,
                        o_z=1.0,
                    ),
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
                    center=Pose(
                        x=-129.84615384615384,
                        y=165.53846153846155,
                        z=511.46153846153845,
                        o_z=1.0,
                    ),
                    box=RectangularPrism(dims_mm=Vector3(x=5.0, y=4.0, z=7.0)),
                )
            ],
        ),
    ),
]

# Use string value of CameraMimeType because ViamImage accepts a string mime type in the worst case
# and it may not have the expected CameraMimeType methods defined on it.
VISION_IMAGE = ViamImage(bytes([0, 100]), CameraMimeType.JPEG.value)

PROPERTIES = Vision.Properties(
    classifications_supported=True,
    detections_supported=True,
    object_point_clouds_supported=True,
)


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
        image=VISION_IMAGE,
        properties=PROPERTIES,
    )


@pytest.fixture(scope="function")
def service(vision: MockVision) -> VisionRPCService:
    rm = ResourceManager([vision])
    return VisionRPCService(rm)


class TestVision:
    async def test_get_properties(self, vision: MockVision):
        extra = {"foo": "get_properties"}
        response = await vision.get_properties(extra=extra)
        assert response == PROPERTIES
        assert vision.extra == extra

    async def test_capture_all_from_camera(self, vision: MockVision):
        extra = {"foo": "capture_all_from_camera"}
        response = await vision.capture_all_from_camera(
            "fake-camera",
            return_image=True,
            return_detections=True,
            extra=extra,
        )
        assert response.image is not None
        assert response.image.data == VISION_IMAGE.data
        assert response.image.mime_type == VISION_IMAGE.mime_type
        assert response.detections == DETECTIONS
        assert response.classifications is None
        assert response.objects is None
        assert vision.extra == extra

    async def test_get_detections_from_camera(self, vision: MockVision):
        extra = {"foo": "get_detections_from_camera"}
        response = await vision.get_detections_from_camera("fake-camera", extra=extra)
        assert response == DETECTIONS
        assert vision.extra == extra

    async def test_get_detections(self, vision: MockVision):
        extra = {"foo": "get_detections"}
        response = await vision.get_detections(IMAGE, extra=extra)
        assert response == DETECTIONS
        assert vision.extra == extra

    async def test_get_classifications_from_camera(self, vision: MockVision):
        extra = {"foo": "get_classifications_from_camera"}
        response = await vision.get_classifications_from_camera(
            "fake-camera", 1, extra=extra
        )
        assert response == CLASSIFICATIONS
        assert vision.extra == extra

    async def test_get_classifications(self, vision: MockVision):
        extra = {"foo": "get_classifications"}
        response = await vision.get_classifications(IMAGE, 1, extra=extra)
        assert response == CLASSIFICATIONS
        assert vision.extra == extra

    async def test_get_object_point_clouds(self, vision: MockVision):
        extra = {"foo": "get_object_point_clouds"}
        response = await vision.get_object_point_clouds("camera", extra=extra)
        assert response == POINT_CLOUDS
        assert vision.extra == extra

    async def test_do(self, vision: MockVision):
        command = {"command": "args"}
        response = await vision.do_command(command)
        assert response["cmd"] == command


class TestService:
    async def test_capture_all_from_camera(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "capture_all_from_camera"}
            request = CaptureAllFromCameraRequest(
                name=vision.name,
                camera_name="fake-camera",
                return_image=True,
                return_classifications=True,
                extra=dict_to_struct(extra),
            )
            response: CaptureAllFromCameraResponse = await client.CaptureAllFromCamera(
                request
            )
            assert response.image.image == VISION_IMAGE.data
            assert response.image.mime_type == VISION_IMAGE.mime_type
            # TODO(RSDK-11728): remove this once we deleted the format field
            assert response.image.format == VISION_IMAGE.mime_type.to_proto()
            assert response.classifications == CLASSIFICATIONS
            assert response.detections == []
            assert response.objects == []
            assert vision.extra == extra

    async def test_get_properties(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_properties"}
            request = GetPropertiesRequest(
                name=vision.name, extra=dict_to_struct(extra)
            )
            response: GetPropertiesResponse = await client.GetProperties(request)
            assert (
                response.classifications_supported
                == PROPERTIES.classifications_supported
            )
            assert response.detections_supported == PROPERTIES.detections_supported
            assert (
                response.object_point_clouds_supported
                == PROPERTIES.object_point_clouds_supported
            )
            assert vision.extra == extra

    async def test_get_detections_from_camera(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_detections_from_camera"}
            request = GetDetectionsFromCameraRequest(
                name=vision.name, camera_name="fake-camera", extra=dict_to_struct(extra)
            )
            response: GetDetectionsFromCameraResponse = (
                await client.GetDetectionsFromCamera(request)
            )
            assert response.detections == DETECTIONS
            assert vision.extra == extra

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

    async def test_get_classifications_from_camera(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_classifications_from_camera"}
            request = GetClassificationsFromCameraRequest(
                name=vision.name,
                camera_name="fake-camera",
                n=1,
                extra=dict_to_struct(extra),
            )
            response: GetClassificationsFromCameraResponse = (
                await client.GetClassificationsFromCamera(request)
            )
            assert response.classifications == CLASSIFICATIONS
            assert vision.extra == extra

    async def test_get_classifications(
        self, vision: MockVision, service: VisionRPCService
    ):
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
            response: GetClassificationsResponse = await client.GetClassifications(
                request
            )
            assert response.classifications == CLASSIFICATIONS
            assert vision.extra == extra

    async def test_get_object_point_clouds(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            extra = {"foo": "get_object_point_clouds"}
            request = GetObjectPointCloudsRequest(
                name=vision.name,
                camera_name="camera",
                mime_type=CameraMimeType.PCD,
                extra=dict_to_struct(extra),
            )
            response: GetObjectPointCloudsResponse = await client.GetObjectPointClouds(
                request
            )
            assert response.objects == POINT_CLOUDS
            assert vision.extra == extra

    async def test_do(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(
                name=vision.name, command=dict_to_struct(command)
            )
            response: DoCommandResponse = await client.DoCommand(request)
            assert struct_to_dict(response.result)["cmd"] == command


class TestClient:
    async def test_get_properties(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_properties"}
            response = await client.get_properties(extra=extra)
            assert response == PROPERTIES
            assert vision.extra == extra

    async def test_capture_all_from_camera(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "capture_all_from_camera"}
            response = await client.capture_all_from_camera(
                "fake-camera",
                return_image=True,
                return_object_point_clouds=True,
                extra=extra,
            )
            assert response.image is not None
            assert response.image.data == VISION_IMAGE.data
            assert response.image.mime_type == VISION_IMAGE.mime_type
            assert response.detections is None
            assert response.classifications is None
            assert response.objects == POINT_CLOUDS
            assert vision.extra == extra

    async def test_get_detections_from_camera(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detections_from_camera"}
            response = await client.get_detections_from_camera(
                "fake-camera", extra=extra
            )
            assert response == DETECTIONS
            assert vision.extra == extra

    async def test_get_detections(self, vision: MockVision, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_detections"}
            response = await client.get_detections(IMAGE, extra=extra)
            assert response == DETECTIONS
            assert vision.extra == extra

    async def test_get_classifications_from_camera(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifications_from_camera"}
            response = await client.get_classifications_from_camera(
                "fake-camera", 1, extra=extra
            )
            assert response == CLASSIFICATIONS
            assert vision.extra == extra

    async def test_get_classifications(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_classifications"}
            response = await client.get_classifications(IMAGE, 1, extra=extra)
            assert response == CLASSIFICATIONS
            assert vision.extra == extra

    async def test_get_object_point_clouds(
        self, vision: MockVision, service: VisionRPCService
    ):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            extra = {"foo": "get_object_point_clouds"}
            response = await client.get_object_point_clouds("camera", extra=extra)
            assert response == POINT_CLOUDS
            assert vision.extra == extra

    async def test_do(self, service: VisionRPCService):
        async with ChannelFor([service]) as channel:
            client = VisionClient(VISION_SERVICE_NAME, channel)
            command = {"command": "args"}
            response = await client.do_command(command)
            assert response["cmd"] == command

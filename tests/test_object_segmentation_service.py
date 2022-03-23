from typing import Dict, List, Tuple
import pytest
from grpclib.testing import ChannelFor
from viam.proto.api.common import (GeometriesInFrame, Geometry,
                                   PointCloudObject, Pose, RectangularPrism)
from viam.services.object_segmentation import ObjectSegmentationClient

from .mocks.services import MockObjectSegmentationService

SEGMENTERS = [
    'segmenter-0',
    'segmenter-1',
]
PARAMETERS: Dict[str, List[Tuple[str, str]]] = {
    'segmenter-0': [
        ('parameter-0', 'float64'),
        ('parameter-1', 'string'),
    ],
    'segmenter-1': [
        ('parameter-0', 'int'),
        ('parameter-1', 'float64'),
    ],
}
POINT_CLOUDS = [
    PointCloudObject(
        point_cloud=b'THIS IS A POINT CLOUD',
        geometries=GeometriesInFrame(
            reference_frame='depth1',
            geometries=[
                Geometry(
                    center=Pose(
                        x=282.45238095238096,
                        y=241.66666666666666,
                        z=902.8809523809524,
                        o_z=1.0
                    ),
                    box=RectangularPrism(
                        width_mm=13,
                        length_mm=7,
                        depth_mm=11
                    )
                )
            ]
        )
    ),
    PointCloudObject(
        point_cloud=b'THIS IS A POINT CLOUD',
        geometries=GeometriesInFrame(
            reference_frame='depth1',
            geometries=[
                Geometry(
                    center=Pose(
                        x=-129.84615384615384,
                        y=165.53846153846155,
                        z=511.46153846153845,
                        o_z=1.0
                    ),
                    box=RectangularPrism(
                        width_mm=5.0,
                        length_mm=4.0,
                        depth_mm=7.0
                    )
                )
            ]
        )
    )
]


@pytest.fixture(scope='function')
def service() -> MockObjectSegmentationService:
    return MockObjectSegmentationService(
        segmenters=SEGMENTERS,
        parameters=PARAMETERS,
        point_clouds=POINT_CLOUDS
    )


class TestClient:
    @pytest.mark.asyncio
    async def test_get_segmenters(
        self,
        service: MockObjectSegmentationService
    ):
        async with ChannelFor([service]) as channel:
            client = ObjectSegmentationClient(channel)
            response = await client.get_segmenters()
            assert response == SEGMENTERS

    @pytest.mark.asyncio
    async def test_get_segmenter_parameters(
        self,
        service: MockObjectSegmentationService
    ):
        async with ChannelFor([service]) as channel:
            client = ObjectSegmentationClient(channel)
            response = await client.get_segmenter_parameters('segmenter-0')
            assert response == PARAMETERS['segmenter-0']

    @pytest.mark.asyncio
    async def test_get_object_point_clouds(
        self,
        service: MockObjectSegmentationService
    ):
        async with ChannelFor([service]) as channel:
            client = ObjectSegmentationClient(channel)
            response = await client.get_object_point_clouds('camera',
                                                            'segmenter',
                                                            {})
            assert response == POINT_CLOUDS

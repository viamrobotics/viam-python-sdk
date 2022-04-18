import pytest
from grpclib.testing import ChannelFor
from viam.components.resource_manager import ResourceManager
from viam.proto.api.common import ResourceName
from viam.proto.api.service.metadata import (MetadataServiceStub,
                                             ResourcesRequest,
                                             ResourcesResponse)
from viam.services.metadata.client import MetadataClient
from viam.services.metadata.service import MetadataService

from .mocks.components import MockArm, MockCamera, MockMotor

EXPECTED = [
    ResourceName(
        namespace='rdk',
        type='service',
        subtype='metadata',
    ),
    ResourceName(
        namespace='rdk',
        type='service',
        subtype='status',
    ),
    ResourceName(
        namespace='rdk',
        type='component',
        subtype='arm',
        name='arm1'
    ),
    ResourceName(
        namespace='rdk',
        type='component',
        subtype='camera',
        name='camera1'
    ),
    ResourceName(
        namespace='rdk',
        type='component',
        subtype='motor',
        name='motor1'
    ),
]


@pytest.fixture(scope='function')
def service() -> MetadataService:
    resources = [
        MockArm(name='arm1'),
        MockCamera(name='camera1'),
        MockMotor(name='motor1'),
    ]

    manager = ResourceManager(resources)
    return MetadataService(manager)


@pytest.mark.asyncio
async def test_status_client(service: MetadataService):
    async with ChannelFor([service]) as channel:
        client = MetadataClient(channel)
        resources = await client.resources()
        assert resources == EXPECTED


@pytest.mark.asyncio
async def test_status_service(service: MetadataService):
    async with ChannelFor([service]) as channel:
        client = MetadataServiceStub(channel)
        request = ResourcesRequest()
        response: ResourcesResponse = await client.Resources(request)
        assert list(response.resources) == EXPECTED

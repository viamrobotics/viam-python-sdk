import pytest

from typing import Dict
from grpclib.testing import ChannelFor

from viam.proto.service.mlmodel import InferRequest, InferResponse, Metadata, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.manager import ResourceManager
from viam.services.mlmodel.service import MLModelServiceRPCService

from .mocks.services import MockMLModelService


OUTPUT_DATA = {"thing": "thing"}
METADATA_INFO = Metadata()


class TestMLModel:
    name = "mlmodel"
    mlmodel = MockMLModelService(name=name)

    @pytest.mark.asyncio
    async def test_infer(self):
        resp = await self.mlmodel.infer()
        assert resp == OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        resp = await self.mlmodel.metadata()
        assert resp == METADATA_INFO

    @pytest.mark.asyncio
    async def do_command(self):
        command = {"command": "args"}
        resp = await self.mlmodel.do_command(command)
        assert resp == {"command": command}



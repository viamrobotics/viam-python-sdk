from typing import List

import pytest
from grpclib.testing import ChannelFor

from viam.proto.service.mlmodel import InferRequest, InferResponse, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.manager import ResourceManager
from viam.services.mlmodel import MLModelClient, MLModelRPCService
from viam.utils import struct_to_dict

from .mocks.services import MockMLModel


class TestMLModel:
    name = "mlmodel"
    mlmodel = MockMLModel(name=name)

    @pytest.mark.asyncio
    async def test_infer(self):
        resp = await self.mlmodel.infer(input_data=MockMLModel.INPUT_DATA)
        assert resp == MockMLModel.OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        resp = await self.mlmodel.metadata()
        assert resp == MockMLModel.META

    @pytest.mark.asyncio
    async def do_command(self):
        command = {"command": "args"}
        resp = await self.mlmodel.do_command(command)
        assert resp == {"command": command}


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "mlmodel"
        cls.mlmodel = MockMLModel(name=cls.name)
        cls.manager = ResourceManager([cls.mlmodel])
        cls.service = MLModelRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_infer(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceStub(channel)
            request = InferRequest(name=self.name)
            response: InferResponse = await client.Infer(request)
            assert struct_to_dict(response.output_data) == MockMLModel.OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceStub(channel)
            request = MetadataRequest(name=self.name)
            response: MetadataResponse = await client.Metadata(request)
            assert response.metadata == MockMLModel.META


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "mlmodel"
        cls.mlmodel = MockMLModel(name=cls.name)
        cls.manager = ResourceManager([cls.mlmodel])
        cls.service = MLModelRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_infer(self):
        OUTPUT_DATA = MockMLModel.OUTPUT_DATA
        async with ChannelFor([self.service]) as channel:
            client = MLModelClient(self.name, channel)
            response = await client.infer(MockMLModel.INPUT_DATA)
            assert "confidence_scores" in response.keys()
            assert "labels" in response.keys()
            assert "locations" in response.keys()
            assert isinstance(response["confidence_scores"], List)
            assert isinstance(response["labels"], List)
            assert isinstance(response["locations"], List)
            assert response["n_detections"] == OUTPUT_DATA["n_detections"]
            assert len(response["confidence_scores"][0]) == len(OUTPUT_DATA["confidence_scores"][0])
            assert len(response["labels"][0]) == len(OUTPUT_DATA["labels"][0])
            assert response["locations"][0][0] == OUTPUT_DATA["locations"][0][0]
            assert response == OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        async with ChannelFor([self.service]) as channel:
            META = MockMLModel.META
            META_INPUTS = MockMLModel.META_INPUTS
            META_OUTPUTS = MockMLModel.META_OUTPUTS
            client = MLModelClient(self.name, channel)
            response = await client.metadata()
            assert response.name == META.name
            assert response.type == META.type
            assert response.description == META.description
            assert len(response.input_info) == len(META_INPUTS)
            assert response.input_info[0].shape == META_INPUTS[0].shape
            assert response.input_info == META_INPUTS
            output_info = response.output_info
            assert len(output_info) == len(META_OUTPUTS)
            assert output_info[0].name == META_OUTPUTS[0].name
            assert len(output_info[0].associated_files) == len(META_OUTPUTS[0].associated_files)
            assert output_info[2].name == META_OUTPUTS[2].name
            assert output_info[2].associated_files[0].name == META_OUTPUTS[2].associated_files[0].name
            assert output_info[3].name == META_OUTPUTS[3].name
            assert output_info[3].shape == META_OUTPUTS[3].shape
            assert output_info == META_OUTPUTS
            assert response == META

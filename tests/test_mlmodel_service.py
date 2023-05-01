import pytest

from typing import Dict
from grpclib.testing import ChannelFor
from viam.proto.service.mlmodel import InferRequest, InferResponse, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.manager import ResourceManager
from viam.services.mlmodel import File, LabelType, Metadata, MLModelServiceClient, MLModelServiceRPCService, TensorInfo
from viam.utils import struct_to_dict
from .mocks.services import MockMLModelService


INPUT_DATA: Dict = {"image": [10, 10, 255, 0, 0, 255, 255, 0, 100]}
OUTPUT_DATA = {
    "n_detections": [3],
    "confidence_scores": [[0.9084375, 0.7359375, 0.33984375]],
    "labels": [[0, 0, 4]],
    "locations": [[0.1, 0.4, 0.22, 0.4], [0.02, 0.22, 0.77, 0.90], [0.40, 0.50, 0.40, 0.50]],
}
META_INPUTS = [TensorInfo(name="image", description="i0", data_type="uint8", shape=[300, 200])]
META_OUTPUTS = [
    TensorInfo(name="n_detections", description="o0", data_type="int32", shape=[1]),
    TensorInfo(name="confidence_scores", description="o1", data_type="float32", shape=[3, 1]),
    TensorInfo(
        name="labels",
        description="o2",
        data_type="int32",
        shape=[3, 1],
        associated_files=[
            File(
                name="category_labels.txt",
                description="these labels represent types of plants",
                label_type=LabelType.LABEL_TYPE_TENSOR_VALUE,
            )
        ],
    ),
    TensorInfo(name="locations", description="o3", data_type="float32", shape=[4, 3, 1]),
]
META = Metadata(name="fake_detector", type="object_detector", description="desc", input_info=META_INPUTS, output_info=META_OUTPUTS)


class TestMLModel:
    name = "mlmodel"
    mlmodel = MockMLModelService(name=name)

    @pytest.mark.asyncio
    async def test_infer(self):
        resp = await self.mlmodel.infer(input_data=INPUT_DATA)
        assert resp == OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        resp = await self.mlmodel.metadata()
        assert resp == META

    @pytest.mark.asyncio
    async def do_command(self):
        command = {"command": "args"}
        resp = await self.mlmodel.do_command(command)
        assert resp == {"command": command}


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "mlmodel"
        cls.mlmodel = MockMLModelService(name=cls.name)
        cls.manager = ResourceManager([cls.mlmodel])
        cls.service = MLModelServiceRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_infer(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceStub(channel)
            request = InferRequest(name=self.name)
            response: InferResponse = await client.Infer(request)
            assert struct_to_dict(response.output_data) == OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceStub(channel)
            request = MetadataRequest(name=self.name)
            response: MetadataResponse = await client.Metadata(request)
            assert response.metadata == META


class TestClient:
    @classmethod
    def setup_class(cls):
        cls.name = "mlmodel"
        cls.mlmodel = MockMLModelService(name=cls.name)
        cls.manager = ResourceManager([cls.mlmodel])
        cls.service = MLModelServiceRPCService(cls.manager)

    @pytest.mark.asyncio
    async def test_infer(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceClient(self.name, channel)
            response = await client.infer(INPUT_DATA)
            assert response == OUTPUT_DATA

    @pytest.mark.asyncio
    async def test_metadata(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceClient(self.name, channel)
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

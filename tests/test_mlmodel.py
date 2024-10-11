import numpy as np
import pytest
from grpclib.testing import ChannelFor

from viam.proto.service.mlmodel import InferRequest, InferResponse, MetadataRequest, MetadataResponse, MLModelServiceStub
from viam.resource.manager import ResourceManager
from viam.services.mlmodel import MLModelClient, MLModelRPCService

from .mocks.services import MockMLModel


class TestMLModel:
    name = "mlmodel"
    mlmodel = MockMLModel(name=name)

    async def test_infer(self):
        resp = await self.mlmodel.infer(input_tensors=MockMLModel.EMPTY_NDARRAYS)
        assert resp == MockMLModel.EMPTY_NDARRAYS

    async def test_metadata(self):
        resp = await self.mlmodel.metadata()
        assert resp == MockMLModel.META


class TestService:
    @classmethod
    def setup_class(cls):
        cls.name = "mlmodel"
        cls.mlmodel = MockMLModel(name=cls.name)
        cls.manager = ResourceManager([cls.mlmodel])
        cls.service = MLModelRPCService(cls.manager)

    async def test_infer(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelServiceStub(channel)
            request = InferRequest(name=self.name)
            response: InferResponse = await client.Infer(request)
            assert response.output_tensors == MockMLModel.EMPTY_TENSORS

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

    #  ignore warning about our out-of-bound int casting (i.e. uint32 -> int16) because we don't store uint32s for int16 & uint16 tensor
    #  data > 2^16-1 in the first place (inherently they are int16, we just cast them to uint32 for the grpc message)
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    async def test_infer(self):
        async with ChannelFor([self.service]) as channel:
            client = MLModelClient(self.name, channel)
            response = await client.infer(MockMLModel.EMPTY_NDARRAYS)
            assert not response

            response = await client.infer(MockMLModel.DOUBLE_NDARRAYS)
            assert len(response.keys()) == 1
            assert "0" in response.keys()
            assert np.array_equal(response["0"], MockMLModel.DOUBLE_NDARRAY)
            assert response["0"].dtype == np.float64

            response = await client.infer(MockMLModel.DOUBLE_FLOAT_NDARRAYS)
            assert len(response.keys()) == 2
            assert response["0"].dtype == np.float64
            assert np.array_equal(response["0"], MockMLModel.DOUBLE_NDARRAY)
            assert response["1"].dtype == np.float32
            assert np.array_equal(response["1"], MockMLModel.FLOAT_NDARRAY)

            response = await client.infer(MockMLModel.INTS_NDARRAYS)
            assert len(response.keys()) == 4
            assert all(name in response.keys() for name in ["0", "1", "2", "3"])
            assert np.array_equal(response["0"], MockMLModel.INT8_NDARRAY)
            assert response["0"].dtype == np.int8
            assert np.array_equal(response["1"], MockMLModel.INT16_NDARRAY)
            assert response["1"].dtype == np.int16
            assert np.array_equal(response["2"], MockMLModel.INT32_NDARRAY)
            assert response["2"].dtype == np.int32
            assert np.array_equal(response["3"], MockMLModel.INT64_NDARRAY)
            assert response["3"].dtype == np.int64

            response = await client.infer(MockMLModel.UINTS_NDARRAYS)
            assert len(response.keys()) == 4
            assert all(name in response.keys() for name in ["0", "1", "2", "3"])
            assert np.array_equal(response["0"], MockMLModel.UINT8_NDARRAY)
            assert response["0"].dtype == np.uint8
            assert np.array_equal(response["1"], MockMLModel.UINT16_NDARRAY)
            assert response["1"].dtype == np.uint16
            assert np.array_equal(response["2"], MockMLModel.UINT32_NDARRAY)
            assert response["2"].dtype == np.uint32
            assert np.array_equal(response["3"], MockMLModel.UINT64_NDARRAY)
            assert response["3"].dtype == np.uint64

            response = await client.infer(MockMLModel.SQUARE_INT_UINT_NDARRAYS)
            assert len(response.keys()) == 2
            assert all(name in response for name in ["0", "1"])
            assert np.array_equal(response["0"], MockMLModel.SQUARE_INT16_NDARRAY)
            assert response["0"].dtype == np.int16
            assert np.array_equal(response["1"], MockMLModel.UINT64_NDARRAY)
            assert response["1"].dtype == np.uint64

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

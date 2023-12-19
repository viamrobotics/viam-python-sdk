import builtins

import numpy as np
import pytest

from viam.services.mlmodel.utils import flat_tensors_to_ndarrays, ndarrays_to_flat_tensors

from .mocks.services import MockMLModel


#  ignore warning about our out-of-bound int casting (i.e. uint32 -> int16) because we don't store uint32s for int16 & uint16 tensor data
# > 2^16-1 in the first place (inherently they are int16, we just cast them to uint32 for the grpc message)
@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_flat_tensors_to_ndarrays():
    output = flat_tensors_to_ndarrays(MockMLModel.INTS_FLAT_TENSORS)
    assert len(output.keys()) == 4
    assert all(name in output.keys() for name in ["0", "1", "2", "3"])
    assert np.array_equal(output["0"], MockMLModel.INT8_NDARRAY)
    assert output["0"].dtype == np.int8
    assert np.array_equal(output["1"], MockMLModel.INT16_NDARRAY)
    assert output["1"].dtype == np.int16
    assert np.array_equal(output["2"], MockMLModel.INT32_NDARRAY)
    assert output["2"].dtype == np.int32
    assert np.array_equal(output["3"], MockMLModel.INT64_NDARRAY)
    assert output["3"].dtype == np.int64

    output = flat_tensors_to_ndarrays(MockMLModel.UINTS_FLAT_TENSORS)
    assert len(output.keys()) == 4
    assert all(name in output.keys() for name in ["0", "1", "2", "3"])
    assert np.array_equal(output["0"], MockMLModel.UINT8_NDARRAY)
    assert output["0"].dtype == np.uint8
    assert np.array_equal(output["1"], MockMLModel.UINT16_NDARRAY)
    assert output["1"].dtype == np.uint16
    assert np.array_equal(output["2"], MockMLModel.UINT32_NDARRAY)
    assert output["2"].dtype == np.uint32
    assert np.array_equal(output["3"], MockMLModel.UINT64_NDARRAY)
    assert output["3"].dtype == np.uint64

    output = flat_tensors_to_ndarrays(MockMLModel.DOUBLE_FLOAT_TENSORS)
    assert len(output.keys()) == 2
    assert all(name in output.keys() for name in ["0", "1"])
    assert np.array_equal(output["0"], MockMLModel.DOUBLE_NDARRAY)
    assert output["0"].dtype == np.float64
    assert np.array_equal(output["1"], MockMLModel.FLOAT_NDARRAY)
    assert output["1"].dtype == np.float32


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_ndarrays_to_flat_tensors():
    output = ndarrays_to_flat_tensors(MockMLModel.INTS_NDARRAYS)
    assert len(output.tensors) == 4
    assert all(name in output.tensors.keys() for name in ["0", "1", "2", "3"])
    assert type(output.tensors["0"].int8_tensor.data) is builtins.bytes
    bytes_buffer = output.tensors["0"].int8_tensor.data
    assert np.array_equal(np.frombuffer(bytes_buffer, dtype=np.int8).reshape(output.tensors["0"].shape), MockMLModel.INT8_NDARRAY)
    assert np.array_equal(np.array(output.tensors["1"].int16_tensor.data, dtype=np.int16), MockMLModel.INT16_NDARRAY)
    assert np.array_equal(np.array(output.tensors["2"].int32_tensor.data, dtype=np.int32), MockMLModel.INT32_NDARRAY)
    assert np.array_equal(np.array(output.tensors["3"].int64_tensor.data, dtype=np.int64), MockMLModel.INT64_NDARRAY)

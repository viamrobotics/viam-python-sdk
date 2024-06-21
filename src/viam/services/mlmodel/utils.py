from typing import Dict

import numpy as np
from numpy.typing import NDArray

from viam.proto.service.mlmodel import (
    FlatTensor,
    FlatTensorDataDouble,
    FlatTensorDataFloat,
    FlatTensorDataInt8,
    FlatTensorDataInt16,
    FlatTensorDataInt32,
    FlatTensorDataInt64,
    FlatTensorDataUInt8,
    FlatTensorDataUInt16,
    FlatTensorDataUInt32,
    FlatTensorDataUInt64,
    FlatTensors,
)


def flat_tensors_to_ndarrays(flat_tensors: FlatTensors) -> Dict[str, NDArray]:
    property_name_to_dtype = {
        "float_tensor": np.float32,
        "double_tensor": np.float64,
        "int8_tensor": np.int8,
        "int16_tensor": np.int16,
        "int32_tensor": np.int32,
        "int64_tensor": np.int64,
        "uint8_tensor": np.uint8,
        "uint16_tensor": np.uint16,
        "uint32_tensor": np.uint32,
        "uint64_tensor": np.uint64,
    }

    def make_ndarray(flat_data, dtype, shape):
        """Takes flat data (protobuf RepeatedScalarFieldContainer | bytes) to output an ndarray
        of appropriate dtype and shape"""
        make_array = np.frombuffer if dtype == np.int8 or dtype == np.uint8 else np.array
        return make_array(flat_data, dtype).reshape(shape)

    ndarrays: Dict[str, NDArray] = dict()
    for name, flat_tensor in flat_tensors.tensors.items():
        property_name = flat_tensor.WhichOneof("tensor") or flat_tensor.WhichOneof(b"tensor")
        if property_name:
            tensor_data = getattr(flat_tensor, property_name)
            flat_data, dtype, shape = tensor_data.data, property_name_to_dtype[property_name], flat_tensor.shape
            ndarrays[name] = make_ndarray(flat_data, dtype, shape)
    return ndarrays


def ndarrays_to_flat_tensors(ndarrays: Dict[str, NDArray]) -> FlatTensors:
    dtype_name_to_tensor_data_class = {
        "float32": FlatTensorDataFloat,
        "float64": FlatTensorDataDouble,
        "int8": FlatTensorDataInt8,
        "int16": FlatTensorDataInt16,
        "int32": FlatTensorDataInt32,
        "int64": FlatTensorDataInt64,
        "uint8": FlatTensorDataUInt8,
        "uint16": FlatTensorDataUInt16,
        "uint32": FlatTensorDataUInt32,
        "uint64": FlatTensorDataUInt64,
    }

    def get_tensor_data(ndarray: NDArray):
        """Takes an ndarray and returns the corresponding tensor data class instance
        for example FlatTensorDataInt8, FlatTensorDataUInt8 etc."""
        tensor_data_class = dtype_name_to_tensor_data_class[ndarray.dtype.name]
        data = ndarray.flatten()
        if tensor_data_class == FlatTensorDataInt8 or tensor_data_class == FlatTensorDataUInt8:
            data = data.tobytes()  # as per the proto, int8 and uint8 are stored as bytes
        elif tensor_data_class == FlatTensorDataInt16 or tensor_data_class == FlatTensorDataUInt16:
            data = data.astype(np.uint32)  # as per the proto, int16 and uint16 are stored as uint32
        tensor_data = tensor_data_class(data=data)
        return tensor_data

    def get_tensor_data_type(ndarray: NDArray):
        """Takes ndarray and returns a FlatTensor datatype property to be set
        for example "float_tensor", "uint32_tensor" etc."""
        if ndarray.dtype == np.float32:
            return "float_tensor"
        elif ndarray.dtype == np.float64:
            return "double_tensor"
        return f"{ndarray.dtype.name}_tensor"

    tensors_mapping: Dict[str, FlatTensor] = dict()
    for name, ndarray in ndarrays.items():
        prop_name, prop_value = get_tensor_data_type(ndarray), get_tensor_data(ndarray)
        tensors_mapping[name] = FlatTensor(shape=ndarray.shape, **{prop_name: prop_value})
    return FlatTensors(tensors=tensors_mapping)

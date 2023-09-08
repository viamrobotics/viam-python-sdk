import asyncio
import contextvars
import functools
import numpy as np
import sys
import threading
from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, SupportsBytes, SupportsFloat, Type, TypeVar, Union
from numpy.typing import NDArray

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message
from google.protobuf.struct_pb2 import ListValue, Struct, Value
from google.protobuf.timestamp_pb2 import Timestamp

from viam.proto.common import Geometry, GeoPoint, GetGeometriesRequest, GetGeometriesResponse, Orientation, ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry
from viam.resource.types import Subtype, SupportsGetGeometries
from viam.proto.service.mlmodel import (
    FlatTensors,
    FlatTensor,
    FlatTensorDataDouble,
    FlatTensorDataFloat,
    FlatTensorDataInt16,
    FlatTensorDataInt32,
    FlatTensorDataInt64,
    FlatTensorDataInt8,
    FlatTensorDataUInt16,
    FlatTensorDataUInt32,
    FlatTensorDataUInt64,
    FlatTensorDataUInt8,
)

if sys.version_info >= (3, 9):
    from collections.abc import Callable
else:
    from typing import Callable

if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


ValueTypes = Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, None]
"""Types that can be encoded into a protobuf `Value`"""


def primitive_to_value(v: ValueTypes) -> Value:
    """
    Create a new google.protobuf.struct_pb2.Value
    Supports primitive types of
    - None
    - Number
    - Bool
    - String
    - Dict
    - List
    - Bytes

    Args:
        v (ValueTypes): object to convert to a Value

    Raises:
        TypeError: If the object cannot be converted

    Returns:
        Value: a protobuf Value instance of the object
    """
    if v is None:
        return Value(null_value=v)
    if isinstance(v, bool):
        return Value(bool_value=v)
    if isinstance(v, SupportsFloat):
        return Value(number_value=float(v))
    if isinstance(v, str):
        return Value(string_value=v)
    if isinstance(v, Dict):
        sv: Dict[str, Value] = {}
        for key, value in v.items():
            if not isinstance(key, str):
                raise TypeError(f"Invalid UTF-8 in string: {key}")
            sv[key] = primitive_to_value(value)
        struct = Struct(fields=sv)
        return Value(struct_value=struct)
    if isinstance(v, List):
        lv = []
        for vv in v:
            lv.append(primitive_to_value(vv))
        list_value = ListValue(values=lv)
        return Value(list_value=list_value)
    if isinstance(v, (bytes, bytearray)):
        return Value(string_value=v.decode())
    raise TypeError(f"Invalid type {type(v)}")


def value_to_primitive(value: Value) -> ValueTypes:
    if value.HasField("list_value"):
        return [value_to_primitive(v) for v in value.list_value.values]
    if value.HasField("struct_value"):
        return {k: value_to_primitive(v) for (k, v) in value.struct_value.fields.items()}
    if value.HasField("string_value"):
        return value.string_value
    if value.HasField("number_value"):
        return value.number_value
    if value.HasField("bool_value"):
        return value.bool_value
    if value.HasField("null_value"):
        return value.null_value
    return None


def resource_names_for_resource(resource: ResourceBase) -> List[ResourceName]:
    rns: List[ResourceName] = []

    for klass in resource.__class__.mro():
        for registration in Registry.REGISTERED_SUBTYPES().values():
            if klass is registration.resource_type:
                subtype: Subtype = registration.resource_type.SUBTYPE
                rns.append(
                    ResourceName(
                        namespace=subtype.namespace, type=subtype.resource_type, subtype=subtype.resource_subtype, name=resource.name
                    )
                )
    return rns


def message_to_struct(message: Message) -> Struct:
    struct = Struct()
    struct.update(
        MessageToDict(
            message,
            including_default_value_fields=True,
            preserving_proto_field_name=True,
        ),
    )
    return struct


_T = TypeVar("_T", bound=Message)


def struct_to_message(struct: Struct, message_type: Type[_T]) -> _T:
    dct = struct_to_dict(struct)
    return ParseDict(dct, message_type())


def dict_to_struct(obj: Mapping[str, ValueTypes]) -> Struct:
    def _convert(v: ValueTypes) -> Any:
        if isinstance(v, bool):
            return v
        if isinstance(v, SupportsFloat):
            return float(v)
        if isinstance(v, SupportsBytes):
            return bytes(v)
        if isinstance(v, List):
            return [_convert(vv) for vv in v]
        if isinstance(v, Mapping):
            return {k: _convert(vv) for (k, vv) in v.items()}
        return v

    struct = Struct()
    struct.update({k: _convert(v) for (k, v) in obj.items()})
    return struct


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
        e.g. FlatTensorDataInt8, FlatTensorDataUInt8 etc."""
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
        e.g. "float_tensor", "uint32_tensor" etc."""
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


def struct_to_dict(struct: Struct) -> Dict[str, ValueTypes]:
    return {key: value_to_primitive(value) for (key, value) in struct.fields.items()}


def datetime_to_timestamp(dt: Optional[datetime]) -> Optional[Timestamp]:
    if dt is None:
        return None
    timestamp = Timestamp()
    timestamp.FromDatetime(dt)
    return timestamp


async def get_geometries(
    client: SupportsGetGeometries, name: str, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None
) -> List[Geometry]:
    if extra is None:
        extra = {}
    request = GetGeometriesRequest(name=name, extra=dict_to_struct(extra))
    response: GetGeometriesResponse = await client.GetGeometries(request, timeout=timeout)
    return [geometry for geometry in response.geometries]


def sensor_readings_native_to_value(readings: Mapping[str, Any]) -> Mapping[str, Any]:
    prim_readings = dict(readings)
    for key, reading in readings.items():
        if isinstance(reading, Vector3):
            prim_readings[key] = {"x": reading.x, "y": reading.y, "z": reading.z, "_type": "vector3"}
        elif isinstance(reading, GeoPoint):
            prim_readings[key] = {"lat": reading.latitude, "lng": reading.longitude, "_type": "geopoint"}
        elif isinstance(reading, Orientation):
            prim_readings[key] = {
                "ox": reading.o_x,
                "oy": reading.o_y,
                "oz": reading.o_z,
                "theta": reading.theta,
                "_type": "orientation_vector_degrees",
            }
    return {key: primitive_to_value(value) for (key, value) in prim_readings.items()}


def sensor_readings_value_to_native(readings: Mapping[str, Value]) -> Mapping[str, Any]:
    prim_readings: Dict[str, Any] = {key: value_to_primitive(value) for (key, value) in readings.items()}
    for key, reading in prim_readings.items():
        if isinstance(reading, Mapping):
            kind = reading.get("_type", "")
            if kind == "angular_velocity":
                prim_readings[key] = Vector3(x=reading["x"], y=reading["y"], z=reading["z"])
            elif kind == "vector3":
                prim_readings[key] = Vector3(x=reading["x"], y=reading["y"], z=reading["z"])
            elif kind == "geopoint":
                prim_readings[key] = GeoPoint(latitude=reading["lat"], longitude=reading["lng"])
            elif kind == "orientation_vector_degrees":
                prim_readings[key] = Orientation(o_x=reading["ox"], o_y=reading["oy"], o_z=reading["oz"], theta=reading["theta"])
    return prim_readings


class PointerCounter:
    def __init__(self) -> None:
        self._event = asyncio.Event()
        self._lock = threading.Lock()
        self._count = 0
        self._event.set()

    def increment(self) -> int:
        self._lock.acquire()
        self._count += 1
        self._event.clear()
        self._lock.release()
        return self._count

    def decrement(self) -> int:
        self._lock.acquire()
        assert self._count > 0, "Pointer count cannot go below zero"
        self._count -= 1
        if self._count == 0:
            self._event.set()
        self._lock.release()
        return self._count

    async def wait(self) -> None:
        await self._event.wait()

    @property
    def count(self) -> int:
        with self._lock:
            return self._count


_P = ParamSpec("_P")
_R = TypeVar("_R")


async def to_thread(func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs) -> _R:
    """Asynchronously run a function in a separate thread.

    This is a copy of the function defined in the python source,
    which is only available in python >= 3.9.

    See: https://github.com/python/cpython/blob/main/Lib/asyncio/threads.py
    """
    if sys.version_info >= (3, 9):
        return await asyncio.to_thread(func, *args, **kwargs)
    loop = asyncio.events.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)  # type: ignore


def from_dm_from_extra(extra: Optional[Dict[str, Any]]) -> bool:
    """Used in modular filter components to get the 'fromDataManagement' value from an extra map."""
    if extra is None:
        return False

    return bool(extra["fromDataManagement"])

import asyncio
import contextvars
import functools
import sys
import threading
from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, SupportsBytes, SupportsFloat, Type, TypeVar, Union

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message
from google.protobuf.struct_pb2 import ListValue, Struct, Value
from google.protobuf.timestamp_pb2 import Timestamp

from viam.proto.app.data import CaptureInterval, Filter, TagsFilter
from viam.proto.common import Geometry, GeoPoint, GetGeometriesRequest, GetGeometriesResponse, Orientation, ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry
from viam.resource.types import Subtype, SupportsGetGeometries

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

SensorReading = Union[ValueTypes, Vector3, GeoPoint, Orientation]
"""Types that can be returned from a sensor"""


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
            True,
            True,
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


def sensor_readings_native_to_value(readings: Mapping[str, Any]) -> Mapping[str, Value]:
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


def sensor_readings_value_to_native(readings: Mapping[str, Value]) -> Mapping[str, SensorReading]:
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

    return bool(extra.get("fromDataManagement", False))


def create_filter(
    component_name: Optional[str] = None,
    component_type: Optional[str] = None,
    method: Optional[str] = None,
    robot_name: Optional[str] = None,
    robot_id: Optional[str] = None,
    part_name: Optional[str] = None,
    part_id: Optional[str] = None,
    location_ids: Optional[List[str]] = None,
    organization_ids: Optional[List[str]] = None,
    mime_type: Optional[List[str]] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    tags: Optional[List[str]] = None,
    bbox_labels: Optional[List[str]] = None,
    dataset_id: Optional[str] = None,
) -> Filter:
    """Create a `Filter`.

    Args:
        component_name (Optional[str]): Optional name of the component that captured the data being filtered (for example, "left_motor").
        component_type (Optional[str]): Optional type of the componenet that captured the data being filtered (for example, "motor").
        method (Optional[str]): Optional name of the method used to capture the data being filtered (for example, "IsPowered").
        robot_name (Optional[str]): Optional name of the robot associated with the data being filtered (for example, "viam_rover_1").
        robot_id (Optional[str]): Optional ID of the robot associated with the data being filtered.
        part_name (Optional[str]): Optional name of the system part associated with the data being filtered (for example,
            "viam_rover_1-main").
        part_id (Optional[str]): Optional ID of the system part associated with the data being filtered.
        location_ids (Optional[List[str]]): Optional list of location IDs associated with the data being filtered.
        organization_ids (Optional[List[str]]): Optional list of organization IDs associated with the data being filtered.
        mime_type (Optional[List[str]]): Optional mime type of data being filtered (for example, "image/png").
        start_time (Optional[datetime.datetime]): Optional start time of an interval to filter data by.
        end_time (Optional[datetime.datetime]): Optional end time of an interval to filter data by.
        tags (Optional[List[str]]): Optional list of tags attached to the data being filtered (for example, ["test"]).
        bbox_labels (Optional[List[str]]): Optional list of bounding box labels attached to the data being filtered (for example, ["square",
            "circle"]).
        dataset_id (Optional[str]): Optional ID of dataset associated with data being filtered

    Returns:
        viam.proto.app.data.Filter: The `Filter` object.
    """
    return Filter(
        component_name=component_name if component_name else "",
        component_type=component_type if component_type else "",
        method=method if method else "",
        robot_name=robot_name if robot_name else "",
        robot_id=robot_id if robot_id else "",
        part_name=part_name if part_name else "",
        part_id=part_id if part_id else "",
        location_ids=location_ids,
        organization_ids=organization_ids,
        mime_type=mime_type,
        interval=(
            CaptureInterval(
                start=datetime_to_timestamp(start_time),
                end=datetime_to_timestamp(end_time),
            )
        )
        if start_time or end_time
        else None,
        tags_filter=TagsFilter(tags=tags),
        bbox_labels=bbox_labels,
        dataset_id=dataset_id if dataset_id else "",
    )

import asyncio
import builtins
import numpy as np

import pytest
from google.protobuf.json_format import ParseError
from google.protobuf.struct_pb2 import ListValue, Struct, Value
from google.protobuf.timestamp_pb2 import Timestamp

from .mocks.services import MockMLModel

from viam.proto.common import ActuatorStatus, GeoPoint, Orientation, ResourceName, Vector3
from viam.utils import (
    PointerCounter,
    dict_to_struct,
    message_to_struct,
    primitive_to_value,
    sensor_readings_native_to_value,
    sensor_readings_value_to_native,
    struct_to_dict,
    struct_to_message,
    value_to_primitive,
    datetime_to_timestamp,
    flat_tensors_to_ndarrays,
    ndarrays_to_flat_tensors,
)


def test_primitive_to_value():
    v = None
    nv = primitive_to_value(v)
    assert nv == Value(null_value=v)

    v = "blink"
    nv = primitive_to_value(v)
    assert nv == Value(string_value=v)

    v = 182
    nv = primitive_to_value(v)
    assert nv == Value(number_value=v)

    v = False
    nv = primitive_to_value(v)
    assert nv == Value(bool_value=v)

    v = {"foo": "bar", "one": 1}
    nv = primitive_to_value(v)
    struct = Struct(
        fields={
            "foo": Value(string_value=v["foo"]),
            "one": Value(number_value=v["one"]),
        }
    )
    assert nv == Value(struct_value=struct)

    v = [1, "two", 3]
    nv = primitive_to_value(v)
    list_value = ListValue(
        values=[
            Value(number_value=1),
            Value(string_value="two"),
            Value(number_value=3),
        ]
    )
    assert nv == Value(list_value=list_value)

    v = b"viamtest"
    nv = primitive_to_value(v)
    assert nv == Value(string_value=v.decode())


def test_primitive_to_value_errors():
    # Only strings are allowed as keys
    v = {1: 2, 3: 4}
    with pytest.raises(TypeError):
        primitive_to_value(v)

    # Unsupported type
    class X:
        pass

    v = X()
    with pytest.raises(TypeError):
        primitive_to_value(v)  # type: ignore


def test_value_to_primitive():
    v = Value(null_value=None)
    prim = value_to_primitive(v)
    assert prim is None

    v = Value(string_value="blink")
    prim = value_to_primitive(v)
    assert prim == "blink"

    v = Value(number_value=182)
    prim = value_to_primitive(v)
    assert prim == 182

    v = Value(bool_value=False)
    prim = value_to_primitive(v)
    assert prim is False

    struct = Struct(
        fields={
            "foo": Value(string_value="bar"),
            "one": Value(number_value=1),
        }
    )
    v = Value(struct_value=struct)
    prim = value_to_primitive(v)
    assert prim == {"foo": "bar", "one": 1}

    list_value = ListValue(
        values=[
            Value(number_value=1),
            Value(string_value="two"),
            Value(number_value=3),
        ]
    )
    v = Value(list_value=list_value)
    prim = value_to_primitive(v)
    assert prim == [1, "two", 3]

    v = Value(string_value=b"viamtest".decode())
    prim = value_to_primitive(v)
    assert prim == b"viamtest".decode()


@pytest.mark.parametrize(
    "input,expected",
    [
        (ActuatorStatus(is_moving=False), Struct(fields={"is_moving": Value(bool_value=False)})),
        (ActuatorStatus(is_moving=True), Struct(fields={"is_moving": Value(bool_value=True)})),
        (
            Struct(
                fields={
                    "foo": Value(string_value="bar"),
                    "one": Value(number_value=1),
                }
            ),
            Struct(
                fields={
                    "foo": Value(string_value="bar"),
                    "one": Value(number_value=1),
                }
            ),
        ),
    ],
)
def test_message_to_struct(input, expected):
    assert message_to_struct(input) == expected


def test_message_to_struct_keys():
    status = ActuatorStatus(is_moving=True)
    struct = message_to_struct(status)
    key = list(struct.keys())[0]
    assert key == "is_moving"


@pytest.mark.parametrize(
    "input,msg_type,expected",
    [
        (message_to_struct(ActuatorStatus(is_moving=True)), ActuatorStatus, ActuatorStatus(is_moving=True)),
        (Struct(fields={"is_moving": Value(bool_value=True)}), ActuatorStatus, ActuatorStatus(is_moving=True)),
        (message_to_struct(ActuatorStatus(is_moving=False)), ActuatorStatus, ActuatorStatus(is_moving=False)),
        (Struct(fields={"is_moving": Value(bool_value=False)}), ActuatorStatus, ActuatorStatus(is_moving=False)),
        (Struct(fields={"isMoving": Value(bool_value=True)}), ActuatorStatus, ActuatorStatus(is_moving=True)),
        (Struct(fields={"isMoving": Value(bool_value=False)}), ActuatorStatus, ActuatorStatus(is_moving=False)),
        (
            Struct(
                fields={
                    "namespace": Value(string_value="rdk"),
                    "type": Value(string_value="component"),
                    "subtype": Value(string_value="arm"),
                    "name": Value(string_value="arm1"),
                }
            ),
            ResourceName,
            ResourceName(namespace="rdk", type="component", subtype="arm", name="arm1"),
        ),
    ],
)
def test_struct_to_message(input, msg_type, expected):
    assert struct_to_message(input, msg_type) == expected


def test_struct_to_message_error():
    struct = Struct(fields={"IsMoving": Value(bool_value=True)})
    with pytest.raises(ParseError):
        struct_to_message(struct, ActuatorStatus)


def test_dict_to_struct():
    expected = {"a": 1, "b": "2", "c": [3, 4, 5], "d": True, "e": {"1": 2, "3": "4", "5": [6, 7, 8], "9": False}}

    # Just testing that this doesn't error, since this calls ``primitive_to_value``
    _ = dict_to_struct(expected)

    # Unsupported type
    class X:
        pass

    expected["x"] = X()
    with pytest.raises(ValueError):
        _ = dict_to_struct(expected)


def test_struct_to_dict():
    expected = {"a": 1, "b": "2", "c": [3, 4, 5], "d": True, "e": {"1": 2, "3": "4", "5": [6, 7, 8], "9": False}}
    struct = dict_to_struct(expected)

    assert struct_to_dict(struct) == expected


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


def test_datetime_to_timestamp():
    expected = Timestamp(
        seconds=1686045600,
    )
    datetime = expected.ToDatetime()

    assert datetime_to_timestamp(datetime) == expected


def test_sensor_readings():
    expected = {
        "VEC3": Vector3(x=0.1, y=2.3, z=4.5),
        "POINT": GeoPoint(latitude=123.45, longitude=678.9),
        "ORIENTATION": Orientation(o_x=1, o_y=2, o_z=3, theta=4),
        "NATIVE": 1.23,
    }

    test = sensor_readings_native_to_value(expected)
    response = sensor_readings_value_to_native(test)

    assert response == expected


@pytest.mark.asyncio
async def test_pointer_counter():
    counter = PointerCounter()

    assert counter.count == 0

    counter.increment()
    assert counter.count == 1

    async def final_test():
        assert counter.count > 0
        await counter.wait()
        assert counter.count == 0

    task = asyncio.get_running_loop().create_task(final_test())

    await asyncio.sleep(0)  # Needed to start the final_test task

    counter.decrement()

    await task

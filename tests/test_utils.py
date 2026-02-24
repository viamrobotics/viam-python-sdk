import asyncio

import pytest
from google.protobuf.json_format import ParseError
from google.protobuf.struct_pb2 import ListValue, Struct, Value
from google.protobuf.timestamp_pb2 import Timestamp

from viam.proto.common import ActuatorStatus, GeoPoint, Orientation, ResourceName, Vector3
from viam.utils import (
    PointerCounter,
    datetime_to_timestamp,
    dict_to_struct,
    message_to_struct,
    primitive_to_value,
    sensor_readings_native_to_value,
    sensor_readings_value_to_native,
    struct_to_dict,
    struct_to_message,
    value_to_primitive,
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


class TestLooseApprox:
    """Tests that loose_approx uses absolute tolerance (50ms), not relative."""

    def test_within_tolerance(self):
        from . import loose_approx

        assert 1.82 == loose_approx(1.82)
        assert 1.84 == loose_approx(1.82)
        assert 1.80 == loose_approx(1.82)

    def test_outside_tolerance(self):
        from . import loose_approx

        assert 1.82 + 0.06 != loose_approx(1.82)
        assert 1.82 - 0.06 != loose_approx(1.82)

    def test_absolute_not_relative(self):
        """A small value and a large value should have the same absolute tolerance."""
        from . import loose_approx

        # For a small value like 0.001, a relative tolerance of 1% would be 0.00001.
        # With absolute tolerance of 50ms, 0.001 + 0.04 should still match.
        assert 0.041 == loose_approx(0.001)

        # For a large value like 100, a relative tolerance of 1% would be 1.0.
        # With absolute tolerance of 50ms, 100 + 0.06 should NOT match.
        assert 100.06 != loose_approx(100)

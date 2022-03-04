from google.protobuf.struct_pb2 import Struct, ListValue, Value
import pytest

from viam.utils import primitive_to_value, value_to_primitive


def test_primitive_to_value():
    v = None
    nv = primitive_to_value(v)
    assert nv == Value(null_value=v)

    v = 'blink'
    nv = primitive_to_value(v)
    assert nv == Value(string_value=v)

    v = 182
    nv = primitive_to_value(v)
    assert nv == Value(number_value=v)

    v = False
    nv = primitive_to_value(v)
    assert nv == Value(bool_value=v)

    v = {'foo': 'bar', 'one': 1}
    nv = primitive_to_value(v)
    struct = Struct(fields={
        'foo': Value(string_value=v['foo']),
        'one': Value(number_value=v['one']),
    })
    assert nv == Value(struct_value=struct)

    v = [1, 'two', 3]
    nv = primitive_to_value(v)
    list_value = ListValue(values=[
        Value(number_value=1),
        Value(string_value='two'),
        Value(number_value=3),
    ])
    assert nv == Value(list_value=list_value)

    v = b'viamtest'
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
        primitive_to_value(v)


def test_value_to_primitive():
    v = Value(null_value=None)
    prim = value_to_primitive(v)
    assert prim is None

    v = Value(string_value='blink')
    prim = value_to_primitive(v)
    assert prim == 'blink'

    v = Value(number_value=182)
    prim = value_to_primitive(v)
    assert prim == 182

    v = Value(bool_value=False)
    prim = value_to_primitive(v)
    assert prim is False

    struct = Struct(fields={
        'foo': Value(string_value='bar'),
        'one': Value(number_value=1),
    })
    v = Value(struct_value=struct)
    prim = value_to_primitive(v)
    assert prim == {'foo': 'bar', 'one': 1}

    list_value = ListValue(values=[
        Value(number_value=1),
        Value(string_value='two'),
        Value(number_value=3),
    ])
    v = Value(list_value=list_value)
    prim = value_to_primitive(v)
    assert prim == [1, 'two', 3]

    v = Value(string_value=b'viamtest'.decode())
    prim = value_to_primitive(v)
    assert prim == b'viamtest'.decode()

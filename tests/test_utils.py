from google.protobuf.struct_pb2 import Struct, ListValue, Value
import pytest

from viam.utils import new_value


def test_new_value():
    v = None
    nv = new_value(v)
    assert nv == Value(null_value=v)

    v = 'blink'
    nv = new_value(v)
    assert nv == Value(string_value=v)

    v = 182
    nv = new_value(v)
    assert nv == Value(number_value=v)

    v = False
    nv = new_value(v)
    assert nv == Value(bool_value=v)

    v = {'foo': 'bar', 'one': 1}
    nv = new_value(v)
    struct = Struct(fields={
        'foo': Value(string_value=v['foo']),
        'one': Value(number_value=v['one']),
    })
    assert nv == Value(struct_value=struct)

    v = [1, 'two', 3]
    nv = new_value(v)
    list_value = ListValue(values=[
        Value(number_value=1),
        Value(string_value='two'),
        Value(number_value=3),
    ])
    assert nv == Value(list_value=list_value)

    v = b'viamtest'
    nv = new_value(v)
    assert nv == Value(string_value=v.decode())


def test_new_value_errors():
    # Only strings are allowed as keys
    v = {1: 2, 3: 4}
    with pytest.raises(TypeError):
        new_value(v)

    # Unsupported type
    class X:
        pass
    v = X()
    with pytest.raises(TypeError):
        new_value(v)

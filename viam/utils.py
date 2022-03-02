from typing import Any, List, SupportsFloat, Dict
from google.protobuf.struct_pb2 import Struct, Value, ListValue


def new_value(v: Any) -> Value:
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
        v (Any): object to convert to a Value

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
        for (key, value) in v.items():
            if not isinstance(key, str):
                raise TypeError(f'Invalid UTF-8 in string: {key}')
            sv[key] = new_value(value)
        struct = Struct(fields=sv)
        return Value(struct_value=struct)
    if isinstance(v, List):
        lv = []
        for vv in v:
            lv.append(new_value(vv))
        list_value = ListValue(values=lv)
        return Value(list_value=list_value)
    if isinstance(v, (bytes, bytearray)):
        return Value(string_value=v.decode())
    raise TypeError(f'Invalid type {type(v)}')

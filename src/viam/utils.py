from typing import Any, Dict, List, SupportsFloat

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message
from google.protobuf.struct_pb2 import ListValue, Struct, Value

from viam.components.component_base import ComponentBase
from viam.proto.api.common import ResourceName
from viam.registry import Registry


def primitive_to_value(v: Any) -> Value:
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
    raise TypeError(f'Invalid type {type(v)}')


def value_to_primitive(value: Value) -> Any:
    if value.HasField('list_value'):
        return [value_to_primitive(v) for v in value.list_value.values]
    if value.HasField('struct_value'):
        return {k: value_to_primitive(v)
                for (k, v) in value.struct_value.fields.items()}
    if value.HasField('string_value'):
        return value.string_value
    if value.HasField('number_value'):
        return value.number_value
    if value.HasField('bool_value'):
        return value.bool_value
    if value.HasField('null_value'):
        return value.null_value
    return None


def resource_names_for_component(
    component: ComponentBase
) -> List[ResourceName]:
    rns: List[ResourceName] = []
    for klass in component.__class__.mro():
        component_type = ''
        for registration in Registry.REGISTERED_COMPONENTS.values():
            if klass is registration.component_type:
                component_type = registration.name

        if not component_type:
            class_name = str(klass)
            if 'viam.components' not in class_name:
                continue
            if 'ComponentBase' in class_name:
                continue

            component_type = class_name \
                .split('viam.components.')[1] \
                .split('.')[0]

        rns.append(ResourceName(
            namespace='rdk',
            type='component',
            subtype=component_type,
            name=component.name
        ))
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


def struct_to_message(struct: Struct, message: Message) -> Message:
    dct = struct_to_dict(struct)
    return ParseDict(dct, message)


def dict_to_struct(obj: Dict[str, Any]) -> Struct:
    struct = Struct()
    struct.update(obj)
    return struct


def struct_to_dict(struct: Struct) -> Dict[str, Any]:
    return {key: value_to_primitive(value) for (key, value) in struct.fields.items()}

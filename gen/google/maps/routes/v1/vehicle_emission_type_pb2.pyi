"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _VehicleEmissionType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _VehicleEmissionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_VehicleEmissionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    VEHICLE_EMISSION_TYPE_UNSPECIFIED: VehicleEmissionType.ValueType = ...  # 0
    """No emission type specified. Default to GASOLINE."""

    GASOLINE: VehicleEmissionType.ValueType = ...  # 1
    """Gasoline/petrol fueled vehicle."""

    ELECTRIC: VehicleEmissionType.ValueType = ...  # 2
    """Electricity powered vehicle."""

    HYBRID: VehicleEmissionType.ValueType = ...  # 3
    """Hybrid fuel (such as gasoline + electric) vehicle."""

class VehicleEmissionType(_VehicleEmissionType, metaclass=_VehicleEmissionTypeEnumTypeWrapper):
    """A set of values describing the vehicle's emission type.
    Applies only to the DRIVE travel mode.
    """
    pass

VEHICLE_EMISSION_TYPE_UNSPECIFIED: VehicleEmissionType.ValueType = ...  # 0
"""No emission type specified. Default to GASOLINE."""

GASOLINE: VehicleEmissionType.ValueType = ...  # 1
"""Gasoline/petrol fueled vehicle."""

ELECTRIC: VehicleEmissionType.ValueType = ...  # 2
"""Electricity powered vehicle."""

HYBRID: VehicleEmissionType.ValueType = ...  # 3
"""Hybrid fuel (such as gasoline + electric) vehicle."""

global___VehicleEmissionType = VehicleEmissionType


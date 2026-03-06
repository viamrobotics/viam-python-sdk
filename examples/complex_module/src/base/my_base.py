from typing import Any, ClassVar, Mapping, Dict, List, Optional, cast, Sequence, Tuple

from typing_extensions import Self

from viam.components.base import Base
from viam.components.motor import Motor
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.resource.base import ResourceBase
from viam.proto.common import Geometry, Vector3, ResourceName
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily
from viam.utils import struct_to_dict


class MyBase(Base, Reconfigurable):
    """
    MyBase implements a base that only supports set_power (basic forward/back/turn controls), is_moving (check if in motion), and stop (stop
    all motion).

    It inherits from the built-in resource subtype Base and conforms to the ``Reconfigurable`` protocol, which signifies that this component
    can be reconfigured. Additionally, it specifies a constructor function ``MyBase.new`` which conforms to the
    ``resource.types.ResourceCreator`` type required for all models. It also specifies a validator function `MyBase.validate_config` which
    conforms to the ``resource.types.Validator`` type and returns implicit dependencies for the model.
    """

    # Subclass the Viam Base component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "base"), "mybase")

    def __init__(self, name: str):
        super().__init__(name)

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        base = cls(config.name)
        base.reconfigure(config, dependencies)
        return base

    # Validates JSON Configuration
    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Tuple[Sequence[str], Sequence[str]]:
        attributes_dict = struct_to_dict(config.attributes)
        left_name = attributes_dict.get("left", "")
        assert isinstance(left_name, str)
        if left_name == "":
            raise Exception("A left attribute is required for a MyBase component.")

        right_name = attributes_dict.get("right", "")
        assert isinstance(right_name, str)
        if right_name == "":
            raise Exception("A right attribute is required for a MyBase component.")
        return [left_name, right_name], []

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        attributes_dict = struct_to_dict(config.attributes)
        left_name = attributes_dict.get("left")
        right_name = attributes_dict.get("right")

        assert isinstance(left_name, str) and isinstance(right_name, str)

        left_motor = dependencies[Motor.get_resource_name(left_name)]
        right_motor = dependencies[Motor.get_resource_name(right_name)]

        self.left = cast(Motor, left_motor)
        self.right = cast(Motor, right_motor)

    # Not implemented
    async def move_straight(
        self,
        distance: int,
        velocity: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        raise NotImplementedError()

    # Not implemented
    async def spin(
        self,
        angle: float,
        velocity: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        raise NotImplementedError()

    # Set the linear and angular velocity of the left and right motors on the base
    async def set_power(
        self,
        linear: Vector3,
        angular: Vector3,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        # stop the base if absolute value of linear and angular velocity is less than 0.01
        if abs(linear.y) < 0.01 and abs(angular.z) < 0.01:
            await self.stop(extra=extra, timeout=timeout)
            return

        # use linear and angular velocity to calculate percentage of max power to pass to SetPower for left & right motors
        sum = abs(linear.y) + abs(angular.z)

        await self.left.set_power(power=((linear.y - angular.z) / sum), extra=extra, timeout=timeout)
        await self.right.set_power(power=((linear.y + angular.z) / sum), extra=extra, timeout=timeout)

    # Not implemented
    async def set_velocity(
        self,
        linear: Vector3,
        angular: Vector3,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        raise NotImplementedError()

    # Stop the base from moving by stopping both motors
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        await self.left.stop(extra=extra, timeout=timeout)
        await self.right.stop(extra=extra, timeout=timeout)

    # Check if either motor on the base is moving with motors' is_moving
    async def is_moving(self) -> bool:
        return await self.left.is_moving() or await self.right.is_moving()

    # Not implemented
    async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Base.Properties:
        raise NotImplementedError()

    # Not implemented
    async def get_geometries(self) -> List[Geometry]:
        raise NotImplementedError()


Registry.register_resource_creator(Base.API, MyBase.MODEL, ResourceCreatorRegistration(MyBase.new, MyBase.validate_config))

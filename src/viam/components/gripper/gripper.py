import abc
from dataclasses import dataclass
from typing import Any, Dict, Final, Optional, Tuple

from viam.components.component_base import ComponentBase
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT

from . import KinematicsFileFormat


class Gripper(ComponentBase):
    """
    Gripper represents a physical robotic gripper.

    This acts as an abstract base class for any drivers representing specific
    gripper implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.gripper import Gripper

    For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gripper"
    )

    @dataclass
    class HoldingStatus:
        """
        HoldingStatus represents whether the gripper is currently holding onto an object. The
        additional ``meta`` attribute contains other optional contextual information (i.e. confidence
        interval, pressure, etc.)
        """

        is_holding_something: bool
        meta: Optional[Dict[str, Any]] = None

    @abc.abstractmethod
    async def open(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Open the gripper.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Open the gripper.
            await my_gripper.open()

        For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/#open>`_.
        """
        ...

    @abc.abstractmethod
    async def grab(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bool:
        """
        Instruct the gripper to grab.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Grab with the gripper.
            grabbed = await my_gripper.grab()

        Returns:
            bool: Indicates if the gripper grabbed something.

        For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/#grab>`_.
        """
        ...

    @abc.abstractmethod
    async def is_holding_something(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> HoldingStatus:
        """
        Get information about whether the gripper is currently holding onto an object.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Grab with the gripper.
            holding_status = await my_gripper.is_holding_something()
            # get the boolean result
            is_holding_something = holding_status.is_holding_something

        Returns:
            HoldingStatus: see documentation on `HoldingStatus` for more information

        For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/#grab>`_.

        """

    @abc.abstractmethod
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop the gripper. It is assumed the gripper stops immediately.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Stop the gripper.
            await my_gripper.stop()

        For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/#stop>`_.
        """
        ...

    @abc.abstractmethod
    async def is_moving(self) -> bool:
        """
        Get if the gripper is currently moving.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Check whether the gripper is currently moving.
            moving = await my_gripper.is_moving()
            print('Moving:', moving)

        Returns:
            bool: Whether the gripper is moving.

        For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/#is_moving>`_.
        """
        ...

    @abc.abstractmethod
    async def get_kinematics(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        """
        Get the kinematics information associated with the gripper.

        ::

            my_gripper = Gripper.from_robot(robot=machine, name="my_gripper")

            # Get the kinematics information associated with the gripper.
            kinematics = await my_gripper.get_kinematics()

            # Get the format of the kinematics file.
            k_file = kinematics[0]

            # Get the byte contents of the file.
            k_bytes = kinematics[1]

        Returns:
            Tuple[KinematicsFileFormat.ValueType, bytes]: A tuple containing two values; the first [0] value represents the format of the
            file, either in URDF format (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_URDF``) or
            Viam's kinematic parameter format (spatial vector algebra) (``KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA``),
            and the second [1] value represents the byte contents of the file.

        For more information, see `Gripper component <https://docs.viam.com/dev/reference/apis/components/gripper/#getkinematics>`_.
        """
        ...

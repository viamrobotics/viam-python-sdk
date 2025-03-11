import abc
from typing import Any, Final, Mapping, Optional

from viam.components.component_base import ComponentBase
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT


class Switch(ComponentBase):
    """
    Switch represents a device with two or more finite states (or positions) than can be set and retrieved.

    This acts as an abstract base class for any drivers representing specific
    switch implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.switch import Switch

    For more information, see `Switch component <https://docs.viam.com/dev/reference/apis/components/switch/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "switch"
    )

    @abc.abstractmethod
    async def get_position(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        """
        Get the current position of the switch

        ::

            my_switch = Switch.from_robot(robot=machine, name="my_switch")

            # Update the switch from its current position to the desired position of 1.
            await my_switch.set_position(1)

            # Get the current set position of the switch.
            pos1 = await my_switch.get_position()

            # Update the switch from its current position to the desired position.
            await my_switch.set_position(0)

            # Get the current set position of the switch.
            pos2 = await my_switch.get_position()

        Returns:
            int: The current position of the switch within the range of available positions.

        For more information, see `Switch component <https://docs.viam.com/dev/reference/apis/components/Switch/#getposition>`_.
        """
        ...

    @abc.abstractmethod
    async def set_position(
        self, position: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> None:
        """
        Sets the current position of the switch.

        ::

            my_switch = Switch.from_robot(robot=machine, name="my_switch")

            # Update the switch from its current position to the desired position of 1.
            await my_switch.set_position(1)

            # Update the switch from its current position to the desired position of 0.
            await my_switch.set_position(0)

        Args:
            position (int): The position of the switch within the range of available positions.

        For more information, see `Switch component <https://docs.viam.com/dev/reference/apis/components/switch/#setposition>`_.
        """
        ...

    @abc.abstractmethod
    async def get_number_of_positions(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> int:
        """
        Get the number of available positions on the switch.

        ::

            my_switch = Switch.from_robot(robot=machine, name="my_switch")

            print(await my_switch.get_number_of_positions())

        Returns:
            int: The number of available positions.

        For more information, see `Switch component <https://docs.viam.com/dev/reference/apis/components/switch/#getnumberofpositions>`_.
        """
        ...

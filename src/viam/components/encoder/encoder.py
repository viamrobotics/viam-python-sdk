import abc
from dataclasses import dataclass
from typing import Any, Dict, Final, Optional, Tuple

from viam.proto.component.encoder import PositionType
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

from ..component_base import ComponentBase


class Encoder(ComponentBase):
    @dataclass
    class Properties:
        ticks_count_supported: bool
        angle_degrees_supported: bool

    """
    Encoder represents a physical encoder.

    This acts as an abstract base class for any drivers representing specific
    encoder implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.encoder import Encoder

    For more information, see `Encoder component <https://docs.viam.com/components/encoder/>`_.
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "encoder"
    )

    @abc.abstractmethod
    async def reset_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Set the current position to be the new zero (home) position.

        ::

            my_encoder = Encoder.from_robot(robot=robot, name='my_encoder')

            # Reset the zero position of the encoder.
            await my_encoder.reset_position()


        For more information, see `Encoder component <https://docs.viam.com/components/encoder/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_position(
        self,
        position_type: Optional[PositionType.ValueType] = None,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[float, PositionType.ValueType]:
        """
        Report the position of the encoder.
        The value returned is the current position in terms of it's ``position_type``.
        The position will be either in relative units (ticks away from a zero position) for
        ``PositionType.POSITION_TYPE_TICKS_COUNT`` or absolute units (degrees along a circle)
        for ``PositionType.POSITION_TYPE_ANGLE_DEGREES``.

        ::

            my_encoder = Encoder.from_robot(robot=robot, name='my_encoder')

            # Get the position of the encoder in ticks
            position = await my_encoder.get_position(PositionType.POSITION_TYPE_TICKS_COUNT)
            print("The encoder position is currently ", position[0], position[1])

        Args:
            position_type (PositionType): The desired output type of the position.

        Returns:
            Tuple[float, PositionType]:
            A tuple containing two values; the first [0] the position of the encoder which can either be
            ticks since last zeroing for a relative encoder or degrees for an absolute encoder, and the second [1] the type of
            position the encoder returns (ticks or degrees).

        For more information, see `Encoder component <https://docs.viam.com/components/encoder/>`_.
        """
        ...

    @abc.abstractmethod
    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Properties:
        """
        Return a dictionary of the types of position reporting this encoder supports.

        ::

            my_encoder = Encoder.from_robot(robot=robot, name='my_encoder')

            # Get whether the encoder returns position in ticks or degrees.
            properties = await my_encoder.get_properties()

        Returns:
            Encoder.Properties: Map of position types to supported status.

        For more information, see `Encoder component <https://docs.viam.com/components/encoder/>`_.
        """
        ...

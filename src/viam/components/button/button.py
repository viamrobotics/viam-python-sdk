import abc
from typing import Any, Final, Mapping, Optional

from viam.components.component_base import ComponentBase
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT


class Button(ComponentBase):
    """
    Button represents a device that can be pushed.

    This acts as an abstract base class for any drivers representing specific
    button implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    ::

        from viam.components.button import Button

    For more information, see `Button component <https://docs.viam.com/dev/reference/apis/components/button/>` _.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "button"
    )

    @abc.abstractmethod
    async def push(self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> None:
        """
        Push the button.

        ::

            my_button = Button.from_robot(robot=machine, name="my_button")

            # Push the button
            await my_button.push()

        For more information, see `Button component <https://docs.viam.com/dev/reference/apis/components/button/>` _.
        """
        ...

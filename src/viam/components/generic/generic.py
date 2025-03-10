from typing import Final

from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT

from ..component_base import ComponentBase


class Generic(ComponentBase):
    """
    Generic component, which represents any type of component that can executes arbitrary commands

    This acts as an abstract base class for any drivers representing generic components.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.

    To create a Generic component (an arbitrary component that can process commands), this ``Generic`` component should be subclassed
    and the ``do_command`` function implemented.

    ::

        from viam.components.generic import Generic

    Example::

        class ComplexComponent(Generic):

            async def do_command(
                self,
                command: Mapping[str, ValueTypes],
                *,
                timeout: Optional[float] = None,
                **kwargs
            ) -> Mapping[str, ValueTypes]:
                result = {key: False for key in command.keys()}
                for (name, args) in command.items():
                    if name == 'on':
                        self.on(*args)
                        result[name] = True
                    if name == 'set_frequency':
                        self.set_frequency(*args)
                        result[name] = True
                    if name == 'get_frequency':
                        result[name] = self.frequency
                    if name == 'complex_command':
                        self.complex_command(*args)
                        result[name] = True
                return result

            def set_frequency(self, frequency: int):
                self.frequency = frequency

            def on(self, frequency: int, duration: int):
                self.frequency = frequency
                self.power = 1
                task = threading.Timer(duration, self.off)
                task.start()

            def off(self):
                self.power = 0

            def complex_command(self, arg1, arg2, arg3):
                ...

    To execute commands, simply call the ``do_command`` function with the appropriate parameters.
    ::

        await component.do_command({'on': [300, 10]})
        component.power  # 1
        await asyncio.sleep(10)
        component.power  # 0

    For more information, see `Gantry component <https://docs.viam.com/dev/reference/apis/components/generic/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "generic"
    )

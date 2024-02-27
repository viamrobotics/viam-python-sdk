from typing import Final

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype

from ..service_base import ServiceBase


class Generic(ServiceBase):
    """
    Generic service, which represents any type of service that can execute arbitrary commands

    This acts as an abstract base class for any drivers representing generic services.
    This cannot be used on its own. If the ``__init__()`` function is overridden, it must call the ``super().__init__()`` function.

    To create a Generic service (an arbitrary service that can process commands), this ``Generic`` service should be subclassed
    and the ``do_command`` function implemented.

    Example::

        class ComplexService(Generic):

            async def do_command(
                self,
                command: Mapping[str, ValueTypes],
                *,
                timeout: Optional[float] = None,
                **kwargs
            ) -> Mapping[str, ValueTypes]:
                result = {key: False for key in command.keys()}
                for (name, args) in command.items():
                    if name == 'set_val':
                        self.set_val(*args)
                        result[name] = True
                    if name == 'get_val':
                        result[name] = self.val
                    if name == 'complex_command':
                        self.complex_command(*args)
                        result[name] = True
                return result

            def set_val(self, val: int):
                self.val = val

            def complex_command(self, arg1, arg2, arg3):
                ...

    To execute commands, simply call the ``do_command`` function with the appropriate parameters.
    ::

        await service.do_command({'set_val': 10})
        service.val  # 10
        await service.do_command({'set_val': 5})
        service.val  # 5
    """

    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "generic"
    )

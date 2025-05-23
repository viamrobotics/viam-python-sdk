import inspect
import re
from abc import ABCMeta
from typing import Callable, ClassVar, Mapping, Sequence, Tuple, Union

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName

from .. import logging
from ..errors import MethodNotImplementedError
from .base import ResourceBase
from .registry import Registry, ResourceCreatorRegistration
from .types import API, Model, ModelFamily

modelRegex = re.compile(r"^([^:]+):([^:]+):([^:]+)$")

logger = logging.getLogger(__name__)


def _parse_model(orig: Union[str, Model]) -> Model:
    "take a model or string and turn it into a Model"
    if isinstance(orig, Model):
        return orig
    match = modelRegex.match(orig)
    if not match:
        raise ValueError(f"MODEL {orig} doesn't match expected format 'org:type:name'")
    *family, name = match.groups()
    return Model(ModelFamily(*family), name)


def _create_stub_fn(name: str, is_async: bool) -> Callable:
    """
    This creates a sync or async stub function which returns a MethodNotImplementedError.
    The stub_model decorator uses these to stub out an abstract base class.
    """
    if is_async:
        # note: this is a pyright bug https://github.com/microsoft/pyright/issues/2136
        async def stub_fn(*args, **kwargs):  # pyright: ignore [reportRedeclaration]
            logger.info(f"{name} not implemented")
            raise MethodNotImplementedError(name)

    else:

        def stub_fn(*args, **kwargs):
            logger.info(f"{name} not implemented")
            raise MethodNotImplementedError(name)

    stub_fn.__name__ = f"{name}_stub"
    return stub_fn


def stub_model(cls: ABCMeta) -> ABCMeta:
    """
    Class decorator which adds error implementations of abstract functions. This means they will fail
    when called, rather than the default where they fail when instantiated. This is intended for developers
    who want to build and test incrementally, not for production use.

    Example:

        @stub_model
        class MyMotor(Motor, EasyResource):
            MODEL = 'viam:motor:easy-resource-example'

    Normally this class would fail to instantiate. With the decorator, it will succeed but the unimplemented
    methods will throw errors at runtime.
    """
    for attr in list(cls.__abstractmethods__):
        val = getattr(cls, attr)
        is_async = inspect.iscoroutinefunction(val)
        stub_fn = _create_stub_fn(attr, is_async)
        setattr(cls, attr, stub_fn)
        logger.debug("patched %s.%s with %s", cls, attr, stub_fn)
        cls.__abstractmethods__ -= {attr}
    return cls


class EasyResource:
    """
    EasyResource is a mixin that simplifies the process of creating Viam modules (extension programs)
    and resources (the resource classes provided by those extension programs).

    Basic usage:

    ::

        class MyModel(Sensor, EasyResource):
            MODEL = "my-org:sensor:my-sensor"

            async def get_readings(self, **kwargs):
                return {"ok": True}

    See examples/easy_resource/main.py for extended usage.
    """

    API: ClassVar[API]
    MODEL: ClassVar[Model]

    def __init_subclass__(cls, register=True, **kwargs):
        """
        When you subclass this mixin, it parses cls.MODEL and registers cls in global registry.
        """
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "MODEL"):
            raise ValueError("Please define a MODEL with the format 'org:type:name' on your class, for example 'viam:camera:IMX219'")
        cls.MODEL = _parse_model(cls.MODEL)
        if register:
            cls.register()

    def __init__(self, name: str):
        # note: this mirrors the constructor for ComponentBase and ServiceBase.
        self.name = name

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        """
        This is passed to register_resource_creator; the default implementation calls reconfigure()
        when an instance of your model is instantiated. You can override this in your subclass.
        """
        self = cls(config.name)
        logger.debug("created %s %s %s", cls.API, cls.MODEL, config.name)
        self.reconfigure(config, dependencies)
        return self

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Tuple[Sequence[str], Sequence[str]]:
        """This method allows you to validate the configuration object received from the machine,
        as well as to return any implicit dependencies based on that `config`.

        Args:
            config (ComponentConfig): The configuration for this resource

        Returns:
            Tuple[Sequence[str], Sequence[str]]: One list of required implicit dependencies and one of optional deps.
        """
        return [], []

    @classmethod
    def register(cls):
        """
        This adds the model to the global registry. It is called by __init_subclass__ and you typically
        won't call it directly.
        """
        logger.debug("registering %s %s", cls.API, cls.MODEL)
        # note: We could fix this pyright-ignore if EasyResource inherited ResourceBase, but that crashes in the mro()
        # walk in ResourceManager.register.
        Registry.register_resource_creator(
            cls.API,
            cls.MODEL,
            ResourceCreatorRegistration(cls.new, cls.validate_config),  # pyright: ignore [reportArgumentType]
        )

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        logger.debug("reconfigure %s %s", self.API, self.MODEL)

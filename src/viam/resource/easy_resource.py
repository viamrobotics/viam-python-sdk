import re
from typing import Mapping, Union

from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName

from .. import logging
from .base import ResourceBase
from .types import Model, ModelFamily, Subtype
from .registry import Registry, ResourceCreatorRegistration

modelRegex = re.compile(r"^([^:]+):([^:]+):([^:]+)$")

logger = logging.getLogger(__name__)

def parse_model(orig: Union[str, Model]) -> Model:
    "take a model or string and turn it into a Model"
    if isinstance(orig, Model):
        return orig
    match = modelRegex.match(orig)
    if not match:
        raise ValueError(f"MODEL {orig} doesn't match expected format 'org:type:name'")
    *family, name = match.groups()
    return Model(ModelFamily(*family), name)

class EasyResource:
    """
    EasyResource is a mixin that ...
    See ...
    """
    SUBTYPE: Subtype
    MODEL: Model

    def __init_subclass__(cls, register=True, **kwargs):
        """
        When you subclass this mixin, it parses cls.MODEL and registers cls in global registry.
        """
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "MODEL"):
            raise ValueError("please define a MODEL like 'org:type:name' on your class, for example 'viam:camera:IMX219'")
        cls.MODEL = parse_model(cls.MODEL)
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
        logger.debug("created %s %s %s", self.SUBTYPE, self.MODEL, config.name)
        self.reconfigure(config, dependencies)
        return self

    @classmethod
    def register(cls):
        """
        This adds the model to the global registry. It is called by __init_subclass__ and you typically
        won't call it directly.
        """
        logger.debug('registering %s %s', cls.SUBTYPE, cls.MODEL)
        Registry.register_resource_creator(cls.SUBTYPE, cls.MODEL, ResourceCreatorRegistration(cls.new))

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        logger.debug('reconfigure %s %s', self.SUBTYPE, self.MODEL)

import abc

from typing import Dict, Final, Optional
from viam.proto.service.mlmodel import Metadata
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.utils import ValueTypes

from ..service_base import ServiceBase


class MLModel(ServiceBase):
    """
    MLModel represents a Machine Learning Model service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "slam")

    @abc.abstractmethod
    async def infer(self, input_data: Dict[str, ValueTypes], *, timeout: Optional[float]) -> Dict[str, ValueTypes]:
        ...

    @abc.abstractmethod
    async def metadata(self, *, timeout: Optional[float]) -> Metadata:
        ...

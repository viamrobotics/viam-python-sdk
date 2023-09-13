import abc
from typing import Dict, Final, Optional
from viam.proto.service.mlmodel import Metadata
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, Subtype
from viam.utils import _numpy_import_error_string

from ..service_base import ServiceBase

try:
    from numpy.typing import NDArray
except ImportError:
    import warnings

    warnings.warn(_numpy_import_error_string)  # will want to replace the e.g. suggestion with a link to docs when that is available
    raise


class MLModel(ServiceBase):
    """
    MLModel represents a Machine Learning Model service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.
    """

    SUBTYPE: Final = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "mlmodel")

    @abc.abstractmethod
    async def infer(self, input_tensors: Dict[str, NDArray], *, timeout: Optional[float]) -> Dict[str, NDArray]:
        """Take an already ordered input tensor as an array, make an inference on the model, and return an output tensor map.

        Args:
            input_tensors (Dict[str, NDArray]): A dictionary of input flat tensors as specified in the metadata

        Returns:
            Dict[str, NDArray]: A dictionary of output flat tensors as specified in the metadata
        """
        ...

    @abc.abstractmethod
    async def metadata(self, *, timeout: Optional[float]) -> Metadata:
        """Get the metadata (such as name, type, expected tensor/array shape, inputs, and outputs) associated with the ML model.

        Returns:
            Metadata: The metadata
        """
        ...

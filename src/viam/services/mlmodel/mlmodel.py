import abc
from typing import Dict, Final, Mapping, Optional

from numpy.typing import NDArray

from viam.proto.service.mlmodel import Metadata
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE
from viam.utils import ValueTypes

from ..service_base import ServiceBase


class MLModel(ServiceBase):
    """
    MLModel represents a Machine Learning Model service.

    This acts as an abstract base class for any drivers representing specific
    arm implementations. This cannot be used on its own. If the ``__init__()`` function is
    overridden, it must call the ``super().__init__()`` function.

    For more information, see `ML model service <https://docs.viam.com/dev/reference/apis/services/ml/>`_.
    """

    API: Final = API(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_SERVICE, "mlmodel"
    )

    @abc.abstractmethod
    async def infer(
        self,
        input_tensors: Dict[str, NDArray],
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> Dict[str, NDArray]:
        """Take an already ordered input tensor as an array, make an inference on the model, and return an output tensor map.

        ::

            import numpy as np

            my_mlmodel = MLModelClient.from_robot(robot=machine, name="my_mlmodel_service")

            image_data = np.zeros((1, 384, 384, 3), dtype=np.uint8)

            # Create the input tensors dictionary
            input_tensors = {
                "image": image_data
            }

            output_tensors = await my_mlmodel.infer(input_tensors)

        Args:
            input_tensors (Dict[str, NDArray]): A dictionary of input flat tensors as specified in the metadata

        Returns:
            Dict[str, NDArray]: A dictionary of output flat tensors as specified in the metadata

        For more information, see `ML model service <https://docs.viam.com/dev/reference/apis/services/ml/#infer>`_.
        """
        ...

    @abc.abstractmethod
    async def metadata(self, *, extra: Optional[Mapping[str, ValueTypes]] = None, timeout: Optional[float] = None) -> Metadata:
        """Get the metadata (such as name, type, expected tensor/array shape, inputs, and outputs) associated with the ML model.

        ::

            my_mlmodel = MLModelClient.from_robot(robot=machine, name="my_mlmodel_service")

            metadata = await my_mlmodel.metadata()

        Returns:
            Metadata: The metadata

        For more information, see `ML model service <https://docs.viam.com/dev/reference/apis/services/ml/#metadata>`_.
        """
        ...

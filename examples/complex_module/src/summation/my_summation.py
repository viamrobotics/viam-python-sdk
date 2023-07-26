from typing import ClassVar, Mapping, Sequence

from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model

from ..summation.api import SummationService


class MySummationService(SummationService, Reconfigurable):
    """This is the specific implementation of a ``SummationService`` (defined in api.py)

    It inherits from SummationService, as well as conforms to the ``Reconfigurable`` protocol, which signifies that this component can be
    reconfigured. It also specifies a function ``MySummationService.new``, which conforms to the ``resource.types.ResourceCreator`` type,
    which is required for all models.
    """

    MODEL: ClassVar[Model] = Model.from_string("acme:demo:mysum")
    subtract: bool

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        summer = cls(config.name)
        summer.subtract = config.attributes.fields["subtract"].bool_value or False
        return summer

    async def sum(self, nums: Sequence[float]) -> float:
        if len(nums) <= 0:
            raise ValueError("Must provided at least one number to sum")

        result = 0
        for num in nums:
            if self.subtract:
                result -= num
            else:
                result += num
        return result

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.subtract = config.attributes.fields["subtract"].bool_value or False

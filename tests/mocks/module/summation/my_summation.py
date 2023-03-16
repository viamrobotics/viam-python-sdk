from typing import ClassVar, Mapping, Sequence

from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model

from ..summation.api import SummationService


class MySummationService(SummationService, Reconfigurable):
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

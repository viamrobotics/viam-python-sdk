from typing import Protocol, List
from typing_extensions import Self

from viam.components.component_base import ComponentBase


class ModularComponent(Protocol):
    def new(self, dependencies: List[ComponentBase]) -> Self:
        ...

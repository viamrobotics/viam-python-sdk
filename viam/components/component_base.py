import abc
from typing import cast
from typing_extensions import Self

from viam.proto.api.common import ResourceName
from viam.robot.client import RobotClient


class ComponentBase(abc.ABC):
    """
    Base component.
    All components must inherit from this class.
    """

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def get_resource_name(cls, name: str) -> ResourceName:
        """
        Get the ResourceName for this component type with the given name

        Args:
            name (str): The name of the Component
        """
        for klass in cls.mro():
            class_name = str(klass)
            if 'viam.components' not in class_name:
                continue
            if 'ComponentBase' in class_name:
                continue

            subtype = class_name \
                .split('viam.components.')[1] \
                .split('.')[0]

            return ResourceName(
                namespace='rdk',
                type='component',
                subtype=subtype,
                name=name
            )

        # Getting here should be impossible!
        raise TypeError(
            f'Unable to create a ResourceName for {cls} named {name}.' +
            'This should not be possible. Please file an issue.'
        )

    @classmethod
    def from_robot(cls, robot: RobotClient, name: str) -> Self:
        component = robot.get_component_by_name(cls.get_resource_name(name))
        return cast(cls, component)

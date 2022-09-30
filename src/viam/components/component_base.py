import abc
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast

from typing_extensions import Self

from viam.operations import Operation
from viam.proto.common import ResourceName

if TYPE_CHECKING:
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
            if "viam.components" not in class_name:
                continue
            if "ComponentBase" in class_name:
                continue

            subtype = class_name.split("viam.components.")[1].split(".")[0]

            return ResourceName(namespace="rdk", type="component", subtype=subtype, name=name)

        # Getting here should be impossible!
        raise TypeError(f"Unable to create a ResourceName for {cls} named {name}." + "This should not be possible. Please file an issue.")

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the component named `name` from the provided robot.

        Args:
            robot (RobotClient): The robot
            name (str): The name of the component

        Returns:
            Self: The component, if it exists on the robot
        """
        component = robot.get_component(cls.get_resource_name(name))
        return cast(cls, component)

    def get_operation(self, kwargs: Mapping[str, Any]) -> Operation:
        """Get the `Operation` associated with the currently running function.

        When writing custom components, you should get the `Operation` by calling this function and check to see if it's cancelled.
        If the `Operation` is cancelled, then you can perform any necessary (terminating long running tasks, cleaning up connections, etc.).

        Args:
            kwargs (Mapping[str, Any]): The kwargs object containing the operation

        Returns:
            Operation: The operation associated with this function
        """
        return kwargs.get(Operation.ARG_NAME, Operation._noop())

    async def do_command(self, command: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Send/Receive arbitrary commands

        Args:
            command (Dict[str, Any]): The command to execute

        Raises:
            NotImplementedError: Raised if the component does not support arbitrary commands

        Returns:
            Dict[str, Any]: Result of the executed command
        """
        raise NotImplementedError()

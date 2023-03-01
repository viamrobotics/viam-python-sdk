import abc
from typing import TYPE_CHECKING, Any, SupportsBytes, ClassVar, Dict, SupportsFloat, SupportsInt, List, Mapping, Optional, Union, cast

from typing_extensions import Self

from viam.operations import Operation
from viam.proto.common import ResourceName
from viam.resource.types import Subtype

if TYPE_CHECKING:
    from viam.robot.client import RobotClient

DoCommandTypes = Union[bool, SupportsBytes, SupportsFloat, SupportsInt, List, Mapping, str, None]


class ComponentBase(abc.ABC):
    """
    Base component.
    All components must inherit from this class.
    """

    SUBTYPE: ClassVar[Subtype]

    name: str

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def get_resource_name(cls, name: str) -> ResourceName:
        """
        Get the ResourceName for this component type with the given name

        Args:
            name (str): The name of the Component
        """
        return ResourceName(
            namespace=cls.SUBTYPE.namespace,
            type=cls.SUBTYPE.resource_type,
            subtype=cls.SUBTYPE.resource_subtype,
            name=name,
        )

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the component named ``name`` from the provided robot.

        Args:
            robot (RobotClient): The robot
            name (str): The name of the component

        Returns:
            Self: The component, if it exists on the robot
        """
        component = robot.get_component(cls.get_resource_name(name))
        return cast(cls, component)

    def get_operation(self, kwargs: Mapping[str, Any]) -> Operation:
        """Get the ``Operation`` associated with the currently running function.

        When writing custom components, you should get the ``Operation`` by calling this function and check to see if it's cancelled.
        If the ``Operation`` is cancelled, then you can perform any necessary (terminating long running tasks, cleaning up connections, etc.
        ).

        Args:
            kwargs (Mapping[str, Any]): The kwargs object containing the operation

        Returns:
            Operation: The operation associated with this function
        """
        return kwargs.get(Operation.ARG_NAME, Operation._noop())

    async def do_command(
        self, command: Dict[str, DoCommandTypes], *, timeout: Optional[float] = None, **kwargs
    ) -> Dict[str, DoCommandTypes]:
        """Send/Receive arbitrary commands

        Args:
            command (Dict[str, Any]): The command to execute

        Raises:
            NotImplementedError: Raised if the component does not support arbitrary commands

        Returns:
            Dict[str, Any]: Result of the executed command
        """
        raise NotImplementedError()

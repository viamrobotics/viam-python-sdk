import abc
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    List,
    Mapping,
    Optional,
    SupportsBytes,
    SupportsFloat,
    Union,
    cast,
)

from typing_extensions import Self

from viam.operations import Operation
from viam.resource.types import ResourceBase

if TYPE_CHECKING:
    from viam.resource.types import Subtype
    from viam.robot.client import RobotClient


ValueTypes = Union[bool, SupportsBytes, SupportsFloat, List, Mapping, str, None]


class ComponentBase(abc.ABC, ResourceBase):
    """
    Base component.
    All components must inherit from this class.
    """

    SUBTYPE: ClassVar["Subtype"]

    def __init__(self, name: str):
        self.name = name

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

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        raise NotImplementedError()

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, ClassVar, Mapping, Optional, Protocol, runtime_checkable

from typing_extensions import Self

from viam.operations import Operation
from viam.proto.common import ResourceName

from .types import Subtype

if TYPE_CHECKING:
    from viam.robot.client import RobotClient
    from viam.utils import ValueTypes


@runtime_checkable
class ResourceBase(Protocol):
    """
    The base requirements for a Resource.
    """

    SUBTYPE: ClassVar["Subtype"]
    """The Subtype of the Resource"""

    name: str
    """The name of the Resource"""

    @classmethod
    def get_resource_name(cls, name: str) -> ResourceName:
        """
        Get the ResourceName for this Resource with the given name

        ::

            # Can be used with any resource, using an arm as an example
            my_arm_name = my_arm.get_resource_name("my_arm")

        Args:
            name (str): The name of the Resource

        Returns:
            ResourceName: The ResourceName of this Resource
        """
        return ResourceName(
            namespace=cls.SUBTYPE.namespace,
            type=cls.SUBTYPE.resource_type,
            subtype=cls.SUBTYPE.resource_subtype,
            name=name,
        )

    @classmethod
    @abstractmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the Resource named ``name`` from the provided robot.

        ::

            # Can be used with any resource, using an arm as an example
            my_arm = Arm.from_robot(robot, "my_arm")

        Args:
            robot (RobotClient): The robot
            name (str): The name of the Resource

        Returns:
            Self: The Resource, if it exists on the robot
        """
        ...

    @abstractmethod
    async def do_command(
        self, command: Mapping[str, "ValueTypes"], *, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, "ValueTypes"]:
        """Send/Receive arbitrary commands to the Resource

        ::

            command = {"cmd": "test", "data1": 500}
            result = component.do(command)

        Args:
            command (Mapping[str, ValueTypes]): The command to execute

        Raises:
            NotImplementedError: Raised if the Resource does not support arbitrary commands

        Returns:
            Mapping[str, ValueTypes]: Result of the executed command
        """
        ...

    def get_operation(self, kwargs: Mapping[str, Any]) -> Operation:
        """Get the ``Operation`` associated with the currently running function.

        When writing custom resources, you should get the ``Operation`` by calling this function and check to see if it's cancelled.
        If the ``Operation`` is cancelled, then you can perform any necessary (terminating long running tasks, cleaning up connections, etc.
        ).

        Args:
            kwargs (Mapping[str, Any]): The kwargs object containing the operation

        Returns:
            viam.operations.Operation: The operation associated with this function
        """
        return kwargs.get(Operation.ARG_NAME, Operation._noop())

    async def close(self):
        """Safely shut down the resource and prevent further use.

        Close must be idempotent. Later configuration may allow a resource to be "open" again.
        If a resource does not want or need a close function, it is assumed that the resource does not need to return errors when future
        non-Close methods are called.

        ::

            await component.close()

        """
        return

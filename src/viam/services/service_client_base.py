import abc
from typing import Any, ClassVar, Dict, Optional, TYPE_CHECKING
from typing_extensions import Self
from grpclib.client import Channel
from viam.errors import ServiceNotImplementedError
from viam.proto.common import ResourceName


if TYPE_CHECKING:
    from viam.robot.client import RobotClient


class ServiceClientBase(abc.ABC):
    """
    Base service client.
    All service clients must inherit from this class.
    """

    SERVICE_TYPE: ClassVar[str]

    def __init__(self, name: str, channel: Channel):
        self.name = name
        self.channel = channel

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str = "builtin") -> Self:
        """Get the service client named ``name`` from the provided robot.

        Args:
            robot (RobotClient): The robot
            name (str): The name of the service client

        Returns:
            Self: The service client, if it exists on the robot
        """
        resource_name = ResourceName(namespace="rdk", type="service", subtype=cls.SERVICE_TYPE, name=name)
        if resource_name not in robot.resource_names:
            raise ServiceNotImplementedError(resource_name.subtype, resource_name.name)
        return cls(name, robot._channel)

    def do_command(self, command: Dict[str, Any], *, timeout: Optional[float] = None, **kwargs) -> Dict[str, Any]:
        """Send/Receive arbitrary commands

        Args:
            command (Dict[str, Any]): The command to execute

        Raises:
            NotImplementedError: Raised if the component does not support arbitrary commands

        Returns:
            Dict[str, Any]: Result of the executed command
        """
        raise NotImplementedError()

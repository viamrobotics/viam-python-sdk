import abc
from typing import TYPE_CHECKING, ClassVar, Mapping, Optional

from grpclib.client import Channel
from typing_extensions import Self

from viam.errors import ResourceNotFoundError
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase, Subtype
from viam.utils import ValueTypes

if TYPE_CHECKING:
    from viam.robot.client import RobotClient


class ServiceClientBase(abc.ABC, ResourceBase):
    """
    Base service client.
    All service clients must inherit from this class.
    """

    SUBTYPE: ClassVar[Subtype]
    channel: Channel

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
        resource_name = ResourceName(namespace="rdk", type="service", subtype=cls.SUBTYPE.resource_subtype, name=name)
        if resource_name not in robot.resource_names:
            raise ResourceNotFoundError(resource_name.subtype, resource_name.name)
        return cls(name, robot._channel)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        raise NotImplementedError()

from typing import TYPE_CHECKING, Mapping, Optional, Protocol, Self, cast

from viam.resource.types import ResourceBase
from viam.utils import ValueTypes

if TYPE_CHECKING:
    from viam.robot.client import RobotClient


class ServiceBase(ResourceBase, Protocol):
    """This class describes the base functionality required for a Viam Service.
    All services must inherit from this class.
    """

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the service named ``name`` from the provided robot.

        Args:
            robot (RobotClient): The robot
            name (str): The name of the service

        Returns:
            Self: The service, if it exists on the robot
        """
        service = robot.get_service(cls.get_resource_name(name))
        return cast(cls, service)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        raise NotImplementedError()

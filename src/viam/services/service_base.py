import abc
from typing import TYPE_CHECKING, ClassVar, Mapping, Optional, cast

from typing_extensions import Self

from viam.resource.base import ResourceBase
from viam.utils import ValueTypes

if TYPE_CHECKING:
    from viam.resource.types import Subtype
    from viam.robot.client import RobotClient


class ServiceBase(abc.ABC, ResourceBase):
    """This class describes the base functionality required for a Viam Service.
    All services must inherit from this class.
    """

    SUBTYPE: ClassVar["Subtype"]

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def from_robot(cls, robot: "RobotClient", name: str) -> Self:
        """Get the service named ``name`` from the provided robot.

        ::

            async def connect() -> RobotClient:
                # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
                options = RobotClient.Options.with_api_key("<API-KEY>", "<API-KEY-ID>")
                # Replace "<MACHINE-URL>" (included brackets) with your machine's connection URL or FQDN
                return await RobotClient.at_address("<MACHINE-URL>", options)

            async def main():
                robot = await connect()

                # Can be used with any resource, using the motion service as an example
                motion = MotionClient.from_robot(robot=robot, name="builtin")

                robot.close()

        Args:
            robot (RobotClient): The robot
            name (str): The name of the service

        Returns:
            Self: The service, if it exists on the robot
        """
        service = robot.get_service(cls.get_resource_name(name))
        return cast(cls, service)

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        """Send/receive arbitrary commands.

        ::

            service = SERVICE.from_robot(robot, "builtin")  # replace SERVICE with the appropriate class

            my_command = {
              "cmnd": "dosomething",
              "someparameter": 52
            }

            # Can be used with any resource, using the motion service as an example
            await service.do_command(command=my_command)

        Args:
            command (Dict[str, ValueTypes]): The command to execute

        Returns:
            Dict[str, ValueTypes]: Result of the executed command
        """
        raise NotImplementedError()

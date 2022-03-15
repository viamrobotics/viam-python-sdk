from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.robot import (DoActionRequest, DoActionResponse,
                                  ResourceRunCommandRequest,
                                  ResourceRunCommandResponse, RobotServiceBase)


class RobotService(RobotServiceBase, ComponentServiceBase):

    async def DoAction(
        self,
        stream: Stream[DoActionRequest, DoActionResponse]
    ) -> None:
        pass

    async def ResourceRunCommand(
        self,
        stream: Stream[ResourceRunCommandRequest, ResourceRunCommandResponse]
    ) -> None:
        pass

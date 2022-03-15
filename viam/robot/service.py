from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.robot import (ConfigRequest, ConfigResponse,
                                  DoActionRequest, DoActionResponse,
                                  ExecuteFunctionRequest,
                                  ExecuteFunctionResponse,
                                  ExecuteSourceRequest, ExecuteSourceResponse,
                                  ResourceRunCommandRequest,
                                  ResourceRunCommandResponse, RobotServiceBase)


class RobotService(RobotServiceBase, ComponentServiceBase):

    async def Config(
        self,
        stream: Stream[ConfigRequest, ConfigResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        response = ConfigResponse()
        await stream.send_message(response)

    async def DoAction(
        self,
        stream: Stream[DoActionRequest, DoActionResponse]
    ) -> None:
        pass

    async def ExecuteFunction(
        self,
        stream: Stream[ExecuteFunctionRequest, ExecuteFunctionResponse]
    ) -> None:
        pass

    async def ExecuteSource(
        self,
        stream: Stream[ExecuteSourceRequest, ExecuteSourceResponse]
    ) -> None:
        pass

    async def ResourceRunCommand(
        self,
        stream: Stream[ResourceRunCommandRequest, ResourceRunCommandResponse]
    ) -> None:
        pass

from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.robot import (BlockForOperationRequest,
                                  BlockForOperationResponse,
                                  CancelOperationRequest,
                                  CancelOperationResponse,
                                  GetOperationsRequest, GetOperationsResponse,
                                  ResourceRunCommandRequest,
                                  ResourceRunCommandResponse, RobotServiceBase)


class RobotService(RobotServiceBase, ComponentServiceBase):

    async def ResourceRunCommand(self, stream: Stream[ResourceRunCommandRequest, ResourceRunCommandResponse]) -> None:
        pass

    async def GetOperations(self, stream: Stream[GetOperationsRequest, GetOperationsResponse]) -> None:
        pass

    async def CancelOperation(self, stream: Stream[CancelOperationRequest, CancelOperationResponse]) -> None:
        pass

    async def BlockForOperation(self, stream: Stream[BlockForOperationRequest, BlockForOperationResponse]) -> None:
        pass

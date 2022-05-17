from typing import List

from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.common import ResourceName
from viam.proto.api.robot import (BlockForOperationRequest,
                                  BlockForOperationResponse,
                                  CancelOperationRequest,
                                  CancelOperationResponse,
                                  GetOperationsRequest, GetOperationsResponse,
                                  ResourceNamesRequest, ResourceNamesResponse,
                                  RobotServiceBase)
from viam.utils import resource_names_for_component


class RobotService(RobotServiceBase, ComponentServiceBase):

    def _generate_metadata(self) -> List[ResourceName]:
        md: List[ResourceName] = [
            ResourceName(
                namespace='rdk',
                type='service',
                subtype='status',
            ),
        ]

        for component in self.manager.components.values():
            md.extend(resource_names_for_component(component))

        return md

    async def ResourceNames(self, stream: Stream[ResourceNamesRequest, ResourceNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        metadata = self._generate_metadata()
        response = ResourceNamesResponse(resources=metadata)
        await stream.send_message(response)

    async def GetOperations(self, stream: Stream[GetOperationsRequest, GetOperationsResponse]) -> None:
        pass

    async def CancelOperation(self, stream: Stream[CancelOperationRequest, CancelOperationResponse]) -> None:
        pass

    async def BlockForOperation(self, stream: Stream[BlockForOperationRequest, BlockForOperationResponse]) -> None:
        pass

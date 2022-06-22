import asyncio
from typing import Iterable, List

from grpclib.server import Stream
from grpclib import GRPCError, Status as GRPCStatus
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.common import ResourceName
from viam.proto.api.robot import (BlockForOperationRequest,
                                  BlockForOperationResponse,
                                  CancelOperationRequest,
                                  CancelOperationResponse,
                                  DiscoverComponentsRequest,
                                  DiscoverComponentsResponse,
                                  FrameSystemConfigRequest,
                                  FrameSystemConfigResponse,
                                  GetOperationsRequest, GetOperationsResponse,
                                  GetStatusRequest, GetStatusResponse,
                                  ResourceNamesRequest, ResourceNamesResponse,
                                  ResourceRPCSubtypesRequest, ResourceRPCSubtypesResponse,
                                  RobotServiceBase, Status,
                                  StreamStatusRequest, StreamStatusResponse,
                                  TransformPoseRequest, TransformPoseResponse)
from viam.registry import Registry
from viam.utils import resource_names_for_component


class RobotService(RobotServiceBase, ComponentServiceBase):

    def _generate_metadata(self) -> List[ResourceName]:
        md: List[ResourceName] = []

        for component in self.manager.components.values():
            md.extend(resource_names_for_component(component))

        return md

    async def _generate_status(
        self,
        resource_names: Iterable[ResourceName]
    ) -> List[Status]:
        statuses: List[Status] = []

        for component in self.manager.components.values():
            for registration in Registry.REGISTERED_COMPONENTS.values():
                if isinstance(component, registration.component_type):
                    status = await registration.create_status(component)
                    statuses.append(status)

        if resource_names:
            statuses = [s for s in statuses if s.name in resource_names]
        return statuses

    async def ResourceNames(self, stream: Stream[ResourceNamesRequest, ResourceNamesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        metadata = self._generate_metadata()
        response = ResourceNamesResponse(resources=metadata)
        await stream.send_message(response)

    async def GetStatus(self, stream: Stream[GetStatusRequest, GetStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        status = await self._generate_status(request.resource_names)
        response = GetStatusResponse(status=status)
        await stream.send_message(response)

    async def StreamStatus(self, stream: Stream[StreamStatusRequest, StreamStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        interval = 1
        every = request.every.ToSeconds()
        if every > 0:
            interval = every
        while True:
            status = await self._generate_status(request.resource_names)
            response = StreamStatusResponse(status=status)
            await stream.send_message(response)
            await asyncio.sleep(interval)

    async def GetOperations(self, stream: Stream[GetOperationsRequest, GetOperationsResponse]) -> None:
        pass

    async def ResourceRPCSubtypes(self, stream: Stream[ResourceRPCSubtypesRequest, ResourceRPCSubtypesResponse]) -> None:
        raise GRPCError(
            GRPCStatus.UNIMPLEMENTED,
            "Method ResourceRPCSubtypes not implemented."
        )

    async def CancelOperation(self, stream: Stream[CancelOperationRequest, CancelOperationResponse]) -> None:
        raise GRPCError(
            GRPCStatus.UNIMPLEMENTED,
            "Method CancelOperation not implemented."
        )

    async def BlockForOperation(self, stream: Stream[BlockForOperationRequest, BlockForOperationResponse]) -> None:
        raise GRPCError(
            GRPCStatus.UNIMPLEMENTED,
            "Method BlockForOperation not implemented."
        )

    async def FrameSystemConfig(self, stream: Stream[FrameSystemConfigRequest, FrameSystemConfigResponse]) -> None:
        raise GRPCError(
            GRPCStatus.UNIMPLEMENTED,
            "Method FrameSystemConfig not implemented."
        )

    async def TransformPose(self, stream: Stream[TransformPoseRequest, TransformPoseResponse]) -> None:
        raise GRPCError(
            GRPCStatus.UNIMPLEMENTED,
            "Method TransformPose not implemented."
        )

    async def DiscoverComponents(self, stream: Stream[DiscoverComponentsRequest, DiscoverComponentsResponse]) -> None:
        raise GRPCError(
            GRPCStatus.UNIMPLEMENTED,
            "Method DiscoverComponents not implemented."
        )

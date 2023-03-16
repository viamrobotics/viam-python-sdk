import asyncio
from typing import Any, Dict, Iterable, List

from grpclib.server import Stream

from viam import logging
from viam.errors import MethodNotImplementedError, ViamGRPCError
from viam.proto.common import ResourceName
from viam.proto.robot import (
    BlockForOperationRequest,
    BlockForOperationResponse,
    CancelOperationRequest,
    CancelOperationResponse,
    DiscoverComponentsRequest,
    DiscoverComponentsResponse,
    FrameSystemConfigRequest,
    FrameSystemConfigResponse,
    GetOperationsRequest,
    GetOperationsResponse,
    GetSessionsRequest,
    GetSessionsResponse,
    GetStatusRequest,
    GetStatusResponse,
    ResourceNamesRequest,
    ResourceNamesResponse,
    ResourceRPCSubtypesRequest,
    ResourceRPCSubtypesResponse,
    RobotServiceBase,
    SendSessionHeartbeatRequest,
    SendSessionHeartbeatResponse,
    StartSessionRequest,
    StartSessionResponse,
    Status,
    StopAllRequest,
    StopAllResponse,
    StreamStatusRequest,
    StreamStatusResponse,
    TransformPCDRequest,
    TransformPCDResponse,
    TransformPoseRequest,
    TransformPoseResponse,
)
from viam.resource.registry import Registry
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import resource_names_for_resource, struct_to_dict

LOGGER = logging.getLogger(__name__)


class RobotService(RobotServiceBase, ResourceRPCServiceBase):
    def _generate_metadata(self) -> List[ResourceName]:
        md: List[ResourceName] = []

        for component in self.manager.resources.values():
            md.extend(resource_names_for_resource(component))

        return md

    async def _generate_status(self, resource_names: Iterable[ResourceName]) -> List[Status]:
        statuses: List[Status] = []

        for component in self.manager.resources.values():
            for registration in Registry.REGISTERED_SUBTYPES().values():
                if isinstance(component, registration.resource_type):
                    if resource_names and component.get_resource_name(component.name) not in resource_names:
                        continue
                    try:
                        status = await registration.create_status(component)
                        statuses.append(status)
                    except ViamGRPCError as e:
                        raise e.grpc_error

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
        raise MethodNotImplementedError("GetOperations").grpc_error

    async def ResourceRPCSubtypes(self, stream: Stream[ResourceRPCSubtypesRequest, ResourceRPCSubtypesResponse]) -> None:
        raise MethodNotImplementedError("ResourceRPCSubtypes").grpc_error

    async def CancelOperation(self, stream: Stream[CancelOperationRequest, CancelOperationResponse]) -> None:
        raise MethodNotImplementedError("CancelOperation").grpc_error

    async def BlockForOperation(self, stream: Stream[BlockForOperationRequest, BlockForOperationResponse]) -> None:
        raise MethodNotImplementedError("BlockForOperation").grpc_error

    async def FrameSystemConfig(self, stream: Stream[FrameSystemConfigRequest, FrameSystemConfigResponse]) -> None:
        raise MethodNotImplementedError("FrameSystemConfig").grpc_error

    async def TransformPose(self, stream: Stream[TransformPoseRequest, TransformPoseResponse]) -> None:
        raise MethodNotImplementedError("TransformPose").grpc_error

    async def DiscoverComponents(self, stream: Stream[DiscoverComponentsRequest, DiscoverComponentsResponse]) -> None:
        raise MethodNotImplementedError("DiscoverComponents").grpc_error

    async def StopAll(self, stream: Stream[StopAllRequest, StopAllResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None

        extra: Dict[ResourceName, Dict[str, Any]] = {}
        for ex in request.extra:
            extra[ex.name] = struct_to_dict(ex.params)

        errors: List[str] = []
        for component in self.manager.resources.values():
            if callable(getattr(component, "stop", None)):
                try:
                    rn = component.get_resource_name(component.name)
                    if rn in extra:
                        try:
                            await component.stop(extra=extra[rn])  # type: ignore
                        except TypeError:
                            await component.stop()  # type: ignore
                    else:
                        await component.stop()  # type: ignore
                except Exception:
                    LOGGER.exception(f"Failed to stop component named {component.name}")
                    errors.append(component.name)

        if errors:
            raise ViamGRPCError(f'Failed to stop components named {", ".join(errors)}')
        await stream.send_message(StopAllResponse())

    async def GetSessions(self, stream: Stream[GetSessionsRequest, GetSessionsResponse]) -> None:
        raise MethodNotImplementedError("GetSessions").grpc_error

    async def StartSession(self, stream: Stream[StartSessionRequest, StartSessionResponse]) -> None:
        raise MethodNotImplementedError("StartSession").grpc_error

    async def SendSessionHeartbeat(self, stream: Stream[SendSessionHeartbeatRequest, SendSessionHeartbeatResponse]) -> None:
        raise MethodNotImplementedError("SendSessionHeartbeat").grpc_error

    async def TransformPCD(self, stream: Stream[TransformPCDRequest, TransformPCDResponse]) -> None:
        raise MethodNotImplementedError("TransformPCD").grpc_error

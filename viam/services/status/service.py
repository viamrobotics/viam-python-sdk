import asyncio
from typing import Iterable, List

from google.protobuf.struct_pb2 import Struct
from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.proto.api.common import ResourceName
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           Status, StatusServiceBase,
                                           StreamStatusRequest,
                                           StreamStatusResponse)
from viam.registry import Registry


class StatusService(StatusServiceBase, ComponentServiceBase):

    async def _generate_status(
        self,
        resource_names: Iterable[ResourceName]
    ) -> List[Status]:
        statuses: List[Status] = [
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='service',
                    subtype='robot',
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='service',
                    subtype='status',
                ),
                status=Struct()
            ),
        ]

        for component in self.manager.components.values():
            for registration in Registry.REGISTERED_COMPONENTS.values():
                if isinstance(component, registration.component_type):
                    status = await registration.create_status(component)
                    statuses.append(status)

        if resource_names:
            statuses = [s for s in statuses if s.name in resource_names]
        return statuses

    async def GetStatus(
        self,
        stream: Stream[GetStatusRequest, GetStatusResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        status = await self._generate_status(request.resource_names)
        response = GetStatusResponse(status=status)
        await stream.send_message(response)

    async def StreamStatus(
        self,
        stream: Stream[StreamStatusRequest, StreamStatusResponse]
    ) -> None:
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

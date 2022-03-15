import asyncio
from typing import List

from google.protobuf.struct_pb2 import Struct
from grpclib.server import Stream
from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.motor import Motor
from viam.components.sensor import Sensor
from viam.components.service_base import ComponentServiceBase
from viam.components.servo import Servo
from viam.proto.api.component.arm import Status as ArmStatus
from viam.proto.api.component.motor import Status as MotorStatus
from viam.proto.api.component.servo import Status as ServoStatus
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           Status, StatusServiceBase,
                                           StreamStatusRequest,
                                           StreamStatusResponse)
from viam.utils import message_to_struct, resource_name_for_component_type


class StatusService(StatusServiceBase, ComponentServiceBase):

    async def _generate_status(self) -> List[Status]:
        statuses: List[Status] = []

        for component in self.manager.components.values():
            if isinstance(component, Arm):
                end_position = await component.get_end_position()
                joint_positions = await component.get_joint_positions()
                s = ArmStatus(
                    end_position=end_position,
                    joint_positions=joint_positions
                )
                as_struct = message_to_struct(s)
                status = Status(
                    name=resource_name_for_component_type(component, Arm),
                    status=as_struct
                )
                statuses.append(status)
            if isinstance(component, Base):
                status = Status(
                    name=resource_name_for_component_type(component, Base),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Motor):
                s = MotorStatus()
                s.is_on = await component.is_powered()
                s.position = await component.get_position()
                features = await component.get_features()
                s.position_reporting = features['position_reporting']
                as_struct = message_to_struct(s)
                status = Status(
                    name=resource_name_for_component_type(component, Motor),
                    status=as_struct
                )
                statuses.append(status)
            if isinstance(component, Sensor):
                status = Status(
                    name=resource_name_for_component_type(component, Sensor),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Servo):
                s = ServoStatus()
                s.position_deg = await component.get_position()
                as_struct = message_to_struct(s)
                status = Status(
                    name=resource_name_for_component_type(component, Servo),
                    status=as_struct
                )
                statuses.append(status)

        return statuses

    async def GetStatus(
        self,
        stream: Stream[GetStatusRequest, GetStatusResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        status = await self._generate_status()
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
            status = await self._generate_status()
            response = StreamStatusResponse(status=status)
            await stream.send_message(response)
            await asyncio.sleep(interval)

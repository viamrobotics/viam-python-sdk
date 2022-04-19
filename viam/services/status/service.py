import asyncio
from typing import Iterable, List

from google.protobuf.struct_pb2 import Struct
from grpclib.server import Stream
from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.board import Board
from viam.components.camera import Camera
from viam.components.gantry import Gantry
from viam.components.gps import GPS
from viam.components.gripper import Gripper
from viam.components.imu import IMU
from viam.components.motor import Motor
from viam.components.pose_tracker import PoseTracker
from viam.components.sensor import Sensor
from viam.components.service_base import ComponentServiceBase
from viam.components.servo import Servo
from viam.proto.api.common import ResourceName
from viam.proto.api.component.arm import Status as ArmStatus
from viam.proto.api.component.gantry import Status as GantryStatus
from viam.proto.api.component.motor import Status as MotorStatus
from viam.proto.api.component.servo import Status as ServoStatus
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           Status, StatusServiceBase,
                                           StreamStatusRequest,
                                           StreamStatusResponse)
from viam.utils import message_to_struct


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
                    subtype='metadata',
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
            if isinstance(component, Arm):
                end_position = await component.get_end_position()
                joint_positions = await component.get_joint_positions()
                s = ArmStatus(
                    end_position=end_position,
                    joint_positions=joint_positions
                )
                as_struct = message_to_struct(s)
                status = Status(
                    name=Arm.get_resource_name(component.name),
                    status=as_struct
                )
                statuses.append(status)
            if isinstance(component, Base):
                status = Status(
                    name=Base.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Board):
                status = Status(
                    name=Board.get_resource_name(component.name),
                    status=message_to_struct(await component.status())
                )
                statuses.append(status)
            if isinstance(component, Camera):
                status = Status(
                    name=Camera.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Gantry):
                s = GantryStatus(
                    positions_mm=await component.get_position(),
                    lengths_mm=await component.get_lengths()
                )
                as_struct = message_to_struct(s)
                status = Status(
                    name=Gantry.get_resource_name(component.name),
                    status=as_struct
                )
                statuses.append(status)
            if isinstance(component, GPS):
                status = Status(
                    name=GPS.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Gripper):
                status = Status(
                    name=Gripper.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, IMU):
                status = Status(
                    name=IMU.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Motor):
                s = MotorStatus()
                s.is_on = await component.is_powered()
                s.position = await component.get_position()
                features = await component.get_features()
                s.position_reporting = features.position_reporting
                as_struct = message_to_struct(s)
                status = Status(
                    name=Motor.get_resource_name(component.name),
                    status=as_struct
                )
                statuses.append(status)
            if isinstance(component, PoseTracker):
                status = Status(
                    name=PoseTracker.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Sensor):
                status = Status(
                    name=Sensor.get_resource_name(component.name),
                    status=Struct()
                )
                statuses.append(status)
            if isinstance(component, Servo):
                s = ServoStatus()
                s.position_deg = await component.get_position()
                as_struct = message_to_struct(s)
                status = Status(
                    name=Servo.get_resource_name(component.name),
                    status=as_struct
                )
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

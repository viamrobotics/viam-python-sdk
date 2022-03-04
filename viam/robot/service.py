import asyncio
from typing import Dict

from grpclib.server import Stream
from viam.components.arm import Arm
from viam.components.base import Base
from viam.components.motor import Motor
from viam.components.sensor import Sensor
from viam.components.service_base import ComponentServiceBase
from viam.components.servo import Servo
from viam.proto.api.robot import (ArmStatus, ConfigRequest, ConfigResponse,
                                  DoActionRequest, DoActionResponse,
                                  ExecuteFunctionRequest,
                                  ExecuteFunctionResponse,
                                  ExecuteSourceRequest, ExecuteSourceResponse,
                                  JointPositions, MotorStatus, Pose,
                                  ResourceRunCommandRequest,
                                  ResourceRunCommandResponse, RobotServiceBase,
                                  SensorStatus, ServoStatus, Status,
                                  StatusRequest, StatusResponse,
                                  StatusStreamRequest, StatusStreamResponse)


class RobotService(RobotServiceBase, ComponentServiceBase):

    async def _generate_status(self) -> Status:
        arm_statuses: Dict[str, ArmStatus] = {}
        base_statuses: Dict[str, bool] = {}
        motor_statuses: Dict[str, MotorStatus] = {}
        sensor_statuses: Dict[str, SensorStatus] = {}
        servo_statuses: Dict[str, ServoStatus] = {}

        for component in self.manager.components.values():
            if isinstance(component, Arm):
                grid_position = await component.get_end_position()
                gp = Pose(
                    x=grid_position.x,
                    y=grid_position.y,
                    z=grid_position.z,
                    o_x=grid_position.o_x,
                    o_y=grid_position.o_y,
                    o_z=grid_position.o_z,
                    theta=grid_position.theta
                )
                joint_positions = await component.get_joint_positions()
                jp = JointPositions(degrees=joint_positions.degrees)
                s = ArmStatus(
                    grid_position=gp,
                    joint_positions=jp
                )
                arm_statuses[component.name] = s
            if isinstance(component, Base):
                base_statuses[component.name] = True
            if isinstance(component, Motor):
                s = MotorStatus()
                s.on = await component.is_powered()
                s.position = await component.get_position()
                features = await component.get_features()
                s.position_supported = features['position_reporting']
                motor_statuses[component.name] = s
            if isinstance(component, Sensor):
                s = SensorStatus()
                s.type = 'sensor'
                sensor_statuses[component.name] = s
            if isinstance(component, Servo):
                s = ServoStatus()
                s.angle = await component.get_position()
                servo_statuses[component.name] = s

        return Status(
            bases=base_statuses,
            motors=motor_statuses,
            servos=servo_statuses,
        )

    async def Status(
        self,
        stream: Stream[StatusRequest, StatusResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        status = await self._generate_status()
        response = StatusResponse(status=status)
        await stream.send_message(response)

    async def StatusStream(
        self,
        stream: Stream[StatusStreamRequest, StatusStreamResponse]
    ) -> None:
        request = stream.recv_message()
        assert request is not None
        interval = 1  # seconds
        while True:
            status = await self._generate_status()
            response = StatusStreamResponse(status=status)
            await stream.send_message(response)
            await asyncio.sleep(interval)

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

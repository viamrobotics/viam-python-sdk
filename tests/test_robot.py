import pytest
from grpclib.testing import ChannelFor

from viam.components.resource_manager import ResourceManager
from viam.proto.api.robot import (
    RobotServiceStub,
    Status,
    MotorStatus, ServoStatus,
    StatusRequest,
    StatusResponse
)
from viam.robot.service import RobotService

from .mocks.components import MockIMU, MockMotor, MockServo


@pytest.mark.asyncio
async def test_robot_service():
    resources = [
        MockIMU(name='imu1'),
        MockIMU(name='imu2'),
        MockMotor(name='motor1'),
        MockMotor(name='motor2'),
        MockServo(name='servo1'),
        MockServo(name='servo2'),
    ]

    manager = ResourceManager(resources)
    service = RobotService(manager)

    async with ChannelFor([service]) as channel:
        client = RobotServiceStub(channel)
        request = StatusRequest()
        response: StatusResponse = await client.Status(request)
        assert response.status == Status(
            motors={
                'motor1': MotorStatus(
                    on=False,
                    position=0,
                    position_supported=True,
                ),
                'motor2': MotorStatus(
                    on=False,
                    position=0,
                    position_supported=True,
                ),
            },
            servos={
                'servo1': ServoStatus(
                    angle=0
                ),
                'servo2': ServoStatus(
                    angle=0
                )
            }
        )

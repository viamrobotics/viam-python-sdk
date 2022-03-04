import pytest
from grpclib.testing import ChannelFor

from viam.components.resource_manager import ResourceManager
from viam.proto.api.robot import ArmStatus, JointPositions, Pose
from viam.proto.api.robot import (
    RobotServiceStub,
    Status,
    MotorStatus, ServoStatus,
    StatusRequest,
    StatusResponse
)
from viam.robot.service import RobotService

from .mocks.components import MockArm, MockBase, MockIMU, MockMotor, MockServo


@pytest.mark.asyncio
async def test_robot_service():
    resources = [
        MockArm(name='arm1'),
        MockArm(name='arm2'),
        MockBase(name='base1'),
        MockBase(name='base2'),
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
            arms={
                'arm1': ArmStatus(
                    grid_position=Pose(
                        x=1,
                        y=2,
                        z=3,
                        o_x=2,
                        o_y=3,
                        o_z=4,
                        theta=20,
                    ),
                    joint_positions=JointPositions(degrees=[0, 0, 0, 0, 0, 0])
                ),
                'arm2': ArmStatus(
                    grid_position=Pose(
                        x=1,
                        y=2,
                        z=3,
                        o_x=2,
                        o_y=3,
                        o_z=4,
                        theta=20,
                    ),
                    joint_positions=JointPositions(degrees=[0, 0, 0, 0, 0, 0])
                ),
            },
            bases={
                'base1': True,
                'base2': True,
            },
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

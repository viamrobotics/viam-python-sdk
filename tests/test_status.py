import pytest
from google.protobuf.struct_pb2 import Struct
from grpclib.testing import ChannelFor
from viam.components.resource_manager import ResourceManager
from viam.proto.api.common import Pose, ResourceName
from viam.proto.api.component.arm import JointPositions
from viam.proto.api.component.arm import Status as ArmStatus
from viam.proto.api.component.motor import Status as MotorStatus
from viam.proto.api.component.servo import Status as ServoStatus
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           Status, StatusServiceStub)
from viam.status.service import StatusService
from viam.utils import message_to_struct

from .mocks.components import MockArm, MockBase, MockIMU, MockMotor, MockServo


@pytest.mark.asyncio
async def test_status_service():
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
    service = StatusService(manager)

    async with ChannelFor([service]) as channel:
        client = StatusServiceStub(channel)
        request = GetStatusRequest()
        response: GetStatusResponse = await client.GetStatus(request)
        expected = [
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='arm',
                    name='arm1'
                ),
                status=message_to_struct(ArmStatus(
                    end_position=Pose(
                        x=1,
                        y=2,
                        z=3,
                        o_x=2,
                        o_y=3,
                        o_z=4,
                        theta=20,
                    ),
                    joint_positions=JointPositions(degrees=[0, 0, 0, 0, 0, 0])
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='arm',
                    name='arm2'
                ),
                status=message_to_struct(ArmStatus(
                    end_position=Pose(
                        x=1,
                        y=2,
                        z=3,
                        o_x=2,
                        o_y=3,
                        o_z=4,
                        theta=20,
                    ),
                    joint_positions=JointPositions(degrees=[0, 0, 0, 0, 0, 0])
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='base',
                    name='base1'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='base',
                    name='base2'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='motor',
                    name='motor1'
                ),
                status=message_to_struct(MotorStatus(
                    is_on=False,
                    position=0,
                    position_reporting=True
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='motor',
                    name='motor2'
                ),
                status=message_to_struct(MotorStatus(
                    is_on=False,
                    position=0,
                    position_reporting=True
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='servo',
                    name='servo1'
                ),
                status=message_to_struct(ServoStatus(
                    position_deg=0
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='servo',
                    name='servo2'
                ),
                status=message_to_struct(ServoStatus(
                    position_deg=0
                ))
            ),
        ]
        assert list(response.status) == expected

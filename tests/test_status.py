import pytest
from google.protobuf.struct_pb2 import Struct
from grpclib.testing import ChannelFor
from viam.components.gps import GPS
from viam.components.resource_manager import ResourceManager
from viam.proto.api.common import (AnalogStatus, BoardStatus,
                                   DigitalInterruptStatus, Pose, ResourceName)
from viam.proto.api.component.arm import JointPositions
from viam.proto.api.component.arm import Status as ArmStatus
from viam.proto.api.component.gantry import Status as GantryStatus
from viam.proto.api.component.motor import Status as MotorStatus
from viam.proto.api.component.servo import Status as ServoStatus
from viam.proto.api.service.status import (GetStatusRequest, GetStatusResponse,
                                           Status, StatusServiceStub)
from viam.status.service import StatusService
from viam.utils import message_to_struct

from .mocks.components import (MockAnalogReader, MockArm, MockBase, MockBoard,
                               MockCamera, MockDigitalInterrupt, MockGantry,
                               MockGPIOPin, MockGPS, MockGripper, MockIMU,
                               MockMotor, MockPoseTracker, MockServo)


@pytest.mark.asyncio
async def test_status_service():
    resources = [
        MockArm(name='arm1'),
        MockArm(name='arm2'),
        MockBase(name='base1'),
        MockBase(name='base2'),
        MockBoard(
            name='board1',
            analog_readers={
                'reader1': MockAnalogReader('reader1', 3),
            },
            digital_interrupts={
                'interrupt1': MockDigitalInterrupt('interrupt1'),
            },
            gpio_pins={
                'pin1': MockGPIOPin('pin1')
            }
        ),
        MockBoard(
            name='board2',
            analog_readers={
                'reader2': MockAnalogReader('reader2', 3),
            },
            digital_interrupts={
                'interrupt2': MockDigitalInterrupt('interrupt2'),
            },
            gpio_pins={
                'pin2': MockGPIOPin('pin2')
            }
        ),
        MockCamera(name='camera1'),
        MockCamera(name='camera2'),
        MockGantry(name='gantry1', position=[1, 2, 3], lengths=[4, 5, 6]),
        MockGantry(name='gantry2', position=[7, 8, 9], lengths=[10, 11, 12]),
        MockGPS(
            name='gps1',
            location=GPS.Point(40.664679865782624, -73.97668056188789),
            altitude=15,
            speed=1341.12
        ),
        MockGPS(
            name='gps2',
            location=GPS.Point(-49.55979219617353, 69.4930936568856),
            altitude=1850,
            speed=614.57
        ),
        MockGripper(name='gripper1'),
        MockGripper(name='gripper2'),
        MockIMU(name='imu1'),
        MockIMU(name='imu2'),
        MockMotor(name='motor1'),
        MockMotor(name='motor2'),
        MockPoseTracker(name='pose_tracker1', poses=[]),
        MockPoseTracker(name='pose_tracker2', poses=[]),
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
                    type='service',
                    subtype='status',
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='service',
                    subtype='object_segmentation',
                ),
                status=Struct()
            ),
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
                    subtype='board',
                    name='board1'
                ),
                status=message_to_struct(BoardStatus(
                    analogs={
                        'reader1': AnalogStatus(value=3)
                    },
                    digital_interrupts={
                        'interrupt1': DigitalInterruptStatus(value=0)
                    }
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='board',
                    name='board2'
                ),
                status=message_to_struct(BoardStatus(
                    analogs={
                        'reader2': AnalogStatus(value=3)
                    },
                    digital_interrupts={
                        'interrupt2': DigitalInterruptStatus(value=0)
                    }
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='camera',
                    name='camera1'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='camera',
                    name='camera2'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='gantry',
                    name='gantry1'
                ),
                status=message_to_struct(GantryStatus(
                    positions_mm=[1, 2, 3],
                    lengths_mm=[4, 5, 6]
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='gantry',
                    name='gantry2'
                ),
                status=message_to_struct(GantryStatus(
                    positions_mm=[7, 8, 9],
                    lengths_mm=[10, 11, 12]
                ))
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='gps',
                    name='gps1'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='gps',
                    name='gps2'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='gripper',
                    name='gripper1'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='gripper',
                    name='gripper2'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='imu',
                    name='imu1'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='imu',
                    name='imu2'
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
                    subtype='pose_tracker',
                    name='pose_tracker1'
                ),
                status=Struct()
            ),
            Status(
                name=ResourceName(
                    namespace='rdk',
                    type='component',
                    subtype='pose_tracker',
                    name='pose_tracker2'
                ),
                status=Struct()
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

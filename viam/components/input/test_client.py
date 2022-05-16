import asyncio
from datetime import datetime, timedelta
from time import time

from viam.components.input.input import Control, Controller, Event, EventType
from viam.components.motor.motor import Motor
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions


async def client():

    async with await RobotClient.at_address('localhost:9090', RobotClient.Options(dial_options=DialOptions(insecure=True))) as robot:

        controller = Controller.from_robot(robot, 'controller')
        controller.register_control_callback(Control.ABSOLUTE_X, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_Y, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_Z, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_RX, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_RY, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_RZ, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_HAT0_X, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.ABSOLUTE_HAT0_Y, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_SOUTH, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_EAST, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_WEST, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_NORTH, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_LT, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_RT, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_L_THUMB, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_R_THUMB, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_SELECT, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_START, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_MENU, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_RECORD, [EventType.ALL_EVENTS], lambda ev: print(ev))
        controller.register_control_callback(Control.BUTTON_E_STOP, [EventType.ALL_EVENTS], lambda ev: print(ev))

        await controller.trigger_event(Event(time(), EventType.BUTTON_RELEASE, Control.ABSOLUTE_X, 1))

        motor = Motor.from_robot(robot, 'motor')
        await motor.go_for(100, 100)

        while True:
            pass
            # print('Sending trigger')
            # await asyncio.sleep(1)
            # await controller.trigger_event(Event(time(), EventType.BUTTON_RELEASE, Control.ABSOLUTE_X, 1))


if __name__ == '__main__':
    try:
        asyncio.run(client())
        while True:
            pass
    except KeyboardInterrupt:
        pass

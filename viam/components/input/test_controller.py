import asyncio
from time import time
from typing import Dict, List, Optional

from viam.rpc.server import Server
from tests.mocks.components import MockMotor

from .input import Control, ControlFunction, Controller, Event, EventType


class TestController(Controller):

    def __init__(self, name: str):
        super().__init__(name)
        self.callbacks: Dict[Control, Dict[EventType, Optional[ControlFunction]]] = {}

    async def get_controls(self) -> List[Control]:
        return [
            Control.ABSOLUTE_X,
            Control.ABSOLUTE_Y,
            Control.ABSOLUTE_Z,
            Control.ABSOLUTE_RX,
            Control.ABSOLUTE_RY,
            Control.ABSOLUTE_RZ,
            Control.ABSOLUTE_HAT0_X,
            Control.ABSOLUTE_HAT0_Y,
            Control.BUTTON_SOUTH,
            Control.BUTTON_EAST,
            Control.BUTTON_WEST,
            Control.BUTTON_NORTH,
            Control.BUTTON_LT,
            Control.BUTTON_RT,
            Control.BUTTON_L_THUMB,
            Control.BUTTON_R_THUMB,
            Control.BUTTON_SELECT,
            Control.BUTTON_START,
            Control.BUTTON_MENU,
            Control.BUTTON_RECORD,
            Control.BUTTON_E_STOP,
        ]

    async def get_events(self) -> Dict[Control, Event]:
        return {Control.ABSOLUTE_X: Event(time(), EventType.BUTTON_RELEASE, Control.ABSOLUTE_X, 0)}

    def register_control_callback(self, control: Control, triggers: List[EventType], function: Optional[ControlFunction]):
        callbacks = self.callbacks.get(control, {})
        for trigger in triggers:
            if trigger == EventType.BUTTON_CHANGE:
                callbacks[EventType.BUTTON_PRESS] = function
                callbacks[EventType.BUTTON_RELEASE] = function
            else:
                callbacks[trigger] = function
        self.callbacks[control] = callbacks

    async def trigger_event(self, event: Event):
        self._execute_callback(event)

    def _execute_callback(self, event: Event):
        try:
            callbacks = self.callbacks[event.control]
            callback = callbacks.get(event.event, None)
            all_callback = callbacks.get(EventType.ALL_EVENTS, None)
        except KeyError:
            return

        if callback is not None:
            callback(event)
        if all_callback is not None:
            all_callback(event)


async def main():
    controller = TestController('controller')
    motor = MockMotor('motor')
    srv = Server([controller, motor])
    await srv.serve()

    # try:
    #     while True:
    #         value = input('Gimme gimme an int: ')
    #         controller._execute_callback(Event(time(), EventType.BUTTON_RELEASE, Control.ABSOLUTE_X, float(value)))
    # except KeyboardInterrupt:
    #     pass

if __name__ == '__main__':
    asyncio.run(main())

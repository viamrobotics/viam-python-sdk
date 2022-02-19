import random

from viam.components.servo import ServoBase


class Servo(ServoBase):
    async def move(self, angle: int):
        print(angle)

    async def get_position(self) -> int:
        pos = random.randint(0, 180)
        return pos

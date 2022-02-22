from viam.components.servo import ServoBase


class Servo(ServoBase):

    angle: int

    async def move(self, angle: int):
        self.angle = angle

    async def get_position(self) -> int:
        return self.angle

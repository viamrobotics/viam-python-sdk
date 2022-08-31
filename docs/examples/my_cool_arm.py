# my-python-robot/my_cool_arm.py

from typing import Any, Dict, Optional
from viam.components.arm import Arm, JointPositions, Pose, WorldState


class MyCoolArm(Arm):
    # Subclass the Viam Arm component and implement the required functions

    def __init__(self, name: str):
        # Starting position
        self.position = Pose(
            x=0,
            y=0,
            z=0,
            o_x=0,
            o_y=0,
            o_z=0,
            theta=0,
        )

        # Starting joint positions
        self.joint_positions = JointPositions(values=[0, 0, 0, 0, 0, 0])
        self.is_stoppped = True
        super().__init__(name)

    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None) -> Pose:
        return self.position

    async def move_to_position(self, pose: Pose, world_state: Optional[WorldState] = None, extra: Optional[Dict[str, Any]] = None):
        self.is_stoppped = False
        self.position = pose

    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None) -> JointPositions:
        return self.joint_positions

    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None):
        self.is_stoppped = False
        self.joint_positions = positions

    async def stop(self, extra: Optional[Dict[str, Any]] = None):
        self.is_stoppped = True

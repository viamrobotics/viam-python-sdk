import asyncio
import os
from typing import Any, ClassVar, Dict, List, Mapping, Optional, Tuple

from typing_extensions import Self

from viam.components.arm import Arm, JointPositions, KinematicsFileFormat, Pose
from viam.logging import getLogger
from viam.operations import run_with_operation
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import Capsule, Geometry, Mesh, ResourceName, Sphere
from viam.proto.component.arm import MoveOptions
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily

LOGGER = getLogger(__name__)


class MyArm(Arm):
    # Subclass the Viam Arm component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viam", "arm"), "myarm")

    def __init__(self, name: str):
        # Starting position
        self.position = Pose(
            x=0,
            y=0,
            z=0,
            o_x=0,
            o_y=0,
            o_z=1,
            theta=0,
        )

        # Starting joint positions
        self.joint_positions = JointPositions(values=[0, 0, 0, 0, 0, 0])
        self.is_stopped = True
        self.geometries = [
            Geometry(center=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20), sphere=Sphere(radius_mm=2)),
            Geometry(center=Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20), capsule=Capsule(radius_mm=3, length_mm=8)),
        ]
        super().__init__(name)

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        arm = cls(config.name)
        return arm

    async def get_end_position(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Pose:
        return self.position

    @run_with_operation
    async def move_to_position(
        self,
        pose: Pose,
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        operation = self.get_operation(kwargs)

        self.is_stopped = False

        # Simulate the length of time it takes for the arm to move to its new position
        for x in range(10):
            await asyncio.sleep(1)

            # Check if the operation is cancelled and, if it is, stop the arm's motion
            if await operation.is_cancelled():
                await self.stop()
                break

        self.position = pose
        self.is_stopped = True

    async def get_joint_positions(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> JointPositions:
        return self.joint_positions

    @run_with_operation
    async def move_to_joint_positions(self, positions: JointPositions, extra: Optional[Dict[str, Any]] = None, **kwargs):
        operation = self.get_operation(kwargs)

        self.is_stopped = False

        # Simulate the length of time it takes for the arm to move to its new joint position
        for x in range(10):
            await asyncio.sleep(1)

            # Check if the operation is cancelled and, if it is, stop the arm's motion
            if await operation.is_cancelled():
                await self.stop()
                break

        self.joint_positions = positions
        self.is_stopped = True

    @run_with_operation
    async def move_through_joint_positions(
        self,
        positions: List[JointPositions],
        options: Optional[MoveOptions] = None,
        extra: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        operation = self.get_operation(kwargs)

        self.is_stopped = False

        # Move through each waypoint in order, honoring cancellation between them.
        # A real driver is expected to honor the velocity/acceleration ceilings in
        # `options`, checking e.g. options.HasField("max_vel_degs_per_sec") before
        # applying it (an unset field reads as 0.0); this example ignores them and
        # just sleeps for a fixed interval between waypoints.
        for position in positions:
            await asyncio.sleep(1)

            if await operation.is_cancelled():
                await self.stop()
                break

            self.joint_positions = position

        self.is_stopped = True

    async def get_3d_models(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Mesh]:
        # This arm has no meshes to report.
        return {}

    async def set_manual_mode(self, manual_mode: bool, enabled_for: int = 0, extra: Optional[Dict[str, Any]] = None, **kwargs):
        # This arm does not support manual mode.
        raise NotImplementedError()

    async def get_manual_mode(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> bool:
        # This arm does not support manual mode.
        raise NotImplementedError()

    async def get_properties(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Arm.Properties:
        return Arm.Properties(support_manual_mode=False, support_cartesian_commands=True)

    async def stop(self, extra: Optional[Dict[str, Any]] = None, **kwargs):
        self.is_stopped = True

    async def is_moving(self) -> bool:
        return not self.is_stopped

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None) -> List[Geometry]:
        return self.geometries

    async def get_kinematics(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Tuple[KinematicsFileFormat.ValueType, bytes]:
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, "./my_arm_kinematics.json")
        with open(filepath, mode="rb") as f:
            file_data = f.read()
        return (KinematicsFileFormat.KINEMATICS_FILE_FORMAT_SVA, file_data)

    async def close(self):
        # This is a completely optional function to include. This will be called when the resource is removed from the config or the module
        # is shutting down.
        LOGGER.info(f"{self.name} is closed.")


Registry.register_resource_creator(Arm.API, MyArm.MODEL, ResourceCreatorRegistration(MyArm.new))

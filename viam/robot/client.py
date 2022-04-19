import asyncio
from dataclasses import dataclass
from threading import Lock
from typing import List, Optional

from grpclib.client import Channel
from typing_extensions import Self
from viam import logging
from viam.components.arm import ArmClient
from viam.components.base import BaseClient
from viam.components.board import BoardClient
from viam.components.camera import CameraClient
from viam.components.component_base import ComponentBase
from viam.components.gantry import GantryClient
from viam.components.gps import GPSClient
from viam.components.gripper import GripperClient
from viam.components.imu import IMUClient
from viam.components.motor import MotorClient
from viam.components.pose_tracker import PoseTrackerClient
from viam.components.resource_manager import ResourceManager
from viam.components.sensor import SensorClient
from viam.components.servo import ServoClient
from viam.errors import ServiceNotImplementedError, ViamError
from viam.proto.api.common import ResourceName
from viam.rpc.dial import DialOptions, dial_direct
from viam.services import ServiceType
from viam.services.metadata.client import MetadataClient
from viam.services.types import Service

LOGGER = logging.getLogger(__name__)


class RobotClient:
    """gRPC client for a Robot. This class should be used for all interactions with a robot.

    There are 2 ways to instantiate a robot client:

        RobotClient.at_address(...)\n
        RobotClient.with_channel(...)

    You can use the client standalone or within a context

        robot = await RobotClient.at_address(...)\n
        async with await RobotClient.with_channel(...) as robot: ...

    You must `close()` the robot to release resources.

    Note: Robots used within a context are automatically closed UNLESS created with a channel. Robots created using `with_channel` are
    not automatically closed.
    """

    @dataclass
    class Options:
        refresh_interval: int = 0
        """
        How often to refresh the status/parts of the robot in seconds.
        If not set, the robot will not be refreshed automatically
        """

        dial_options: Optional[DialOptions] = None
        """
        Options used to connect clients to gRPC servers
        """

    @classmethod
    async def at_address(cls, address: str, options: Options) -> Self:
        """Create a robot client that is connected to the robot at the provided address.

        Args:
            address (str): Address of the robot (IP address, URL, etc.)
            options (Options): Options for connecting and refreshing

        Returns:
            Self: the RobotClient
        """
        channel = await dial_direct(address, options.dial_options)
        robot = await RobotClient.with_channel(channel, options)
        robot._should_close_channel = True
        return robot

    @classmethod
    async def with_channel(cls, channel: Channel, options: Options) -> Self:
        """Create a robot that is connected to a robot over the given channel.

        Any robots created using this method will *NOT* automatically close the channel upon exit.

        Args:
            channel (Channel): The gRPC channel that is connected to a robot
            options (Options): Options for refreshing. Any connection options will be ignored.

        Returns:
            Self: the RobotClient
        """
        self = cls()
        self._channel = channel
        self._metadata_client = MetadataClient(self._channel)
        self._manager = ResourceManager()
        self._lock = Lock()
        self._resource_names = []
        self._should_close_channel = False
        await self.refresh()

        if options.refresh_interval > 0:
            loop = asyncio.get_event_loop()
            self._refresh_task = loop.create_task(self._refresh_every(options.refresh_interval))

        return self

    _channel: Channel
    _lock: Lock
    _manager: ResourceManager
    _metadata_client: MetadataClient
    _refresh_task: Optional[asyncio.Task] = None
    _resource_names: List[ResourceName]
    _should_close_channel: bool

    async def refresh(self):
        """
        Manually refresh the underlying parts of this robot
        """
        resource_names = await self._metadata_client.resources()
        if resource_names == self._resource_names:
            return
        manager = ResourceManager()
        for rname in resource_names:
            if rname.type != 'component':
                continue
            if rname.subtype == 'remote':
                continue
            subtype = rname.subtype
            if subtype == 'arm':
                manager.register(ArmClient(rname.name, self._channel))
            elif subtype == 'base':
                manager.register(BaseClient(rname.name, self._channel))
            elif subtype == 'board':
                manager.register(BoardClient(rname.name, self._channel))
            elif subtype == 'camera':
                manager.register(CameraClient(rname.name, self._channel))
            elif subtype == 'gantry':
                manager.register(GantryClient(rname.name, self._channel))
            elif subtype == 'gps':
                manager.register(GPSClient(rname.name, self._channel))
            elif subtype == 'gripper':
                manager.register(GripperClient(rname.name, self._channel))
            elif subtype == 'imu':
                manager.register(IMUClient(rname.name, self._channel))
            elif subtype == 'motor':
                manager.register(MotorClient(rname.name, self._channel))
            elif subtype == 'pose_tracker':
                manager.register(PoseTrackerClient(rname.name, self._channel))
            elif subtype == 'sensor':
                manager.register(SensorClient(rname.name, self._channel))
            elif subtype == 'servo':
                manager.register(ServoClient(rname.name, self._channel))
            else:
                LOGGER.warn(f'Component of type {subtype} is not implemented')
        with self._lock:
            self._resource_names = resource_names
            if manager.components != self._manager.components:
                self._manager = manager

    async def _refresh_every(self, interval: int):
        while True:
            await asyncio.sleep(interval)
            try:
                await self.refresh()
            except Exception as e:
                LOGGER.error('Failed to refresh status', exc_info=e)

    def get_component(self, name: ResourceName) -> ComponentBase:
        """Get a component using its ResourceName.

        This function should not be used except in specific cases. The method `Component.from_robot(...)` is the preferred method
        for obtaining components.

        ```python3
        arm = Arm.from_robot(robot=robot, name='my_arm')
        ```

        Because this function returns a generic `ComponentBase` rather than the specific
        component type, it will be necessary to cast the returned component to the desired component. This can be done using a few
        different methods:

        - Assertion

        ```python3
            arm = robot.get_component(Arm.get_resource_name('my_arm'))
            assert isinstance(arm, Arm)
            end_pos = await arm.get_end_position()
        ```

        - Explicit cast

        ```python3
            from typing import cast

            arm = robot.get_component(Arm.get_resource_name('my_arm'))
            arm = cast(Arm, arm)
            end_pos = await arm.get_end_position()
        ```

        - Declare type on variable assignment.
          - Note: If using an IDE, a type error may be shown which can be ignored.

        ```python3
            arm: Arm = robot.get_component(Arm.get_resource_name('my_arm'))  # type: ignore
            end_pos = await arm.get_end_position()
        ```

        Args:
            name (ResourceName): The component's name

        Raises:
            ViamError: Raised if the requested resource is not a component
            ComponentNotFoundError: Error if component with the given type and name does not exist in the registry

        Returns:
            ComponentBase: The component
        """
        if name.type != 'component':
            raise ViamError(f'ResourceName does not describe a component: {name}')
        with self._lock:
            return self._manager.get_component(ComponentBase, name.name)

    def get_service(self, service_type: ServiceType[Service]) -> Service:
        """Get a service by specifying the `ServiceType`.

        Args:
            service_type (ServiceType): The service type

        Raises:
            ServiceNotImplementedError: Raised the service is not implemented or available on the Robot

        Returns:
            Service: The service
        """
        with self._lock:
            if service_type.name in [rn.subtype for rn in self._resource_names if rn.type == 'service']:
                return service_type.with_channel(self._channel)
            raise ServiceNotImplementedError(service_type.name)

    @property
    def resource_names(self) -> List[ResourceName]:
        """
        Get a list of all resource names

        Returns:
            List[ResourceName]: The list of resource names
        """
        with self._lock:
            return [r for r in self._resource_names]

    def close(self):
        """
        Cleanly close the underlying connections and stop any periodic tasks
        """
        try:
            self._lock.release()
        except RuntimeError:
            pass
        if self._refresh_task is not None:
            self._refresh_task.cancel()
        if self._should_close_channel:
            self._channel.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.close()

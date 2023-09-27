import asyncio
from dataclasses import dataclass
from threading import RLock
from typing import Any, Dict, List, Optional, Union

from grpclib.client import Channel
from typing_extensions import Self

import viam
from viam import logging
from viam.components.component_base import ComponentBase
from viam.components.movement_sensor import MovementSensor
from viam.components.sensor import Sensor
from viam.errors import ResourceNotFoundError
from viam.proto.common import PoseInFrame, ResourceName, Transform
from viam.proto.robot import (
    BlockForOperationRequest,
    CancelOperationRequest,
    DiscoverComponentsRequest,
    DiscoverComponentsResponse,
    Discovery,
    DiscoveryQuery,
    FrameSystemConfig,
    FrameSystemConfigRequest,
    FrameSystemConfigResponse,
    GetOperationsRequest,
    GetOperationsResponse,
    GetStatusRequest,
    GetStatusResponse,
    Operation,
    ResourceNamesRequest,
    ResourceNamesResponse,
    RobotServiceStub,
    StopAllRequest,
    StopExtraParameters,
    TransformPoseRequest,
    TransformPoseResponse,
)
from viam.resource.base import ResourceBase
from viam.resource.manager import ResourceManager
from viam.resource.registry import Registry
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase, ResourceRPCClientBase
from viam.resource.types import RESOURCE_TYPE_COMPONENT, RESOURCE_TYPE_SERVICE, Subtype
from viam.rpc.dial import DialOptions, ViamChannel, dial
from viam.services.service_base import ServiceBase
from viam.sessions_client import SessionsClient
from viam.utils import dict_to_struct

LOGGER = logging.getLogger(__name__)


class RobotClient:
    """gRPC client for a Robot. This class should be used for all interactions with a robot.

    There are 2 ways to instantiate a robot client::

        RobotClient.at_address(...)
        RobotClient.with_channel(...)

    You can use the client standalone or within a context::

        robot = await RobotClient.at_address(...)
        async with await RobotClient.with_channel(...) as robot: ...

    You must ``close()`` the robot to release resources.

    Note: Robots used within a context are automatically closed UNLESS created with a channel. Robots created using ``with_channel`` are
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

        log_level: int = logging.INFO
        """
        The log level to output
        """

        check_connection_interval: int = 10
        """
        The frequency (in seconds) at which to check if the robot is still connected. 0 (zero) signifies no connection checks
        """

        attempt_reconnect_interval: int = 1
        """
        The frequency (in seconds) at which to attempt to reconnect a disconnected robot. 0 (zero) signifies no reconnection attempts
        """

        disable_sessions: bool = False
        """
        Whether sessions are disabled
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
        logging.setLevel(options.log_level)
        channel = await dial(address, options.dial_options)
        robot = await cls._with_channel(channel, options, True)
        robot._address = address
        return robot

    @classmethod
    async def with_channel(cls, channel: Union[Channel, ViamChannel], options: Options) -> Self:
        """Create a robot that is connected to a robot over the given channel.

        Any robots created using this method will *NOT* automatically close the channel upon exit.

        Args:
            channel (ViamChannel): The channel that is connected to a robot, obtained by ``viam.rpc.dial``
            options (Options): Options for refreshing. Any connection options will be ignored.

        Returns:
            Self: the RobotClient
        """
        logging.setLevel(options.log_level)
        return await cls._with_channel(channel, options, False)

    @classmethod
    async def _with_channel(cls, channel: Union[Channel, ViamChannel], options: Options, close_channel: bool):
        """INTERNAL USE ONLY"""

        self = cls()

        if isinstance(channel, Channel):
            self._channel = channel
            self._viam_channel = None
        else:
            self._channel = channel.channel
            self._viam_channel = channel

        self._connected = True
        self._client = RobotServiceStub(self._channel)
        self._manager = ResourceManager()
        self._lock = RLock()
        self._resource_names = []
        self._should_close_channel = close_channel
        self._options = options
        self._address = self._channel._path if self._channel._path else f"{self._channel._host}:{self._channel._port}"
        self._sessions_client = SessionsClient(
            self._channel, self._address, self._options.dial_options, disabled=self._options.disable_sessions
        )

        try:
            await self.refresh()
        except Exception:
            LOGGER.error("Unable to establish a connection to the robot. Ensure the robot is online and reachable and try again.")
            await self.close()
            raise ConnectionError("Unable to establish a connection to the robot.")

        if options.refresh_interval > 0:
            self._refresh_task = asyncio.create_task(
                self._refresh_every(options.refresh_interval), name=f"{viam._TASK_PREFIX}-robot_refresh_metadata"
            )

        if options.check_connection_interval > 0 or options.attempt_reconnect_interval > 0:
            self._check_connection_task = asyncio.create_task(
                self._check_connection(options.check_connection_interval, options.attempt_reconnect_interval),
                name=f"{viam._TASK_PREFIX}-robot_check_connection",
            )

        return self

    _channel: Channel
    _viam_channel: Optional[ViamChannel]
    _lock: RLock
    _manager: ResourceManager
    _client: RobotServiceStub
    _connected: bool
    _address: str
    _options: Options
    _refresh_task: Optional[asyncio.Task] = None
    _check_connection_task: Optional[asyncio.Task] = None
    _resource_names: List[ResourceName]
    _should_close_channel: bool
    _closed: bool = False
    _sessions_client: SessionsClient

    async def refresh(self):
        """
        Manually refresh the underlying parts of this robot
        """
        response: ResourceNamesResponse = await self._client.ResourceNames(ResourceNamesRequest())
        resource_names: List[ResourceName] = list(response.resources)
        with self._lock:
            if resource_names == self._resource_names:
                return
            for rname in resource_names:
                if rname.type not in [RESOURCE_TYPE_COMPONENT, RESOURCE_TYPE_SERVICE]:
                    continue
                if rname.subtype == "remote":
                    continue

                # If the resource is a MovementSensor, DO NOT include Sensor as well (it will get added via MovementSensor)
                if rname.subtype == Sensor.SUBTYPE.resource_subtype and MovementSensor.get_resource_name(rname.name) in resource_names:
                    continue

                self._create_or_reset_client(rname)

            for rname in self.resource_names:
                if rname not in resource_names:
                    self._manager.remove_resource(rname)

            self._resource_names = resource_names

    def _create_or_reset_client(self, resourceName: ResourceName):
        if resourceName in self._manager.resources:
            res = self._manager.get_resource(ResourceBase, resourceName)

            # If the channel hasn't changed, we don't need to do anything for existing clients
            if isinstance(res, ResourceRPCClientBase) or (hasattr(res, "channel") and isinstance(getattr(res, "channel"), Channel)):
                if self._channel is res.channel:  # type: ignore
                    return

            if isinstance(res, ReconfigurableResourceRPCClientBase):
                res.reset_channel(self._channel)
            else:
                self._manager.remove_resource(resourceName)
                self._manager.register(
                    Registry.lookup_subtype(Subtype.from_resource_name(resourceName)).create_rpc_client(resourceName.name, self._channel)
                )
        else:
            try:
                self._manager.register(
                    Registry.lookup_subtype(Subtype.from_resource_name(resourceName)).create_rpc_client(resourceName.name, self._channel)
                )
            except ResourceNotFoundError:
                pass

    async def _refresh_every(self, interval: int):
        while True:
            await asyncio.sleep(interval)
            try:
                await self.refresh()
            except Exception as e:
                LOGGER.error("Failed to refresh status", exc_info=e)

    async def _check_connection(self, check_every: int, reconnect_every: int):
        if check_every <= 0:
            check_every = reconnect_every
        if check_every <= 0 and reconnect_every <= 0:
            return

        while True:
            await asyncio.sleep(check_every)

            # Failure to grab resources could be for spurious, non-networking reasons. Try three times just to be safe.
            connection_error = None
            for _ in range(3):
                try:
                    _: ResourceNamesResponse = await self._client.ResourceNames(ResourceNamesRequest(), timeout=1)
                    connection_error = None
                    break
                except Exception as e:
                    connection_error = e
                    await asyncio.sleep(0.1)
            if connection_error:
                msg = "Lost connection to robot."
                if reconnect_every > 0:
                    msg += (
                        f" Attempting to reconnect to {self._address} every {reconnect_every} second{'s' if reconnect_every != 1 else ''}"
                    )
                LOGGER.error(msg, exc_info=connection_error)
                self._close_channel()
                self._connected = False

            if reconnect_every <= 0:
                continue

            if self._connected:
                continue

            reconnect_attempts = self._options.dial_options.max_reconnect_attempts if self._options.dial_options else 3

            for _ in range(reconnect_attempts):
                try:
                    self._sessions_client.reset()

                    channel = await dial(self._address, self._options.dial_options)

                    client: RobotServiceStub
                    if isinstance(channel, Channel):
                        client = RobotServiceStub(channel)
                    else:
                        client = RobotServiceStub(channel.channel)
                    _: ResourceNamesResponse = await client.ResourceNames(ResourceNamesRequest())

                    if isinstance(channel, Channel):
                        self._channel = channel
                        self._viam_channel = None
                    else:
                        self._channel = channel.channel
                        self._viam_channel = channel
                    self._client = RobotServiceStub(self._channel)
                    direct_dial_address = self._channel._path if self._channel._path else f"{self._channel._host}:{self._channel._port}"
                    self._sessions_client = SessionsClient(
                        channel=self._channel,
                        direct_dial_address=direct_dial_address,
                        dial_options=self._options.dial_options,
                        disabled=self._options.disable_sessions,
                    )

                    await self.refresh()
                    self._connected = True
                    LOGGER.debug("Successfully reconnected robot")
                    break
                except Exception as e:
                    LOGGER.error(f"Failed to reconnect, trying again in {reconnect_every}sec", exc_info=e)
                    self._sessions_client.reset()
                    self._close_channel()
                    await asyncio.sleep(reconnect_every)

    def get_component(self, name: ResourceName) -> ComponentBase:
        """Get a component using its ResourceName.

        This function should not be called directly except in specific cases. The method ``Component.from_robot(...)`` is the preferred
        method for obtaining components.
        ::

            arm = Arm.from_robot(robot=robot, name="my_arm")

        Because this function returns a generic ``ComponentBase`` rather than the specific
        component type, it will be necessary to cast the returned component to the desired component. This can be done using a few
        different methods:

        - Assertion::

            arm = robot.get_component(Arm.get_resource_name("my_arm"))
            assert isinstance(arm, Arm)
            end_pos = await arm.get_end_position()

        - Explicit cast::

            from typing import cast
            arm = robot.get_component(Arm.get_resource_name("my_arm"))
            arm = cast(Arm, arm)
            end_pos = await arm.get_end_position()

        - Declare type on variable assignment.

            - Note: If using an IDE, a type error may be shown which can be ignored.
            ::

                arm: Arm = robot.get_component(Arm.get_resource_name("my_arm"))  # type: ignore
                end_pos = await arm.get_end_position()

        Args:
            name (viam.proto.common.ResourceName): The component's ResourceName

        Raises:
            ValueError: Raised if the requested resource is not a component
            ComponentNotFoundError: Error if component with the given type and name does not exist in the registry

        Returns:
            ComponentBase: The component
        """
        if name.type != RESOURCE_TYPE_COMPONENT:
            raise ValueError(f"ResourceName does not describe a component: {name}")
        with self._lock:
            return self._manager.get_resource(ComponentBase, name)

    def get_service(self, name: ResourceName) -> ServiceBase:
        """Get a service using its ResourceName

        This function should not be called directly except in specific cases. The method ``Service.from_robot(...)`` is the preferred
        method for obtaining services.
        ::

            service = MyService.from_robot(robot=robot, name="my_service")

        Because this function returns a generic ``ServiceBase`` rather than a specific service type, it will be necessary to cast the
        returned service to the desired service. This can be done using a few methods:

        - Assertion::

            service = robot.get_service(MyService.get_resource_name("my_service"))
            assert isinstance(service, MyService)

        - Explicit cast::

            from typing import cast
            service = robot.get_service(MyService.get_resource_name("my_service"))
            service = cast(MyService, my_service)

        - Declare type on variable assignment

            - Note: If using an IDE, a type error may be shown which can be ignored.
            ::

                service: MyService = robot.get_service(MyService.get_resource_name("my_service"))  # type: ignore

        Args:
            name (viam.proto.common.ResourceName): The service's ResourceName

        Raises:
            ValueError: Raised if the requested resource is not a component
            ComponentNotFoundError: Error if component with the given type and name does not exist in the registry

        Returns:
            ServiceBase: The service
        """
        if name.type != RESOURCE_TYPE_SERVICE:
            raise ValueError(f"ResourceName does not describe a service: {name}")
        with self._lock:
            return self._manager.get_resource(ServiceBase, name)

    @property
    def resource_names(self) -> List[ResourceName]:
        """
        Get a list of all resource names

        Returns:
            List[viam.proto.common.ResourceName]: The list of resource names
        """
        with self._lock:
            return [r for r in self._resource_names]

    def _close_channel(self, *, tab_count=0):
        tabs = "".join(["\t" for _ in range(tab_count)])
        if self._viam_channel is not None:
            LOGGER.debug(f"{tabs} Closing ViamChannel instance")
            self._viam_channel.close()
        else:
            LOGGER.debug(f"{tabs} Closing grpc-lib Channel instance")
            self._channel.close()

    async def close(self):
        """
        Cleanly close the underlying connections and stop any periodic tasks
        """
        LOGGER.debug("Closing RobotClient")
        if self._closed:
            LOGGER.debug("RobotClient is already closed")
            return

        try:
            self._lock.release()
        except RuntimeError:
            pass

        self._sessions_client.reset()

        # Cancel all tasks created by VIAM
        LOGGER.debug("Closing tasks spawned by Viam")
        tasks = [task for task in asyncio.all_tasks() if task.get_name().startswith(viam._TASK_PREFIX)]
        for task in tasks:
            LOGGER.debug(f"\tClosing task {task.get_name()}")
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

        if self._should_close_channel:
            LOGGER.debug("Closing gRPC channel to remote robot")
            self._close_channel(tab_count=1)

        self._closed = True

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    ##########
    # STATUS #
    ##########
    async def get_status(self, components: Optional[List[ResourceName]] = None):
        """
        Get the status of the robot's components. You can optionally
        provide a list of ``ResourceName`` for which you want statuses.

        Args:
            components (Optional[List[viam.proto.common.ResourceName]]): Optional list of
                ``ResourceName`` for components you want statuses.
        """
        names = components if components is not None else []
        request = GetStatusRequest(resource_names=names)
        response: GetStatusResponse = await self._client.GetStatus(request)
        return list(response.status)

    ##############
    # OPERATIONS #
    ##############

    async def get_operations(self) -> List[Operation]:
        """
        Get the list of operations currently running on the robot.

        Returns:
            List[viam.proto.robot.Operation]: The list of operations currently running on a given robot.
        """
        request = GetOperationsRequest()
        response: GetOperationsResponse = await self._client.GetOperations(request)
        return list(response.operations)

    async def cancel_operation(self, id: str):
        """
        Cancels the specified operation on the robot.

        Args:
            id (str): ID of operation to kill.
        """
        request = CancelOperationRequest(id=id)
        await self._client.CancelOperation(request)

    async def block_for_operation(self, id: str):
        """
        Blocks on the specified operation on the robot. This function will only return when the specific operation
        has finished or has been cancelled.

        Args:
            id (str): ID of operation to block on.
        """
        request = BlockForOperationRequest(id=id)
        await self._client.BlockForOperation(request)

    ################
    # FRAME SYSTEM #
    ################

    async def get_frame_system_config(self, additional_transforms: Optional[List[Transform]] = None) -> List[FrameSystemConfig]:
        """
        Get the configuration of the frame system of a given robot.

        Returns:
            List[viam.proto.robot.FrameSystemConfig]: The configuration of a given robot's frame system.
        """
        request = FrameSystemConfigRequest(supplemental_transforms=additional_transforms)
        response: FrameSystemConfigResponse = await self._client.FrameSystemConfig(request)
        return list(response.frame_system_configs)

    async def transform_pose(
        self, query: PoseInFrame, destination: str, additional_transforms: Optional[List[Transform]] = None
    ) -> PoseInFrame:
        """
        Transform a given source Pose from the reference frame to a new specified destination which is a reference frame.

        Args:

            query (viam.proto.common.PoseInFrame): The pose that should be transformed.
            destination (str) : The name of the reference frame to transform the given pose to.

        """
        request = TransformPoseRequest(source=query, destination=destination, supplemental_transforms=additional_transforms)
        response: TransformPoseResponse = await self._client.TransformPose(request)
        return response.pose

    async def transform_point_cloud(self):
        raise NotImplementedError()

    #######################
    # COMPONENT DISCOVERY #
    #######################

    async def discover_components(
        self,
        queries: List[DiscoveryQuery],
    ) -> List[Discovery]:
        """
        Get the list of discovered component configurations.

        Args:

            queries (List[viam.proto.robot.DiscoveryQuery]): The list of component models to lookup configurations for.

        """
        request = DiscoverComponentsRequest(queries=queries)
        response: DiscoverComponentsResponse = await self._client.DiscoverComponents(request)
        return list(response.discovery)

    ############
    # STOP ALL #
    ############

    async def stop_all(self, extra: Dict[ResourceName, Dict[str, Any]] = {}):
        """
        Cancel all current and outstanding operations for the robot and stop all actuators and movement

        Args:
            extra (Dict[viam.proto.common.ResourceName, Dict[str, Any]]): Any extra parameters to pass to the resources' ``stop`` methods,
                keyed on the resource's ``ResourceName``

        """
        ep: List[StopExtraParameters] = []
        for name, params in extra.items():
            ep.append(StopExtraParameters(name=name, params=dict_to_struct(params)))
        request = StopAllRequest(extra=ep)
        await self._client.StopAll(request)

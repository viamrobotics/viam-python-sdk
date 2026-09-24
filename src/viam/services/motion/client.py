import asyncio
from typing import Any, AsyncIterator, Mapping, Optional, Sequence

from grpclib.client import Channel

from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeoGeometry,
    Geometry,
    GeoPoint,
    GetStatusRequest,
    GetStatusResponse,
    Pose,
    PoseInFrame,
    Transform,
    WorldState,
)
from viam.proto.component.arm import JointPositions
from viam.proto.service.motion import (
    Constraints,
    GetPlanRequest,
    GetPlanResponse,
    GetPoseRequest,
    GetPoseResponse,
    ListPlanStatusesRequest,
    ListPlanStatusesResponse,
    MotionConfiguration,
    MotionServiceStub,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
    PlanStatusWithID,
    StopPlanRequest,
    StopPlanResponse,
    TempStreamArmJointPositionsRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, struct_to_dict

from .motion import Motion


def _validate_name(value: str, param_name: str) -> str:
    """Reject non-string names here, where the field and the expected type can be named.

    Passing a ``ResourceName``, as older SDK releases required, otherwise fails inside the protobuf extension with
    "TypeError: bad argument type for built-in operation".
    """
    if isinstance(value, str):
        return value
    resource = param_name.removesuffix("_name").replace("_", " ")
    raise TypeError(f"{param_name} must be the {resource}'s name as a string, e.g. 'pick-grip'")


class MotionClient(Motion, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for the Motion service.
    """

    client: MotionServiceStub

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = MotionServiceStub(channel)
        super().__init__(name)

    async def move(
        self,
        component_name: str,
        destination: PoseInFrame,
        world_state: Optional[WorldState] = None,
        constraints: Optional[Constraints] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> bool:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MoveRequest(
            name=self.name,
            destination=destination,
            component_name=_validate_name(component_name, "component_name"),
            world_state=world_state,
            constraints=constraints,
            extra=dict_to_struct(extra),
        )
        response: MoveResponse = await self.client.Move(request, timeout=timeout, metadata=md)
        return response.success

    async def move_on_globe(
        self,
        component_name: str,
        destination: GeoPoint,
        movement_sensor_name: str,
        obstacles: Optional[Sequence[GeoGeometry]] = None,
        heading: Optional[float] = None,
        configuration: Optional[MotionConfiguration] = None,
        *,
        bounding_regions: Optional[Sequence[GeoGeometry]] = None,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> str:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MoveOnGlobeRequest(
            name=self.name,
            component_name=_validate_name(component_name, "component_name"),
            destination=destination,
            movement_sensor_name=_validate_name(movement_sensor_name, "movement_sensor_name"),
            obstacles=obstacles,
            heading=heading,
            motion_configuration=configuration,
            bounding_regions=bounding_regions,
            extra=dict_to_struct(extra),
        )
        response: MoveOnGlobeResponse = await self.client.MoveOnGlobe(request, timeout=timeout, metadata=md)
        return response.execution_id

    async def move_on_map(
        self,
        component_name: str,
        destination: Pose,
        slam_service_name: str,
        configuration: Optional[MotionConfiguration] = None,
        obstacles: Optional[Sequence[Geometry]] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> str:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MoveOnMapRequest(
            name=self.name,
            destination=destination,
            component_name=_validate_name(component_name, "component_name"),
            slam_service_name=_validate_name(slam_service_name, "slam_service_name"),
            motion_configuration=configuration,
            obstacles=obstacles,
            extra=dict_to_struct(extra),
        )
        response: MoveOnMapResponse = await self.client.MoveOnMap(request, timeout=timeout, metadata=md)
        return response.execution_id

    async def stop_plan(
        self,
        component_name: str,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        md = kwargs.get("metadata", self.Metadata()).proto

        request = StopPlanRequest(
            name=self.name,
            component_name=_validate_name(component_name, "component_name"),
            extra=dict_to_struct(extra),
        )
        _: StopPlanResponse = await self.client.StopPlan(request, timeout=timeout, metadata=md)
        return

    async def get_plan(
        self,
        component_name: str,
        last_plan_only: bool = False,
        execution_id: Optional[str] = None,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> GetPlanResponse:
        md = kwargs.get("metadata", self.Metadata()).proto

        request = GetPlanRequest(
            name=self.name,
            component_name=_validate_name(component_name, "component_name"),
            last_plan_only=last_plan_only,
            execution_id=execution_id,
            extra=dict_to_struct(extra),
        )
        response: GetPlanResponse = await self.client.GetPlan(request, timeout=timeout, metadata=md)
        return response

    async def list_plan_statuses(
        self,
        only_active_plans: bool = False,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Sequence[PlanStatusWithID]:
        md = kwargs.get("metadata", self.Metadata()).proto

        request = ListPlanStatusesRequest(
            name=self.name,
            only_active_plans=only_active_plans,
            extra=dict_to_struct(extra),
        )
        response: ListPlanStatusesResponse = await self.client.ListPlanStatuses(request, timeout=timeout, metadata=md)
        return response.plan_statuses_with_ids

    async def get_pose(
        self,
        component_name: str,
        destination_frame: str,
        supplemental_transforms: Optional[Sequence[Transform]] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> PoseInFrame:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetPoseRequest(
            name=self.name,
            component_name=_validate_name(component_name, "component_name"),
            destination_frame=destination_frame,
            supplemental_transforms=supplemental_transforms,
            extra=dict_to_struct(extra),
        )
        response: GetPoseResponse = await self.client.GetPose(request, timeout=timeout, metadata=md)
        return response.pose

    async def temp_stream_arm_joint_positions(  # type: ignore
        self,
        component_name: str,
        target_batches: AsyncIterator[Sequence[JointPositions]],
        options: Optional[Motion.StreamOptions] = None,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> AsyncIterator[None]:
        md = kwargs.get("metadata", self.Metadata()).proto
        # A timeout, if the caller supplies one, bounds the whole stream rather than a single
        # message, so it defaults to none; binding a deadline here would cancel a long but
        # healthy session partway through.
        async with self.client.TempStreamArmJointPositions.open(timeout=timeout, metadata=md) as stream:
            await stream.send_message(
                TempStreamArmJointPositionsRequest(
                    name=self.name,
                    init=TempStreamArmJointPositionsRequest.Init(
                        component_name=_validate_name(component_name, "component_name"),
                        options=options.to_proto() if options is not None else None,
                        extra=dict_to_struct(extra),
                    ),
                )
            )

            # Sending and receiving run concurrently as tasks: the motion service can report an
            # acknowledgement or a fault at any point, including while the caller is still
            # producing target batches. An async generator cannot yield a value produced inside a
            # task, so the receive task feeds a queue that this generator drains and yields from;
            # a sentinel marks the point past which no more acknowledgements will arrive.
            #
            # A failure of the caller's own target iterator is recorded separately. It is the
            # caller's bug and the fault they need to see, so it wins over whatever the receive
            # side reports while the stream is torn down.
            producer_exception: Optional[BaseException] = None
            acks: asyncio.Queue = asyncio.Queue()
            end_of_acks = object()

            async def send_targets() -> None:
                nonlocal producer_exception
                try:
                    async for batch in target_batches:
                        await stream.send_message(
                            TempStreamArmJointPositionsRequest(
                                targets=TempStreamArmJointPositionsRequest.Targets(positions=list(batch)),
                            )
                        )
                    # Targets exhausted cleanly; half-close so the motion service knows the session completed.
                    await stream.end()
                except asyncio.CancelledError:
                    # Our own teardown cancelling this task, not the caller's failure.
                    raise
                except BaseException as exc:
                    producer_exception = exc
                    raise

            async def receive_acks() -> None:
                try:
                    while True:
                        ack = await stream.recv_message()
                        if ack is None:
                            break
                        acks.put_nowait(ack)
                finally:
                    acks.put_nowait(end_of_acks)

            send_task = asyncio.create_task(send_targets())
            receive_task = asyncio.create_task(receive_acks())

            # If the producer fails, stop receiving so the queue terminates and the fault can be
            # surfaced. A clean producer finish leaves the receive alone: the motion service still
            # has acknowledgements to send until it closes the response stream itself.
            def stop_receiving_if_producer_failed(task: asyncio.Task) -> None:
                if not task.cancelled() and task.exception() is not None:
                    receive_task.cancel()

            send_task.add_done_callback(stop_receiving_if_producer_failed)

            try:
                while True:
                    ack = await acks.get()
                    if ack is end_of_acks:
                        break
                    yield None
            finally:
                # Before the `async with` resets the stream, make sure both tasks have finished and
                # their outcomes have been retrieved, so neither is parked in a read or write during
                # the reset. A parked read is exactly what deadlocks a direct stream.cancel(); the
                # reset that aborts the session comes from leaving the `async with` instead. A
                # finished task's result is retrieved with `.exception()` rather than by awaiting it,
                # which keeps a recorded producer failure's traceback pointed at the caller's code.
                for task in (send_task, receive_task):
                    if task.done():
                        if not task.cancelled():
                            task.exception()
                    else:
                        task.cancel()
                        try:
                            await task
                        except BaseException:
                            pass

            # Surface the terminal cause: the caller's producer failure first, then a fault from the
            # receive side, otherwise the stream completed cleanly. Raising leaves the `async with`,
            # which resets the stream so the motion service sees an abort rather than a clean end.
            if producer_exception is not None:
                raise producer_exception
            if not receive_task.cancelled():
                receive_error = receive_task.exception()
                if receive_error is not None:
                    raise receive_error

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = DoCommandRequest(name=self.name, command=dict_to_struct(command))
        response: DoCommandResponse = await self.client.DoCommand(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)

    async def get_status(
        self,
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetStatusRequest(name=self.name)
        response: GetStatusResponse = await self.client.GetStatus(request, timeout=timeout, metadata=md)
        return struct_to_dict(response.result)

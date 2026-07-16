import asyncio
from typing import Any, AsyncIterator, Dict, List, Mapping, Optional

from grpclib.client import Channel

from viam.components import KinematicsReturn
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    Geometry,
    GetKinematicsRequest,
    GetKinematicsResponse,
    GetStatusRequest,
    GetStatusResponse,
)
from viam.proto.component.arm import (
    ArmServiceStub,
    GetEndPositionRequest,
    GetEndPositionResponse,
    GetJointPositionsRequest,
    GetJointPositionsResponse,
    IsMovingRequest,
    IsMovingResponse,
    JointPositions,
    MoveToJointPositionsRequest,
    MoveThroughJointPositionsRequest,
    MoveThroughJointPositionsStreamedRequest,
    MoveToPositionRequest,
    StopRequest,
)
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.utils import ValueTypes, dict_to_struct, get_geometries, struct_to_dict

from . import Arm, Pose


class ArmClient(Arm, ReconfigurableResourceRPCClientBase):
    """
    gRPC client for an Arm component.

    Used to communicate with an existing ``Arm`` implementation over gRPC.
    """

    def __init__(self, name: str, channel: Channel):
        self.channel = channel
        self.client = ArmServiceStub(channel)
        super().__init__(name)

    async def get_end_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Pose:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetEndPositionRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetEndPositionResponse = await self.client.GetEndPosition(request, timeout=timeout, metadata=md)
        return response.pose

    async def move_to_position(
        self,
        pose: Pose,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MoveToPositionRequest(name=self.name, to=pose, extra=dict_to_struct(extra))
        await self.client.MoveToPosition(request, timeout=timeout, metadata=md)

    async def get_joint_positions(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> JointPositions:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetJointPositionsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetJointPositionsResponse = await self.client.GetJointPositions(request, timeout=timeout, metadata=md)
        return response.positions

    async def move_to_joint_positions(
        self,
        positions: JointPositions,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MoveToJointPositionsRequest(name=self.name, positions=positions, extra=dict_to_struct(extra))
        await self.client.MoveToJointPositions(request, timeout=timeout, metadata=md)

    async def move_through_joint_positions(
        self,
        positions: List[JointPositions],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = MoveThroughJointPositionsRequest(name=self.name, positions=positions, extra=dict_to_struct(extra))
        await self.client.MoveThroughJointPositions(request, timeout=timeout, metadata=md)

    async def move_through_joint_positions_streamed(  # type: ignore
        self,
        batches: AsyncIterator[List[Arm.TrajectoryPoint]],
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> AsyncIterator[Arm.TrajectoryUpdate]:
        md = kwargs.get("metadata", self.Metadata()).proto
        # A timeout, if the caller supplies one, bounds the whole stream rather than a single
        # message, so it defaults to none; binding a deadline here would cancel a long but
        # healthy trajectory partway through.
        async with self.client.MoveThroughJointPositionsStreamed.open(timeout=timeout, metadata=md) as stream:
            await stream.send_message(
                MoveThroughJointPositionsStreamedRequest(
                    name=self.name,
                    init=MoveThroughJointPositionsStreamedRequest.Init(
                        extra=dict_to_struct(extra),
                    ),
                )
            )

            # Sending and receiving run concurrently as tasks: the arm can report an update or a
            # fault at any point, including while the caller is still producing batches. An async
            # generator cannot yield a value produced inside a task, so the receive task feeds a
            # queue that this generator drains and yields from; a sentinel marks the point past
            # which no more updates will arrive. Each list the caller yields becomes one wire
            # TrajectoryBatch.
            #
            # A failure of the caller's own batch iterator is recorded separately. It is the
            # caller's bug and the fault they need to see, so it wins over whatever the receive side
            # reports while the stream is torn down.
            producer_exception: Optional[BaseException] = None
            updates: asyncio.Queue = asyncio.Queue()
            end_of_updates = object()

            async def send_batches() -> None:
                nonlocal producer_exception
                try:
                    async for batch in batches:
                        await stream.send_message(
                            MoveThroughJointPositionsStreamedRequest(
                                batch=MoveThroughJointPositionsStreamedRequest.TrajectoryBatch(
                                    points=[point.to_proto() for point in batch],
                                )
                            )
                        )
                    # Batches exhausted cleanly; half-close so the arm knows the trajectory completed.
                    await stream.end()
                except asyncio.CancelledError:
                    # Our own teardown cancelling this task, not the caller's failure.
                    raise
                except BaseException as exc:
                    producer_exception = exc
                    raise

            async def receive_updates() -> None:
                try:
                    while True:
                        update = await stream.recv_message()
                        if update is None:
                            break
                        updates.put_nowait(update)
                finally:
                    updates.put_nowait(end_of_updates)

            send_task = asyncio.create_task(send_batches())
            receive_task = asyncio.create_task(receive_updates())

            # If the producer fails, stop receiving so the queue terminates and the fault can be
            # surfaced. A clean producer finish leaves the receive alone: the arm still has updates
            # to send until it closes the response stream itself.
            def stop_receiving_if_producer_failed(task: asyncio.Task) -> None:
                if not task.cancelled() and task.exception() is not None:
                    receive_task.cancel()

            send_task.add_done_callback(stop_receiving_if_producer_failed)

            try:
                while True:
                    update = await updates.get()
                    if update is end_of_updates:
                        break
                    yield Arm.TrajectoryUpdate.from_proto(update)
            finally:
                # Before the `async with` resets the stream, make sure both tasks have finished and
                # their outcomes have been retrieved, so neither is parked in a read or write during
                # the reset. A parked read is exactly what deadlocks a direct stream.cancel(); the
                # reset that aborts the arm comes from leaving the `async with` instead. A finished
                # task's result is retrieved with `.exception()` rather than by awaiting it, which
                # keeps a recorded producer failure's traceback pointed at the caller's code.
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
            # which resets the stream so the arm sees an abort rather than a clean end.
            if producer_exception is not None:
                raise producer_exception
            if not receive_task.cancelled():
                receive_error = receive_task.exception()
                if receive_error is not None:
                    raise receive_error

    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        md = kwargs.get("metadata", self.Metadata()).proto
        request = StopRequest(name=self.name, extra=dict_to_struct(extra))
        await self.client.Stop(request, timeout=timeout, metadata=md)

    async def is_moving(self, *, timeout: Optional[float] = None, **kwargs) -> bool:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = IsMovingRequest(name=self.name)
        response: IsMovingResponse = await self.client.IsMoving(request, timeout=timeout, metadata=md)
        return response.is_moving

    async def do_command(
        self,
        command: Mapping[str, Any],
        *,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Mapping[str, ValueTypes]:
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

    async def get_kinematics(
        self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> KinematicsReturn:
        md = kwargs.get("metadata", self.Metadata()).proto
        request = GetKinematicsRequest(name=self.name, extra=dict_to_struct(extra))
        response: GetKinematicsResponse = await self.client.GetKinematics(request, timeout=timeout, metadata=md)
        return (response.format, response.kinematics_data, response.meshes_by_urdf_filepath)

    async def get_geometries(self, *, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> List[Geometry]:
        md = kwargs.get("metadata", self.Metadata())
        return await get_geometries(self.client, self.name, extra, timeout, md)

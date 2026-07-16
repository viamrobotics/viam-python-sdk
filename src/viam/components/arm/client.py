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

            # Sending and receiving proceed at the same time: the arm can report an update or a
            # fault at any point, including while the caller is still producing batches. The sends
            # run on their own task and the receives on another; this loop watches both and yields
            # each update to the caller as it arrives. Each list the caller yields becomes one wire
            # TrajectoryBatch.
            #
            # A failure of the caller's own batch iterator is held separately. It is the caller's
            # bug and the fault they need to see, so it wins over whatever the receive side reports
            # while the stream is torn down.
            producer_exception: Optional[BaseException] = None

            async def send_batches() -> None:
                nonlocal producer_exception
                iterator = batches.__aiter__()
                while True:
                    try:
                        batch = await iterator.__anext__()
                        message = MoveThroughJointPositionsStreamedRequest(
                            batch=MoveThroughJointPositionsStreamedRequest.TrajectoryBatch(
                                points=[point.to_proto() for point in batch],
                            )
                        )
                    except StopAsyncIteration:
                        break
                    except asyncio.CancelledError:
                        raise
                    except BaseException as exc:
                        # Record the caller's producer failure and stop. The main loop surfaces it
                        # and aborts the stream. We deliberately do not tear the stream down here:
                        # calling stream.cancel() from this task deadlocks against the concurrent
                        # receive (confirmed end to end against a real server, not just in tests).
                        producer_exception = exc
                        raise
                    await stream.send_message(message)
                # Batches exhausted cleanly; half-close so the arm knows the trajectory completed.
                await stream.end()

            send_task = asyncio.create_task(send_batches())
            recv_task = asyncio.ensure_future(stream.recv_message())
            watch_send = True
            try:
                while True:
                    wait_set = {recv_task, send_task} if watch_send else {recv_task}
                    await asyncio.wait(wait_set, return_when=asyncio.FIRST_COMPLETED)

                    # Handle the send task finishing before consuming any ready update. A clean
                    # finish (batches exhausted and half-closed) just means we stop watching it and
                    # keep receiving until the server closes. A failure means the caller's producer
                    # broke, so we abort by raising into the handler below. The handler tears down
                    # the still-pending receive before the `async with` resets the stream, so nothing
                    # is parked in a read when the reset happens; that is precisely what a direct
                    # stream.cancel() from the send task cannot manage without deadlocking.
                    if watch_send and send_task.done():
                        watch_send = False
                        send_error = send_task.exception()
                        if send_error is not None:
                            raise send_error

                    if recv_task.done():
                        update = recv_task.result()
                        if update is None:
                            # The server closed the response stream: the trajectory is complete.
                            break
                        yield Arm.TrajectoryUpdate.from_proto(update)
                        recv_task = asyncio.ensure_future(stream.recv_message())
            except BaseException:
                # The receive side raised (a server fault or cancellation), the producer failed, or
                # the caller closed this generator. Cancel both tasks and wait them out so neither is
                # left parked in a read or write when the `async with` resets the stream. Prefer the
                # caller's producer failure when there is one.
                for task in (send_task, recv_task):
                    task.cancel()
                    try:
                        await task
                    except BaseException:
                        pass
                if producer_exception is not None:
                    raise producer_exception
                raise
            else:
                # Clean completion: the server closed the response stream after we half-closed. Wait
                # on the send task so a producer failure that raced in right at the end still surfaces.
                await send_task

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

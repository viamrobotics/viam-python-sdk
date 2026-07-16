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

            # Sending and receiving have to proceed at the same time. The arm can report an update
            # or a fault at any point, including while the caller is still producing batches, so we
            # run the sends on a background task and drain the arm's updates here. Each list the
            # caller yields becomes one wire TrajectoryBatch.
            #
            # We hold onto a failure of the caller's own iterator separately. If the caller's batch
            # production raises, that is the caller's bug and the fault they need to see, so it wins
            # over whatever the receive side reports once we tear the stream down (which is usually
            # just a consequence of that same failure).
            producer_exception: Optional[BaseException] = None

            async def send_batches() -> None:
                nonlocal producer_exception
                try:
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
                            # Our own teardown, not the caller's failure; do not claim it as one.
                            raise
                        except BaseException as exc:
                            producer_exception = exc
                            raise
                        await stream.send_message(message)
                finally:
                    # TODO: half-closing is right when the caller's batches are exhausted, but it
                    # also runs when the caller's batch production raised, and there it is wrong. A
                    # half-close tells the arm the trajectory completed normally, when a producer
                    # failure has actually left it truncated, so the arm may be brought to rest at a
                    # point that was never meant to be its last. The C++ SDK cancels the RPC in this
                    # case so the arm sees an abort. Matching that here is not a one-line change:
                    # awaiting stream.cancel() from this task deadlocks against the concurrent
                    # receive loop. A correct fix restructures the teardown to await the receive and
                    # the send together, cancel the pending receive when the producer fails, and let
                    # the producer exception propagate out of the `async with` so grpclib resets the
                    # stream. Deferred to a focused follow-up.
                    await stream.end()

            send_task = asyncio.create_task(send_batches())
            try:
                async for update in stream:
                    yield Arm.TrajectoryUpdate.from_proto(update)
            except BaseException:
                # The receive side ended abnormally: the arm faulted, the caller closed this
                # generator, or the call was cancelled. Cancel the send task, discard whatever it
                # unwinds with, and re-raise, preferring a producer failure over the receive-side
                # error.
                send_task.cancel()
                try:
                    await send_task
                except BaseException:
                    pass
                if producer_exception is not None:
                    raise producer_exception
                raise
            else:
                # The receive side finished cleanly. Wait on the send task so that a failure in the
                # caller's batch production still surfaces rather than being swallowed.
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

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
    ) -> AsyncIterator[Arm.Response]:
        md = kwargs.get("metadata", self.Metadata()).proto
        async with self.client.MoveThroughJointPositionsStreamed.open(timeout=timeout, metadata=md) as stream:
            await stream.send_message(
                MoveThroughJointPositionsStreamedRequest(
                    name=self.name,
                    init=MoveThroughJointPositionsStreamedRequest.Init(
                        extra=dict_to_struct(extra),
                    ),
                )
            )

            # Drive the caller-supplied batch iterator on a background task so that send
            # and receive proceed independently -- arm-side acknowledgements and errors
            # may surface at any time, including while the caller is still producing
            # batches. Each list yielded by the caller maps 1:1 to one wire TrajectoryBatch.
            async def send_loop() -> None:
                try:
                    async for batch in batches:
                        await stream.send_message(
                            MoveThroughJointPositionsStreamedRequest(
                                batch=MoveThroughJointPositionsStreamedRequest.TrajectoryBatch(
                                    points=[point.to_proto() for point in batch],
                                ),
                            )
                        )
                finally:
                    await stream.end()

            send_task = asyncio.create_task(send_loop())
            try:
                async for response in stream:
                    yield Arm.Response.from_proto(response)
            except BaseException:
                # Recv side raised (a gRPC status from the server, the generator being
                # closed by the consumer, or cancellation). Tear down the send side
                # and suppress whatever it produces -- the recv-side cause is what
                # the caller needs to see, not a downstream send-side cleanup error.
                send_task.cancel()
                try:
                    await send_task
                except BaseException:
                    pass
                raise
            else:
                # Recv side completed normally. Surface any send-side failure --
                # most importantly, an exception from the caller's points iterator,
                # which would otherwise be silently swallowed and defeat the whole
                # point of the bidi shape.
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

from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.component.posetracker import GetPosesRequest, GetPosesResponse, PoseTrackerServiceBase

from .pose_tracker import PoseTracker


class PoseTrackerService(PoseTrackerServiceBase, ComponentServiceBase[PoseTracker]):
    """
    gRPC service for a pose tracker
    """

    RESOURCE_TYPE = PoseTracker

    async def GetPoses(self, stream: Stream[GetPosesRequest, GetPosesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            pose_tracker = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error
        poses = await pose_tracker.get_poses(list(request.body_names))
        await stream.send_message(GetPosesResponse(body_poses=poses))

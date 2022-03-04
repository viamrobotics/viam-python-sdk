from grpclib.server import Stream
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError
from viam.proto.api.component.posetracker import (GetPosesRequest,
                                                  GetPosesResponse,
                                                  PoseTrackerServiceBase)

from .pose_tracker import PoseTrackerBase


class PoseTrackerService(
    PoseTrackerServiceBase,
    ComponentServiceBase[PoseTrackerBase]
):
    """
    gRPC service for a pose tracker
    """

    RESOURCE_TYPE = PoseTrackerBase

    async def GetPoses(
        self,
        stream: Stream[GetPosesRequest, GetPosesResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        try:
            pose_tracker = self.get_component(name)
        except ComponentNotFoundError as e:
            raise e.grpc_error()
        poses = await pose_tracker.get_poses(list(request.body_names))
        await stream.send_message(GetPosesResponse(body_poses=poses))

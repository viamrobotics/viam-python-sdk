# TODO: Update type checking based with RSDK-4089
# pyright: reportGeneralTypeIssues=false
from google.api.httpbody_pb2 import HttpBody
from grpclib.server import Stream

from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetGeometriesResponse
from viam.proto.component.camera import (
    CameraServiceBase,
    GetImageRequest,
    GetImageResponse,
    GetImagesRequest,
    GetImagesResponse,
    GetPointCloudRequest,
    GetPointCloudResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    Image,
    RenderFrameRequest,
)
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.utils import dict_to_struct, struct_to_dict

from . import Camera


class CameraRPCService(CameraServiceBase, ResourceRPCServiceBase[Camera]):
    """
    gRPC Service for a generic Camera
    """

    RESOURCE_TYPE = Camera

    async def GetImage(self, stream: Stream[GetImageRequest, GetImageResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        camera = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        image_data, mime_type = await camera.get_image(
            request.mime_type, timeout=timeout, extra=struct_to_dict(request.extra), metadata=stream.metadata
        )
        response = GetImageResponse(mime_type=mime_type, image=image_data)
        await stream.send_message(response)

    async def RenderFrame(self, stream: Stream[RenderFrameRequest, HttpBody]) -> None:
        request = await stream.recv_message()
        assert request is not None
        camera = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        frame_data = await camera.render_frame(
            request.mime_type, timeout=timeout, extra=struct_to_dict(request.extra), metadata=stream.metadata
        )
        response = HttpBody(data=frame_data, content_type=request.mime_type if request.mime_type else "image/jpeg")
        await stream.send_message(response)

    async def GetImages(self, stream: Stream[GetImagesRequest, GetImagesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        camera = self.get_resource(request.name)

        timeout = stream.deadline.time_remaining() if stream.deadline else None
        images, metadata = await camera.get_images(
            timeout=timeout,
            metadata=stream.metadata,
            extra=struct_to_dict(request.extra),
            filter_source_names=request.filter_source_names,
        )
        img_bytes_lst = []
        for img in images:
            img_bytes = img.data
            img_bytes_lst.append(Image(source_name=img.name, mime_type=img.mime_type, image=img_bytes))
        response = GetImagesResponse(images=img_bytes_lst, response_metadata=metadata)
        await stream.send_message(response)

    async def GetPointCloud(self, stream: Stream[GetPointCloudRequest, GetPointCloudResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        camera = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        pc, mimetype = await camera.get_point_cloud(timeout=timeout, extra=struct_to_dict(request.extra), metadata=stream.metadata)
        response = GetPointCloudResponse(mime_type=mimetype, point_cloud=pc)
        await stream.send_message(response)

    async def GetProperties(self, stream: Stream[GetPropertiesRequest, GetPropertiesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name = request.name
        camera = self.get_resource(name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        properties = await camera.get_properties(timeout=timeout, metadata=stream.metadata)
        await stream.send_message(properties)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        camera = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        result = await camera.do_command(command=struct_to_dict(request.command), timeout=timeout, metadata=stream.metadata)
        response = DoCommandResponse(result=dict_to_struct(result))
        await stream.send_message(response)

    async def GetGeometries(self, stream: Stream[GetGeometriesRequest, GetGeometriesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        camera = self.get_resource(request.name)
        timeout = stream.deadline.time_remaining() if stream.deadline else None
        geometries = await camera.get_geometries(extra=struct_to_dict(request.extra), timeout=timeout)
        response = GetGeometriesResponse(geometries=geometries)
        await stream.send_message(response)

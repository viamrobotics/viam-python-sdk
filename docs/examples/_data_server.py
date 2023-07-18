import asyncio

from grpclib.utils import graceful_exit
from grpclib.server import Server, Stream
from google.protobuf.struct_pb2 import Struct

from viam.proto.app.data import (
    AddBoundingBoxToImageByIDResponse,
    AddBoundingBoxToImageByIDRequest,
    AddTagsToBinaryDataByFilterRequest,
    AddTagsToBinaryDataByFilterResponse,
    AddTagsToBinaryDataByIDsRequest,
    AddTagsToBinaryDataByIDsResponse,
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BoundingBoxLabelsByFilterRequest,
    BoundingBoxLabelsByFilterResponse,
    DataServiceBase,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteTabularDataByFilterRequest,
    DeleteTabularDataByFilterResponse,
    RemoveBoundingBoxFromImageByIDResponse,
    RemoveBoundingBoxFromImageByIDRequest,
    RemoveTagsFromBinaryDataByFilterRequest,
    RemoveTagsFromBinaryDataByFilterResponse,
    RemoveTagsFromBinaryDataByIDsRequest,
    RemoveTagsFromBinaryDataByIDsResponse,
    TabularData,
    TabularDataByFilterRequest,
    TabularDataByFilterResponse,
    TagsByFilterRequest,
    TagsByFilterResponse,
)
from viam.proto.app.datasync import (
    DataCaptureUploadRequest,
    DataCaptureUploadResponse,
    DataSyncServiceBase,
    FileUploadRequest,
    FileUploadResponse,
)


class MockData(DataServiceBase):
    def __init__(self):
        self.tabular_data_requested = False
        self.tabular_response = [{"PowerPct": 0, "IsPowered": False}, {"PowerPct": 0, "IsPowered": False}, {"Position": 0}]

    async def TabularDataByFilter(self, stream: [TabularDataByFilterRequest, TabularDataByFilterResponse]) -> None:
        if self.tabular_data_requested:
            await stream.send_message(TabularDataByFilterResponse())
            return
        self.tabular_data_requested = True
        _ = await stream.recv_message()
        n = len(self.tabular_response)
        tabular_structs = [None] * n
        for i in range(n):
            s = Struct()
            s.update(self.tabular_response[i])
            tabular_structs[i] = s
        await stream.send_message(TabularDataByFilterResponse(data=[TabularData(data=struct) for struct in tabular_structs]))

    async def BinaryDataByFilter(self, stream: Stream[BinaryDataByFilterRequest, BinaryDataByFilterResponse]) -> None:
        pass

    async def BinaryDataByIDs(self, stream: Stream[BinaryDataByIDsRequest, BinaryDataByIDsResponse]) -> None:
        pass

    async def DeleteTabularDataByFilter(self, stream: Stream[DeleteTabularDataByFilterRequest, DeleteTabularDataByFilterResponse]) -> None:
        pass

    async def DeleteBinaryDataByFilter(self, stream: Stream[DeleteBinaryDataByFilterRequest, DeleteBinaryDataByFilterResponse]) -> None:
        pass

    async def DeleteBinaryDataByIDs(self, stream: Stream[DeleteBinaryDataByIDsRequest, DeleteBinaryDataByIDsResponse]) -> None:
        pass

    async def AddTagsToBinaryDataByIDs(self, stream: Stream[AddTagsToBinaryDataByIDsRequest, AddTagsToBinaryDataByIDsResponse]) -> None:
        pass

    async def AddTagsToBinaryDataByFilter(
        self,
        stream: Stream[AddTagsToBinaryDataByFilterRequest, AddTagsToBinaryDataByFilterResponse]
    ) -> None:
        pass

    async def RemoveTagsFromBinaryDataByIDs(
        self,
        stream: Stream[RemoveTagsFromBinaryDataByIDsRequest, RemoveTagsFromBinaryDataByIDsResponse]
    ) -> None:
        pass

    async def RemoveTagsFromBinaryDataByFilter(
        self,
        stream: Stream[RemoveTagsFromBinaryDataByFilterRequest, RemoveTagsFromBinaryDataByFilterResponse]
    ) -> None:
        pass

    async def TagsByFilter(self, stream: Stream[TagsByFilterRequest, TagsByFilterResponse]) -> None:
        pass

    async def AddBoundingBoxToImageByID(
        self,
        stream: Stream[AddBoundingBoxToImageByIDRequest, AddBoundingBoxToImageByIDResponse]
    ) -> None:
        pass

    async def RemoveBoundingBoxFromImageByID(
        self,
        stream: Stream[RemoveBoundingBoxFromImageByIDRequest, RemoveBoundingBoxFromImageByIDResponse]
    ) -> None:
        pass

    async def BoundingBoxLabelsByFilter(self, stream: Stream[BoundingBoxLabelsByFilterRequest, BoundingBoxLabelsByFilterResponse]) -> None:
        pass


class MockDataSync(DataSyncServiceBase):
    async def DataCaptureUpload(self, stream: Stream[DataCaptureUploadRequest, DataCaptureUploadResponse]) -> None:
        await stream.send_message(DataCaptureUploadResponse())

    async def FileUpload(self, stream: Stream[FileUploadRequest, FileUploadResponse]) -> None:
        pass


async def main(*, host: str = '127.0.0.1', port: int = 9092) -> None:
    data_server = Server([MockData(), MockDataSync()])
    with graceful_exit([data_server]):
        await data_server.start(host, port)
        await data_server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())

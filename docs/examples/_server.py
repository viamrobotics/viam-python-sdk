import asyncio
from datetime import datetime

from google.protobuf.struct_pb2 import Struct, Value
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.server import Server, Stream
from grpclib.utils import graceful_exit

from viam.app.data_client import DataClient
from viam.proto.app import (
    AddRoleRequest,
    AddRoleResponse,
    ChangeRoleRequest,
    ChangeRoleResponse,
    CheckPermissionsRequest,
    CheckPermissionsResponse,
    CreateFragmentRequest,
    CreateFragmentResponse,
    CreateKeyFromExistingKeyAuthorizationsRequest,
    CreateKeyFromExistingKeyAuthorizationsResponse,
    CreateKeyRequest,
    CreateKeyResponse,
    CreateLocationRequest,
    CreateLocationResponse,
    CreateLocationSecretRequest,
    CreateLocationSecretResponse,
    CreateModuleRequest,
    CreateModuleResponse,
    CreateOrganizationInviteRequest,
    CreateOrganizationInviteResponse,
    CreateOrganizationRequest,
    CreateOrganizationResponse,
    CreateRegistryItemRequest,
    CreateRegistryItemResponse,
    CreateRobotPartSecretRequest,
    CreateRobotPartSecretResponse,
    DeleteFragmentRequest,
    DeleteFragmentResponse,
    DeleteKeyRequest,
    DeleteKeyResponse,
    DeleteLocationRequest,
    DeleteLocationResponse,
    DeleteLocationSecretRequest,
    DeleteLocationSecretResponse,
    DeleteOrganizationInviteRequest,
    DeleteOrganizationInviteResponse,
    DeleteOrganizationMemberRequest,
    DeleteOrganizationMemberResponse,
    DeleteOrganizationRequest,
    DeleteOrganizationResponse,
    DeleteRegistryItemRequest,
    DeleteRegistryItemResponse,
    DeleteRobotPartRequest,
    DeleteRobotPartResponse,
    DeleteRobotPartSecretRequest,
    DeleteRobotPartSecretResponse,
    DeleteRobotRequest,
    DeleteRobotResponse,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationNamespaceAvailabilityRequest,
    GetOrganizationNamespaceAvailabilityResponse,
    GetOrganizationRequest,
    GetOrganizationResponse,
    GetOrganizationsWithAccessToLocationRequest,
    GetOrganizationsWithAccessToLocationResponse,
    GetRegistryItemRequest,
    GetRegistryItemResponse,
    GetRobotAPIKeysRequest,
    GetRobotAPIKeysResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartRequest,
    GetRobotPartResponse,
    GetRobotPartsRequest,
    GetRobotPartsResponse,
    GetRobotRequest,
    GetRobotResponse,
    GetRoverRentalRobotsRequest,
    GetRoverRentalRobotsResponse,
    GetUserIDByEmailRequest,
    GetUserIDByEmailResponse,
    ListAuthorizationsRequest,
    ListAuthorizationsResponse,
    ListFragmentsRequest,
    ListFragmentsResponse,
    ListKeysRequest,
    ListKeysResponse,
    ListLocationsRequest,
    ListLocationsResponse,
    ListModulesRequest,
    ListModulesResponse,
    ListOrganizationMembersRequest,
    ListOrganizationMembersResponse,
    ListOrganizationsByUserRequest,
    ListOrganizationsByUserResponse,
    ListOrganizationsRequest,
    ListOrganizationsResponse,
    ListRegistryItemsRequest,
    ListRegistryItemsResponse,
    ListRobotsRequest,
    ListRobotsResponse,
    Location,
    LocationAuthRequest,
    LocationAuthResponse,
    MarkPartAsMainRequest,
    MarkPartAsMainResponse,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    RemoveRoleRequest,
    RemoveRoleResponse,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
    RotateKeyRequest,
    RotateKeyResponse,
    ShareLocationRequest,
    ShareLocationResponse,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    UnimplementedAppServiceBase,
    UnshareLocationRequest,
    UnshareLocationResponse,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRegistryItemRequest,
    UpdateRegistryItemResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    UploadModuleFileResponse,
)
from viam.proto.app.data import (
    AddBinaryDataToDatasetByIDsRequest,
    AddBinaryDataToDatasetByIDsResponse,
    AddBoundingBoxToImageByIDRequest,
    AddBoundingBoxToImageByIDResponse,
    UpdateBoundingBoxRequest,
    UpdateBoundingBoxResponse,
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
    CaptureMetadata,
    ConfigureDatabaseUserRequest,
    ConfigureDatabaseUserResponse,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteTabularDataRequest,
    DeleteTabularDataResponse,
    GetDatabaseConnectionRequest,
    GetDatabaseConnectionResponse,
    RemoveBinaryDataFromDatasetByIDsRequest,
    RemoveBinaryDataFromDatasetByIDsResponse,
    RemoveBoundingBoxFromImageByIDRequest,
    RemoveBoundingBoxFromImageByIDResponse,
    RemoveTagsFromBinaryDataByFilterRequest,
    RemoveTagsFromBinaryDataByFilterResponse,
    RemoveTagsFromBinaryDataByIDsRequest,
    RemoveTagsFromBinaryDataByIDsResponse,
    TabularData,
    TabularDataByFilterRequest,
    TabularDataByFilterResponse,
    TabularDataByMQLRequest,
    TabularDataByMQLResponse,
    TabularDataBySQLRequest,
    TabularDataBySQLResponse,
    TagsByFilterRequest,
    TagsByFilterResponse,
    UnimplementedDataServiceBase,
)
from viam.proto.app.datasync import (
    DataCaptureUploadRequest,
    DataCaptureUploadResponse,
    DataSyncServiceBase,
    FileUploadRequest,
    FileUploadResponse,
    StreamingDataCaptureUploadRequest,
    StreamingDataCaptureUploadResponse,
)
from viam.proto.common import LogEntry as LogEntryPB
from viam.utils import datetime_to_timestamp, dict_to_struct, value_to_primitive


class MockData(UnimplementedDataServiceBase):
    def __init__(self):
        self.tabular_data_requested = False
        self.tabular_response = [
            DataClient.TabularData(
                {"PowerPct": 0, "IsPowered": False},
                CaptureMetadata(method_name="IsPowered"),
                datetime(2022, 1, 1, 1, 1, 1),
                datetime(2022, 12, 31, 23, 59, 59),
            ),
            DataClient.TabularData(
                {"PowerPct": 0, "IsPowered": False}, CaptureMetadata(location_id="loc-id"), datetime(2023, 1, 2), datetime(2023, 3, 4)
            ),
            DataClient.TabularData(
                {"Position": 0},
                CaptureMetadata(),
                datetime(2023, 5, 6),
                datetime(2023, 7, 8),
            ),
        ]

    async def TabularDataByFilter(self, stream: Stream[TabularDataByFilterRequest, TabularDataByFilterResponse]) -> None:
        if self.tabular_data_requested:
            await stream.send_message(TabularDataByFilterResponse())
            return
        self.tabular_data_requested = True
        _ = await stream.recv_message()
        tabular_structs = []
        tabular_metadata = [data.metadata for data in self.tabular_response]
        for idx, tabular_data in enumerate(self.tabular_response):
            tabular_structs.append(
                TabularData(
                    data=dict_to_struct(tabular_data.data),
                    metadata_index=idx,
                    time_requested=datetime_to_timestamp(tabular_data.time_requested),
                    time_received=datetime_to_timestamp(tabular_data.time_received),
                )
            )
        await stream.send_message(
            TabularDataByFilterResponse(
                data=tabular_structs,
                metadata=tabular_metadata,
            )
        )

    async def BinaryDataByFilter(self, stream: Stream[BinaryDataByFilterRequest, BinaryDataByFilterResponse]) -> None:
        pass

    async def BinaryDataByIDs(self, stream: Stream[BinaryDataByIDsRequest, BinaryDataByIDsResponse]) -> None:
        pass

    async def DeleteTabularData(self, stream: Stream[DeleteTabularDataRequest, DeleteTabularDataResponse]) -> None:
        pass

    async def DeleteBinaryDataByFilter(self, stream: Stream[DeleteBinaryDataByFilterRequest, DeleteBinaryDataByFilterResponse]) -> None:
        pass

    async def DeleteBinaryDataByIDs(self, stream: Stream[DeleteBinaryDataByIDsRequest, DeleteBinaryDataByIDsResponse]) -> None:
        pass

    async def AddTagsToBinaryDataByIDs(self, stream: Stream[AddTagsToBinaryDataByIDsRequest, AddTagsToBinaryDataByIDsResponse]) -> None:
        pass

    async def AddTagsToBinaryDataByFilter(
        self, stream: Stream[AddTagsToBinaryDataByFilterRequest, AddTagsToBinaryDataByFilterResponse]
    ) -> None:
        pass

    async def RemoveTagsFromBinaryDataByIDs(
        self, stream: Stream[RemoveTagsFromBinaryDataByIDsRequest, RemoveTagsFromBinaryDataByIDsResponse]
    ) -> None:
        pass

    async def RemoveTagsFromBinaryDataByFilter(
        self, stream: Stream[RemoveTagsFromBinaryDataByFilterRequest, RemoveTagsFromBinaryDataByFilterResponse]
    ) -> None:
        pass

    async def TagsByFilter(self, stream: Stream[TagsByFilterRequest, TagsByFilterResponse]) -> None:
        pass

    async def AddBoundingBoxToImageByID(self, stream: Stream[AddBoundingBoxToImageByIDRequest, AddBoundingBoxToImageByIDResponse]) -> None:
        pass

    async def UpdateBoundingBox(self, stream: Stream[UpdateBoundingBoxRequest, UpdateBoundingBoxResponse]) -> None:
        pass

    async def RemoveBoundingBoxFromImageByID(
        self, stream: Stream[RemoveBoundingBoxFromImageByIDRequest, RemoveBoundingBoxFromImageByIDResponse]
    ) -> None:
        pass

    async def BoundingBoxLabelsByFilter(self, stream: Stream[BoundingBoxLabelsByFilterRequest, BoundingBoxLabelsByFilterResponse]) -> None:
        pass

    async def GetDatabaseConnection(self, stream: Stream[GetDatabaseConnectionRequest, GetDatabaseConnectionResponse]) -> None:
        pass

    async def ConfigureDatabaseUser(self, stream: Stream[ConfigureDatabaseUserRequest, ConfigureDatabaseUserResponse]) -> None:
        pass

    async def AddBinaryDataToDatasetByIDs(
        self, stream: Stream[AddBinaryDataToDatasetByIDsRequest, AddBinaryDataToDatasetByIDsResponse]
    ) -> None:
        pass

    async def RemoveBinaryDataFromDatasetByIDs(
        self, stream: Stream[RemoveBinaryDataFromDatasetByIDsRequest, RemoveBinaryDataFromDatasetByIDsResponse]
    ) -> None:
        pass

    async def TabularDataBySQL(self, stream: Stream[TabularDataBySQLRequest, TabularDataBySQLResponse]) -> None:
        pass

    async def TabularDataByMQL(self, stream: Stream[TabularDataByMQLRequest, TabularDataByMQLResponse]) -> None:
        pass


class MockDataSync(DataSyncServiceBase):
    async def DataCaptureUpload(self, stream: Stream[DataCaptureUploadRequest, DataCaptureUploadResponse]) -> None:
        await stream.send_message(DataCaptureUploadResponse())

    async def FileUpload(self, stream: Stream[FileUploadRequest, FileUploadResponse]) -> None:
        pass

    async def StreamingDataCaptureUpload(
        self, stream: Stream[StreamingDataCaptureUploadRequest, StreamingDataCaptureUploadResponse]
    ) -> None:
        pass


class MockApp(UnimplementedAppServiceBase):
    def __init__(self):
        self.organization = Organization(id="id", name="name", public_namespace="public_namespace", default_region="default_region")
        self.locations = [Location()]
        self.robots = [Robot(name=f"robot-{i}") for i in range(4)]
        self.new_id = "new_id"
        self.updated_robot = Robot(id="id", name="name", location="location")
        self.log = LogEntryPB(
            host="mypi",
            level="error",
            time=Timestamp(seconds=1690824474, nanos=501000000),
            logger_name="robot_server",
            message="module config validation error; skipping",
            caller=dict_to_struct(
                {
                    "Line": 922,
                    "Function": "go.viam.com/rdk/robot/impl.(*resourceManager).updateResources",
                    "File": "/__w/rdk/rdk/robot/impl/resource_manager.go",
                    "Defined": True,
                }
            ),
            fields=[
                dict_to_struct({"Type": 15, "String": "my-module", "Key": "module", "Interface": 0, "Integer": 0}),
                dict_to_struct(
                    {
                        "Type": 26,
                        "String": "module modules.0 executable path error: stat /Users/user-1/Desktop/run.sh: no such file or directory",
                        "Key": "error",
                        "Interface": value_to_primitive(value=Value(struct_value=Struct())),
                        "Integer": 0,
                    }
                ),
            ],
        )

    async def GetUserIDByEmail(self, stream: Stream[GetUserIDByEmailRequest, GetUserIDByEmailResponse]) -> None:
        pass

    async def CreateOrganization(self, stream: Stream[CreateOrganizationRequest, CreateOrganizationResponse]) -> None:
        pass

    async def ListOrganizations(self, stream: Stream[ListOrganizationsRequest, ListOrganizationsResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(ListOrganizationsResponse(organizations=[self.organization]))

    async def ListOrganizationsByUser(self, stream: Stream[ListOrganizationsByUserRequest, ListOrganizationsByUserResponse]) -> None:
        pass

    async def GetOrganization(self, stream: Stream[GetOrganizationRequest, GetOrganizationResponse]) -> None:
        pass

    async def GetOrganizationNamespaceAvailability(
        self, stream: Stream[GetOrganizationNamespaceAvailabilityRequest, GetOrganizationNamespaceAvailabilityResponse]
    ) -> None:
        pass

    async def UpdateOrganization(self, stream: Stream[UpdateOrganizationRequest, UpdateOrganizationResponse]) -> None:
        pass

    async def DeleteOrganization(self, stream: Stream[DeleteOrganizationRequest, DeleteOrganizationResponse]) -> None:
        pass

    async def ListOrganizationMembers(self, stream: Stream[ListOrganizationMembersRequest, ListOrganizationMembersResponse]) -> None:
        pass

    async def CreateOrganizationInvite(self, stream: Stream[CreateOrganizationInviteRequest, CreateOrganizationInviteResponse]) -> None:
        pass

    async def UpdateOrganizationInviteAuthorizations(
        self, stream: Stream[UpdateOrganizationInviteAuthorizationsRequest, UpdateOrganizationInviteAuthorizationsResponse]
    ) -> None:
        pass

    async def DeleteOrganizationMember(self, stream: Stream[DeleteOrganizationMemberRequest, DeleteOrganizationMemberResponse]) -> None:
        pass

    async def DeleteOrganizationInvite(self, stream: Stream[DeleteOrganizationInviteRequest, DeleteOrganizationInviteResponse]) -> None:
        pass

    async def ResendOrganizationInvite(self, stream: Stream[ResendOrganizationInviteRequest, ResendOrganizationInviteResponse]) -> None:
        pass

    async def CreateLocation(self, stream: Stream[CreateLocationRequest, CreateLocationResponse]) -> None:
        pass

    async def GetLocation(self, stream: Stream[GetLocationRequest, GetLocationResponse]) -> None:
        pass

    async def UpdateLocation(self, stream: Stream[UpdateLocationRequest, UpdateLocationResponse]) -> None:
        pass

    async def DeleteLocation(self, stream: Stream[DeleteLocationRequest, DeleteLocationResponse]) -> None:
        pass

    async def ListLocations(self, stream: Stream[ListLocationsRequest, ListLocationsResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(ListLocationsResponse(locations=self.locations))

    async def ShareLocation(self, stream: Stream[ShareLocationRequest, ShareLocationResponse]) -> None:
        pass

    async def UnshareLocation(self, stream: Stream[UnshareLocationRequest, UnshareLocationResponse]) -> None:
        pass

    async def LocationAuth(self, stream: Stream[LocationAuthRequest, LocationAuthResponse]) -> None:
        pass

    async def CreateLocationSecret(self, stream: Stream[CreateLocationSecretRequest, CreateLocationSecretResponse]) -> None:
        pass

    async def DeleteLocationSecret(self, stream: Stream[DeleteLocationSecretRequest, DeleteLocationSecretResponse]) -> None:
        pass

    async def GetRobot(self, stream: Stream[GetRobotRequest, GetRobotResponse]) -> None:
        pass

    async def GetRoverRentalRobots(self, stream: Stream[GetRoverRentalRobotsRequest, GetRoverRentalRobotsResponse]) -> None:
        pass

    async def GetRobotParts(self, stream: Stream[GetRobotPartsRequest, GetRobotPartsResponse]) -> None:
        pass

    async def GetRobotPart(self, stream: Stream[GetRobotPartRequest, GetRobotPartResponse]) -> None:
        pass

    async def GetRobotPartLogs(self, stream: Stream[GetRobotPartLogsRequest, GetRobotPartLogsResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(GetRobotPartLogsResponse(logs=[self.log]))

    async def TailRobotPartLogs(self, stream: Stream[TailRobotPartLogsRequest, TailRobotPartLogsResponse]) -> None:
        pass

    async def GetRobotPartHistory(self, stream: Stream[GetRobotPartHistoryRequest, GetRobotPartHistoryResponse]) -> None:
        pass

    async def UpdateRobotPart(self, stream: Stream[UpdateRobotPartRequest, UpdateRobotPartResponse]) -> None:
        pass

    async def NewRobotPart(self, stream: Stream[NewRobotPartRequest, NewRobotPartResponse]) -> None:
        pass

    async def DeleteRobotPart(self, stream: Stream[DeleteRobotPartRequest, DeleteRobotPartResponse]) -> None:
        pass

    async def MarkPartAsMain(self, stream: Stream[MarkPartAsMainRequest, MarkPartAsMainResponse]) -> None:
        pass

    async def MarkPartForRestart(self, stream: Stream[MarkPartForRestartRequest, MarkPartForRestartResponse]) -> None:
        pass

    async def CreateRobotPartSecret(self, stream: Stream[CreateRobotPartSecretRequest, CreateRobotPartSecretResponse]) -> None:
        pass

    async def DeleteRobotPartSecret(self, stream: Stream[DeleteRobotPartSecretRequest, DeleteRobotPartSecretResponse]) -> None:
        pass

    async def ListRobots(self, stream: Stream[ListRobotsRequest, ListRobotsResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(ListRobotsResponse(robots=self.robots))

    async def NewRobot(self, stream: Stream[NewRobotRequest, NewRobotResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(NewRobotResponse(id=self.new_id))

    async def UpdateRobot(self, stream: Stream[UpdateRobotRequest, UpdateRobotResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(UpdateRobotResponse(robot=self.updated_robot))

    async def DeleteRobot(self, stream: Stream[DeleteRobotRequest, DeleteRobotResponse]) -> None:
        await stream.recv_message()
        await stream.send_message(DeleteRobotResponse())

    async def ListFragments(self, stream: Stream[ListFragmentsRequest, ListFragmentsResponse]) -> None:
        pass

    async def GetFragment(self, stream: Stream[GetFragmentRequest, GetFragmentResponse]) -> None:
        pass

    async def CreateFragment(self, stream: Stream[CreateFragmentRequest, CreateFragmentResponse]) -> None:
        pass

    async def UpdateFragment(self, stream: Stream[UpdateFragmentRequest, UpdateFragmentResponse]) -> None:
        pass

    async def DeleteFragment(self, stream: Stream[DeleteFragmentRequest, DeleteFragmentResponse]) -> None:
        pass

    async def AddRole(self, stream: Stream[AddRoleRequest, AddRoleResponse]) -> None:
        pass

    async def RemoveRole(self, stream: Stream[RemoveRoleRequest, RemoveRoleResponse]) -> None:
        pass

    async def ChangeRole(self, stream: Stream[ChangeRoleRequest, ChangeRoleResponse]) -> None:
        pass

    async def ListAuthorizations(self, stream: Stream[ListAuthorizationsRequest, ListAuthorizationsResponse]) -> None:
        pass

    async def CheckPermissions(self, stream: Stream[CheckPermissionsRequest, CheckPermissionsResponse]) -> None:
        pass

    async def CreateModule(self, stream: Stream[CreateModuleRequest, CreateModuleResponse]) -> None:
        pass

    async def UpdateModule(self, stream: Stream[UpdateModuleRequest, UpdateModuleResponse]) -> None:
        pass

    async def UploadModuleFile(self, stream: Stream[UploadModuleFileRequest, UploadModuleFileResponse]) -> None:
        pass

    async def GetModule(self, stream: Stream[GetModuleRequest, GetModuleResponse]) -> None:
        pass

    async def ListModules(self, stream: Stream[ListModulesRequest, ListModulesResponse]) -> None:
        pass

    async def CreateKey(self, stream: Stream[CreateKeyRequest, CreateKeyResponse]) -> None:
        pass

    async def GetRobotAPIKeys(self, stream: Stream[GetRobotAPIKeysRequest, GetRobotAPIKeysResponse]) -> None:
        pass

    async def DeleteKey(self, stream: Stream[DeleteKeyRequest, DeleteKeyResponse]) -> None:
        pass

    async def ListKeys(self, stream: Stream[ListKeysRequest, ListKeysResponse]) -> None:
        pass

    async def RotateKey(self, stream: Stream[RotateKeyRequest, RotateKeyResponse]) -> None:
        pass

    async def CreateKeyFromExistingKeyAuthorizations(
        self, stream: Stream[CreateKeyFromExistingKeyAuthorizationsRequest, CreateKeyFromExistingKeyAuthorizationsResponse]
    ) -> None:
        pass

    async def CreateRegistryItem(self, stream: Stream[CreateRegistryItemRequest, CreateRegistryItemResponse]) -> None:
        raise NotImplementedError()

    async def GetOrganizationsWithAccessToLocation(
        self, stream: Stream[GetOrganizationsWithAccessToLocationRequest, GetOrganizationsWithAccessToLocationResponse]
    ) -> None:
        raise NotImplementedError()

    async def ListRegistryItems(self, stream: Stream[ListRegistryItemsRequest, ListRegistryItemsResponse]) -> None:
        raise NotImplementedError()

    async def UpdateRegistryItem(self, stream: Stream[UpdateRegistryItemRequest, UpdateRegistryItemResponse]) -> None:
        raise NotImplementedError()

    async def DeleteRegistryItem(self, stream: Stream[DeleteRegistryItemRequest, DeleteRegistryItemResponse]) -> None:
        raise NotImplementedError()

    async def GetRegistryItem(self, stream: Stream[GetRegistryItemRequest, GetRegistryItemResponse]) -> None:
        raise NotImplementedError()


async def main(*, host: str = "127.0.0.1", port: int = 9092) -> None:
    server = Server([MockData(), MockDataSync(), MockApp()])
    with graceful_exit([server]):
        await server.start(host, port)
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())

from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, Sequence, Union

import bson
import numpy as np
from grpclib.server import Stream
from numpy.typing import NDArray

from viam.app.data_client import DataClient
from viam.gen.app.v1.app_pb2 import FragmentHistoryEntry, GetFragmentHistoryRequest, GetFragmentHistoryResponse
from viam.media.video import ViamImage
from viam.proto.app import (
    AddRoleRequest,
    AddRoleResponse,
    APIKeyWithAuthorizations,
    Authorization,
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
    Fragment,
    GetFragmentRequest,
    GetFragmentResponse,
    GetLocationMetadataRequest,
    GetLocationMetadataResponse,
    GetLocationRequest,
    GetLocationResponse,
    GetModuleRequest,
    GetModuleResponse,
    GetOrganizationMetadataRequest,
    GetOrganizationMetadataResponse,
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
    GetRobotMetadataRequest,
    GetRobotMetadataResponse,
    GetRobotPartHistoryRequest,
    GetRobotPartHistoryResponse,
    GetRobotPartLogsRequest,
    GetRobotPartLogsResponse,
    GetRobotPartMetadataRequest,
    GetRobotPartMetadataResponse,
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
    LocationAuth,
    LocationAuthRequest,
    LocationAuthResponse,
    MarkPartAsMainRequest,
    MarkPartAsMainResponse,
    MarkPartForRestartRequest,
    MarkPartForRestartResponse,
    Module,
    NewRobotPartRequest,
    NewRobotPartResponse,
    NewRobotRequest,
    NewRobotResponse,
    Organization,
    OrganizationIdentity,
    OrganizationInvite,
    OrganizationMember,
    OrgDetails,
    RegistryItem,
    RemoveRoleRequest,
    RemoveRoleResponse,
    ResendOrganizationInviteRequest,
    ResendOrganizationInviteResponse,
    Robot,
    RobotPart,
    RobotPartHistoryEntry,
    RotateKeyRequest,
    RotateKeyResponse,
    RoverRentalRobot,
    ShareLocationRequest,
    ShareLocationResponse,
    TailRobotPartLogsRequest,
    TailRobotPartLogsResponse,
    UnimplementedAppServiceBase,
    UnshareLocationRequest,
    UnshareLocationResponse,
    UpdateFragmentRequest,
    UpdateFragmentResponse,
    UpdateLocationMetadataRequest,
    UpdateLocationMetadataResponse,
    UpdateLocationRequest,
    UpdateLocationResponse,
    UpdateModuleRequest,
    UpdateModuleResponse,
    UpdateOrganizationInviteAuthorizationsRequest,
    UpdateOrganizationInviteAuthorizationsResponse,
    UpdateOrganizationMetadataRequest,
    UpdateOrganizationMetadataResponse,
    UpdateOrganizationRequest,
    UpdateOrganizationResponse,
    UpdateRegistryItemRequest,
    UpdateRegistryItemResponse,
    UpdateRobotMetadataRequest,
    UpdateRobotMetadataResponse,
    UpdateRobotPartMetadataRequest,
    UpdateRobotPartMetadataResponse,
    UpdateRobotPartRequest,
    UpdateRobotPartResponse,
    UpdateRobotRequest,
    UpdateRobotResponse,
    UploadModuleFileRequest,
    UploadModuleFileResponse,
)
from viam.proto.app.billing import (
    GetCurrentMonthUsageRequest,
    GetCurrentMonthUsageResponse,
    GetInvoicePdfRequest,
    GetInvoicePdfResponse,
    GetInvoicesSummaryRequest,
    GetInvoicesSummaryResponse,
    GetOrgBillingInformationRequest,
    GetOrgBillingInformationResponse,
    UnimplementedBillingServiceBase,
)
from viam.proto.app.data import (
    AddBinaryDataToDatasetByIDsRequest,
    AddBinaryDataToDatasetByIDsResponse,
    AddBoundingBoxToImageByIDRequest,
    AddBoundingBoxToImageByIDResponse,
    AddTagsToBinaryDataByFilterRequest,
    AddTagsToBinaryDataByFilterResponse,
    AddTagsToBinaryDataByIDsRequest,
    AddTagsToBinaryDataByIDsResponse,
    BinaryData,
    BinaryDataByFilterRequest,
    BinaryDataByFilterResponse,
    BinaryDataByIDsRequest,
    BinaryDataByIDsResponse,
    BoundingBoxLabelsByFilterRequest,
    BoundingBoxLabelsByFilterResponse,
    ConfigureDatabaseUserRequest,
    ConfigureDatabaseUserResponse,
    DeleteBinaryDataByFilterRequest,
    DeleteBinaryDataByFilterResponse,
    DeleteBinaryDataByIDsRequest,
    DeleteBinaryDataByIDsResponse,
    DeleteTabularDataRequest,
    DeleteTabularDataResponse,
    ExportTabularDataRequest,
    ExportTabularDataResponse,
    GetDatabaseConnectionRequest,
    GetDatabaseConnectionResponse,
    GetLatestTabularDataRequest,
    GetLatestTabularDataResponse,
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
from viam.proto.app.datapipelines import (
    CreateDataPipelineRequest,
    CreateDataPipelineResponse,
    DataPipeline,
    DataPipelineRun,
    DataPipelinesServiceBase,
    DeleteDataPipelineRequest,
    DeleteDataPipelineResponse,
    DisableDataPipelineRequest,
    DisableDataPipelineResponse,
    EnableDataPipelineRequest,
    EnableDataPipelineResponse,
    GetDataPipelineRequest,
    GetDataPipelineResponse,
    ListDataPipelineRunsRequest,
    ListDataPipelineRunsResponse,
    ListDataPipelinesRequest,
    ListDataPipelinesResponse,
    UpdateDataPipelineRequest,
    UpdateDataPipelineResponse,
)
from viam.proto.app.dataset import (
    CreateDatasetRequest,
    CreateDatasetResponse,
    Dataset,
    DatasetServiceBase,
    DeleteDatasetRequest,
    DeleteDatasetResponse,
    ListDatasetsByIDsRequest,
    ListDatasetsByIDsResponse,
    ListDatasetsByOrganizationIDRequest,
    ListDatasetsByOrganizationIDResponse,
    RenameDatasetRequest,
    RenameDatasetResponse,
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
from viam.proto.app.mltraining import (
    CancelTrainingJobRequest,
    CancelTrainingJobResponse,
    DeleteCompletedTrainingJobRequest,
    DeleteCompletedTrainingJobResponse,
    GetTrainingJobRequest,
    GetTrainingJobResponse,
    ListTrainingJobsRequest,
    ListTrainingJobsResponse,
    SubmitCustomTrainingJobRequest,
    SubmitCustomTrainingJobResponse,
    SubmitTrainingJobRequest,
    SubmitTrainingJobResponse,
    TrainingJobMetadata,
    UnimplementedMLTrainingServiceBase,
)
from viam.proto.app.packages import PackageType
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import (
    DoCommandRequest,
    DoCommandResponse,
    GeoGeometry,
    GeoPoint,
    LogEntry,
    PointCloudObject,
    Pose,
    PoseInFrame,
    ResourceName,
)
from viam.proto.provisioning import (
    GetNetworkListRequest,
    GetNetworkListResponse,
    GetSmartMachineStatusRequest,
    GetSmartMachineStatusResponse,
    NetworkInfo,
    SetNetworkCredentialsRequest,
    SetNetworkCredentialsResponse,
    SetSmartMachineCredentialsRequest,
    SetSmartMachineCredentialsResponse,
    UnimplementedProvisioningServiceBase,
)
from viam.proto.service.mlmodel import (
    FlatTensor,
    FlatTensorDataDouble,
    FlatTensorDataFloat,
    FlatTensorDataInt8,
    FlatTensorDataInt16,
    FlatTensorDataInt32,
    FlatTensorDataInt64,
    FlatTensorDataUInt8,
    FlatTensorDataUInt16,
    FlatTensorDataUInt32,
    FlatTensorDataUInt64,
    FlatTensors,
)
from viam.proto.service.motion import (
    Constraints,
    GetPlanRequest,
    GetPlanResponse,
    GetPoseRequest,
    GetPoseResponse,
    ListPlanStatusesRequest,
    ListPlanStatusesResponse,
    MotionServiceBase,
    MoveOnGlobeRequest,
    MoveOnGlobeResponse,
    MoveOnMapRequest,
    MoveOnMapResponse,
    MoveRequest,
    MoveResponse,
    StopPlanRequest,
    StopPlanResponse,
)
from viam.proto.service.navigation import MapType, Mode, Path, Waypoint
from viam.proto.service.slam import MappingMode, SensorInfo, SensorType
from viam.proto.service.vision import Classification, Detection
from viam.services.discovery import Discovery
from viam.services.generic import Generic as GenericService
from viam.services.mlmodel import File, LabelType, Metadata, MLModel, TensorInfo
from viam.services.mlmodel.utils import flat_tensors_to_ndarrays, ndarrays_to_flat_tensors
from viam.services.navigation import Navigation
from viam.services.slam import SLAM
from viam.services.vision import CaptureAllResult, Vision
from viam.utils import ValueTypes, datetime_to_timestamp, dict_to_struct, struct_to_dict


class MockVision(Vision):
    def __init__(
        self,
        name: str,
        detectors: List[str],
        detections: List[Detection],
        classifiers: List[str],
        classifications: List[Classification],
        segmenters: List[str],
        point_clouds: List[PointCloudObject],
        image: ViamImage,
        properties: Vision.Properties,
    ):
        self.detectors = detectors
        self.detections = detections
        self.classifiers = classifiers
        self.classifications = classifications
        self.segmenters = segmenters
        self.point_clouds = point_clouds
        self.image = image
        self.properties = properties
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_properties(
        self,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> Vision.Properties:
        self.extra = extra
        self.timeout = timeout
        return self.properties

    async def capture_all_from_camera(
        self,
        camera_name: str,
        return_image: bool = False,
        return_classifications: bool = False,
        return_detections: bool = False,
        return_object_point_clouds: bool = False,
        *,
        extra: Optional[Mapping[str, Any]] = None,
        timeout: Optional[float] = None,
    ) -> CaptureAllResult:
        self.extra = extra
        self.timeout = timeout
        result = CaptureAllResult()
        if return_image:
            result.image = self.image
        if return_classifications:
            result.classifications = self.classifications
        if return_detections:
            result.detections = self.detections
        if return_object_point_clouds:
            result.objects = self.point_clouds
        return result

    async def get_detections_from_camera(
        self, camera_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Detection]:
        self.extra = extra
        self.timeout = timeout
        return self.detections

    async def get_detections(
        self, image: ViamImage, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Detection]:
        self.extra = extra
        self.timeout = timeout
        return self.detections

    async def get_classifications_from_camera(
        self, camera_name: str, count: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Classification]:
        self.extra = extra
        self.timeout = timeout
        return self.classifications

    async def get_classifications(
        self, image: ViamImage, count: int, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[Classification]:
        self.extra = extra
        self.timeout = timeout
        return self.classifications

    async def get_object_point_clouds(
        self, camera_name: str, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None
    ) -> List[PointCloudObject]:
        self.extra = extra
        self.timeout = timeout
        return self.point_clouds

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        self.timeout = timeout
        return {"cmd": command}


class MockDiscovery(Discovery):
    def __init__(
        self,
        name: str,
    ):
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def discover_resources(
        self,
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> List[ComponentConfig]:
        self.extra = extra
        self.timeout = timeout
        result = ComponentConfig()
        return [result]

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None) -> Mapping[str, ValueTypes]:
        self.timeout = timeout
        return {"cmd": command}


class MockMLModel(MLModel):
    INT8_NDARRAY = np.array([[0, -1], [8, 8]], dtype=np.int8)
    INT16_NDARRAY = np.array([1, 0, 0, 69, -1, 16], dtype=np.int16)
    INT32_NDARRAY = np.array([0, -1, 32], dtype=np.int32)
    INT64_NDARRAY = np.array([(-2) ** 63, -1, 64], dtype=np.int64)
    UINT8_NDARRAY = np.array([0, 1, 8], dtype=np.uint8)
    UINT16_NDARRAY = np.array([[0, 1], [16, 16]], dtype=np.uint16)
    UINT32_NDARRAY = np.array([0, 1, 32], dtype=np.uint32)
    UINT64_NDARRAY = np.array([0, 1, 2**63], dtype=np.uint64)
    FLOAT_NDARRAY = np.array([[0, -88.8], [32, 32]], dtype=np.float32)
    DOUBLE_NDARRAY = np.array([0, -88.8, 88888888], dtype=np.float64)
    SQUARE_INT16_NDARRAY = np.array([[-257, 0, 256], [-257, 0, 256], [-257, 0, 256]], dtype=np.int16)

    EMPTY_NDARRAYS = {}
    EMPTY_TENSORS = FlatTensors(tensors=None)

    DOUBLE_NDARRAYS = {"0": DOUBLE_NDARRAY}
    DOUBLE_TENSORS = FlatTensors(tensors={"0": FlatTensor(shape=(3,), double_tensor=FlatTensorDataDouble(data=DOUBLE_NDARRAY))})

    DOUBLE_FLOAT_NDARRAYS = {"0": DOUBLE_NDARRAY, "1": FLOAT_NDARRAY}
    DOUBLE_FLOAT_TENSORS = FlatTensors(
        tensors={
            "0": FlatTensor(shape=(3,), double_tensor=FlatTensorDataDouble(data=DOUBLE_NDARRAY)),
            "1": FlatTensor(shape=(2, 2), float_tensor=FlatTensorDataFloat(data=FLOAT_NDARRAY.flatten())),
        }
    )

    INTS_NDARRAYS = {"0": INT8_NDARRAY, "1": INT16_NDARRAY, "2": INT32_NDARRAY, "3": INT64_NDARRAY}
    INTS_FLAT_TENSORS = FlatTensors(
        tensors={
            "0": FlatTensor(shape=(2, 2), int8_tensor=FlatTensorDataInt8(data=INT8_NDARRAY.tobytes())),
            "1": FlatTensor(shape=(6,), int16_tensor=FlatTensorDataInt16(data=INT16_NDARRAY.flatten().astype(np.uint32))),
            "2": FlatTensor(shape=(3,), int32_tensor=FlatTensorDataInt32(data=INT32_NDARRAY)),
            "3": FlatTensor(shape=(3,), int64_tensor=FlatTensorDataInt64(data=INT64_NDARRAY)),
        }
    )

    UINTS_NDARRAYS = {"0": UINT8_NDARRAY, "1": UINT16_NDARRAY, "2": UINT32_NDARRAY, "3": UINT64_NDARRAY}
    UINTS_FLAT_TENSORS = FlatTensors(
        tensors={
            "0": FlatTensor(shape=(3,), uint8_tensor=FlatTensorDataUInt8(data=UINT8_NDARRAY.tobytes())),
            "1": FlatTensor(shape=(2, 2), uint16_tensor=FlatTensorDataUInt16(data=UINT16_NDARRAY.flatten().astype(np.uint32))),
            "2": FlatTensor(shape=(3,), uint32_tensor=FlatTensorDataUInt32(data=UINT32_NDARRAY)),
            "3": FlatTensor(shape=(3,), uint64_tensor=FlatTensorDataUInt64(data=UINT64_NDARRAY)),
        }
    )

    SQUARE_INT_UINT_NDARRAYS = {"0": SQUARE_INT16_NDARRAY, "1": UINT64_NDARRAY}
    SQUARE_INT_UINT_TENSORS = {
        "0": FlatTensor(shape=(3, 3), int16_tensor=FlatTensorDataInt16(data=SQUARE_INT16_NDARRAY)),
        "1": FlatTensor(shape=(3,), int64_tensor=FlatTensorDataInt64(data=INT64_NDARRAY)),
    }

    META_INPUTS = [TensorInfo(name="image", description="i0", data_type="uint8", shape=[300, 200])]
    META_OUTPUTS = [
        TensorInfo(name="n_detections", description="o0", data_type="int32", shape=[1]),
        TensorInfo(name="confidence_scores", description="o1", data_type="float32", shape=[3, 1]),
        TensorInfo(
            name="labels",
            description="o2",
            data_type="int32",
            shape=[3, 1],
            associated_files=[
                File(
                    name="category_labels.txt",
                    description="these labels represent types of plants",
                    label_type=LabelType.LABEL_TYPE_TENSOR_VALUE,
                )
            ],
        ),
        TensorInfo(name="locations", description="o3", data_type="float32", shape=[4, 3, 1]),
    ]
    META = Metadata(name="fake_detector", type="object_detector", description="desc", input_info=META_INPUTS, output_info=META_OUTPUTS)

    def __init__(self, name: str):
        self.timeout: Optional[float] = None

        super().__init__(name)

    async def infer(
        self,
        input_tensors: Dict[str, NDArray],
        *,
        extra: Optional[Mapping[str, ValueTypes]] = None,
        timeout: Optional[float] = None,
    ) -> Dict[str, NDArray]:
        self.timeout = timeout
        request_data = ndarrays_to_flat_tensors(input_tensors)
        response_data = flat_tensors_to_ndarrays(request_data)
        return response_data

    async def metadata(self, *, extra: Optional[Mapping[str, ValueTypes]] = None, timeout: Optional[float] = None) -> Metadata:
        self.timeout = timeout
        return self.META


class MockMotion(MotionServiceBase):
    def __init__(
        self,
        move_responses: Dict[str, bool],
        get_pose_responses: Dict[str, PoseInFrame],
        get_plan_response: GetPlanResponse,
        list_plan_statuses_response: ListPlanStatusesResponse,
    ):
        self.move_responses = move_responses
        self.get_pose_responses = get_pose_responses
        self.get_plan_response = get_plan_response
        self.list_plan_statuses_response = list_plan_statuses_response
        self.constraints: Optional[Constraints] = None
        self.extra: Optional[Mapping[str, Any]] = None
        self.timeout: Optional[float] = None

    async def Move(self, stream: Stream[MoveRequest, MoveResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        self.constraints = request.constraints
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        success = self.move_responses[name.name]
        response = MoveResponse(success=success)
        await stream.send_message(response)

    async def MoveOnMap(self, stream: Stream[MoveOnMapRequest, MoveOnMapResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.component_name = request.component_name
        self.destination = request.destination
        self.slam_service = request.slam_service_name
        self.configuration = request.motion_configuration
        self.obstacles = request.obstacles
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.execution_id = "some execution id"
        await stream.send_message(MoveOnMapResponse(execution_id=self.execution_id))

    async def MoveOnGlobe(self, stream: Stream[MoveOnGlobeRequest, MoveOnGlobeResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.component_name = request.component_name
        self.destination = request.destination
        self.movement_sensor = request.movement_sensor_name
        self.obstacles = request.obstacles
        self.heading = request.heading
        self.configuration = request.motion_configuration
        self.bounding_regions = request.bounding_regions
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        self.execution_id = "some execution id"
        await stream.send_message(MoveOnGlobeResponse(execution_id=self.execution_id))

    async def GetPose(self, stream: Stream[GetPoseRequest, GetPoseResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        name: ResourceName = request.component_name
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        pose = self.get_pose_responses[name.name]
        response = GetPoseResponse(pose=pose)
        await stream.send_message(response)

    async def StopPlan(self, stream: Stream[StopPlanRequest, StopPlanResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.component_name = request.component_name
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(StopPlanResponse())

    async def ListPlanStatuses(self, stream: Stream[ListPlanStatusesRequest, ListPlanStatusesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.only_active_plans = request.only_active_plans
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        response = self.list_plan_statuses_response
        await stream.send_message(response)

    async def GetPlan(self, stream: Stream[GetPlanRequest, GetPlanResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.component_name = request.component_name
        self.last_plan_only = request.last_plan_only
        self.execution_id = request.execution_id
        self.extra = struct_to_dict(request.extra)
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(self.get_plan_response)

    async def DoCommand(self, stream: Stream[DoCommandRequest, DoCommandResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.timeout = stream.deadline.time_remaining() if stream.deadline else None
        await stream.send_message(DoCommandResponse(result=request.command))


class MockSLAM(SLAM):
    INTERNAL_STATE_CHUNKS = [bytes(5), bytes(2)]
    POINT_CLOUD_PCD_CHUNKS = [bytes(3), bytes(2)]
    POINT_CLOUD_PCD_CHUNKS_EDITED = [bytes(7), bytes(4)]
    POSITION = Pose(x=1, y=2, z=3, o_x=2, o_y=3, o_z=4, theta=20)
    CLOUD_SLAM = False
    MAPPING_MODE = MappingMode.MAPPING_MODE_UNSPECIFIED
    INTERNAL_STATE_FILE_TYPE = ".pbstream"
    SENSOR_INFO = [
        SensorInfo(name="my-camera", type=SensorType.SENSOR_TYPE_CAMERA),
        SensorInfo(name="my-movement-sensor", type=SensorType.SENSOR_TYPE_MOVEMENT_SENSOR),
    ]

    def __init__(self, name: str):
        self.name = name
        self.timeout: Optional[float] = None
        self.properties = SLAM.Properties(
            cloud_slam=self.CLOUD_SLAM,
            mapping_mode=self.MAPPING_MODE,
            internal_state_file_type=self.INTERNAL_STATE_FILE_TYPE,
            sensor_info=self.SENSOR_INFO,
        )
        super().__init__(name)

    async def get_internal_state(self, *, timeout: Optional[float] = None) -> List[bytes]:
        self.timeout = timeout
        return self.INTERNAL_STATE_CHUNKS

    async def get_point_cloud_map(self, return_edited_map: bool = False, *, timeout: Optional[float] = None) -> List[bytes]:
        self.timeout = timeout
        if return_edited_map:
            return self.POINT_CLOUD_PCD_CHUNKS_EDITED
        return self.POINT_CLOUD_PCD_CHUNKS

    async def get_position(self, *, timeout: Optional[float] = None) -> Pose:
        self.timeout = timeout
        return self.POSITION

    async def get_properties(self, *, timeout: Optional[float] = None) -> SLAM.Properties:
        self.timeout = timeout
        return self.properties

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockNavigation(Navigation):
    LOCATION = GeoPoint(latitude=100.0, longitude=150.0)
    OBSTACLES = [GeoGeometry(location=GeoPoint(latitude=200.0, longitude=250.0))]
    WAYPOINTS = [Waypoint(location=GeoPoint(latitude=300.0, longitude=350.0))]
    PATHS = [Path(destination_waypoint_id="foo", geopoints=[LOCATION])]

    def __init__(self, name: str):
        self.name = name
        self.add_waypoints: list[GeoPoint] = []
        self.remove_waypoints: list[str] = []
        self.mode = Mode.MODE_UNSPECIFIED
        self.map_type = MapType.MAP_TYPE_UNSPECIFIED
        self.timeout: Optional[float] = None
        super().__init__(name)

    async def get_paths(self, *, timeout: Optional[float] = None) -> List[Path]:
        self.timeout = timeout
        return self.PATHS

    async def get_location(self, *, timeout: Optional[float] = None) -> GeoPoint:
        self.timeout = timeout
        return self.LOCATION

    async def get_obstacles(self, *, timeout: Optional[float] = None) -> List[GeoGeometry]:
        self.timeout = timeout
        return self.OBSTACLES

    async def get_waypoints(self, *, timeout: Optional[float] = None) -> List[Waypoint]:
        self.timeout = timeout
        return self.WAYPOINTS

    async def add_waypoint(self, point: GeoPoint, *, timeout: Optional[float] = None):
        self.timeout = timeout
        self.add_waypoints.append(point)

    async def remove_waypoint(self, id: str, *, timeout: Optional[float] = None):
        self.timeout = timeout
        self.remove_waypoints.append(id)

    async def get_mode(self, *, timeout: Optional[float] = None) -> Mode.ValueType:
        self.timeout = timeout
        return self.mode

    async def set_mode(self, mode: Mode.ValueType, *, timeout: Optional[float] = None):
        self.timeout = timeout
        self.mode = mode

    async def get_properties(self, *, timeout: Optional[float] = None) -> MapType.ValueType:
        self.timeout = timeout
        return self.map_type

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        return {"command": command}


class MockProvisioning(UnimplementedProvisioningServiceBase):
    def __init__(
        self,
        smart_machine_status: GetSmartMachineStatusResponse,
        network_info: List[NetworkInfo],
    ):
        self.smart_machine_status = smart_machine_status
        self.network_info = network_info

    async def GetNetworkList(self, stream: Stream[GetNetworkListRequest, GetNetworkListResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetNetworkListResponse(networks=self.network_info))

    async def GetSmartMachineStatus(self, stream: Stream[GetSmartMachineStatusRequest, GetSmartMachineStatusResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(self.smart_machine_status)

    async def SetNetworkCredentials(self, stream: Stream[SetNetworkCredentialsRequest, SetNetworkCredentialsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.network_type = request.type
        self.ssid = request.ssid
        self.psk = request.psk
        await stream.send_message(SetNetworkCredentialsResponse())

    async def SetSmartMachineCredentials(
        self,
        stream: Stream[SetSmartMachineCredentialsRequest, SetSmartMachineCredentialsResponse],
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.cloud_config = request.cloud
        await stream.send_message(SetSmartMachineCredentialsResponse())


class MockData(UnimplementedDataServiceBase):
    def __init__(
        self,
        tabular_response: List[DataClient.TabularData],
        tabular_export_response: List[ExportTabularDataResponse],
        tabular_query_response: List[Dict[str, Union[ValueTypes, datetime]]],
        binary_response: List[BinaryData],
        delete_remove_response: int,
        tags_response: List[str],
        bbox_labels_response: List[str],
        hostname_response: str,
        additional_params: Mapping[str, ValueTypes],
    ):
        self.tabular_response = tabular_response
        self.tabular_export_response = tabular_export_response
        self.tabular_query_response = tabular_query_response
        self.binary_response = binary_response
        self.delete_remove_response = delete_remove_response
        self.tags_response = tags_response
        self.bbox_labels_response = bbox_labels_response
        self.hostname_response = hostname_response
        self.was_tabular_data_requested = False
        self.was_binary_data_requested = False
        self.additional_params = additional_params

    async def TabularDataByFilter(self, stream: Stream[TabularDataByFilterRequest, TabularDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        if self.was_tabular_data_requested:
            await stream.send_message(TabularDataByFilterResponse(data=None))
            return
        self.filter = request.data_request.filter
        self.order = request.data_request.sort_order
        self.limit = request.data_request.limit
        self.count_only = request.count_only
        self.last = request.data_request.last
        tabular_response_structs = []
        tabular_metadata = [data.metadata for data in self.tabular_response]
        for idx, tabular_data in enumerate(self.tabular_response):
            tabular_response_structs.append(
                TabularData(
                    data=dict_to_struct(tabular_data.data),
                    metadata_index=idx,
                    time_requested=datetime_to_timestamp(tabular_data.time_requested),
                    time_received=datetime_to_timestamp(tabular_data.time_received),
                )
            )
        await stream.send_message(
            TabularDataByFilterResponse(
                data=tabular_response_structs,
                metadata=tabular_metadata,
                count=len(tabular_response_structs),
                last="LAST_TABULAR_DATA_PAGE_ID",
            )
        )
        self.was_tabular_data_requested = True

    async def BinaryDataByFilter(self, stream: Stream[BinaryDataByFilterRequest, BinaryDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        if self.was_binary_data_requested:
            await stream.send_message(BinaryDataByFilterResponse())
            return
        self.filter = request.data_request.filter
        self.order = request.data_request.sort_order
        self.limit = request.data_request.limit
        self.include_binary = request.include_binary
        self.count_only = request.count_only
        self.include_internal_data = request.include_internal_data
        self.last = request.data_request.last
        await stream.send_message(
            BinaryDataByFilterResponse(
                data=self.binary_response,
                count=len(self.binary_response),
                last="LAST_BINARY_DATA_PAGE_ID",
            )
        )
        self.was_binary_data_requested = True

    async def BinaryDataByIDs(self, stream: Stream[BinaryDataByIDsRequest, BinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        self.binary_data_ids = request.binary_data_ids
        await stream.send_message(BinaryDataByIDsResponse(data=self.binary_response))

    async def DeleteTabularData(self, stream: Stream[DeleteTabularDataRequest, DeleteTabularDataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        self.delete_older_than_days = request.delete_older_than_days
        await stream.send_message(DeleteTabularDataResponse(deleted_count=self.delete_remove_response))

    async def DeleteBinaryDataByFilter(self, stream: Stream[DeleteBinaryDataByFilterRequest, DeleteBinaryDataByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(DeleteBinaryDataByFilterResponse(deleted_count=self.delete_remove_response))

    async def DeleteBinaryDataByIDs(self, stream: Stream[DeleteBinaryDataByIDsRequest, DeleteBinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        self.binary_data_ids = request.binary_data_ids
        await stream.send_message(DeleteBinaryDataByIDsResponse(deleted_count=self.delete_remove_response))

    async def AddTagsToBinaryDataByIDs(self, stream: Stream[AddTagsToBinaryDataByIDsRequest, AddTagsToBinaryDataByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        self.binary_data_ids = request.binary_data_ids
        self.tags = request.tags
        await stream.send_message(AddTagsToBinaryDataByIDsResponse())

    async def AddTagsToBinaryDataByFilter(
        self, stream: Stream[AddTagsToBinaryDataByFilterRequest, AddTagsToBinaryDataByFilterResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        self.tags = request.tags
        await stream.send_message(AddTagsToBinaryDataByFilterResponse())

    async def RemoveTagsFromBinaryDataByIDs(
        self, stream: Stream[RemoveTagsFromBinaryDataByIDsRequest, RemoveTagsFromBinaryDataByIDsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.binary_ids = request.binary_ids
        self.binary_data_ids = request.binary_data_ids
        self.tags = request.tags
        await stream.send_message(RemoveTagsFromBinaryDataByIDsResponse(deleted_count=self.delete_remove_response))

    async def RemoveTagsFromBinaryDataByFilter(
        self, stream: Stream[RemoveTagsFromBinaryDataByFilterRequest, RemoveTagsFromBinaryDataByFilterResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        self.tags = request.tags
        await stream.send_message(RemoveTagsFromBinaryDataByFilterResponse(deleted_count=len(request.tags)))

    async def TagsByFilter(self, stream: Stream[TagsByFilterRequest, TagsByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(TagsByFilterResponse(tags=self.tags_response))

    async def AddBoundingBoxToImageByID(self, stream: Stream[AddBoundingBoxToImageByIDRequest, AddBoundingBoxToImageByIDResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(AddBoundingBoxToImageByIDResponse(bbox_id=self.bbox_labels_response[0]))

    async def RemoveBoundingBoxFromImageByID(
        self, stream: Stream[RemoveBoundingBoxFromImageByIDRequest, RemoveBoundingBoxFromImageByIDResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.removed_label = request.bbox_id
        self.removed_id = request.binary_id
        self.removed_binary_data_id = request.binary_data_id
        await stream.send_message(RemoveBoundingBoxFromImageByIDResponse())

    async def BoundingBoxLabelsByFilter(self, stream: Stream[BoundingBoxLabelsByFilterRequest, BoundingBoxLabelsByFilterResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.filter = request.filter
        await stream.send_message(BoundingBoxLabelsByFilterResponse(labels=self.bbox_labels_response))

    async def GetDatabaseConnection(self, stream: Stream[GetDatabaseConnectionRequest, GetDatabaseConnectionResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        await stream.send_message(GetDatabaseConnectionResponse(hostname=self.hostname_response))

    async def ConfigureDatabaseUser(self, stream: Stream[ConfigureDatabaseUserRequest, ConfigureDatabaseUserResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        self.password = request.password
        await stream.send_message(ConfigureDatabaseUserResponse())

    async def AddBinaryDataToDatasetByIDs(
        self, stream: Stream[AddBinaryDataToDatasetByIDsRequest, AddBinaryDataToDatasetByIDsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.added_data_ids = request.binary_ids
        self.added_binary_data_ids = request.binary_data_ids
        self.dataset_id = request.dataset_id
        await stream.send_message(AddBinaryDataToDatasetByIDsResponse())

    async def RemoveBinaryDataFromDatasetByIDs(
        self, stream: Stream[RemoveBinaryDataFromDatasetByIDsRequest, RemoveBinaryDataFromDatasetByIDsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.removed_data_ids = request.binary_ids
        self.removed_binary_data_ids = request.binary_data_ids
        self.dataset_id = request.dataset_id
        await stream.send_message(RemoveBinaryDataFromDatasetByIDsResponse())

    async def TabularDataBySQL(self, stream: Stream[TabularDataBySQLRequest, TabularDataBySQLResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(TabularDataBySQLResponse(raw_data=[bson.encode(dict) for dict in self.tabular_query_response]))

    async def TabularDataByMQL(self, stream: Stream[TabularDataByMQLRequest, TabularDataByMQLResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(TabularDataByMQLResponse(raw_data=[bson.encode(dict) for dict in self.tabular_query_response]))

    async def GetLatestTabularData(self, stream: Stream[GetLatestTabularDataRequest, GetLatestTabularDataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.part_id = request.part_id
        self.resource_name = request.resource_name
        self.resource_subtype = request.resource_subtype
        self.method_name = request.method_name
        timestamp = datetime_to_timestamp(datetime(2024, 12, 25))
        data = dict_to_struct(self.tabular_response[0].data)
        await stream.send_message(GetLatestTabularDataResponse(time_captured=timestamp, time_synced=timestamp, payload=data))

    async def ExportTabularData(self, stream: Stream[ExportTabularDataRequest, ExportTabularDataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.part_id = request.part_id
        self.resource_name = request.resource_name
        self.resource_subtype = request.resource_subtype
        self.method_name = request.method_name
        self.interval = request.interval
        self.additional_params = request.additional_parameters
        for tabular_data in self.tabular_export_response:
            await stream.send_message(tabular_data)


class MockDataset(DatasetServiceBase):
    def __init__(self, create_response: str, datasets_response: Sequence[Dataset]):
        self.create_response = create_response
        self.datasets_response = datasets_response

    async def CreateDataset(self, stream: Stream[CreateDatasetRequest, CreateDatasetResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.org_id = request.organization_id
        await stream.send_message(CreateDatasetResponse(id=self.create_response))

    async def DeleteDataset(self, stream: Stream[DeleteDatasetRequest, DeleteDatasetResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.deleted_id = request.id
        await stream.send_message(DeleteDatasetResponse())

    async def ListDatasetsByIDs(self, stream: Stream[ListDatasetsByIDsRequest, ListDatasetsByIDsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.ids = request.ids
        await stream.send_message(ListDatasetsByIDsResponse(datasets=self.datasets_response))

    async def ListDatasetsByOrganizationID(
        self, stream: Stream[ListDatasetsByOrganizationIDRequest, ListDatasetsByOrganizationIDResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.org_id = request.organization_id
        await stream.send_message(ListDatasetsByOrganizationIDResponse(datasets=self.datasets_response))

    async def RenameDataset(self, stream: Stream[RenameDatasetRequest, RenameDatasetResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.id
        self.name = request.name
        await stream.send_message((RenameDatasetResponse()))


class MockDataSync(DataSyncServiceBase):
    def __init__(self, file_upload_response: str):
        self.file_upload_response = file_upload_response

    async def DataCaptureUpload(self, stream: Stream[DataCaptureUploadRequest, DataCaptureUploadResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.metadata = request.metadata
        self.sensor_contents = request.sensor_contents
        await stream.send_message(DataCaptureUploadResponse(binary_data_id=self.file_upload_response, file_id=self.file_upload_response))

    async def FileUpload(self, stream: Stream[FileUploadRequest, FileUploadResponse]) -> None:
        request_metadata = await stream.recv_message()
        assert request_metadata is not None
        self.metadata = request_metadata.metadata
        request_file_contents = await stream.recv_message()
        assert request_file_contents is not None
        self.binary_data = request_file_contents.file_contents.data
        await stream.send_message(FileUploadResponse(binary_data_id=self.file_upload_response))

    async def StreamingDataCaptureUpload(
        self, stream: Stream[StreamingDataCaptureUploadRequest, StreamingDataCaptureUploadResponse]
    ) -> None:
        request_metadata = await stream.recv_message()
        assert request_metadata is not None
        self.metadata = request_metadata.metadata.upload_metadata
        request_data_contents = await stream.recv_message()
        assert request_data_contents is not None
        self.binary_data = request_data_contents.data
        await stream.send_message(StreamingDataCaptureUploadResponse(binary_data_id=self.file_upload_response))


class MockDataPipelines(DataPipelinesServiceBase):
    def __init__(self, create_response: str, list_response: Sequence[DataPipeline], runs_response: Sequence[DataPipelineRun]):
        self.create_response = create_response
        self.list_response = list_response
        self.runs_response = runs_response

    async def CreateDataPipeline(self, stream: Stream[CreateDataPipelineRequest, CreateDataPipelineResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.mql_binary = request.mql_binary
        self.schedule = request.schedule
        self.org_id = request.organization_id
        self.enable_backfill = request.enable_backfill
        self.data_source_type = request.data_source_type
        await stream.send_message(CreateDataPipelineResponse(id=self.create_response))

    async def GetDataPipeline(self, stream: Stream[GetDataPipelineRequest, GetDataPipelineResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.id
        await stream.send_message(GetDataPipelineResponse(data_pipeline=self.list_response[0]))

    async def ListDataPipelines(self, stream: Stream[ListDataPipelinesRequest, ListDataPipelinesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.org_id = request.organization_id
        await stream.send_message(ListDataPipelinesResponse(data_pipelines=self.list_response))

    async def UpdateDataPipeline(self, stream: Stream[UpdateDataPipelineRequest, UpdateDataPipelineResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.id
        self.name = request.name
        self.mql_binary = request.mql_binary
        self.schedule = request.schedule
        await stream.send_message(UpdateDataPipelineResponse())

    async def DeleteDataPipeline(self, stream: Stream[DeleteDataPipelineRequest, DeleteDataPipelineResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.deleted_id = request.id
        await stream.send_message(DeleteDataPipelineResponse())

    async def EnableDataPipeline(self, stream: Stream[EnableDataPipelineRequest, EnableDataPipelineResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.enabled_id = request.id
        await stream.send_message(EnableDataPipelineResponse())

    async def DisableDataPipeline(self, stream: Stream[DisableDataPipelineRequest, DisableDataPipelineResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.disabled_id = request.id
        await stream.send_message(DisableDataPipelineResponse())

    async def ListDataPipelineRuns(self, stream: Stream[ListDataPipelineRunsRequest, ListDataPipelineRunsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.id
        await stream.send_message(ListDataPipelineRunsResponse(pipeline_id=self.id, runs=self.runs_response))


class MockMLTraining(UnimplementedMLTrainingServiceBase):
    def __init__(self, job_id: str, training_metadata: TrainingJobMetadata):
        self.job_id = job_id
        self.training_metadata = training_metadata

    async def SubmitTrainingJob(self, stream: Stream[SubmitTrainingJobRequest, SubmitTrainingJobResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.dataset_id = request.dataset_id
        self.org_id = request.organization_id
        self.model_name = request.model_name
        self.model_version = request.model_version
        self.model_type = request.model_type
        self.tags = request.tags
        await stream.send_message(SubmitTrainingJobResponse(id=self.job_id))

    async def SubmitCustomTrainingJob(self, stream: Stream[SubmitCustomTrainingJobRequest, SubmitCustomTrainingJobResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.dataset_id = request.dataset_id
        self.registry_item_id = request.registry_item_id
        self.org_id = request.organization_id
        self.model_name = request.model_name
        self.model_version = request.model_version
        await stream.send_message(SubmitCustomTrainingJobResponse(id=self.job_id))

    async def GetTrainingJob(self, stream: Stream[GetTrainingJobRequest, GetTrainingJobResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.training_job_id = request.id
        await stream.send_message(GetTrainingJobResponse(metadata=self.training_metadata))

    async def ListTrainingJobs(self, stream: Stream[ListTrainingJobsRequest, ListTrainingJobsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.training_status = request.status
        self.org_id = request.organization_id
        await stream.send_message(ListTrainingJobsResponse(jobs=[self.training_metadata]))

    async def CancelTrainingJob(self, stream: Stream[CancelTrainingJobRequest, CancelTrainingJobResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.cancel_job_id = request.id
        await stream.send_message(CancelTrainingJobResponse())

    async def DeleteCompletedTrainingJob(
        self, stream: Stream[DeleteCompletedTrainingJobRequest, DeleteCompletedTrainingJobResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.delete_id = request.id
        await stream.send_message(DeleteCompletedTrainingJobResponse())


class MockBilling(UnimplementedBillingServiceBase):
    def __init__(
        self,
        pdf: bytes,
        curr_month_usage: GetCurrentMonthUsageResponse,
        invoices_summary: GetInvoicesSummaryResponse,
        billing_info: GetOrgBillingInformationResponse,
    ):
        self.pdf = pdf
        self.curr_month_usage = curr_month_usage
        self.invoices_summary = invoices_summary
        self.billing_info = billing_info

    async def GetCurrentMonthUsage(self, stream: Stream[GetCurrentMonthUsageRequest, GetCurrentMonthUsageResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.org_id = request.org_id
        await stream.send_message(self.curr_month_usage)

    async def GetInvoicePdf(self, stream: Stream[GetInvoicePdfRequest, GetInvoicePdfResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.org_id = request.org_id
        self.invoice_id = request.id
        response = GetInvoicePdfResponse(chunk=self.pdf)
        await stream.send_message(response)

    async def GetInvoicesSummary(self, stream: Stream[GetInvoicesSummaryRequest, GetInvoicesSummaryResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.org_id = request.org_id
        await stream.send_message(self.invoices_summary)

    async def GetOrgBillingInformation(self, stream: Stream[GetOrgBillingInformationRequest, GetOrgBillingInformationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.org_id = request.org_id
        await stream.send_message(self.billing_info)


class MockApp(UnimplementedAppServiceBase):
    def __init__(
        self,
        organizations: List[Organization],
        location: Location,
        robot: Robot,
        robot_part: RobotPart,
        log_entry: LogEntry,
        id: str,
        name: str,
        fragment: Fragment,
        available: bool,
        location_auth: LocationAuth,
        robot_part_history: List[RobotPartHistoryEntry],
        fragment_history: List[FragmentHistoryEntry],
        authorizations: List[Authorization],
        url: str,
        module: Module,
        members: List[OrganizationMember],
        invite: OrganizationInvite,
        rover_rental_robots: List[RoverRentalRobot],
        api_key: str,
        api_keys_with_authorizations: List[APIKeyWithAuthorizations],
        items: List[RegistryItem],
        package_type: PackageType.ValueType,
    ):
        self.organizations = organizations
        self.location = location
        self.robot = robot
        self.robot_part = robot_part
        self.log_entry = log_entry
        self.id = id
        self.name = name
        self.fragment = fragment
        self.available = available
        self.location_auth = location_auth
        self.robot_part_history = robot_part_history
        self.fragment_history = fragment_history
        self.authorizations = authorizations
        self.url = url
        self.module = module
        self.members = members
        self.invite = invite
        self.rover_rental_robots = rover_rental_robots
        self.api_key = api_key
        self.api_keys_with_authorizations = api_keys_with_authorizations
        self.items = items
        self.package_type = package_type
        self.send_email_invite = False
        self.organization_metadata = {}
        self.location_metadata = {}
        self.robot_metadata = {}
        self.robot_part_metadata = {}

    async def GetUserIDByEmail(self, stream: Stream[GetUserIDByEmailRequest, GetUserIDByEmailResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetUserIDByEmailResponse(user_id=self.id))

    async def CreateOrganization(self, stream: Stream[CreateOrganizationRequest, CreateOrganizationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(CreateOrganizationResponse(organization=self.organizations[0]))

    async def ListOrganizations(self, stream: Stream[ListOrganizationsRequest, ListOrganizationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListOrganizationsResponse(organizations=self.organizations))

    async def ListOrganizationsByUser(self, stream: Stream[ListOrganizationsByUserRequest, ListOrganizationsByUserResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListOrganizationsByUserResponse(orgs=[OrgDetails(org_id=self.id, org_name=self.name)]))

    async def GetOrganization(self, stream: Stream[GetOrganizationRequest, GetOrganizationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetOrganizationResponse(organization=self.organizations[0]))

    async def GetOrganizationNamespaceAvailability(
        self, stream: Stream[GetOrganizationNamespaceAvailabilityRequest, GetOrganizationNamespaceAvailabilityResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.namespace = request.public_namespace
        await stream.send_message(GetOrganizationNamespaceAvailabilityResponse(available=self.available))

    async def UpdateOrganization(self, stream: Stream[UpdateOrganizationRequest, UpdateOrganizationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.update_region = request.region
        self.update_cid = request.cid
        self.update_name = request.name
        self.update_namespace = request.public_namespace
        await stream.send_message(UpdateOrganizationResponse(organization=self.organizations[0]))

    async def DeleteOrganization(self, stream: Stream[DeleteOrganizationRequest, DeleteOrganizationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.delete_org_called = True
        await stream.send_message(DeleteOrganizationResponse())

    async def ListOrganizationMembers(self, stream: Stream[ListOrganizationMembersRequest, ListOrganizationMembersResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListOrganizationMembersResponse(members=self.members, invites=[self.invite]))

    async def CreateOrganizationInvite(self, stream: Stream[CreateOrganizationInviteRequest, CreateOrganizationInviteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.send_email_invite = request.send_email_invite
        await stream.send_message(CreateOrganizationInviteResponse(invite=self.invite))

    async def UpdateOrganizationInviteAuthorizations(
        self, stream: Stream[UpdateOrganizationInviteAuthorizationsRequest, UpdateOrganizationInviteAuthorizationsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.email = request.email
        self.add_authorizations = request.add_authorizations
        self.remove_authorizations = request.remove_authorizations
        await stream.send_message(UpdateOrganizationInviteAuthorizationsResponse(invite=self.invite))

    async def DeleteOrganizationMember(self, stream: Stream[DeleteOrganizationMemberRequest, DeleteOrganizationMemberResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.deleted_member_id = request.user_id
        await stream.send_message(DeleteOrganizationMemberResponse())

    async def DeleteOrganizationInvite(self, stream: Stream[DeleteOrganizationInviteRequest, DeleteOrganizationInviteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.deleted_invite_email = request.email
        await stream.send_message(DeleteOrganizationInviteResponse())

    async def ResendOrganizationInvite(self, stream: Stream[ResendOrganizationInviteRequest, ResendOrganizationInviteResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.resent_invite_email = request.email
        await stream.send_message(ResendOrganizationInviteResponse())

    async def CreateLocation(self, stream: Stream[CreateLocationRequest, CreateLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.parent_location_id = request.parent_location_id
        await stream.send_message(CreateLocationResponse(location=self.location))

    async def GetLocation(self, stream: Stream[GetLocationRequest, GetLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(GetLocationResponse(location=self.location))

    async def UpdateLocation(self, stream: Stream[UpdateLocationRequest, UpdateLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        self.name = request.name
        self.parent_location_id = request.parent_location_id
        await stream.send_message(UpdateLocationResponse(location=self.location))

    async def DeleteLocation(self, stream: Stream[DeleteLocationRequest, DeleteLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(DeleteLocationResponse())

    async def ListLocations(self, stream: Stream[ListLocationsRequest, ListLocationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListLocationsResponse(locations=[self.location]))

    async def ShareLocation(self, stream: Stream[ShareLocationRequest, ShareLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        self.location_id = request.location_id
        await stream.send_message(ShareLocationResponse())

    async def UnshareLocation(self, stream: Stream[UnshareLocationRequest, UnshareLocationResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_id = request.organization_id
        self.location_id = request.location_id
        await stream.send_message(UnshareLocationResponse())

    async def LocationAuth(self, stream: Stream[LocationAuthRequest, LocationAuthResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(LocationAuthResponse(auth=self.location_auth))

    async def CreateLocationSecret(self, stream: Stream[CreateLocationSecretRequest, CreateLocationSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(CreateLocationSecretResponse(auth=self.location_auth))

    async def DeleteLocationSecret(self, stream: Stream[DeleteLocationSecretRequest, DeleteLocationSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        self.secret_id = request.secret_id
        await stream.send_message(DeleteLocationSecretResponse())

    async def GetRobot(self, stream: Stream[GetRobotRequest, GetRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.id
        await stream.send_message(GetRobotResponse(robot=self.robot))

    async def GetRoverRentalRobots(self, stream: Stream[GetRoverRentalRobotsRequest, GetRoverRentalRobotsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetRoverRentalRobotsResponse(robots=self.rover_rental_robots))

    async def GetRobotParts(self, stream: Stream[GetRobotPartsRequest, GetRobotPartsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.robot_id
        await stream.send_message(GetRobotPartsResponse(parts=[self.robot_part]))

    async def GetRobotPart(self, stream: Stream[GetRobotPartRequest, GetRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        await stream.send_message(GetRobotPartResponse(part=self.robot_part))

    async def GetRobotPartLogs(self, stream: Stream[GetRobotPartLogsRequest, GetRobotPartLogsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        self.filter = request.filter
        self.errors_only = request.errors_only
        self.levels = request.levels
        await stream.send_message(GetRobotPartLogsResponse(logs=[self.log_entry]))

    async def TailRobotPartLogs(self, stream: Stream[TailRobotPartLogsRequest, TailRobotPartLogsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        self.errors_only = request.errors_only
        self.filter = request.filter
        await stream.send_message(TailRobotPartLogsResponse(logs=[]))

    async def GetRobotPartHistory(self, stream: Stream[GetRobotPartHistoryRequest, GetRobotPartHistoryResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        await stream.send_message(GetRobotPartHistoryResponse(history=self.robot_part_history))

    async def UpdateRobotPart(self, stream: Stream[UpdateRobotPartRequest, UpdateRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.id
        self.name = request.name
        self.robot_config = request.robot_config
        self.last_known_update = request.last_known_update
        await stream.send_message(UpdateRobotPartResponse(part=self.robot_part))

    async def NewRobotPart(self, stream: Stream[NewRobotPartRequest, NewRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.robot_id
        self.part_name = request.part_name
        await stream.send_message(NewRobotPartResponse(part_id=self.id))

    async def DeleteRobotPart(self, stream: Stream[DeleteRobotPartRequest, DeleteRobotPartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(DeleteRobotPartResponse())

    async def MarkPartAsMain(self, stream: Stream[MarkPartAsMainRequest, MarkPartAsMainResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(MarkPartAsMainResponse())

    async def MarkPartForRestart(self, stream: Stream[MarkPartForRestartRequest, MarkPartForRestartResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(MarkPartForRestartResponse())

    async def CreateRobotPartSecret(self, stream: Stream[CreateRobotPartSecretRequest, CreateRobotPartSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        await stream.send_message(CreateRobotPartSecretResponse(part=self.robot_part))

    async def DeleteRobotPartSecret(self, stream: Stream[DeleteRobotPartSecretRequest, DeleteRobotPartSecretResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_id = request.part_id
        self.secret_id = request.secret_id
        await stream.send_message(DeleteRobotPartSecretResponse())

    async def ListRobots(self, stream: Stream[ListRobotsRequest, ListRobotsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_id = request.location_id
        await stream.send_message(ListRobotsResponse(robots=[self.robot]))

    async def NewRobot(self, stream: Stream[NewRobotRequest, NewRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.location_id = request.location
        await stream.send_message(NewRobotResponse(id=self.id))

    async def UpdateRobot(self, stream: Stream[UpdateRobotRequest, UpdateRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.id
        self.name = request.name
        self.location_id = request.location
        await stream.send_message(UpdateRobotResponse(robot=self.robot))

    async def DeleteRobot(self, stream: Stream[DeleteRobotRequest, DeleteRobotResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_id = request.id
        await stream.send_message(DeleteRobotResponse())

    async def ListFragments(self, stream: Stream[ListFragmentsRequest, ListFragmentsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_visibility = request.fragment_visibility
        await stream.send_message(ListFragmentsResponse(fragments=[self.fragment]))

    async def GetFragment(self, stream: Stream[GetFragmentRequest, GetFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_id = request.id
        await stream.send_message(GetFragmentResponse(fragment=self.fragment))

    async def GetFragmentHistory(self, stream: Stream[GetFragmentHistoryRequest, GetFragmentHistoryResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.id
        self.page_token = request.page_token
        self.page_limit = request.page_limit
        await stream.send_message(GetFragmentHistoryResponse(history=self.fragment_history))

    async def CreateFragment(self, stream: Stream[CreateFragmentRequest, CreateFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        await stream.send_message(CreateFragmentResponse(fragment=self.fragment))

    async def UpdateFragment(self, stream: Stream[UpdateFragmentRequest, UpdateFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_id = request.id
        self.name = request.name
        self.public = request.public
        self.last_known_update = request.last_known_update
        await stream.send_message(UpdateFragmentResponse(fragment=self.fragment))

    async def DeleteFragment(self, stream: Stream[DeleteFragmentRequest, DeleteFragmentResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.fragment_id = request.id
        await stream.send_message(DeleteFragmentResponse())

    async def AddRole(self, stream: Stream[AddRoleRequest, AddRoleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.identity_id = request.authorization.identity_id
        self.role = request.authorization.authorization_id.split("_")[-1]
        self.resource_type = request.authorization.resource_type
        self.resource_id = request.authorization.resource_id
        await stream.send_message(AddRoleResponse())

    async def RemoveRole(self, stream: Stream[RemoveRoleRequest, RemoveRoleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.identity_id = request.authorization.identity_id
        self.role = request.authorization.authorization_id.split("_")[-1]
        self.resource_type = request.authorization.resource_type
        self.resource_id = request.authorization.resource_id
        await stream.send_message(RemoveRoleResponse())

    async def ChangeRole(self, stream: Stream[ChangeRoleRequest, ChangeRoleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.change_role_called = True
        await stream.send_message(ChangeRoleResponse())

    async def ListAuthorizations(self, stream: Stream[ListAuthorizationsRequest, ListAuthorizationsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.resource_ids = request.resource_ids
        await stream.send_message(ListAuthorizationsResponse(authorizations=self.authorizations))

    async def CheckPermissions(self, stream: Stream[CheckPermissionsRequest, CheckPermissionsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(CheckPermissionsResponse(authorized_permissions=request.permissions))

    async def CreateModule(self, stream: Stream[CreateModuleRequest, CreateModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        await stream.send_message(CreateModuleResponse(module_id=self.id, url=self.url))

    async def UpdateModule(self, stream: Stream[UpdateModuleRequest, UpdateModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.module_id = request.module_id
        self.module_url = request.url
        self.description = request.description
        self.models = request.models
        self.entrypoint = request.entrypoint
        self.visibility = request.visibility
        await stream.send_message(UpdateModuleResponse(url=self.url))

    async def UploadModuleFile(self, stream: Stream[UploadModuleFileRequest, UploadModuleFileResponse]) -> None:
        request_file_info = await stream.recv_message()
        assert request_file_info is not None
        self.module_file_info = request_file_info.module_file_info
        request_file = await stream.recv_message()
        assert request_file is not None
        self.file = request_file.file
        await stream.send_message(UploadModuleFileResponse(url=self.id))

    async def GetModule(self, stream: Stream[GetModuleRequest, GetModuleResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.module_id = request.module_id
        await stream.send_message(GetModuleResponse(module=self.module))

    async def ListModules(self, stream: Stream[ListModulesRequest, ListModulesResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListModulesResponse(modules=[self.module]))

    async def CreateKey(self, stream: Stream[CreateKeyRequest, CreateKeyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(CreateKeyResponse(key=self.api_key, id=self.id))

    async def GetRobotAPIKeys(self, stream: Stream[GetRobotAPIKeysRequest, GetRobotAPIKeysResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetRobotAPIKeysResponse(api_keys=self.api_keys_with_authorizations))

    async def DeleteKey(self, stream: Stream[DeleteKeyRequest, DeleteKeyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.id
        self.delete_key_called = True
        await stream.send_message((DeleteKeyResponse()))

    async def ListKeys(self, stream: Stream[ListKeysRequest, ListKeysResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListKeysResponse(api_keys=self.api_keys_with_authorizations))

    async def RotateKey(self, stream: Stream[RotateKeyRequest, RotateKeyResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(RotateKeyResponse(id=self.id, key=self.api_key))

    async def CreateKeyFromExistingKeyAuthorizations(
        self, stream: Stream[CreateKeyFromExistingKeyAuthorizationsRequest, CreateKeyFromExistingKeyAuthorizationsResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(CreateKeyFromExistingKeyAuthorizationsResponse(key=self.api_key, id=self.id))

    async def CreateRegistryItem(self, stream: Stream[CreateRegistryItemRequest, CreateRegistryItemResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.name = request.name
        self.package_type = request.type
        self.organization_id = request.organization_id
        await stream.send_message(CreateRegistryItemResponse())

    async def GetOrganizationsWithAccessToLocation(
        self, stream: Stream[GetOrganizationsWithAccessToLocationRequest, GetOrganizationsWithAccessToLocationResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(
            GetOrganizationsWithAccessToLocationResponse(organization_identities=[OrganizationIdentity(id=self.id, name=self.name)])
        )

    async def ListRegistryItems(self, stream: Stream[ListRegistryItemsRequest, ListRegistryItemsResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(ListRegistryItemsResponse(items=self.items))

    async def UpdateRegistryItem(self, stream: Stream[UpdateRegistryItemRequest, UpdateRegistryItemResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.id = request.item_id
        self.package_type = request.type
        self.description = request.description
        self.visibility = request.visibility
        await stream.send_message(UpdateRegistryItemResponse())

    async def DeleteRegistryItem(self, stream: Stream[DeleteRegistryItemRequest, DeleteRegistryItemResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.delete_item_called = True
        await stream.send_message(DeleteRegistryItemResponse())

    async def GetRegistryItem(self, stream: Stream[GetRegistryItemRequest, GetRegistryItemResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.include_markdown_documentation = request.include_markdown_documentation
        await stream.send_message(GetRegistryItemResponse(item=self.items[0]))

    async def GetOrganizationMetadata(self, stream: Stream[GetOrganizationMetadataRequest, GetOrganizationMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(
            GetOrganizationMetadataResponse(data=self.organization_metadata.get(request.organization_id, dict_to_struct({})))
        )

    async def UpdateOrganizationMetadata(
        self, stream: Stream[UpdateOrganizationMetadataRequest, UpdateOrganizationMetadataResponse]
    ) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.organization_metadata[request.organization_id] = request.data
        await stream.send_message(UpdateOrganizationMetadataResponse())

    async def GetLocationMetadata(self, stream: Stream[GetLocationMetadataRequest, GetLocationMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetLocationMetadataResponse(data=self.location_metadata.get(request.location_id, dict_to_struct({}))))

    async def UpdateLocationMetadata(self, stream: Stream[UpdateLocationMetadataRequest, UpdateLocationMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.location_metadata[request.location_id] = request.data
        await stream.send_message(UpdateLocationMetadataResponse())

    async def GetRobotMetadata(self, stream: Stream[GetRobotMetadataRequest, GetRobotMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetRobotMetadataResponse(data=self.robot_metadata.get(request.id, dict_to_struct({}))))

    async def UpdateRobotMetadata(self, stream: Stream[UpdateRobotMetadataRequest, UpdateRobotMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_metadata[request.id] = request.data
        await stream.send_message(UpdateRobotMetadataResponse())

    async def GetRobotPartMetadata(self, stream: Stream[GetRobotPartMetadataRequest, GetRobotPartMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        await stream.send_message(GetRobotPartMetadataResponse(data=self.robot_part_metadata.get(request.id, dict_to_struct({}))))

    async def UpdateRobotPartMetadata(self, stream: Stream[UpdateRobotPartMetadataRequest, UpdateRobotPartMetadataResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        self.robot_part_metadata[request.id] = request.data
        await stream.send_message(UpdateRobotPartMetadataResponse())


class MockGenericService(GenericService):
    timeout: Optional[float] = None

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, ValueTypes]:
        self.timeout = timeout
        return {key: True for key in command.keys()}

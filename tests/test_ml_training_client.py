import pytest
from google.protobuf.timestamp_pb2 import Timestamp
from grpclib.testing import ChannelFor

from viam.app.ml_training_client import MLTrainingClient
from viam.proto.app.mltraining import ModelType, SubmitTrainingJobRequest, TrainingJobMetadata, TrainingStatus
from viam.utils import create_filter

from .mocks.services import MockMLTraining

AUTH_TOKEN = "auth_token"
ML_TRAINING_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}
ID = "id"
TRAINING_JOB_ID = "training-job-id"
CANCEL_ID = "cancel-id"
DELETE_ID = "delete-id"
JOB_ID = "job-id"
ORG_ID = "org-id"
DATASET_ID = "dataset-id"
REGISTRY_ITEM_ID = "registry-item-id"
MODEL_ID = "model-id"
MODEL_NAME = "model-name"
MODEL_VERSION = "model-version"
MODEL_TYPE = ModelType.MODEL_TYPE_UNSPECIFIED
TRAINING_STATUS = TrainingStatus.TRAINING_STATUS_UNSPECIFIED
CREATED_ON = Timestamp(seconds=100, nanos=0)
LAST_MODIFIED = Timestamp(seconds=101, nanos=0)
TAGS = ["tag"]
FILTER = create_filter(
    component_name="component",
    component_type="type",
    method="method",
    robot_name="robot",
    robot_id="robo-id",
    part_name="part",
    part_id="part-id",
    location_ids=["location-id"],
    organization_ids=[ORG_ID],
    mime_type=["mime-type"],
    start_time=CREATED_ON.ToDatetime(),
    end_time=LAST_MODIFIED.ToDatetime(),
    tags=TAGS,
    bbox_labels=["bbox-label"],
)
SUBMIT_JOB_REQUEST = SubmitTrainingJobRequest(organization_id=ORG_ID)
TRAINING_METADATA = TrainingJobMetadata(
    status=TRAINING_STATUS,
    created_on=CREATED_ON,
    last_modified=LAST_MODIFIED,
    synced_model_id=MODEL_ID,
    id=ID,
    error_status=None,
)


@pytest.fixture(scope="function")
def service() -> MockMLTraining:
    return MockMLTraining(job_id=JOB_ID, training_metadata=TRAINING_METADATA)


class TestClient:
    @pytest.mark.asyncio
    async def test_cancel_training_job(self, service: MockMLTraining):
        async with ChannelFor([service]) as channel:
            client = MLTrainingClient(channel, ML_TRAINING_SERVICE_METADATA)
            await client.cancel_training_job(CANCEL_ID)
            assert service.cancel_job_id == CANCEL_ID

    @pytest.mark.asyncio
    async def test_submit_training_job(self, service: MockMLTraining):
        async with ChannelFor([service]) as channel:
            client = MLTrainingClient(channel, ML_TRAINING_SERVICE_METADATA)
            id = await client.submit_training_job(
                org_id=ORG_ID, dataset_id=DATASET_ID, model_name=MODEL_NAME, model_version=MODEL_VERSION, model_type=MODEL_TYPE, tags=TAGS
            )
            assert id == JOB_ID

    @pytest.mark.asyncio
    async def test_custom_submit_training_job(self, service: MockMLTraining):
        async with ChannelFor([service]) as channel:
            client = MLTrainingClient(channel, ML_TRAINING_SERVICE_METADATA)
            id = await client.submit_custom_training_job(
                org_id=ORG_ID, dataset_id=DATASET_ID, registry_item_id=REGISTRY_ITEM_ID, model_name=MODEL_NAME, model_version=MODEL_VERSION
            )
            assert id == JOB_ID

    @pytest.mark.asyncio
    async def test_get_training_job(self, service: MockMLTraining):
        async with ChannelFor([service]) as channel:
            client = MLTrainingClient(channel, ML_TRAINING_SERVICE_METADATA)
            training_metadata = await client.get_training_job(id=TRAINING_JOB_ID)
            assert training_metadata == TRAINING_METADATA
            assert service.training_job_id == TRAINING_JOB_ID

    @pytest.mark.asyncio
    async def test_list_training_jobs(self, service: MockMLTraining):
        async with ChannelFor([service]) as channel:
            client = MLTrainingClient(channel, ML_TRAINING_SERVICE_METADATA)
            training_jobs = await client.list_training_jobs(ORG_ID, TRAINING_STATUS)
            assert len(training_jobs) == 1
            assert training_jobs[0] == TRAINING_METADATA
            assert service.training_status == TRAINING_STATUS
            assert service.org_id == ORG_ID

    @pytest.mark.asyncio
    async def test_delete_completed_training_job(self, service: MockMLTraining):
        async with ChannelFor([service]) as channel:
            client = MLTrainingClient(channel, ML_TRAINING_SERVICE_METADATA)
            await client.delete_completed_training_job(DELETE_ID)
            assert service.delete_id == DELETE_ID

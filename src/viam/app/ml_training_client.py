from typing import List, Mapping, Optional

from grpclib.client import Channel

from viam import logging
from viam.proto.app.mltraining import (
    CancelTrainingJobRequest,
    DeleteCompletedTrainingJobRequest,
    GetTrainingJobRequest,
    GetTrainingJobResponse,
    ListTrainingJobsRequest,
    ListTrainingJobsResponse,
    MLTrainingServiceStub,
    ModelType,
    SubmitCustomTrainingJobRequest,
    SubmitCustomTrainingJobResponse,
    SubmitTrainingJobRequest,
    SubmitTrainingJobResponse,
    TrainingJobMetadata,
    TrainingStatus,
)

LOGGER = logging.getLogger(__name__)


class MLTrainingClient:
    """gRPC client for working with ML training jobs.

    Constructor is used by `ViamClient` to instantiate relevant service stubs.
    Calls to `MLTrainingClient` methods should be made through `ViamClient`.

    Establish a Connection::

        import asyncio

        from viam.rpc.dial import DialOptions, Credentials
        from viam.app.viam_client import ViamClient


        async def connect() -> ViamClient:
            # Replace "<API-KEY>" (including brackets) with your API key and "<API-KEY-ID>" with your API key ID
            dial_options = DialOptions.with_api_key("<API-KEY>", "<API-KEY-ID>")
            return await ViamClient.create_from_dial_options(dial_options)


        async def main():

            # Make a ViamClient
            viam_client = await connect()
            # Instantiate an MLTrainingClient to run ML training client API methods on
            ml_training_client = viam_client.ml_training_client

            viam_client.close()

        if __name__ == '__main__':
            asyncio.run(main())

    For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `MLTrainingClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """
        self._metadata = metadata
        self._ml_training_client = MLTrainingServiceStub(channel)
        self._channel = channel

    async def submit_training_job(
        self,
        org_id: str,
        dataset_id: str,
        model_name: str,
        model_version: str,
        model_type: ModelType.ValueType,
        tags: List[str],
    ) -> str:
        """Submit a training job.

        ::

            job_id = await ml_training_client.submit_training_job(
                organization_id=organization_id,
                dataset_id=dataset_id,
                model_name="your-model-name",
                model_version="1",
                model_type="ModelType.MODEL_TYPE_SINGLE_LABEL_CLASSIFICATION",
                tags=tags
            )

        Args:
            org_id (str): the id of the org to submit the training job to
            dataset_id (str): the id of the dataset
            model_name (str): the model name
            model_version (str): the model version
            model_type (ModelType.ValueType): the model type
            tags (List[str]): the tags

        Returns:
            str: the id of the training job

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """

        request = SubmitTrainingJobRequest(
            dataset_id=dataset_id,
            organization_id=org_id,
            model_name=model_name,
            model_version=model_version,
            model_type=model_type,
            tags=tags,
        )
        response: SubmitTrainingJobResponse = await self._ml_training_client.SubmitTrainingJob(request, metadata=self._metadata)
        return response.id

    async def submit_custom_training_job(
        self, org_id: str, dataset_id: str, registry_item_id: str, registry_item_version: str, model_name: str, model_version: str
    ) -> str:
        """Submit a custom training job.

        ::

            job_id = await ml_training_client.submit_custom_training_job(
                organization_id=organization_id,
                dataset_id=dataset_id,
                registry_item_id="your-registry-item-id",
                registry_item_version="your-registry-item-version",
                model_name="your-model-name",
                model_version="1"
            )

        Args:
            org_id (str): the id of the org to submit the training job to
            dataset_id (str): the id of the dataset
            registry_item_id (str): the id of the registry item
            registry_item_version (str): the version of the registry item
            model_name (str): the model name
            model_version (str): the model version

        Returns:
            str: the id of the training job

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """

        request = SubmitCustomTrainingJobRequest(
            dataset_id=dataset_id,
            registry_item_id=registry_item_id,
            registry_item_version=registry_item_version,
            organization_id=org_id,
            model_name=model_name,
            model_version=model_version,
        )
        response: SubmitCustomTrainingJobResponse = await self._ml_training_client.SubmitCustomTrainingJob(request, metadata=self._metadata)
        return response.id

    async def get_training_job(self, id: str) -> TrainingJobMetadata:
        """Gets training job data.

        ::

            job_metadata = await ml_training_client.get_training_job(
                id="INSERT YOUR JOB ID")

        Args:
            id (str): the id of the requested training job.

        Returns:
            viam.proto.app.mltraining.TrainingJobMetadata: training job data.

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """

        request = GetTrainingJobRequest(id=id)
        response: GetTrainingJobResponse = await self._ml_training_client.GetTrainingJob(request, metadata=self._metadata)

        return response.metadata

    async def list_training_jobs(
        self,
        org_id: str,
        training_status: Optional[TrainingStatus.ValueType] = None,
    ) -> List[TrainingJobMetadata]:
        """Returns training job data for all jobs within an org.

        ::

            jobs_metadata = await ml_training_client.list_training_jobs(
                org_id="INSERT YOUR ORG ID")

            first_job_id = jobs_metadata[1].id

        Args:
            org_id (str): the id of the org to request training job data from.
            training_status (Optional[TrainingStatus]): status of training jobs to filter the list by.
                If unspecified, all training jobs will be returned.

        Returns:
            List[viam.proto.app.mltraining.TrainingJobMetadata]: a list of training job data.

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """

        training_status = training_status if training_status else TrainingStatus.TRAINING_STATUS_UNSPECIFIED
        request = ListTrainingJobsRequest(organization_id=org_id, status=training_status)
        response: ListTrainingJobsResponse = await self._ml_training_client.ListTrainingJobs(request, metadata=self._metadata)

        return list(response.jobs)

    async def cancel_training_job(self, id: str) -> None:
        """Cancels the specified training job.

        ::

            await ml_training_client.cancel_training_job(
                id="INSERT YOUR JOB ID")

        Args:
            id (str): the id of the job to be canceled.

        Raises:
            GRPCError: if no training job exists with the given id.

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """

        request = CancelTrainingJobRequest(id=id)
        await self._ml_training_client.CancelTrainingJob(request, metadata=self._metadata)

    async def delete_completed_training_job(self, id: str) -> None:
        """Delete a completed training job from the database, whether the job succeeded or failed.

        ::

            await ml_training_client.delete_completed_training_job(
                id="INSERT YOUR JOB ID")

        Args:
            id (str): the id of the training job

        For more information, see `ML Training Client API <https://docs.viam.com/appendix/apis/ml-training-client/>`_.
        """
        request = DeleteCompletedTrainingJobRequest(id=id)
        await self._ml_training_client.DeleteCompletedTrainingJob(request, metadata=self._metadata)

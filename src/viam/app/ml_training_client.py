from typing import List, Mapping, Optional

from grpclib.client import Channel

from viam import logging
from viam.proto.app.data import Filter
from viam.proto.app.mltraining import (
    CancelTrainingJobRequest,
    GetTrainingJobRequest,
    GetTrainingJobResponse,
    ListTrainingJobsRequest,
    ListTrainingJobsResponse,
    MLTrainingServiceStub,
    ModelType,
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
    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `MLTrainingClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._ml_training_client = MLTrainingServiceStub(channel)
        self._channel = channel

    async def submit_training_job(
        self,
        org_id: str,
        model_name: str,
        model_version: str,
        model_type: ModelType,
        tags: List[str],
        filter: Optional[Filter] = None,
    ) -> str:
        raise NotImplementedError()

    async def get_training_job(self, id: str) -> TrainingJobMetadata:
        """Gets training job data.

        ::

            job_metadata = await ml_training_client.get_training_job(
                id="INSERT YOUR JOB ID")

        Args:
            id (str): id of the requested training job.

        Returns:
            viam.proto.app.mltraining.TrainingJobMetadata: training job data.
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
        """

        request = CancelTrainingJobRequest(id=id)
        await self._ml_training_client.CancelTrainingJob(request, metadata=self._metadata)

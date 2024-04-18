from typing import List, Mapping, Optional

from grpclib.client import Channel

from viam import logging
from viam.proto.provisioning import (
    CloudConfig,
    GetNetworkListRequest,
    GetNetworkListResponse,
    GetSmartMachineStatusRequest,
    GetSmartMachineStatusResponse,
    NetworkInfo,
    ProvisioningServiceStub,
    SetNetworkCredentialsRequest,
    SetSmartMachineCredentialsRequest,
)

LOGGER = logging.getLogger(__name__)


class ProvisioningClient:
    """gRPC client for getting and setting smart machine info.

    Constructor is used by `ViamClient` to instantiate relevant service stubs. Calls to
    `ProvisioningClient` methods should be made through `ViamClient`.

    Establish a connection::

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
            # Instantiate a ProvisioningClient to run provisioning client API methods on
            provisioning_client = viam_client.provisioning_client

            viam_client.close()

        if __name__ == '__main__':
            asyncio.run(main())

    """

    def __init__(self, channel: Channel, metadata: Mapping[str, str]):
        """Create a `ProvisioningClient` that maintains a connection to app.

        Args:
            channel (grpclib.client.Channel): Connection to app.
            metadata (Mapping[str, str]): Required authorization token to send requests to app.
        """
        self._metadata = metadata
        self._provisioning_client = ProvisioningServiceStub(channel)
        self._channel = channel

    _provisioning_client: ProvisioningServiceStub
    _metadata: Mapping[str, str]
    _channel: Channel

    async def get_network_list(self) -> List[NetworkInfo]:
        """Returns list of networks that are visible to the Smart Machine."""
        request = GetNetworkListRequest()
        resp: GetNetworkListResponse = await self._provisioning_client.GetNetworkList(request, metadata=self._metadata)
        return list(resp.networks)

    async def get_smart_machine_status(self) -> GetSmartMachineStatusResponse:
        """Returns the status of the smart machine."""
        request = GetSmartMachineStatusRequest()
        return await self._provisioning_client.GetSmartMachineStatus(request, metadata=self._metadata)

    async def set_network_credentials(self, network_type: str, ssid: str, psk: str) -> None:
        """Sets the network credentials of the Smart Machine.

        Args:
            network_type (str): The type of the network.
            ssid (str): The SSID of the network.
            psk (str): The network's passkey.
        """

        request = SetNetworkCredentialsRequest(type=network_type, ssid=ssid, psk=psk)
        await self._provisioning_client.SetNetworkCredentials(request, metadata=self._metadata)

    async def set_smart_machine_credentials(self, cloud_config: Optional[CloudConfig] = None) -> None:
        request = SetSmartMachineCredentialsRequest(cloud=cloud_config)
        await self._provisioning_client.SetSmartMachineCredentials(request, metadata=self._metadata)

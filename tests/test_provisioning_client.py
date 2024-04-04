import pytest

from grpclib.testing import ChannelFor

from viam.app.provisioning_client import ProvisioningClient

from viam.proto.provisioning import GetSmartMachineStatusResponse, NetworkInfo, ProvisioningInfo, CloudConfig

from .mocks.services import MockProvisioning

ID = "id"
MODEL = "model"
MANUFACTURER = "acme"
PROVISIONING_INFO = ProvisioningInfo(fragment_id=ID, model=MODEL, manufacturer=MANUFACTURER)
HAS_CREDENTIALS = True
IS_ONLINE = True
NETWORK_TYPE = "type"
SSID = "ssid"
ERROR = "error"
ERRORS = [ERROR]
PSK = "psk"
SECRET = "secret"
APP_ADDRESS = "address"
NETWORK_INFO_LATEST = NetworkInfo(
    type=NETWORK_TYPE,
    ssid=SSID,
    security="security",
    signal=12,
    connected=IS_ONLINE,
    last_error=ERROR,
)
NETWORK_INFO = [NETWORK_INFO_LATEST]
SMART_MACHINE_STATUS_RESPONSE = GetSmartMachineStatusResponse(
    provisioning_info=PROVISIONING_INFO,
    has_smart_machine_credentials=HAS_CREDENTIALS,
    is_online=IS_ONLINE,
    latest_connection_attempt=NETWORK_INFO_LATEST,
    errors=ERRORS
)
CLOUD_CONFIG = CloudConfig(id=ID, secret=SECRET, app_address=APP_ADDRESS)

AUTH_TOKEN = "auth_token"
PROVISIONING_SERVICE_METADATA = {"authorization": f"Bearer {AUTH_TOKEN}"}

@pytest.fixture(scope="function")
def service() -> MockProvisioning:
    return MockProvisioning(smart_machine_status=SMART_MACHINE_STATUS_RESPONSE, network_info=NETWORK_INFO)


class TestClient:
    @pytest.mark.asyncio
    async def test_get_network_list(self, service: MockProvisioning):
        async with ChannelFor([service]) as channel:
            client = ProvisioningClient(channel, PROVISIONING_SERVICE_METADATA)
            network_info = await client.get_network_list(channel, PROVISIONING_SERVICE_METADATA)
            assert network_info == NETWORK_INFO


    @pytest.mark.asyncio
    async def test_get_smart_machine_status(self, service: MockProvisioning):
        async with ChannelFor([service]) as channel:
            client = ProvisioningClient(channel, PROVISIONING_SERVICE_METADATA)
            smart_machine_status = await client.get_smart_machine_status()
            assert smart_machine_status == SMART_MACHINE_STATUS_RESPONSE

    @pytest.mark.asyncio
    async def test_set_network_credentials(self, service: MockProvisioning):
        async with ChannelFor([service]) as channel:
            client = ProvisioningClient(channel, PROVISIONING_SERVICE_METADATA)
            await client.set_network_credentials(type=NETWORK_TYPE, ssid=SSID, psk=PSK)
            assert service.network_type == NETWORK_TYPE
            assert service.ssid == SSID
            assert service.psk == PSK

    @pytest.mark.asyncio
    async def test_set_smart_machine_credentials(self, service: MockProvisioning):
        async with ChannelFor([service]) as channel:
            client = ProvisioningClient(channel, PROVISIONING_SERVICE_METADATA)
            await client.set_smart_machine_credentials(cloud_config=CLOUD_CONFIG)
            assert service.cloud_config == CLOUD_CONFIG

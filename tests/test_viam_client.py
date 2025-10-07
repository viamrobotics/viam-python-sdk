import os
import random
from unittest.mock import patch
from uuid import uuid4

import pytest
from grpclib.testing import ChannelFor

from viam.app.app_client import RobotPart
from viam.app.viam_client import ViamClient
from viam.rpc.dial import Credentials, DialOptions


class TestViamClient:
    async def test_requires_credentials(self):
        with pytest.raises(ValueError):
            await ViamClient.create_from_dial_options(DialOptions())

    async def test_disallows_robot_secret(self):
        with pytest.raises(ValueError):
            creds = Credentials("robot-secret", "SOME_ROBOT_SECRET")
            await ViamClient.create_from_dial_options(DialOptions(credentials=creds))

    async def test_requires_auth_entity(self):
        with pytest.raises(ValueError):
            creds = Credentials("api-key", "SOME_API_KEY")
            await ViamClient.create_from_dial_options(DialOptions(credentials=creds))

    async def test_sets_fields(self):
        async with ChannelFor([]) as channel:
            with patch("viam.app.viam_client._dial_app") as patched_dial:
                patched_dial.return_value = channel
                with patch("viam.app.viam_client._get_access_token") as patched_auth:
                    ACCESS_TOKEN = "MY_ACCESS_TOKEN"
                    patched_auth.return_value = ACCESS_TOKEN

                    creds = Credentials("robot-location-secret", "SOME_LOCATION_SECRET")
                    auth_entity = "SOME.AUTH.ENTITY"
                    DIAL_OPTIONS = DialOptions(credentials=creds, auth_entity=auth_entity)

                    client = await ViamClient.create_from_dial_options(DIAL_OPTIONS)

                    assert client._dial_options == DIAL_OPTIONS
                    assert DIAL_OPTIONS.auth_entity is not None
                    assert client._location_id == DIAL_OPTIONS.auth_entity.split(".")[1]
                    assert client._metadata == {"authorization": f"Bearer {ACCESS_TOKEN}"}

    async def test_clients(self):
        async with ChannelFor([]) as channel:
            with patch("viam.app.viam_client._dial_app") as patched_dial:
                patched_dial.return_value = channel
                with patch("viam.app.viam_client._get_access_token") as patched_auth:
                    ACCESS_TOKEN = "MY_ACCESS_TOKEN"
                    METADATA = {"authorization": f"Bearer {ACCESS_TOKEN}"}
                    patched_auth.return_value = ACCESS_TOKEN

                    creds = Credentials("robot-location-secret", "SOME_LOCATION_SECRET")
                    opts = DialOptions(credentials=creds, auth_entity="SOME.AUTH.ENTITY")

                    client = await ViamClient.create_from_dial_options(opts)

                    assert client.data_client._channel == channel
                    assert client.data_client._metadata == METADATA

                    assert client.app_client._channel == channel
                    assert client.app_client._metadata == METADATA

                    assert client.ml_training_client._channel == channel
                    assert client.ml_training_client._metadata == METADATA

                    assert client.billing_client._channel == channel
                    assert client.billing_client._metadata == METADATA

                    assert client.provisioning_client._channel == channel
                    assert client.provisioning_client._metadata == METADATA

    async def test_client_from_env_vars(self):
        async with ChannelFor([]) as channel:
            with patch("viam.app.viam_client._dial_app") as patched_dial:
                patched_dial.return_value = channel
                with patch("viam.app.viam_client._get_access_token") as patched_auth:
                    ACCESS_TOKEN = "MY_ACCESS_TOKEN"
                    METADATA = {"authorization": f"Bearer {ACCESS_TOKEN}"}
                    patched_auth.return_value = ACCESS_TOKEN

                    os.environ["VIAM_API_KEY"] = "MY_API_KEY"
                    os.environ["VIAM_API_KEY_ID"] = str(uuid4())

                    client = await ViamClient.create_from_env_vars()

                    assert client.data_client._channel == channel
                    assert client.data_client._metadata == METADATA

                    assert client.app_client._channel == channel
                    assert client.app_client._metadata == METADATA

                    assert client.ml_training_client._channel == channel
                    assert client.ml_training_client._metadata == METADATA

                    assert client.billing_client._channel == channel
                    assert client.billing_client._metadata == METADATA

                    assert client.provisioning_client._channel == channel
                    assert client.provisioning_client._metadata == METADATA

    async def test_closes(self):
        async with ChannelFor([]) as channel:
            with patch.object(channel, "close"):
                with patch("viam.app.viam_client._dial_app") as patched_dial:
                    patched_dial.return_value = channel
                    with patch("viam.app.viam_client._get_access_token") as patched_auth:
                        patched_auth.return_value = "MY_ACCESS_TOKEN"

                        creds = Credentials("robot-location-secret", "SOME_LOCATION_SECRET")
                        opts = DialOptions(credentials=creds, auth_entity="SOME.AUTH.ENTITY")

                        client = await ViamClient.create_from_dial_options(opts)

                        assert client._closed is False
                        client.close()
                        assert client._closed is True

    async def test_context_manager(self):
        async with ChannelFor([]) as channel:
            with patch.object(channel, "close"):
                with patch("viam.app.viam_client._dial_app") as patched_dial:
                    patched_dial.return_value = channel
                    with patch("viam.app.viam_client._get_access_token") as patched_auth:
                        patched_auth.return_value = "MY_ACCESS_TOKEN"

                        creds = Credentials("robot-location-secret", "SOME_LOCATION_SECRET")
                        opts = DialOptions(credentials=creds, auth_entity="SOME.AUTH.ENTITY")

                        async with await ViamClient.create_from_dial_options(opts) as client:
                            assert client._closed is False
                        assert client._closed is True

    class TestConnectToMachine:
        @pytest.fixture
        async def client(self):
            async with ChannelFor([]) as channel:
                with patch("viam.app.viam_client._dial_app") as patched_dial:
                    patched_dial.return_value = channel
                    with patch("viam.app.viam_client._get_access_token") as patched_auth:
                        patched_auth.return_value = "MY_ACCESS_TOKEN"

                        creds = Credentials("api-key", "MY_API_KEY")
                        opts = DialOptions(credentials=creds, auth_entity=str(uuid4()))

                        yield await ViamClient.create_from_dial_options(opts)

        async def test_requires_address_or_id(self, client: ViamClient):
            with pytest.raises(ValueError):
                await client.connect_to_machine()

        async def test_address_supersedes_id(self, client: ViamClient):
            with patch("viam.app.app_client.AppClient.get_robot_parts") as get_robot_parts:
                with patch("viam.app.viam_client.RobotClient.at_address") as get_robot_client:
                    ADDRESS = "MACHINE_ADDRESS"
                    await client.connect_to_machine(address=ADDRESS, id="MACHINE_ID")

                    get_robot_parts.assert_not_called()
                    assert get_robot_client.call_args.args[0] == ADDRESS

        async def test_gets_main_part_address(self, client: ViamClient):
            with patch("viam.app.app_client.AppClient.get_robot_parts") as get_robot_parts:
                MAIN_PART = RobotPart()
                MAIN_PART.fqdn = "main.part.fqdn"
                MAIN_PART.main_part = True

                ROBOT_PARTS = [MAIN_PART]
                for _ in range(10):
                    part = RobotPart()
                    part.main_part = False
                    ROBOT_PARTS.append(part)
                random.shuffle(ROBOT_PARTS)

                get_robot_parts.return_value = ROBOT_PARTS

                with patch("viam.app.viam_client.RobotClient.at_address") as get_robot_client:
                    MACHINE_ID = "MACHINE_ID"
                    await client.connect_to_machine(id=MACHINE_ID)
                    get_robot_parts.assert_called_once_with(MACHINE_ID)
                    assert get_robot_client.call_args.args[0] == MAIN_PART.fqdn

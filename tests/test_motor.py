from typing import cast
from unittest.mock import AsyncMock

import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.motor import Motor, MotorClient
from viam.components.motor.service import MotorRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse, GetGeometriesRequest, GetStatusRequest, GetStatusResponse
from viam.proto.component.motor import (
    GetPositionRequest,
    GetPositionResponse,
    GetPropertiesRequest,
    GetPropertiesResponse,
    GoForRequest,
    GoToRequest,
    IsMovingRequest,
    IsMovingResponse,
    IsPoweredRequest,
    IsPoweredResponse,
    MotorServiceStub,
    ResetZeroPositionRequest,
    SetPowerRequest,
    SetRPMRequest,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.resource.rpc_client_base import ResourceRPCClientBase
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks import create_mock_subclass


@pytest.fixture(scope="function")
def motor() -> Motor:
    mm = create_mock_subclass(Motor)
    return mm(name="motor")


@pytest.fixture(scope="function")
def service(motor) -> MotorRPCService:
    manager = ResourceManager([motor])
    return MotorRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(motor) -> GenericRPCService:
    manager = ResourceManager([motor])
    return GenericRPCService(manager)


DEFAULT_EXTRA = {"a": "b"}
DEFAULT_EXTRA_STRUCT = dict_to_struct(DEFAULT_EXTRA)
DEFAULT_TIMEOUT = 1.82
DEFAULT_TIMEOUT_APPROX = loose_approx(DEFAULT_TIMEOUT)
DEFAULT_METADATA = ResourceRPCClientBase.Metadata()
DEFAULT_METADATA.enable_debug_logging


class TestService:
    async def test_set_power(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            request = SetPowerRequest(name=motor.name, power_pct=13, extra=DEFAULT_EXTRA_STRUCT)
            client = MotorServiceStub(channel)
            await client.SetPower(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.set_power).assert_called_once_with(
                13, timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_position(self, motor: Motor, service: MotorRPCService):
        position = 7.86
        cast(AsyncMock, motor.get_position).return_value = position

        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetPositionRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            response: GetPositionResponse = await client.GetPosition(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            assert response.position == position
            cast(AsyncMock, motor.get_position).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_go_for(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GoForRequest(name=motor.name, rpm=30, revolutions=20, extra=DEFAULT_EXTRA_STRUCT)
            await client.GoFor(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.go_for).assert_called_once_with(
                30, 20, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_go_to(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GoToRequest(name=motor.name, rpm=30, position_revolutions=20, extra=DEFAULT_EXTRA_STRUCT)
            await client.GoTo(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.go_to).assert_called_once_with(
                30, 20, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_set_rpm(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = SetRPMRequest(name=motor.name, rpm=30, extra=DEFAULT_EXTRA_STRUCT)
            await client.SetRPM(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.set_rpm).assert_called_once_with(
                30, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_reset_zero(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = ResetZeroPositionRequest(name=motor.name, offset=20, extra=DEFAULT_EXTRA_STRUCT)
            await client.ResetZeroPosition(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.reset_zero_position).assert_called_once_with(
                20, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_properties(self, motor: Motor, service: MotorRPCService):
        properties = Motor.Properties(position_reporting=True)
        cast(AsyncMock, motor.get_properties).return_value = properties

        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetPropertiesRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            response: GetPropertiesResponse = await client.GetProperties(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            assert response.position_reporting == properties.position_reporting
            cast(AsyncMock, motor.get_properties).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_stop(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = StopRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            await client.Stop(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.stop).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_is_powered(self, motor: Motor, service: MotorRPCService):
        is_powered = True
        power_pct = 7.86
        cast(AsyncMock, motor.is_powered).return_value = (is_powered, power_pct)

        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = IsPoweredRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            response: IsPoweredResponse = await client.IsPowered(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            assert response.is_on == is_powered
            assert response.power_pct == power_pct
            cast(AsyncMock, motor.is_powered).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_is_moving(self, motor: Motor, service: MotorRPCService):
        is_moving = True
        cast(AsyncMock, motor.is_moving).return_value = is_moving

        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = IsMovingRequest(name=motor.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving == is_moving
            cast(AsyncMock, motor.is_moving).assert_called_once()

    async def test_do(self, motor: Motor, service: MotorRPCService):
        command = {"command": "args"}
        cast(AsyncMock, motor.do_command).return_value = {"command": command}

        async with ChannelFor([service]) as channel:
            request = DoCommandRequest(name=motor.name, command=dict_to_struct(command))
            client = MotorServiceStub(channel)
            response: DoCommandResponse = await client.DoCommand(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            result = struct_to_dict(response.result)
            assert result == {"command": command}
            cast(AsyncMock, motor.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_status(self, motor: Motor, service: MotorRPCService):
        cast(AsyncMock, motor.get_status).return_value = {}
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetStatusRequest(name=motor.name)
            response: GetStatusResponse = await client.GetStatus(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            assert struct_to_dict(response.result) == {}
            cast(AsyncMock, motor.get_status).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_geometries(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetGeometriesRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            await client.GetGeometries(request, timeout=DEFAULT_TIMEOUT)
            cast(AsyncMock, motor.get_geometries).assert_called_once_with(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX)


class TestClient:
    async def test_set_power(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.set_power(13, timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.set_power).assert_called_once_with(
                13, timeout=DEFAULT_TIMEOUT_APPROX, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_position(self, motor: Motor, service: MotorRPCService):
        position = 7.86
        cast(AsyncMock, motor.get_position).return_value = position

        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            result = await client.get_position(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            assert result == position
            cast(AsyncMock, motor.get_position).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_go_for(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.go_for(30, 20, timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.go_for).assert_called_once_with(
                30, 20, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_go_to(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.go_to(30, 20, timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.go_to).assert_called_once_with(
                30, 20, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_set_rpm(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.set_rpm(30, timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.set_rpm).assert_called_once_with(
                30, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_reset_zero(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.reset_zero_position(20, timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.reset_zero_position).assert_called_once_with(
                20, extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_properties(self, motor: Motor, service: MotorRPCService):
        properties = Motor.Properties(position_reporting=True)
        cast(AsyncMock, motor.get_properties).return_value = properties

        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            result = await client.get_properties(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            assert result == properties
            cast(AsyncMock, motor.get_properties).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_stop(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.stop(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.stop).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_is_powered(self, motor: Motor, service: MotorRPCService):
        is_powered = True
        power_pct = 7.86
        cast(AsyncMock, motor.is_powered).return_value = (is_powered, power_pct)

        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            result_is_on, result_power_pct = await client.is_powered(
                timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA
            )
            assert result_is_on == is_powered
            assert result_power_pct == power_pct
            cast(AsyncMock, motor.is_powered).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_is_moving(self, motor: Motor, service: MotorRPCService):
        is_moving = True
        cast(AsyncMock, motor.is_moving).return_value = is_moving

        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            result = await client.is_moving()
            assert result == is_moving
            cast(AsyncMock, motor.is_moving).assert_called_once()

    async def test_do(self, motor: Motor, service: MotorRPCService):
        command = {"command": "args"}
        cast(AsyncMock, motor.do_command).return_value = {"command": command}

        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            result = await client.do_command(command, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            assert result == {"command": command}
            cast(AsyncMock, motor.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_status(self, motor: Motor, service: MotorRPCService):
        cast(AsyncMock, motor.get_status).return_value = {}
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            status = await client.get_status(timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            assert status == {}
            cast(AsyncMock, motor.get_status).assert_called_once_with(
                timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_geometries(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.get_geometries(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.get_geometries).assert_called_once_with(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX)

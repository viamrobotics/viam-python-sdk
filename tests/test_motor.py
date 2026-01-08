from typing import cast
from unittest.mock import AsyncMock

import pytest
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.motor import Motor, MotorClient
from viam.components.motor.service import MotorRPCService
from viam.proto.common import DoCommandRequest, GetGeometriesRequest
from viam.proto.component.motor import (
    GetPositionRequest,
    GetPropertiesRequest,
    GoForRequest,
    GoToRequest,
    IsMovingRequest,
    IsPoweredRequest,
    MotorServiceStub,
    ResetZeroPositionRequest,
    SetPowerRequest,
    SetRPMRequest,
    StopRequest,
)
from viam.resource.manager import ResourceManager
from viam.resource.rpc_client_base import ResourceRPCClientBase
from viam.utils import dict_to_struct

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
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = GetPositionRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            await client.GetPosition(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
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
        async with ChannelFor([service]) as channel:
            cast(AsyncMock, motor.get_properties).return_value = Motor.Properties(position_reporting=True)
            client = MotorServiceStub(channel)
            request = GetPropertiesRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            await client.GetProperties(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
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
        async with ChannelFor([service]) as channel:
            cast(AsyncMock, motor.is_powered).return_value = (True, 7.86)
            client = MotorServiceStub(channel)
            request = IsPoweredRequest(name=motor.name, extra=DEFAULT_EXTRA_STRUCT)
            await client.IsPowered(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.is_powered).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_is_moving(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorServiceStub(channel)
            request = IsMovingRequest(name=motor.name)
            await client.IsMoving(request)
            cast(AsyncMock, motor.is_moving).assert_called_once()

    async def test_do(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            command = {"command": "args"}
            request = DoCommandRequest(name=motor.name, command=dict_to_struct(command))
            client = MotorServiceStub(channel)
            await client.DoCommand(request, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA.proto)
            cast(AsyncMock, motor.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
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
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.get_position(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
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
        async with ChannelFor([service]) as channel:
            cast(AsyncMock, motor.get_properties).return_value = Motor.Properties(position_reporting=True)
            client = MotorClient(motor.name, channel)
            await client.get_properties(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
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
        async with ChannelFor([service]) as channel:
            cast(AsyncMock, motor.is_powered).return_value = (True, 7.86)
            client = MotorClient(motor.name, channel)
            await client.set_power(13)
            await client.is_powered(timeout=DEFAULT_TIMEOUT, extra=DEFAULT_EXTRA, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.is_powered).assert_called_once_with(
                extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_is_moving(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.is_moving()
            cast(AsyncMock, motor.is_moving).assert_called_once()

    async def test_do(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            command = {"command": "args"}
            await client.do_command(command, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.do_command).assert_called_once_with(
                command=command, timeout=DEFAULT_TIMEOUT_APPROX, metadata=DEFAULT_METADATA.metadata
            )

    async def test_get_geometries(self, motor: Motor, service: MotorRPCService):
        async with ChannelFor([service]) as channel:
            client = MotorClient(motor.name, channel)
            await client.get_geometries(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT, metadata=DEFAULT_METADATA)
            cast(AsyncMock, motor.get_geometries).assert_called_once_with(extra=DEFAULT_EXTRA, timeout=DEFAULT_TIMEOUT_APPROX)

from typing import Any, Dict, Optional

import pytest
from grpclib import GRPCError, Status
from grpclib.testing import ChannelFor

from viam.components.generic.service import GenericRPCService
from viam.components.power_sensor import PowerSensor, PowerSensorClient, PowerSensorRPCService
from viam.proto.common import DoCommandRequest, DoCommandResponse
from viam.proto.component.powersensor import (
    GetVoltageRequest,
    GetVoltageResponse,
    GetCurrentRequest,
    GetCurrentResponse,
    GetPowerRequest,
    GetPowerResponse,
    PowerSensorServiceStub,
)

from viam.resource.manager import ResourceManager
from viam.utils import dict_to_struct, struct_to_dict

from . import loose_approx
from .mocks.components import MockPowerSensor

VOLTS = 3.2
AMPERES = 2.0
WATTS = 1.0
IS_AC = True
EXTRA_PARAMS = {"foo": "bar", "baz": [1, 2, 3]}


@pytest.fixture(scope="function")
def power_sensor() -> PowerSensor:
    return MockPowerSensor("power_sensor", VOLTS, AMPERES, IS_AC, WATTS)


@pytest.fixture(scope="function")
def service(power_sensor: PowerSensor) -> PowerSensorRPCService:
    manager = ResourceManager([power_sensor])
    return PowerSensorRPCService(manager)


@pytest.fixture(scope="function")
def generic_service(power_sensor: PowerSensor) -> GenericRPCService:
    manager = ResourceManager([power_sensor])
    return GenericRPCService(manager)


class TestPowerSensor:
    @pytest.mark.asyncio
    async def test_get_voltage(self, power_sensor: MockPowerSensor):
        assert power_sensor.extra is None
        (volts, is_ac) = await power_sensor.get_voltage(extra=EXTRA_PARAMS)
        assert volts == VOLTS
        assert is_ac == IS_AC
        assert power_sensor.extra == EXTRA_PARAMS

    async def test_get_current(self, power_sensor: MockPowerSensor):
        assert power_sensor.extra is None
        (amperes, is_ac) = await power_sensor.get_current(extra=EXTRA_PARAMS)
        assert amperes == AMPERES
        assert is_ac == IS_AC
        assert power_sensor.extra == EXTRA_PARAMS

    async def test_get_power(self, power_sensor: MockPowerSensor):
        assert power_sensor.extra is None
        watts = await power_sensor.get_power(extra=EXTRA_PARAMS)
        assert watts == WATTS
        assert power_sensor.extra == EXTRA_PARAMS

    async def test_get_readings(self, power_sensor: MockPowerSensor):
        assert power_sensor.extra is None
        value = await power_sensor.get_readings(extra=EXTRA_PARAMS)
        assert value == {"voltage": VOLTS, "current": AMPERES, "is_ac": IS_AC, "power": WATTS}
        assert power_sensor.extra == EXTRA_PARAMS

        # A mock method to replace some get functions just for testing that should result in omitted entries in the dictionary
        async def get_reading(*, extra: Optional[Dict[str, Any]] = None, timeout: Optional[float] = None, **kwargs) -> float:
            raise GRPCError(Status(2), "Unimplemented")

        power_sensor.get_power = get_reading

        value = await power_sensor.get_readings(extra=EXTRA_PARAMS)
        assert value == {"voltage": VOLTS, "current": AMPERES, "is_ac": IS_AC}

    @pytest.mark.asyncio
    async def test_timeout(self, power_sensor: MockPowerSensor):
        assert power_sensor.timeout is None

        await power_sensor.get_voltage(timeout=1.23)
        assert power_sensor.timeout == loose_approx(1.23)

        await power_sensor.get_current(timeout=2.34)
        assert power_sensor.timeout == loose_approx(2.34)

        await power_sensor.get_power(timeout=3.45)
        assert power_sensor.timeout == loose_approx(3.45)

        await power_sensor.get_readings(timeout=8.90)
        assert power_sensor.timeout == loose_approx(8.90)

    @pytest.mark.asyncio
    async def test_do(self, power_sensor: PowerSensor):
        command = {"command": "args"}
        resp = await power_sensor.do_command(command)
        assert resp == {"command": command}


class TestService:
    @pytest.mark.asyncio
    async def test_get_voltage(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorServiceStub(channel)
            request = GetVoltageRequest(name=power_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert power_sensor.extra is None
            response: GetVoltageResponse = await client.GetVoltage(request, timeout=1.23)
            assert response.volts == VOLTS
            assert response.is_ac == IS_AC
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_current(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorServiceStub(channel)
            request = GetCurrentRequest(name=power_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert power_sensor.extra is None
            response: GetCurrentResponse = await client.GetCurrent(request, timeout=1.23)
            assert response.amperes == AMPERES
            assert response.is_ac == IS_AC
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_get_power(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorServiceStub(channel)
            request = GetPowerRequest(name=power_sensor.name, extra=dict_to_struct(EXTRA_PARAMS))
            assert power_sensor.extra is None
            response: GetPowerResponse = await client.GetPower(request, timeout=1.23)
            assert response.watts == WATTS
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(1.23)

    @pytest.mark.asyncio
    async def test_do(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorServiceStub(channel)
            command = {"command": "args"}
            request = DoCommandRequest(name=power_sensor.name, command=dict_to_struct(command))
            response: DoCommandResponse = await client.DoCommand(request)
            result = struct_to_dict(response.result)
            assert result == {"command": command}


class TestClient:
    @pytest.mark.asyncio
    async def test_get_voltage(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorClient(power_sensor.name, channel)
            assert power_sensor.extra is None
            (vol, is_ac) = await client.get_voltage(extra=EXTRA_PARAMS, timeout=1.45)
            assert vol == VOLTS
            assert is_ac == IS_AC
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(1.45)

    @pytest.mark.asyncio
    async def test_get_current(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorClient(power_sensor.name, channel)
            assert power_sensor.extra is None
            (vol, is_ac) = await client.get_voltage(extra=EXTRA_PARAMS, timeout=1.45)
            assert vol == VOLTS
            assert is_ac == IS_AC
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(1.45)

    @pytest.mark.asyncio
    async def test_get_power(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorClient(power_sensor.name, channel)
            assert power_sensor.extra is None
            watts = await client.get_power(extra=EXTRA_PARAMS, timeout=1.45)
            assert watts == WATTS
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(1.45)

    @pytest.mark.asyncio
    async def test_get_readings(self, power_sensor: MockPowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorClient(power_sensor.name, channel)
            assert power_sensor.extra is None
            value = await client.get_readings(extra=EXTRA_PARAMS, timeout=8.90)
            assert value == {
                "voltage": VOLTS,
                "current": AMPERES,
                "is_ac": IS_AC,
                "power": WATTS,
            }
            assert power_sensor.extra == EXTRA_PARAMS
            assert power_sensor.timeout == loose_approx(8.90)

    @pytest.mark.asyncio
    async def test_do(self, power_sensor: PowerSensor, service: PowerSensorRPCService):
        async with ChannelFor([service]) as channel:
            client = PowerSensorClient(power_sensor.name, channel)
            command = {"command": "args"}
            resp = await client.do_command(command)
            assert resp == {"command": command}

import asyncio
import time
from typing import Mapping

import pytest
from grpclib import const
from grpclib.client import Channel

from viam.components.component_base import ComponentBase
from viam.errors import ResourceNotFoundError
from viam.operations import run_with_operation
from viam.resource.manager import ResourceManager
from viam.resource.registry import Registry, ResourceRegistration
from viam.resource.rpc_client_base import ReconfigurableResourceRPCClientBase
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import Subtype


async def test_cancellation_propagation():
    class TestComponent(ComponentBase):
        SUBTYPE = Subtype("test", "test", "test")

        long_running_task_cancelled = False

        @run_with_operation
        async def long_running(self, **kwargs) -> bool:
            operation = self.get_operation(kwargs)
            for _ in range(5):
                time.sleep(0.01)
                if await operation.is_cancelled():
                    self.long_running_task_cancelled = True
                    return self.long_running_task_cancelled
            self.long_running_task_cancelled = False
            return self.long_running_task_cancelled

    class TestClient(TestComponent, ReconfigurableResourceRPCClientBase):
        def __init__(self, name: str, channel: Channel): ...

    class TestService(ResourceRPCServiceBase):
        RESOURCE_TYPE = TestComponent

        async def long_running(self) -> bool:
            component = self.get_resource("test")
            return await component.long_running()

        def __mapping__(self) -> Mapping[str, const.Handler]:
            return {
                "/TestService/long_running": const.Handler(self.long_running, const.Cardinality.UNARY_UNARY, "TestRequest", "TestResponse")
            }

    component = TestComponent("test")
    with pytest.raises(ResourceNotFoundError):
        service = TestService(ResourceManager([component]))

    Registry.register_api(ResourceRegistration(TestComponent, TestService, lambda name, channel: TestClient(name, channel)))
    service = TestService(ResourceManager([component]))

    # Test bare functions
    result = await component.long_running()
    assert result is False

    # Test from service
    result = await service.long_running()
    assert result is False

    # Test cancelled from service
    with pytest.raises(asyncio.CancelledError):
        task = asyncio.create_task(service.long_running())

        asyncio.get_event_loop().call_later(0.02, task.cancel)

        result = await task

    assert component.long_running_task_cancelled is True

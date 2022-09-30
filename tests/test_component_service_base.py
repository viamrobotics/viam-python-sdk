import asyncio
import time
import pytest
from viam.operations import run_with_operation
from viam.components.component_base import ComponentBase
from viam.components.resource_manager import ResourceManager
from viam.components.service_base import ComponentServiceBase


@pytest.mark.asyncio
async def test_cancellation_propagation():
    class TestComponent(ComponentBase):

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

    class TestService(ComponentServiceBase[TestComponent]):

        RESOURCE_TYPE = TestComponent

        async def long_running(self) -> bool:
            component = self.get_component("test")
            return await component.long_running()

    component = TestComponent("test")
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

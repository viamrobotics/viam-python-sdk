import asyncio
import time
import pytest
from viam.operations import run_with_operation
from viam.components.component_base import ComponentBase
from viam.components.resource_manager import ResourceManager
from viam.components.service_base import ComponentServiceBase


@pytest.mark.asyncio
async def test_component_service_base():
    class TestComponent(ComponentBase):

        long_running_task_cancelled = False

        async def no_return(self, **kwargs):
            pass

        async def return_one(self, **kwargs) -> int:
            return 1

        async def add(self, a: float, b: float, **kwargs) -> float:
            return a + b

        @run_with_operation
        async def long_running(self, **kwargs) -> bool:
            operation = self.get_operation(kwargs)
            for i in range(5):
                print(i)
                time.sleep(0.01)
                if await operation.is_cancelled():
                    self.long_running_task_cancelled = True
                    return self.long_running_task_cancelled
            self.long_running_task_cancelled = False
            return self.long_running_task_cancelled

    class TestService(ComponentServiceBase[TestComponent]):

        RESOURCE_TYPE = TestComponent

        async def no_return(self):
            component = self.get_component("test")
            return await component.no_return()

        async def return_one(self) -> int:
            component = self.get_component("test")
            return await component.return_one()

        async def add(self, a: float, b: float) -> float:
            component = self.get_component("test")
            return await component.add(a, b)

        async def long_running(self) -> bool:
            component = self.get_component("test")
            return await component.long_running()

    component = TestComponent("test")
    service = TestService(ResourceManager([component]))

    # Test bare functions
    await component.no_return()

    result = await component.return_one()
    assert result == 1

    result = await component.add(0.2, 0.3)
    assert result == 0.5

    result = await component.long_running()
    assert result is False

    # Test wrapped with operation
    await service.no_return()

    result = await service.return_one()
    assert result == 1

    result = await service.add(0.2, 0.3)
    assert result == 0.5

    result = await service.long_running()
    assert result is False

    # Test cancelled when wrapped with operation
    with pytest.raises(asyncio.CancelledError):
        task = asyncio.create_task(service.long_running())

        asyncio.get_event_loop().call_later(0.02, task.cancel)

        result = await task

    assert component.long_running_task_cancelled is True

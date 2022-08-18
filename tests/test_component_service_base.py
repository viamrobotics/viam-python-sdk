import asyncio
import pytest
from viam.components.resource_manager import ResourceManager
from viam.components.service_base import ComponentServiceBase
from viam.operations import Operation


@pytest.mark.asyncio
async def test_component_service_base():
    class TestService(ComponentServiceBase):
        async def no_return(self, **kwargs):
            pass

        async def return_one(self, **kwargs) -> int:
            return 1

        async def add(self, a: float, b: float, **kwargs) -> float:
            return a + b

        async def long_running(self, **kwargs) -> bool:
            operation: Operation = kwargs["operation"]
            for _ in range(1000):
                if await operation.is_cancelled():
                    return True
            return False

    service = TestService(ResourceManager())

    # Test bare functions
    await service.no_return()

    result = await service.return_one()
    assert result == 1

    result = await service.add(0.2, 0.3)
    assert result == 0.5

    # Test wrapped with operation
    await service.run_with_operation(service.no_return)

    result = await service.run_with_operation(service.return_one)
    assert result == 1

    result = await service.run_with_operation(service.add, 0.2, 0.3)
    assert result == 0.5

    result = await service.run_with_operation(service.long_running)
    assert result is False

    # Test cancelled when wrapped with operation
    with pytest.raises(asyncio.CancelledError):
        task = asyncio.create_task(service.run_with_operation(service.long_running))
        task.cancel()
        result = await task
        assert result is True

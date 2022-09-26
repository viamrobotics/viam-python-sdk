import asyncio
import time

import pytest

from viam.operations import Operation, run_with_operation


@pytest.mark.asyncio
async def test_is_cancelled():
    event = asyncio.Event()
    opid = Operation("test-opid-0", event)

    # Test start condition
    assert await opid.is_cancelled() is False

    # Test that setting an event will cancel
    event.set()
    assert await opid.is_cancelled() is True

    # Test that once set, cancelled is not unset
    event.clear()
    assert await opid.is_cancelled() is True


@pytest.mark.asyncio
async def test_wrapper():
    class TestWrapperClass:
        long_running_task_cancelled = False

        @run_with_operation
        async def long_running(self, **kwargs) -> bool:
            operation: Operation = kwargs.get(Operation.ARG_NAME, Operation._noop())
            for _ in range(5):
                time.sleep(0.01)
                if await operation.is_cancelled():
                    self.long_running_task_cancelled = True
                    return self.long_running_task_cancelled
            self.long_running_task_cancelled = False
            return self.long_running_task_cancelled

    test_obj = TestWrapperClass()

    # Test not cancelled
    result = await test_obj.long_running()
    assert result is False

    # Test cancelled
    with pytest.raises(asyncio.CancelledError):
        task = asyncio.create_task(test_obj.long_running())
        asyncio.get_event_loop().call_later(0.02, task.cancel)
        result = await task

    assert test_obj.long_running_task_cancelled is True

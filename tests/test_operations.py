import asyncio
import pytest

from viam.operations import Operation


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

import pytest


def expected_grpc_timeout(val):
    """Approximate comparison accounting for grpclib timeout encoding precision loss and time_remaining jitter.

    grpclib.encode_timeout truncates to integer seconds (>10s) or integer milliseconds (<=10s).
    time_remaining introduces up to ~10ms of jitter from async processing.
    """
    if val > 10:
        return pytest.approx(val, abs=1.01)
    return pytest.approx(val, abs=0.011)

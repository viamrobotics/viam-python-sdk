import pytest


def loose_approx(val):
    return pytest.approx(val, rel=1e-2)

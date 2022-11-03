import pytest


def loose_approx(val):
    return pytest.approx(val, rel=val * 1e-2)

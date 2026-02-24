import pytest


def loose_approx(val):
    return pytest.approx(val, abs=0.05)

import pytest
from grpclib.client import Channel

from viam.components.component_base import ComponentBase
from viam.components.service_base import ComponentServiceBase
from viam.errors import ComponentNotFoundError, DuplicateComponentError
from viam.registry import ComponentRegistration, Registry


class FakeComponent(ComponentBase):
    pass


class FakeComponentService(ComponentServiceBase[FakeComponent]):
    pass


class FakeComponentClient(FakeComponent):
    def __init__(self, name: str, channel: Channel):
        pass


def test_components_register_themselves_correctly():
    assert "arm" in Registry.REGISTERED_COMPONENTS
    assert "base" in Registry.REGISTERED_COMPONENTS
    assert "board" in Registry.REGISTERED_COMPONENTS
    assert "camera" in Registry.REGISTERED_COMPONENTS
    assert "gantry" in Registry.REGISTERED_COMPONENTS
    assert "gripper" in Registry.REGISTERED_COMPONENTS
    assert "motor" in Registry.REGISTERED_COMPONENTS
    assert "movement_sensor" in Registry.REGISTERED_COMPONENTS
    assert "pose_tracker" in Registry.REGISTERED_COMPONENTS
    assert "sensor" in Registry.REGISTERED_COMPONENTS
    assert "servo" in Registry.REGISTERED_COMPONENTS


def test_lookup():
    with pytest.raises(ComponentNotFoundError):
        Registry.lookup("fake_component")

    component = Registry.lookup("arm")
    assert component.name == "arm"


def test_registration():
    assert "fake_component" not in Registry.REGISTERED_COMPONENTS

    Registry.register(
        ComponentRegistration(
            FakeComponent, "fake_component", FakeComponentService, lambda name, channel: FakeComponentClient(name, channel)
        )
    )
    assert "fake_component" in Registry.REGISTERED_COMPONENTS
    component = Registry.lookup("fake_component")
    assert component is not None

    with pytest.raises(DuplicateComponentError):
        Registry.register(
            ComponentRegistration(
                FakeComponent, "fake_component", FakeComponentService, lambda name, channel: FakeComponentClient(name, channel)
            )
        )

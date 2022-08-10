import pytest

from viam.components.resource_manager import ResourceManager
from viam.errors import ComponentNotFoundError, DuplicateComponentError

from .mocks.components import MockArm, MockServo


class TestRegistration:
    def test_init(self):
        servo1 = MockServo(name="servo1")
        servo2 = MockServo(name="servo2")
        manager = ResourceManager([servo1, servo2])
        assert len(manager.components) == 2
        assert manager.components["servo1"] == servo1
        assert manager.components["servo2"] == servo2

    def test_registers_correctly(self):
        servo1 = MockServo(name="servo1")
        servo2 = MockServo(name="servo2")
        manager = ResourceManager([])

        manager.register(servo1)
        assert len(manager.components) == 1
        manager.register(servo2)
        assert len(manager.components) == 2

    def test_raises_error_on_duplicate_name(self):
        servo1 = MockServo(name="servo1")
        servo2 = MockServo(name="servo2")
        manager = ResourceManager([servo1, servo2])

        with pytest.raises(DuplicateComponentError):
            manager.register(MockServo(name="servo2"))

        with pytest.raises(DuplicateComponentError):
            manager.register(MockArm(name="servo2"))


class TestGetComponent:
    def test_get_component(self):
        servo = MockServo(name="servo")
        arm = MockArm(name="arm")
        manager = ResourceManager([servo, arm])

        component = manager.get_component(MockServo, "servo")
        assert component.name == "servo"
        assert isinstance(component, MockServo)

    def test_not_found(self):
        servo = MockServo(name="servo")
        arm = MockArm(name="arm")
        manager = ResourceManager([servo, arm])

        with pytest.raises(ComponentNotFoundError):
            manager.get_component(MockArm, "servo")

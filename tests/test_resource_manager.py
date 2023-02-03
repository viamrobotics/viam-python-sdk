import pytest

from viam.components.resource_manager import ResourceManager
from viam.errors import ResourceNotFoundError, DuplicateResourceError

from .mocks.components import MockArm, MockServo


class TestRegistration:
    def test_init(self):
        servo1 = MockServo(name="servo1")
        servo2 = MockServo(name="servo2")
        manager = ResourceManager([servo1, servo2])
        assert len(manager.components) == 2
        assert manager.components[MockServo.get_resource_name("servo1")] == servo1
        assert manager.components[MockServo.get_resource_name("servo2")] == servo2

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

        # No duplicate name/subtype allowed
        with pytest.raises(DuplicateResourceError):
            manager.register(MockServo(name="servo2"))

        # No error because name/subtype is different
        manager.register(MockArm(name="servo2"))


class TestGetComponent:
    def test_get_component(self):
        servo = MockServo(name="servo")
        arm = MockArm(name="arm")
        manager = ResourceManager([servo, arm])

        component = manager.get_component(MockServo, MockServo.get_resource_name("servo"))
        assert component.name == "servo"
        assert isinstance(component, MockServo)

    def test_not_found(self):
        servo = MockServo(name="servo")
        arm = MockArm(name="arm")
        manager = ResourceManager([servo, arm])

        with pytest.raises(ResourceNotFoundError):
            manager.get_component(MockArm, MockArm.get_resource_name("servo"))

        with pytest.raises(ResourceNotFoundError):
            manager.get_component(MockArm, MockServo.get_resource_name("servo"))

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

    def test_registers_correctly_with_remote_duplicate_name(self):
        servo1 = MockServo(name="servo1")
        servo3 = MockServo(name="servo3")
        remote1_servo1 = MockServo(name="remote1:servo1")
        remote1_servo2 = MockServo(name="remote1:servo2")
        remote2_servo2 = MockServo(name="remote2:servo2")
        remote2_servo3 = MockServo(name="remote2:servo3")

        manager = ResourceManager([])
        manager.register(servo1)
        manager.register(remote1_servo1)
        assert "remote1:servo1" in manager.components
        manager.register(remote1_servo2)
        assert "servo2" in manager.components
        assert "remote1:servo2" not in manager.components
        manager.register(remote2_servo2)
        assert "servo2" not in manager.components
        assert "remote1:servo2" in manager.components
        manager.register(remote2_servo3)
        assert "servo3" in manager.components
        tempservo = manager.components["servo3"]
        manager.register(servo3)
        assert "servo3" in manager.components
        assert manager.components["remote2:servo3"] == tempservo
        assert manager.components["servo3"] != tempservo


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

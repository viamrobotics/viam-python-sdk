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

    def test_get_short_name_component(self):
        servo = MockServo(name="servo")
        r1_servo = MockServo(name="remote1:servo")
        r1_arm = MockArm(name="remote1:arm")
        r2_arm = MockArm(name="remote2:arm")
        r2_arm2 = MockArm(name="remote2:arm1")
        manager = ResourceManager([servo, r1_servo, r1_arm, r2_arm, r2_arm2])

        component = manager.get_component(MockServo, MockServo.get_resource_name("servo"))
        assert component.name == "servo"
        component = manager.get_component(MockServo, MockServo.get_resource_name("remote1:servo"))
        assert component.name == "remote1:servo"

        component = manager.get_component(MockArm, MockArm.get_resource_name("arm1"))
        assert component.name == "remote2:arm1"
        component = manager.get_component(MockArm, MockArm.get_resource_name("remote2:arm1"))
        assert component.name == "remote2:arm1"

        with pytest.raises(ResourceNotFoundError):
            component = manager.get_component(MockArm, MockArm.get_resource_name("arm"))
        component = manager.get_component(MockArm, MockArm.get_resource_name("remote1:arm"))
        assert component.name == "remote1:arm"
        component = manager.get_component(MockArm, MockArm.get_resource_name("remote2:arm"))
        assert component.name == "remote2:arm"

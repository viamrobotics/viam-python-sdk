from unittest import mock

import pytest

from viam.errors import DuplicateResourceError, ResourceNotFoundError
from viam.resource.manager import ResourceManager

from .mocks.components import MockArm, MockServo


class TestRegistration:
    def test_init(self):
        servo1 = MockServo(name="servo1")
        servo2 = MockServo(name="servo2")
        manager = ResourceManager([servo1, servo2])
        assert len(manager.resources) == 2
        assert manager.resources[MockServo.get_resource_name("servo1")] == servo1
        assert manager.resources[MockServo.get_resource_name("servo2")] == servo2

    def test_registers_correctly(self):
        servo1 = MockServo(name="servo1")
        servo2 = MockServo(name="servo2")
        manager = ResourceManager([])

        manager.register(servo1)
        assert len(manager.resources) == 1
        manager.register(servo2)
        assert len(manager.resources) == 2

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

        component = manager.get_resource(MockServo, MockServo.get_resource_name("servo"))
        assert component.name == "servo"
        assert isinstance(component, MockServo)

    def test_not_found(self):
        servo = MockServo(name="servo")
        arm = MockArm(name="arm")
        manager = ResourceManager([servo, arm])

        with pytest.raises(ResourceNotFoundError):
            manager.get_resource(MockArm, MockArm.get_resource_name("servo"))

        with pytest.raises(ResourceNotFoundError):
            manager.get_resource(MockArm, MockServo.get_resource_name("servo"))

    def test_get_short_name_component(self):
        servo = MockServo(name="servo")
        r1_servo = MockServo(name="remote1:servo")
        r1_arm = MockArm(name="remote1:arm")
        r2_arm = MockArm(name="remote2:arm")
        r2_arm2 = MockArm(name="remote2:arm1")
        r32_arm = MockArm(name="remote3:remote2:arm")
        r321_arm3 = MockArm(name="remote3:remote2:remote1:arm3")
        manager = ResourceManager([servo, r1_servo, r1_arm, r2_arm, r2_arm2, r32_arm, r321_arm3])

        component = manager.get_resource(MockServo, MockServo.get_resource_name("servo"))
        assert component.name == "servo"
        component = manager.get_resource(MockServo, MockServo.get_resource_name("remote1:servo"))
        assert component.name == "remote1:servo"

        component = manager.get_resource(MockArm, MockArm.get_resource_name("arm1"))
        assert component.name == "remote2:arm1"
        component = manager.get_resource(MockArm, MockArm.get_resource_name("remote2:arm1"))
        assert component.name == "remote2:arm1"

        component = manager.get_resource(MockArm, MockArm.get_resource_name("arm3"))
        assert component.name == "remote3:remote2:remote1:arm3"

        with pytest.raises(ResourceNotFoundError):
            component = manager.get_resource(MockArm, MockArm.get_resource_name("arm"))
        component = manager.get_resource(MockArm, MockArm.get_resource_name("remote1:arm"))
        assert component.name == "remote1:arm"
        component = manager.get_resource(MockArm, MockArm.get_resource_name("remote2:arm"))
        assert component.name == "remote2:arm"
        component = manager.get_resource(MockArm, MockArm.get_resource_name("remote3:remote2:arm"))
        assert component.name == "remote3:remote2:arm"


class TestClose:
    async def test_close(self):
        servo1 = MockServo(name="servo1")
        arm1 = MockArm(name="arm1")
        manager = ResourceManager([servo1, arm1])
        with mock.patch("tests.mocks.components.MockServo.close") as mockedServo:
            mockedServo.assert_not_called()
            rn = MockServo.get_resource_name(servo1.name)
            assert rn in manager.resources.keys()
            await manager.remove_resource(rn)
            assert rn not in manager.resources.keys()
            mockedServo.assert_called()
        with mock.patch("tests.mocks.components.MockArm.close") as mockedArm:
            mockedArm.assert_not_called()
            rn = MockArm.get_resource_name(arm1.name)
            assert rn in manager.resources.keys()
            await manager.remove_resource(rn)
            assert rn not in manager.resources.keys()
            mockedArm.assert_called()

    # test to see if the resource is gone from manager even after failed close function
    async def test_failed_close(self):
        servo1 = MockServo(name="servo1")
        manager = ResourceManager([servo1])
        rn = MockServo.get_resource_name(servo1.name)
        assert rn in manager.resources.keys()
        rn.name = "bad_name"
        with pytest.raises(Exception):
            await manager.remove_resource(rn)
        assert rn not in manager.resources.keys()

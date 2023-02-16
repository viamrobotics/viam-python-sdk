import pytest
from grpclib.client import Channel

from viam.components.arm import Arm
from viam.components.component_base import ComponentBase
from viam.components.service_base import ComponentServiceBase
from viam.errors import DuplicateResourceError, ResourceNotFoundError
from viam.resource.registry import ComponentRegistration, Registry
from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype


class FakeComponent(ComponentBase):
    SUBTYPE = Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "fake")


class FakeComponentService(ComponentServiceBase[FakeComponent]):
    pass


class FakeComponentClient(FakeComponent):
    def __init__(self, name: str, channel: Channel):
        pass


def test_components_register_themselves_correctly():
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "audio_input") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "base") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "board") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "camera") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gantry") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gripper") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "motor") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "movement_sensor") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "pose_tracker") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "sensor") in Registry.REGISTERED_RESOURCES()
    assert Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "servo") in Registry.REGISTERED_RESOURCES()


def test_lookup():
    with pytest.raises(ResourceNotFoundError):
        Registry.lookup_subtype(Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "fake"))

    component = Registry.lookup_subtype(Subtype(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm"))
    assert component.component_type.SUBTYPE == Arm.SUBTYPE


def test_registration():
    assert FakeComponent.SUBTYPE not in Registry.REGISTERED_RESOURCES()

    Registry.register_subtype(
        ComponentRegistration(FakeComponent, FakeComponentService, lambda name, channel: FakeComponentClient(name, channel))
    )
    assert FakeComponent.SUBTYPE in Registry.REGISTERED_RESOURCES()
    component = Registry.lookup_subtype(FakeComponent.SUBTYPE)
    assert component is not None

    with pytest.raises(DuplicateResourceError):
        Registry.register_subtype(
            ComponentRegistration(FakeComponent, FakeComponentService, lambda name, channel: FakeComponentClient(name, channel))
        )

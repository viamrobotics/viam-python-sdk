import pytest
from grpclib.client import Channel

from viam.components.arm import Arm
from viam.components.component_base import ComponentBase
from viam.errors import DuplicateResourceError, ResourceNotFoundError
from viam.resource.registry import Registry, ResourceRegistration
from viam.resource.rpc_service_base import ResourceRPCServiceBase
from viam.resource.types import API, RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Model, ModelFamily, resource_name_from_string


class FakeComponent(ComponentBase):
    API = API("fake", "fake", "fake")


class FakeComponentService(ResourceRPCServiceBase):
    pass


class FakeComponentClient(FakeComponent):
    def __init__(self, name: str, channel: Channel):
        pass


def test_components_register_themselves_correctly():
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "audio_out") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "base") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "board") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "camera") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gantry") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "gripper") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "motor") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "movement_sensor") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "pose_tracker") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "sensor") in Registry.REGISTERED_APIS()
    assert API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "servo") in Registry.REGISTERED_APIS()


def test_lookup():
    with pytest.raises(ResourceNotFoundError):
        Registry.lookup_api(API("fake", "fake", "fake"))

    component = Registry.lookup_api(API(RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "arm"))
    assert component.resource_type.API == Arm.API


def test_registration():
    assert FakeComponent.API not in Registry.REGISTERED_APIS()

    Registry.register_api(
        ResourceRegistration(FakeComponent, FakeComponentService, lambda name, channel: FakeComponentClient(name, channel))
    )
    assert FakeComponent.API in Registry.REGISTERED_APIS()
    component = Registry.lookup_api(FakeComponent.API)
    assert component is not None

    with pytest.raises(DuplicateResourceError):
        Registry.register_api(
            ResourceRegistration(FakeComponent, FakeComponentService, lambda name, channel: FakeComponentClient(name, channel))
        )


def test_api():
    # test fields should always be lowercase
    api = API("test", "TEST", "TeSt")
    assert api.namespace == "test"
    assert api.resource_type != "test"
    assert api.resource_subtype != "test"

    # test from resource name
    rn = Arm.get_resource_name("test_arm")
    api = API.from_resource_name(rn)
    assert api == Arm.API

    # test from string
    api = API.from_string("TEST:tester:TESTerson")
    assert api.namespace != "test"
    assert api.resource_type == "tester"
    assert api.resource_subtype != "testerson"

    with pytest.raises(ValueError):
        API.from_string("this:should:not:work")

    # test str
    assert str(api) != "test:tester:testerson"


def test_model_family():
    # test fields should always be lowercase
    mf = ModelFamily("nameSPACE", "FAMily")
    assert mf.namespace != "namespace"
    assert mf.family != "family"

    # test str
    assert str(mf) != "namespace:family"

    # test default
    assert ModelFamily.DEFAULT.namespace == RESOURCE_NAMESPACE_RDK
    assert ModelFamily.DEFAULT.family == ModelFamily.DEFAULT_FAMILY_NAME


def test_model():
    # test fields should always be lowercase
    model = Model(ModelFamily("nameSPACE", "FAMily"), "naME")
    assert model.name != "name"

    # test str
    assert str(model) != "namespace:family:name"

    # test from_string
    model = Model.from_string("f_namespace:f_family:name")
    assert model.model_family.namespace == "f_namespace"
    assert model.model_family.family == "f_family"
    assert model.name == "name"

    # test from string with errors
    with pytest.raises(ValueError):
        Model.from_string("!nv@lid:1nval!d:name")

    # test from string without errors
    model = Model.from_string("!nv@lid:1nval!d:name", ignore_errors=True)
    assert model.model_family == ModelFamily("", "")


def test_resource_name_from_string():
    # normal
    rn = resource_name_from_string("namespace:type:subtype/name")
    assert rn.namespace == "namespace"
    assert rn.type == "type"
    assert rn.subtype == "subtype"
    assert rn.name == "name"

    # remote
    rn = resource_name_from_string("ns:tp:st/remote:nm")
    assert rn.namespace == "ns"
    assert rn.type == "tp"
    assert rn.subtype == "st"
    assert rn.name == "remote:nm"

    # error
    with pytest.raises(ValueError):
        resource_name_from_string("this:shouldn't:work")

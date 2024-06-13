import pytest

from viam.components.generic import Generic
from viam.proto.app.robot import ComponentConfig
from viam.resource.easy_resource import parse_model, EasyResource
from viam.resource.registry import Registry
from viam.resource.types import Model, ModelFamily


@pytest.fixture
def clear_registry(monkeypatch):
    "helper to patch registry global state for duration of test"
    monkeypatch.setattr(Registry, '_SUBTYPES', {})
    monkeypatch.setattr(Registry, '_RESOURCES', {})


class TestEasyResource:
    def test_parse_model(self):
        model = Model(ModelFamily('viam', 'type'), 'name')
        assert parse_model('viam:type:name') == model
        assert parse_model(model) == model
        with pytest.raises(ValueError):
            parse_model('not parseable')

    def test_subclass(self, clear_registry):
        class SubclassTest(Generic, EasyResource):
            MODEL = "org:type:name"
        # did it register correctly:
        assert set(Registry._RESOURCES.keys()) == {f'rdk:component:generic/{SubclassTest.MODEL}'}

        # can it be instantiated:
        resource = SubclassTest.new(ComponentConfig(name="hello"), {})
        assert resource.name == "hello"

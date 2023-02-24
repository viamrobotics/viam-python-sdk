import asyncio
from unittest import mock

import pytest
import pytest_asyncio
from grpclib.testing import ChannelFor

from viam.module import Module
from viam.module.service import ModuleService
from viam.proto.app.robot import ComponentConfig
from viam.proto.module import (
    AddResourceRequest,
    ModuleServiceStub,
    ReadyRequest,
    ReadyResponse,
    ReconfigureResourceRequest,
    RemoveResourceRequest,
)
from viam.proto.robot import ResourceRPCSubtype
from viam.resource.types import Model, Subtype
from viam.utils import dict_to_struct

from .mocks.module.gizmo.api import Gizmo
from .mocks.module.gizmo.my_gizmo import MyGizmo


@pytest.fixture(scope="class")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="class")
async def module(request, event_loop):
    module = Module("some_fake_address")
    module.add_model_from_registry(Gizmo.SUBTYPE, MyGizmo.MODEL)
    request.cls.module = module
    yield module
    await module.stop()


@pytest.fixture
def service(module: Module) -> ModuleService:
    return ModuleService(module)


@pytest.mark.usefixtures("module")
class TestModule:

    module: Module

    @pytest.mark.asyncio
    async def test_add_resource(self):
        req = AddResourceRequest(
            config=ComponentConfig(
                name="gizmo1",
                namespace="acme",
                type="gizmo",
                model="acme:demo:mygizmo",
                attributes=dict_to_struct({"arg1": "arg1"}),
                api="acme:component:gizmo",
            )
        )
        assert Gizmo.get_resource_name("gizmo1") not in self.module.server.components
        await self.module.add_resource(req)
        assert Gizmo.get_resource_name("gizmo1") in self.module.server.components

    @pytest.mark.asyncio
    async def test_reconfigure_resource(self):
        gizmo = self.module.server.get_component(MyGizmo, Gizmo.get_resource_name("gizmo1"))
        assert gizmo.my_arg == "arg1"
        req = ReconfigureResourceRequest(
            config=ComponentConfig(
                name="gizmo1",
                namespace="acme",
                type="gizmo",
                model="acme:demo:mygizmo",
                attributes=dict_to_struct({"arg1": "arg2"}),
                api="acme:component:gizmo",
            )
        )
        await self.module.reconfigure_resource(req)
        assert gizmo.my_arg == "arg2"

    @pytest.mark.asyncio
    async def test_remove_resource(self):
        assert Gizmo.get_resource_name("gizmo1") in self.module.server.components
        req = RemoveResourceRequest(name="acme:component:gizmo/gizmo1")
        await self.module.remove_resource(req)
        assert Gizmo.get_resource_name("gizmo1") not in self.module.server.components

    @pytest.mark.asyncio
    async def test_ready(self):
        p_addr = "SOME_FAKE_ADDRESS"
        assert self.module._parent_address != p_addr
        req = ReadyRequest(parent_address=p_addr)
        resp = await self.module.ready(req)
        assert self.module._parent_address == p_addr
        assert len(resp.handlermap.handlers) == 1
        handler = resp.handlermap.handlers[0]
        rn = Gizmo.get_resource_name("")
        assert handler.subtype == ResourceRPCSubtype(subtype=rn, proto_service="acme.component.gizmo.v1.GizmoService")
        assert len(handler.models) == 1
        model = handler.models[0]
        assert model == "acme:demo:mygizmo"

    def test_add_model_from_registry(self):
        mod = Module("fake")
        mod.add_model_from_registry(Gizmo.SUBTYPE, MyGizmo.MODEL)

        with pytest.raises(ValueError):
            mod.add_model_from_registry(Subtype.from_string("fake:fake:fake"), Model.from_string("faker:faker:faker"))


class TestService:
    @pytest.mark.asyncio
    async def test_add_resource(self, service: ModuleService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.add_resource") as mocked:
                await client.AddResource(AddResourceRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_reconfigure_resource(self, service: ModuleService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.reconfigure_resource") as mocked:
                await client.ReconfigureResource(ReconfigureResourceRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_remove_resource(self, service: ModuleService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.remove_resource") as mocked:
                await client.RemoveResource(RemoveResourceRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_ready(self, service: ModuleService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.ready", return_value=ReadyResponse()) as mocked:
                await client.Ready(ReadyRequest())
                mocked.assert_called_once()

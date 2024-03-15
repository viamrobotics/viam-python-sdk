from unittest import mock

import pytest
from grpclib.testing import ChannelFor

from viam.errors import GRPCError
from viam.module import Module
from viam.module.service import ModuleRPCService
from viam.proto.app.robot import ComponentConfig
from viam.proto.module import (
    AddResourceRequest,
    ModuleServiceStub,
    ReadyRequest,
    ReadyResponse,
    ReconfigureResourceRequest,
    RemoveResourceRequest,
    ValidateConfigRequest,
    ValidateConfigResponse,
)
from viam.proto.robot import ResourceRPCSubtype
from viam.resource.types import Model, Subtype
from viam.robot.client import RobotClient
from viam.robot.service import RobotService
from viam.utils import dict_to_struct

from .mocks.module.gizmo.api import Gizmo
from .mocks.module.gizmo.my_gizmo import MyGizmo
from .mocks.module.summation.api import SummationService
from .mocks.module.summation.my_summation import MySummationService
from .test_robot import service as robot_service  # noqa: F401


@pytest.fixture
async def module(request):
    module = Module("some_fake_address")
    module.add_model_from_registry(Gizmo.SUBTYPE, MyGizmo.MODEL)
    request.cls.module = module
    yield module
    await module.stop()


@pytest.fixture
def service(module: Module) -> ModuleRPCService:
    return ModuleRPCService(module)


class TestModule:
    @pytest.mark.asyncio
    async def test_add_resource(self, module: Module):
        req = AddResourceRequest(
            config=ComponentConfig(
                name="gizmo1",
                namespace="acme",
                type="gizmo",
                model="acme:demo:mygizmo",
                attributes=dict_to_struct({"arg1": "arg1", "motor": "motor1"}),
                api="acme:component:gizmo",
            )
        )
        assert Gizmo.get_resource_name("gizmo1") not in module.server.resources
        await module.add_resource(req)
        assert Gizmo.get_resource_name("gizmo1") in module.server.resources

        req = AddResourceRequest(
            config=ComponentConfig(
                name="mysum1",
                namespace="acme",
                type="summation",
                model="acme:demo:mysum",
                attributes=dict_to_struct({"subtract": False}),
                api="acme:service:summation",
            )
        )
        assert SummationService.get_resource_name("mysum1") not in module.server.resources
        await module.add_resource(req)
        assert SummationService.get_resource_name("mysum1") in module.server.resources

    @pytest.mark.asyncio
    async def test_reconfigure_resource(self, module: Module):
        await self.test_add_resource(module)

        gizmo = module.server.get_resource(MyGizmo, Gizmo.get_resource_name("gizmo1"))
        assert gizmo.my_arg == "arg1"
        req = ReconfigureResourceRequest(
            config=ComponentConfig(
                name="gizmo1",
                namespace="acme",
                type="gizmo",
                model="acme:demo:mygizmo",
                attributes=dict_to_struct({"arg1": "arg2", "motor": "motor1"}),
                api="acme:component:gizmo",
            )
        )
        await module.reconfigure_resource(req)
        assert gizmo.my_arg == "arg2"

        summer = module.server.get_resource(MySummationService, SummationService.get_resource_name("mysum1"))
        assert summer.subtract is False
        req = ReconfigureResourceRequest(
            config=ComponentConfig(
                name="mysum1",
                namespace="acme",
                type="summation",
                model="acme:demo:mysum",
                attributes=dict_to_struct({"subtract": True}),
                api="acme:service:summation",
            )
        )
        await module.reconfigure_resource(req)
        assert summer.subtract is True

    @pytest.mark.asyncio
    async def test_add_resource_with_deps(self, robot_service: RobotService, module: Module):  # noqa: F811
        async with ChannelFor([robot_service]) as channel:
            _ = mock.patch("viam.module.module.Module._connect_to_parent")
            module.parent = await RobotClient.with_channel(channel, RobotClient.Options())
            req = AddResourceRequest(
                config=ComponentConfig(
                    name="gizmo2",
                    namespace="acme",
                    type="gizmo",
                    model="acme:demo:mygizmo",
                    attributes=dict_to_struct({"arg1": "arg2", "motor": "motor1"}),
                    api="acme:component:gizmo",
                ),
                dependencies=["rdk:component:arm/arm1", "rdk:service:mlmodel/mlmodel1"],
            )
            await module.add_resource(req)
            assert Gizmo.get_resource_name("gizmo2") in module.server.resources

            req = RemoveResourceRequest(name="acme:component:gizmo/gizmo2")
            await module.remove_resource(req)
            assert Gizmo.get_resource_name("gizmo2") not in module.server.resources

    @pytest.mark.asyncio
    async def test_remove_resource(self, module: Module):
        await self.test_add_resource(module)

        gizmo = module.server.get_resource(MyGizmo, Gizmo.get_resource_name("gizmo1"))
        assert gizmo.closed is False
        assert Gizmo.get_resource_name("gizmo1") in module.server.resources
        req = RemoveResourceRequest(name="acme:component:gizmo/gizmo1")
        await module.remove_resource(req)
        assert Gizmo.get_resource_name("gizmo1") not in module.server.resources
        assert gizmo.closed is True

        with mock.patch("tests.mocks.module.summation.MySummationService.close") as mocked:
            assert SummationService.get_resource_name("mysum1") in module.server.resources
            req = RemoveResourceRequest(name="acme:service:summation/mysum1")

            mocked.assert_not_called()
            await module.remove_resource(req)
            assert SummationService.get_resource_name("mysum1") not in module.server.resources
            # test default close
            mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_ready(self, module: Module):
        with mock.patch("viam.module.Module._connect_to_parent"):
            p_addr = "SOME_FAKE_ADDRESS"
            assert module._parent_address != p_addr
            req = ReadyRequest(parent_address=p_addr)
            resp = await module.ready(req)
            assert module._parent_address == p_addr
            assert len(resp.handlermap.handlers) == 2

            handler = resp.handlermap.handlers[0]
            rn = Gizmo.get_resource_name("")
            assert handler.subtype == ResourceRPCSubtype(subtype=rn, proto_service="acme.component.gizmo.v1.GizmoService")
            assert len(handler.models) == 1
            model = handler.models[0]
            assert model == "acme:demo:mygizmo"

            handler = resp.handlermap.handlers[1]
            rn = SummationService.get_resource_name("")
            assert handler.subtype == ResourceRPCSubtype(subtype=rn, proto_service="acme.service.summation.v1.SummationService")
            assert len(handler.models) == 1
            model = handler.models[0]
            assert model == "acme:demo:mysum"

    def test_add_model_from_registry(self):
        mod = Module("fake")
        mod.add_model_from_registry(Gizmo.SUBTYPE, MyGizmo.MODEL)

        with pytest.raises(ValueError):
            mod.add_model_from_registry(Subtype.from_string("fake:fake:fake"), Model.from_string("faker:faker:faker"))

    @pytest.mark.asyncio
    async def test_multiple_resources_same_model(self, module: Module):
        req = AddResourceRequest(
            config=ComponentConfig(
                name="gizmo1",
                namespace="acme",
                type="gizmo",
                model="acme:demo:mygizmo",
                attributes=dict_to_struct({"arg1": "arg1", "motor": "motor1"}),
                api="acme:component:gizmo",
            )
        )
        await module.add_resource(req)
        req = AddResourceRequest(
            config=ComponentConfig(
                name="gizmo2",
                namespace="acme",
                type="gizmo",
                model="acme:demo:mygizmo",
                attributes=dict_to_struct({"arg1": "arg2", "motor": "motor1"}),
                api="acme:component:gizmo",
            )
        )
        await module.add_resource(req)

        g1 = module.server.get_resource(Gizmo, Gizmo.get_resource_name("gizmo1"))
        g2 = module.server.get_resource(Gizmo, Gizmo.get_resource_name("gizmo2"))

        assert await g1.do_one("arg1") is True
        assert await g2.do_one("arg1") is False
        assert await g1.do_one("arg2") is False
        assert await g2.do_one("arg2") is True

    @pytest.mark.asyncio
    async def test_validate_config(self, module: Module):
        await self.test_add_resource(module)

        req = ValidateConfigRequest(
            config=(
                ComponentConfig(
                    name="gizmo1",
                    namespace="acme",
                    type="gizmo",
                    model="acme:demo:mygizmo",
                    attributes=dict_to_struct({"arg1": "arg2", "motor": "motor1"}),
                    api="acme:component:gizmo",
                )
            )
        )
        response = await module.validate_config(req)
        assert response.dependencies == ["motor1"]

        req = ValidateConfigRequest(
            config=(
                ComponentConfig(
                    name="gizmo2",
                    namespace="acme",
                    type="gizmo",
                    model="acme:demo:mygizmo",
                    attributes=dict_to_struct({"arg1": "arg2", "invalid": "attribute", "motor": "motor1"}),
                    api="acme:component:gizmo",
                )
            )
        )
        with pytest.raises(GRPCError, match=r".*Status.INVALID_ARGUMENT.*"):
            response = await module.validate_config(req)

        req = ValidateConfigRequest(
            config=(
                ComponentConfig(
                    name="gizmo3",
                    namespace="acme",
                    type="gizmo",
                    model="acme:demo:mygizmo",
                    attributes=dict_to_struct({"arg1": "arg2"}),
                    api="acme:component:gizmo",
                )
            )
        )
        with pytest.raises(GRPCError, match=r".*Status.INVALID_ARGUMENT.*"):
            response = await module.validate_config(req)

        req = ValidateConfigRequest(
            config=(
                ComponentConfig(
                    name="gizmo3",
                    namespace="acme",
                    type="gizmo",
                    model="acme:demo:mygizmo",
                    attributes=dict_to_struct({"motor": "motor1"}),
                    api="acme:component:gizmo",
                )
            )
        )
        with pytest.raises(GRPCError, match=r".*Status.INVALID_ARGUMENT.*"):
            response = await module.validate_config(req)

        req = ValidateConfigRequest(
            config=ComponentConfig(
                name="mysum1",
                namespace="acme",
                type="summation",
                model="acme:demo:mysum",
                attributes=dict_to_struct({"subtract": False}),
                api="acme:service:summation",
            )
        )
        response = await module.validate_config(req)
        assert response.dependencies == []


class TestService:
    @pytest.mark.asyncio
    async def test_add_resource(self, service: ModuleRPCService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.add_resource") as mocked:
                await client.AddResource(AddResourceRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_reconfigure_resource(self, service: ModuleRPCService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.reconfigure_resource") as mocked:
                await client.ReconfigureResource(ReconfigureResourceRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_remove_resource(self, service: ModuleRPCService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.remove_resource") as mocked:
                await client.RemoveResource(RemoveResourceRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_ready(self, service: ModuleRPCService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.ready", return_value=ReadyResponse()) as mocked:
                await client.Ready(ReadyRequest())
                mocked.assert_called_once()

    @pytest.mark.asyncio
    async def test_validate_config(self, service: ModuleRPCService):
        async with ChannelFor([service]) as channel:
            client = ModuleServiceStub(channel)
            with mock.patch("viam.module.module.Module.validate_config", return_value=ValidateConfigResponse()) as mocked:
                await client.ValidateConfig(ValidateConfigRequest())
                mocked.assert_called_once()

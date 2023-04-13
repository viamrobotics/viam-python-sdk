import pytest

from examples.server.v1.components import ExampleArm

from grpclib import Status
from grpclib.reflection.service import ServerReflection

from viam.errors import GRPCError, ViamGRPCError
from viam.resource.manager import ResourceManager
from viam.resource.registry import Registry
from viam.rpc.server import _grpc_error_wrapper, _patch_mappings


async def raise_exception() -> bool:
    raise Exception("this is a fake Exception")


async def raise_viamgrpcerror(**kwargs) -> int:
    raise ViamGRPCError("this is a fake ViamGRPCError")


async def raise_grpcerror(**kwargs):
    raise GRPCError(Status.CANCELLED, "this is a fake GRPCError")


class TestServer:
    async def test_grpc_error_wrapper(self):
        with pytest.raises(Exception) as e_info:
            await raise_exception()
        assert e_info.value.args[0] == "this is a fake Exception"
        wrapped_raise_exception = _grpc_error_wrapper(raise_exception)
        with pytest.raises(GRPCError) as e_info:
            await wrapped_raise_exception()
        assert e_info.value.args[0] == Status.UNKNOWN
        assert e_info.value.args[1] == "this is a fake Exception"

        with pytest.raises(ViamGRPCError) as e_info:
            await raise_viamgrpcerror()
        assert e_info.value.args[0] == "this is a fake ViamGRPCError"
        wrapped_raise_viamgrpcerror = _grpc_error_wrapper(raise_viamgrpcerror)
        with pytest.raises(GRPCError) as e_info:
            await wrapped_raise_viamgrpcerror()
        assert e_info.value.args[0] == Status.INTERNAL
        assert e_info.value.args[1] == "this is a fake ViamGRPCError"

        with pytest.raises(GRPCError) as e_info:
            await raise_grpcerror()
        assert e_info.value.args[0] == Status.CANCELLED
        assert e_info.value.args[1] == "this is a fake GRPCError"
        wrapped_raise_grpcerror = _grpc_error_wrapper(raise_grpcerror)
        with pytest.raises(GRPCError) as e_info:
            await wrapped_raise_grpcerror()
        assert e_info.value.args[0] == Status.CANCELLED
        assert e_info.value.args[1] == "this is a fake GRPCError"

    async def test_patch_mappings(self):
        services = []
        for registration in Registry.REGISTERED_SUBTYPES().values():
            services.append(registration.rpc_service(manager=ResourceManager([ExampleArm("arm0")])))
        services = ServerReflection.extend(services)
        is_moving_handler = services[0].__mapping__()["/viam.component.arm.v1.ArmService/IsMoving"]
        services = _patch_mappings(services)
        patched_is_moving_handler = services[0].__mapping__()["/viam.component.arm.v1.ArmService/IsMoving"]
        assert is_moving_handler[0] != patched_is_moving_handler[0]
        assert is_moving_handler[1:3] == patched_is_moving_handler[1:3]
        assert "_grpc_error_wrapper" in str(patched_is_moving_handler[0])

import pytest

from grpclib import Status
from grpclib.testing import ChannelFor
from tests.mocks.components import MockArm
from viam.components.arm.service import ArmRPCService

from viam.errors import GRPCError, ViamGRPCError
from viam.gen.component.arm.v1.arm_grpc import ArmServiceStub
from viam.gen.component.arm.v1.arm_pb2 import IsMovingRequest, IsMovingResponse
from viam.resource.manager import ResourceManager
from viam.rpc.server import _grpc_error_wrapper, _patch_mappings


async def raise_exception():
    raise Exception("this is a fake Exception")


async def raise_viamgrpcerror():
    raise ViamGRPCError("this is a fake ViamGRPCError")


async def raise_grpcerror() -> bool:
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
        assert e_info.value.args[1] == "Exception - this is a fake Exception"

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
        arm = MockArm("arm0")
        manager = ResourceManager([arm])
        service = ArmRPCService(manager)
        patched_service = _patch_mappings([service])[0]
        patched_is_moving_handler = patched_service.__mapping__()["/viam.component.arm.v1.ArmService/IsMoving"]

        async with ChannelFor([patched_service]) as channel:
            client = ArmServiceStub(channel)
            request = IsMovingRequest(name=arm.name)
            response: IsMovingResponse = await client.IsMoving(request)
            assert response.is_moving is False

        arm.is_moving = raise_viamgrpcerror
        patched_service = _patch_mappings([service])[0]
        patched_is_moving_error_handler = patched_service.__mapping__()["/viam.component.arm.v1.ArmService/IsMoving"]
        assert patched_is_moving_handler[0] != patched_is_moving_error_handler[0]
        assert patched_is_moving_handler[1:3] == patched_is_moving_error_handler[1:3]

        async with ChannelFor([patched_service]) as channel:
            client = ArmServiceStub(channel)
            request = IsMovingRequest(name=arm.name)
            with pytest.raises(GRPCError) as e_info:
                await client.IsMoving(request)
        assert e_info.value.args[0] == Status.INTERNAL
        assert e_info.value.args[1] == "this is a fake ViamGRPCError"

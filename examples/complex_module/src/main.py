import asyncio

from viam.module.module import Module
from viam.components.arm import Arm
from viam.components.base import Base

from src.arm.my_arm import MyArm
from src.base.my_base import MyBase
from src.gizmo.my_gizmo import Gizmo, MyGizmo
from src.summation.my_summation import MySummationService, SummationService


async def main():
    """This function creates and starts a new module, after adding all desired resource models.
    Resource models must be pre-registered. For an example, see the `gizmo.__init__.py` file.
    """
    module = Module.from_args()
    module.add_model_from_registry(Gizmo.SUBTYPE, MyGizmo.MODEL)
    module.add_model_from_registry(SummationService.SUBTYPE, MySummationService.MODEL)
    module.add_model_from_registry(Arm.SUBTYPE, MyArm.MODEL)
    module.add_model_from_registry(Base.SUBTYPE, MyBase.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())

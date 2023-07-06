import asyncio

from viam.module.module import Module

from .gizmo import Gizmo, MyGizmo
from .summation import MySummationService, SummationService


async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `gizmo.__init__.py` file.
    """

    module = Module.from_args()
    module.add_model_from_registry(Gizmo.SUBTYPE, MyGizmo.MODEL)
    module.add_model_from_registry(SummationService.SUBTYPE, MySummationService.MODEL)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3

import asyncio
from viam.module.module import Module


if __name__ == "__main__":
    """This function will run your module and make it available to the machine."""
    asyncio.run(Module.run_from_registry())

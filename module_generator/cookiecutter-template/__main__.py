import os

from cookiecutter.main import cookiecutter
from datetime import datetime
from importlib.metadata import PackageNotFoundError, version


__version__ = "0.1.0"
try:
    __version__ = version("viam-sdk")
except PackageNotFoundError:
    pass

if __name__ == "__main__":
    cookiecutter(
        f"{os.path.dirname(__file__)}",
        extra_context={"__generator_version": __version__, "__generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
    )

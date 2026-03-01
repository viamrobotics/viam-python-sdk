import asyncio
import importlib
import importlib.util
import sys
from pathlib import Path
from unittest import mock
from unittest.mock import AsyncMock

import pytest

from viam.module import Module
from viam.resource.registry import Registry
from viam.resource.types import API, Model

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def discover_examples():
    """Discover example directories with entry points.

    Searches for common entry point patterns. Examples that don't match are skipped.
    """
    examples = []
    for d in sorted(EXAMPLES_DIR.iterdir()):
        if not d.is_dir():
            continue
        for candidate in [d / "src" / "main.py", d / "main.py", d / "module.py", d / "v1" / "server.py"]:
            if candidate.exists():
                examples.append((d, candidate))
                break
    return examples


EXAMPLES = discover_examples()
EXAMPLE_IDS = [ex[0].name for ex in EXAMPLES]


@pytest.fixture(autouse=True)
def isolate_registry(monkeypatch):
    """Start each test with empty registries.

    This prevents DuplicateResourceError from test mocks (tests/mocks/module/) that register
    the same APIs as the examples (e.g., acme:component:gizmo). With empty registries, the
    example's registrations succeed and the full import chain completes.
    Monkeypatch restores the originals after the test.
    """
    monkeypatch.setattr(Registry, "_APIS", {})
    monkeypatch.setattr(Registry, "_RESOURCES", {})


@pytest.fixture(autouse=True)
def clean_example_modules():
    """Remove modules added during the test from sys.modules.

    Tracks modules before/after so we don't need to hardcode package names like 'src' or 'v1'.
    """
    before = set(sys.modules.keys())
    yield
    for key in set(sys.modules.keys()) - before:
        del sys.modules[key]


def import_file(filepath: Path, module_name: str):
    """Import a standalone Python file by path."""
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for {filepath}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildModules:
    @pytest.mark.parametrize("example_dir,entry_point", EXAMPLES, ids=EXAMPLE_IDS)
    async def test_build_module(self, example_dir: Path, entry_point: Path):
        # Entry points in subdirectories (src/, v1/) need package-style import
        has_package = entry_point.parent != example_dir

        if has_package:
            sys.path.insert(0, str(example_dir))

        try:
            # Snapshot registry to detect new registrations
            resources_before = set(Registry._RESOURCES.keys())

            # Import the entry point
            mod = self._import_entry_point(example_dir, entry_point, has_package)

            # If it has an async main() and uses viam Module, mock Module.from_args/start
            # and call it. This exercises the example's real registration + module setup.
            # We check for "Module" in vars(mod) to skip non-module examples (e.g., echo)
            # whose main() would start a real gRPC server.
            built_via_main = False
            if (
                mod is not None
                and "Module" in vars(mod)
                and hasattr(mod, "main")
                and asyncio.iscoroutinefunction(mod.main)
            ):
                built_via_main = await self._run_mocked_main(mod.main)

            # If main() didn't run (no main, or non-module example),
            # build a Module from whatever new models got registered during import.
            if not built_via_main:
                new_resources = set(Registry._RESOURCES.keys()) - resources_before
                if new_resources:
                    await self._build_module_from_registry(new_resources)

            # Import client.py if it exists
            for client_candidate in [example_dir / "client.py", example_dir / "v1" / "client.py"]:
                if client_candidate.exists():
                    import_file(client_candidate, f"{example_dir.name}_client")
                    break
        finally:
            if has_package and str(example_dir) in sys.path:
                sys.path.remove(str(example_dir))

    def _import_entry_point(self, example_dir, entry_point, has_package):
        """Import the entry point, using package import for subdirectory-based examples."""
        if has_package:
            module_path = ".".join(entry_point.relative_to(example_dir).with_suffix("").parts)
            return importlib.import_module(module_path)
        else:
            return import_file(entry_point, f"{example_dir.name}_entry")

    async def _run_mocked_main(self, main_fn) -> bool:
        """Mock Module.from_args/start and call main(). Returns True if successful."""
        fake_module = Module("fake_address")
        with mock.patch("viam.module.module.Module.from_args", return_value=fake_module):
            with mock.patch.object(Module, "start", new_callable=AsyncMock):
                await main_fn()
        await fake_module.stop()
        return True

    async def _build_module_from_registry(self, resource_keys):
        """Build a Module using newly registered resource models."""
        module = Module("fake_address")
        for key in resource_keys:
            api_str, model_str = key.split("/")
            api = API.from_string(api_str)
            model = Model.from_string(model_str)
            module.add_model_from_registry(api, model)
        await module.stop()

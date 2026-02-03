import importlib
import importlib.util
import py_compile
import sys
from pathlib import Path
from typing import List, Optional

import pytest

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


# Python doesn't build all imports automatically, so recursively check all imports, and then the imported module's import, etc...
def verify_python_file_imports(filepath: Path, module_name: str, package_root: Optional[Path] = None) -> None:
    # Temporarily add directory to sys.path if needed for relative imports
    path_added = False
    if package_root and str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))
        path_added = True

    try:
        if package_root:
            # Calculate module name relative to package_root
            rel_to_package_root = filepath.relative_to(package_root)

            # Recalculate module name relative to package_root for module import
            path_to_convert = rel_to_package_root.parent if filepath.name == "__init__.py" else rel_to_package_root.with_suffix("")
            module_name = str(path_to_convert).replace("/", ".").replace("\\", ".")

            importlib.import_module(module_name)
        else:
            # For files without relative imports, load directly (no relative imports expected)
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            if spec is None or spec.loader is None:
                raise ImportError(f"Could not load spec for {filepath}")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
    finally:
        # Clean up sys.path
        if path_added:
            sys.path.remove(str(package_root))


def get_all_python_files() -> List[Path]:
    python_files = []

    def walk_directory(dir_path: Path) -> None:
        try:
            for item in dir_path.iterdir():
                if item.is_dir():
                    walk_directory(item)
                elif item.is_file() and item.suffix == ".py":
                    python_files.append(item)
        except PermissionError:
            # Skip directories we can't access
            pass

    walk_directory(EXAMPLES_DIR)
    return sorted(python_files)


# Get all Python files at module load time for parametrization
_ALL_PYTHON_FILES = get_all_python_files()


def get_package_root_for_file(file_path: Path) -> Optional[Path]:
    # List of example directories that use relative imports and need their directory in sys.path
    EXAMPLES_WITH_PACKAGES = {"complex_module", "simple_module", "server"}

    # Find which example the file belongs to (like complex_module vs server)
    current = file_path.parent
    while current.parent != EXAMPLES_DIR:
        current = current.parent

    # Return the directory if it needs sys.path support for relative imports
    if current.name in EXAMPLES_WITH_PACKAGES:
        return current

    return None


class TestExamplesSyntax:
    @pytest.mark.parametrize("py_file", _ALL_PYTHON_FILES, ids=lambda p: str(p.relative_to(EXAMPLES_DIR)))
    def test_python_file_syntax(self, py_file: Path):
        py_compile.compile(str(py_file), doraise=True)


class TestExamplesImports:
    # list of all python file's path from examples dir + whether it needs to be added to sys.path for proper imports
    _PYTHON_FILES_WITH_PATH = [(py_file, get_package_root_for_file(py_file)) for py_file in _ALL_PYTHON_FILES]
    # create file ids for each test so you can see which file is successfully building/not building
    _PYTHON_FILES_IDS = [str(py_file.relative_to(EXAMPLES_DIR)) for py_file in _ALL_PYTHON_FILES]

    # Verify that all example Python files can be imported (checks import statements).
    @pytest.mark.parametrize("py_file,package_root", _PYTHON_FILES_WITH_PATH, ids=_PYTHON_FILES_IDS)
    def test_python_file_imports(self, py_file: Path, package_root: Optional[Path]):
        relative_path = py_file.relative_to(EXAMPLES_DIR)
        # create unique identifier for each module
        module_name = str(relative_path).replace("/", "_").replace("\\", "_").replace(".py", "")

        # package_root will be the directory to be added to path for files with relative imports or None if none
        verify_python_file_imports(py_file, module_name, package_root=package_root)

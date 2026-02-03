"""Tests to verify that example code compiles and imports correctly."""

import importlib
import importlib.util
import py_compile
from pathlib import Path
from typing import Optional

import pytest

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"


def verify_python_file_imports(filepath: Path, module_name: str, add_to_path: Optional[Path] = None) -> None:
    import sys

    # Temporarily add directory to sys.path if needed for relative imports
    path_added = False
    if add_to_path and str(add_to_path) not in sys.path:
        sys.path.insert(0, str(add_to_path))
        path_added = True

    try:
        # For files with add_to_path (complex_module, simple_module), use proper import
        # This lets Python handle all the package setup automatically
        if add_to_path:
            # Calculate module name relative to add_to_path
            rel_to_add_path = filepath.relative_to(add_to_path)

            # Convert file path to module name:
            # - api.py -> api
            # - gizmo/api.py -> gizmo.api
            # - gizmo/__init__.py -> gizmo (because __init__.py IS the package)
            path_to_convert = rel_to_add_path.parent if filepath.name == "__init__.py" else rel_to_add_path.with_suffix("")
            module_name = str(path_to_convert).replace("/", ".").replace("\\", ".")

            # Use importlib.import_module - Python handles all package setup
            importlib.import_module(module_name)
        else:
            # For files without add_to_path, load directly (no relative imports expected)
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            if spec is None or spec.loader is None:
                raise ImportError(f"Could not load spec for {filepath}")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
    finally:
        # Clean up sys.path
        if path_added:
            sys.path.remove(str(add_to_path))


def get_all_python_files() -> list[Path]:
    # Get all Python files in the examples directory
    if not EXAMPLES_DIR.exists():
        return []

    python_files = []

    def walk_directory(dir_path: Path) -> None:
        # Recursively walk directory, skipping __pycache__ directories.
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


class TestExamplesSyntax:
    """Verify all example Python files have valid syntax."""

    @pytest.mark.parametrize("py_file", _ALL_PYTHON_FILES, ids=lambda p: str(p.relative_to(EXAMPLES_DIR)))
    def test_python_file_syntax(self, py_file: Path):
        """Verify a Python file has valid syntax."""
        py_compile.compile(str(py_file), doraise=True)


def get_add_to_path_for_file(file_path: Path) -> Optional[Path]:
    """
    Determine if a file needs add_to_path for imports.

    Returns the directory to add to sys.path, or None if not needed.
    Files in certain example directories need their top-level directory added to path.
    """
    # List of example directories that use relative imports and need their directory in sys.path
    EXAMPLES_WITH_PACKAGES = {"complex_module", "simple_module", "server"}

    # Find the top-level example directory (first directory under examples/)
    # e.g., examples/complex_module/src/gizmo/api.py -> examples/complex_module
    # e.g., examples/server/v1/server.py -> examples/server
    current = file_path.parent
    while current != EXAMPLES_DIR and current.parent != EXAMPLES_DIR:
        current = current.parent

    # Return the top-level example directory if it's in our list
    if current != EXAMPLES_DIR and current.parent == EXAMPLES_DIR and current.name in EXAMPLES_WITH_PACKAGES:
        return current

    return None


# Get all Python files with their add_to_path settings at module load time
_PYTHON_FILES_WITH_PATH = [(py_file, get_add_to_path_for_file(py_file)) for py_file in _ALL_PYTHON_FILES]
_PYTHON_FILES_IDS = [str(py_file.relative_to(EXAMPLES_DIR)) for py_file in _ALL_PYTHON_FILES]


class TestExamplesImports:
    """Verify all example Python files can be imported (checks import statements)."""

    @pytest.mark.parametrize("py_file,add_to_path", _PYTHON_FILES_WITH_PATH, ids=_PYTHON_FILES_IDS)
    def test_python_file_imports(self, py_file: Path, add_to_path: Optional[Path]):
        """Verify a Python file can be imported."""
        # Generate a module name (only used when add_to_path is None)
        # When add_to_path is set, verify_python_file_imports recalculates it properly
        relative_path = py_file.relative_to(EXAMPLES_DIR)
        module_name = str(relative_path).replace("/", "_").replace("\\", "_").replace(".py", "")

        verify_python_file_imports(py_file, module_name, add_to_path=add_to_path)

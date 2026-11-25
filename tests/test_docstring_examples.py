import ast
import textwrap
from collections.abc import Iterator
from pathlib import Path

import pytest

SRC = Path(__file__).parent.parent / "src" / "viam"
SKIP_DIRS = {"gen", "proto"}


def _literal_blocks(doc: str) -> Iterator[str]:
    """Yield the code of each reST literal block (introduced by a line containing only ``::``)."""
    lines = doc.expandtabs().splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip() == "::":
            i += 1
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i][0] in " \t"):
                block.append(lines[i])
                i += 1
            code = textwrap.dedent("\n".join(block)).strip("\n")
            if code:
                yield code
        else:
            i += 1


def _collect() -> Iterator[tuple[str, str]]:
    for path in sorted(SRC.rglob("*.py")):
        if SKIP_DIRS & set(path.relative_to(SRC).parts):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                doc = ast.get_docstring(node)
                if not doc:
                    continue
                name = getattr(node, "name", "<module>")
                for n, code in enumerate(_literal_blocks(doc)):
                    yield f"{path.relative_to(SRC)}::{name}[{n}]", code


CASES = list(_collect())


def test_examples_found():
    assert len(CASES) > 100


@pytest.mark.parametrize("code", [c for _, c in CASES], ids=[i for i, _ in CASES])
def test_docstring_example_is_valid_python(code: str):
    """Docstring examples are copied into the public docs, so they must at least parse."""
    ast.parse(code)

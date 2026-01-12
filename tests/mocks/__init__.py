import inspect
from typing import Dict, List, Sequence, Set, Tuple, Union, get_args, get_origin, get_type_hints
from unittest.mock import AsyncMock, create_autospec


def create_mock_subclass(abstract_class):
    abstracts = getattr(abstract_class, "__abstractmethods__", set())

    namespace = {}
    for method_name in abstracts:
        original_method = getattr(abstract_class, method_name)

        if inspect.iscoroutinefunction(original_method):
            mock = AsyncMock(spec=f"{abstract_class.__name__}.{method_name}")
            mock.__name__ = method_name
            mock.__signature__ = inspect.signature(original_method)
        else:
            mock = create_autospec(original_method, instance=True)

        namespace[method_name] = mock

    base_methods = [("do_command", {}), ("get_geometries", [])]
    for method_name, return_value in base_methods:
        original_method = getattr(abstract_class, method_name, None)
        if original_method:
            mock = AsyncMock(spec=f"{abstract_class.__name__}.{method_name}")
            mock.__name__ = method_name
            mock.__signature__ = inspect.signature(original_method)
            mock.return_value = return_value
            namespace[method_name] = mock

    return type(f"Mock{abstract_class.__name__}", (abstract_class,), namespace)

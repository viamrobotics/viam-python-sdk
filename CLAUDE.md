# Viam Python SDK

Public Python SDK for the Viam robotics platform (`viam-sdk`).

## Codebase Structure

```
src/viam/
  __init__.py                      — Main package exports
  version_metadata.py              — SDK version and API_VERSION
  gen/                             — Auto-generated protobuf code (never edit, not in repo)
  proto/                           — Hand-crafted proto wrappers
  types.py                         — Shared type definitions (ValueTypes)
  utils.py                         — Shared utilities (dict_to_struct, struct_to_dict, etc.)
  errors.py                        — Exception definitions
  robot/                           — Robot client and service
    client.py                      — RobotClient implementation
  components/<name>/               — Hardware component clients
    <name>.py                      — Abstract base class
    client.py                      — gRPC client wrapper
    service.py                     — gRPC service implementation
  services/<name>/                 — Service clients (same structure as components)
  app/                             — App/cloud API clients
  resource/                        — Resource management, registry, base classes
  rpc/                             — Connection management, gRPC server, WebRTC (Rust lib)
  module/                          — Custom module support
  media/                           — Video/camera utilities
tests/                             — pytest test suite
  mocks/                           — Mock components, services, robot
```

All component/service clients follow the same pattern. Tests live in `tests/` with `test_*.py` naming.

## Python Conventions

- **Line length** is 140 characters (`ruff` enforced).
- **Formatting**: `ruff format` + `ruff check --extend-select I --fix` for import sorting.
- **Type checking**: `pyright` (default/basic mode). Includes `src/`, excludes `gen/` and `proto/`.
- **Async**: All component/service methods are `async`. Tests use `pytest-asyncio` with `asyncio_mode = "auto"`.
- **Method signatures** follow this pattern:
  ```python
  async def method_name(
      self,
      param1: Type1,
      param2: Type2,
      *,
      extra: Optional[Dict[str, Any]] = None,
      timeout: Optional[float] = None,
      **kwargs,
  ) -> ReturnType:
  ```
- **Metadata extraction**: `md = kwargs.get("metadata", self.Metadata()).proto`
- **Extra parameters**: converted via `dict_to_struct(extra)` / `struct_to_dict(result)`.

## Language Notes

- Use `grpclib.testing.ChannelFor` and `tests/mocks/` patterns for test infrastructure.

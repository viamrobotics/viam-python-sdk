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

## Restrictions

- **NEVER** modify `.github/`, `Makefile`, `src/viam/gen/`, or `uv.lock`
- Only run `make buf` (to regenerate `src/viam/gen/`). Do NOT run other make targets unless explicitly needed.
- Do NOT add dependencies unless absolutely necessary — this is a public SDK.

## Tools

- Always prefer dedicated tools (Grep, Glob, Read, Edit, Write) over Bash equivalents (grep, find, cat, sed, etc.)
- Minimize turns: chain Bash commands with `&&`, avoid re-reading files you already explored, and do not use TodoWrite.

## CI Environment

These rules apply when running in GitHub Actions (CI) workflows:

- Run `make lint`, `make typecheck`, and `make test` to verify changes before committing. Fix any errors.
- Dependencies are already installed — do NOT run `make install` or `uv sync`.
- Bash commands CANNOT use pipes (`|`), command substitution (`$()`), or shell redirection. Run each command separately with explicit arguments.
- If a command is blocked or denied, do NOT retry it or try variations of the same approach. Switch to a different tool (e.g., use Edit instead of sed).
- For bulk edits (same change across many files): work in small batches of up to 5 files at a time — Read 5 files, then Edit those 5 files, then move to the next 5. Do NOT read all files at once then edit all at once — the Edit tool may lose track of reads from large batches. Do NOT use `Bash(sed -i ...)` — it is blocked by the sandbox.
- Always Read a file (full read, no offset/limit) before Editing it.
- Do NOT use Task subagents for file editing. Use the Edit tool directly from the main agent. Bash-type subagents only have the Bash tool — they cannot use Edit, Grep, or Glob.
- For commits: do NOT use `mcp__github_file_ops__commit_files` — it cannot target feature branches and will fail on repos with branch protection. Instead, run `git config user.email "noreply@anthropic.com" && git config user.name "Claude"`, then `git commit -m "single-line message"`. The commit message MUST be a single line (no newlines) or the permission glob will reject it.
- For PRs, write the body to `/tmp/pr-body.md` using the Write tool, then run `gh pr create --title "Title" --body-file /tmp/pr-body.md`. NEVER pass multi-line strings directly to `--body`.
- For reviews and comments: write the body to a temp file, then use `--body-file`. Example: `gh pr review 123 --approve --body-file /tmp/review-body.md`. The `*` glob in permission patterns does not match newlines, so inline `--body` with newlines will be denied.

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
- **Before creating a new file**, read 1–2 existing files of the same kind to match patterns exactly (e.g., read an existing `client.py` before writing a new one).

## Implementation

- Follow existing patterns. No new conventions or abstractions.
- Implement the **minimal change**. No refactors or unnecessary additions.
- Maintain backwards compatibility. No breaking changes to the public API.
- Add or update unit tests for changed behavior. Tests should verify meaningful logic, edge cases, error paths, state transitions — not just trivial assertions.
- Use `grpclib.testing.ChannelFor` and `tests/mocks/` patterns for test infrastructure.

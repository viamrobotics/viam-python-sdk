import os
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import pytest

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
PROJECT_ROOT = Path(__file__).parent.parent

STARTUP_SECONDS = 5

# Module examples that can be started as subprocesses with a socket path argument.
# Excludes "echo" (tested separately with server+client) and "server" (not a standalone runnable example).
MODULE_EXAMPLES = []
for _d in sorted(EXAMPLES_DIR.iterdir()):
    if not _d.is_dir() or _d.name in ("echo", "server"):
        continue
    for _candidate in [_d / "src" / "main.py", _d / "main.py", _d / "module.py"]:
        if _candidate.exists():
            MODULE_EXAMPLES.append((_d, _candidate))
            break

MODULE_EXAMPLE_IDS = [ex[0].name for ex in MODULE_EXAMPLES]


def _wait_for_socket(path: str, timeout: float = 5.0) -> bool:
    """Poll until a unix socket file exists."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if os.path.exists(path):
            return True
        time.sleep(0.1)
    return False


def _wait_for_port(host: str, port: int, timeout: float = 5.0) -> bool:
    """Poll until a TCP port is accepting connections."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.1)
    return False


def _terminate(proc: subprocess.Popen):
    """Send SIGTERM and wait; SIGKILL if it doesn't exit."""
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5)


class TestExamplesRun:
    """Start each example as a real subprocess and verify it doesn't crash."""

    @pytest.mark.parametrize("example_dir,entry_point", MODULE_EXAMPLES, ids=MODULE_EXAMPLE_IDS)
    def test_module_starts(self, example_dir: Path, entry_point: Path):
        """Start a module example with NO_MODULE_PARENT and verify it doesn't crash on startup."""
        # Use /tmp directly to avoid AF_UNIX path length limit (~104 chars on macOS).
        # pytest's tmp_path generates paths that are too long for unix sockets.
        tmp_dir = tempfile.mkdtemp(prefix="viam_test_")
        sock_path = os.path.join(tmp_dir, "m.sock")
        env = {**os.environ, "VIAM_NO_MODULE_PARENT": "true", "PYTHONPATH": str(example_dir)}

        proc = subprocess.Popen(
            [sys.executable, str(entry_point), sock_path],
            cwd=str(example_dir),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            ready = _wait_for_socket(sock_path, timeout=STARTUP_SECONDS)
            exit_code = proc.poll()

            if exit_code is not None:
                _, stderr = proc.communicate(timeout=5)
                pytest.fail(
                    f"{example_dir.name} exited with code {exit_code} during startup.\n"
                    f"stderr:\n{stderr.decode(errors='replace')}"
                )

            if not ready:
                _, stderr = proc.communicate(timeout=1) if proc.poll() is not None else (b"", b"(still running)")
                pytest.fail(
                    f"{example_dir.name} did not create socket at {sock_path} within {STARTUP_SECONDS}s.\n"
                    f"stderr:\n{stderr if isinstance(stderr, str) else stderr.decode(errors='replace')}"
                )
        finally:
            _terminate(proc)
            if os.path.exists(sock_path):
                os.unlink(sock_path)
            os.rmdir(tmp_dir)

    def test_echo_server_client(self):
        """Start the echo gRPC server, run the client, assert the client exits cleanly."""
        server_script = EXAMPLES_DIR / "echo" / "v1" / "server.py"
        client_script = EXAMPLES_DIR / "echo" / "v1" / "client.py"

        server_proc = subprocess.Popen(
            [sys.executable, str(server_script)],
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            assert _wait_for_port("127.0.0.1", 8080, timeout=STARTUP_SECONDS), (
                "Echo server did not start listening on port 8080"
            )

            result = subprocess.run(
                [sys.executable, str(client_script)],
                cwd=str(PROJECT_ROOT),
                capture_output=True,
                timeout=10,
            )
            assert result.returncode == 0, (
                f"Echo client failed with code {result.returncode}.\n"
                f"stderr:\n{result.stderr.decode(errors='replace')}"
            )
        finally:
            _terminate(server_proc)

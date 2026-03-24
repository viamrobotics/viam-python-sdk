import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import urlparse

import pytest

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
PROJECT_ROOT = Path(__file__).parent.parent


def _is_local(address: str) -> bool:
    LOCAL_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "::1"}
    if address.startswith("/") or address.startswith("unix://"):
        return True
    parsed = urlparse(address if "://" in address else f"http://{address}")
    return parsed.hostname in LOCAL_HOSTS


# If any new examples are added, add them to this list.
EXAMPLES = [
    {"dir": "complex_module", "entry": "src/main.py", "client": "client.py"},
    {"dir": "easy_resource", "entry": "main.py"},
    {"dir": "optionaldepsmodule", "entry": "module.py"},
    {"dir": "simple_module", "entry": "src/main.py", "client": "client.py"},
    {"dir": "stubbed_model", "entry": "main.py"},
    {"dir": "server", "server": "examples.server.v1.server", "client": "v1/client.py"},
]

HAS_VIAM_SERVER = shutil.which("viam-server") is not None


def _find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _terminate(proc):
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(timeout=5)


def _wait_for_port(host, port, timeout=10.0, proc=None):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if proc is not None and proc.poll() is not None:
            return False
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.1)
    return False


def _get_server_output(proc):
    """Read stdout and stderr from a terminated server process."""
    stdout = proc.stdout.read().decode(errors="replace") if proc.stdout else ""
    stderr = proc.stderr.read().decode(errors="replace") if proc.stderr else ""
    return stdout, stderr


def _wait_for_server_ready(log_path, timeout=30.0):
    """Wait for viam-server to finish loading modules (port opens before modules are ready)."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if os.path.exists(log_path):
            with open(log_path) as f:
                if "Robot constructed with full config" in f.read():
                    return True
        time.sleep(0.2)
    return False


@pytest.mark.parametrize("example", EXAMPLES, ids=[e["dir"] for e in EXAMPLES])
def test_example(example):
    is_server_example = "server" in example

    # if someone is running these tests without viam-server it'll skip, it runs in the github actions workflow anyways
    if not is_server_example and not HAS_VIAM_SERVER:
        pytest.skip("viam-server not found")

    example_dir = EXAMPLES_DIR / example["dir"]
    client_file = example_dir / example["client"] if "client" in example else None
    port = _find_free_port()
    address = f"127.0.0.1:{port}"

    tmp_dir = tempfile.mkdtemp(prefix="viam_test_")
    server_proc = None
    server_log_fh = None

    try:
        if is_server_example:
            server_proc = subprocess.Popen(
                [sys.executable, "-m", example["server"], "127.0.0.1", str(port), "quiet"],
                cwd=str(PROJECT_ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if not _wait_for_port("127.0.0.1", port, proc=server_proc):
                _terminate(server_proc)
                stdout, stderr = _get_server_output(server_proc)
                returncode = server_proc.returncode
                server_proc = None
                msg = f"Server did not start on {address}"
                if returncode is not None:
                    msg += f"\nProcess exited with code {returncode}"
                if stdout.strip():
                    msg += f"\nstdout:\n{stdout}"
                if stderr.strip():
                    msg += f"\nstderr:\n{stderr}"
                pytest.fail(msg)
        else:
            entry_point = example_dir / example["entry"]
            wrapper = os.path.join(tmp_dir, "wrapper.sh")
            with open(wrapper, "w") as f:
                f.write(f'#!/bin/bash\nexec {sys.executable} {entry_point} "$@"\n')
            os.chmod(wrapper, 0o755)

            with open(example_dir / "config.json") as f:
                config = json.load(f)
            for mod in config.get("modules", []):
                mod["executable_path"] = wrapper
            config["network"] = {"bind_address": address}
            test_config = os.path.join(tmp_dir, "config.json")
            with open(test_config, "w") as f:
                json.dump(config, f)

            server_log = os.path.join(tmp_dir, "server.log")
            server_log_fh = open(server_log, "w")
            server_proc = subprocess.Popen(
                ["viam-server", "-config", test_config, "-no-tls", "-allow-insecure-creds"],
                cwd=str(example_dir),
                env={**os.environ, "PYTHONPATH": str(example_dir)},
                stdout=server_log_fh,
                stderr=subprocess.STDOUT,
            )
            assert _wait_for_server_ready(server_log), f"viam-server did not start.\nlog:\n{open(server_log).read()}"

        if client_file:
            local = str(_is_local(address))
            cmd = [sys.executable, str(client_file), address]
            if not is_server_example:
                cmd += ["test_id", "test_key", local]
            result = subprocess.run(
                cmd,
                cwd=str(PROJECT_ROOT) if is_server_example else str(example_dir),
                env={**os.environ, "PYTHONPATH": str(example_dir)},
                capture_output=True,
                timeout=30,
            )
            assert result.returncode == 0, f"Client failed.\nstdout:\n{result.stdout.decode()}\nstderr:\n{result.stderr.decode()}"
    finally:
        if server_proc:
            _terminate(server_proc)
        if server_log_fh:
            server_log_fh.close()
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_check_example_coverage():
    """Check if a new example directory exists that isn't in the EXAMPLES table."""
    known = {e["dir"] for e in EXAMPLES}
    actual = {d.name for d in EXAMPLES_DIR.iterdir() if d.is_dir()}
    unknown = actual - known
    assert not unknown, (
        f"New example directories without test coverage: {unknown}. Add new examples to the EXAMPLES list in tests/test_examples.py."
    )


def test_wait_for_port_detects_process_death():
    """_wait_for_port returns early when the monitored process exits."""
    port = _find_free_port()
    proc = subprocess.Popen(
        [sys.executable, "-c", "import sys; sys.exit(1)"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    start = time.monotonic()
    result = _wait_for_port("127.0.0.1", port, timeout=10.0, proc=proc)
    elapsed = time.monotonic() - start
    assert result is False
    assert elapsed < 5.0, f"Should have returned early when process died, but took {elapsed:.1f}s"
    proc.stdout.close()
    proc.stderr.close()


def test_get_server_output_captures_stderr():
    """_get_server_output captures process stderr for error reporting."""
    error_message = "TypeError: Can't instantiate abstract class"
    proc = subprocess.Popen(
        [sys.executable, "-c", f"import sys; print('{error_message}', file=sys.stderr); sys.exit(1)"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    proc.wait()
    stdout, stderr = _get_server_output(proc)
    assert error_message in stderr
    assert stdout == ""

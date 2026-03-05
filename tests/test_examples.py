import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import pytest

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"

EXAMPLES = [
    {"dir": "complex_module", "entry": "src/main.py", "client": "client.py"},
    {"dir": "easy_resource", "entry": "main.py"},
    {"dir": "optionaldepsmodule", "entry": "module.py"},
    {"dir": "simple_module", "entry": "src/main.py", "client": "client.py"},
    {"dir": "stubbed_model", "entry": "main.py"},
]


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


def _wait_for_server_ready(log_path, timeout=30.0):
    """Poll viam-server log until modules are loaded.

    viam-server opens its port before modules finish loading, so we wait for
    the "Robot constructed with full config" log line.
    """
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if os.path.exists(log_path):
            with open(log_path) as f:
                if "Robot constructed with full config" in f.read():
                    return True
        time.sleep(0.2)
    return False


@pytest.mark.skipif(not shutil.which("viam-server"), reason="viam-server not found")
@pytest.mark.parametrize("example", EXAMPLES, ids=[e["dir"] for e in EXAMPLES])
def test_example(example):
    """Start viam-server with the example's config, optionally run client.py."""
    example_dir = EXAMPLES_DIR / example["dir"]
    entry_point = example_dir / example["entry"]
    config_path = example_dir / "config.json"
    client_file = example_dir / example["client"] if "client" in example else None

    tmp_dir = tempfile.mkdtemp(prefix="viam_test_")
    server_proc = None
    server_log_fh = None

    try:
        # Create wrapper script (bypasses run.sh venv creation)
        wrapper = os.path.join(tmp_dir, "wrapper.sh")
        with open(wrapper, "w") as f:
            f.write(f'#!/bin/bash\nexec {sys.executable} {entry_point} "$@"\n')
        os.chmod(wrapper, 0o755)

        # Patch config with wrapper path and a free port
        with open(config_path) as f:
            config = json.load(f)
        for mod in config.get("modules", []):
            mod["executable_path"] = wrapper
        port = _find_free_port()
        config["network"] = {"bind_address": f"127.0.0.1:{port}"}
        test_config = os.path.join(tmp_dir, "config.json")
        with open(test_config, "w") as f:
            json.dump(config, f)

        # Start viam-server
        server_log = os.path.join(tmp_dir, "server.log")
        server_log_fh = open(server_log, "w")
        server_proc = subprocess.Popen(
            ["viam-server", "-config", test_config, "-no-tls", "-allow-insecure-creds"],
            cwd=str(example_dir),
            env={**os.environ, "PYTHONPATH": str(example_dir)},
            stdout=server_log_fh,
            stderr=subprocess.STDOUT,
        )

        assert _wait_for_server_ready(server_log), (
            f"viam-server did not start.\nlog:\n{open(server_log).read()}"
        )

        # Run client if present
        if client_file:
            result = subprocess.run(
                [sys.executable, str(client_file), f"127.0.0.1:{port}", "test_id", "test_key"],
                cwd=str(example_dir),
                env={**os.environ, "PYTHONPATH": str(example_dir)},
                capture_output=True,
                timeout=30,
            )
            assert result.returncode == 0, (
                f"Client failed.\nstdout:\n{result.stdout.decode()}\nstderr:\n{result.stderr.decode()}"
            )
    finally:
        if server_proc:
            _terminate(server_proc)
        if server_log_fh:
            server_log_fh.close()
        shutil.rmtree(tmp_dir, ignore_errors=True)

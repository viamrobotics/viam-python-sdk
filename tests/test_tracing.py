import asyncio
import os
import threading
from unittest import mock

import pytest

from viam.rpc import tracing

pytestmark = pytest.mark.skipif(not tracing.OTEL_AVAILABLE, reason="opentelemetry extra not installed")


if tracing.OTEL_AVAILABLE:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor, SpanExportResult
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter


@pytest.fixture(scope="module", autouse=True)
def _global_tracer_provider():
    """Install one TracerProvider for the whole test module.

    OpenTelemetry refuses to override an already-installed global
    TracerProvider, so we set it once and share it across tests.
    """
    provider = TracerProvider()
    trace.set_tracer_provider(provider)
    yield provider


@pytest.fixture()
def memory_exporter(_global_tracer_provider):
    exporter = InMemorySpanExporter()
    processor = SimpleSpanProcessor(exporter)
    _global_tracer_provider.add_span_processor(processor)
    yield exporter
    exporter.clear()


@pytest.fixture(autouse=True)
def _reset_tracing_state():
    tracing._reset_for_tests()
    tracing._missing_extra_warned = False
    yield
    tracing._reset_for_tests()
    tracing._missing_extra_warned = False


class TestMissingExtraWarning:
    def test_warns_once_when_env_set_but_otel_absent(self):
        with mock.patch.object(tracing, "OTEL_AVAILABLE", False):
            with mock.patch.dict(os.environ, {tracing.TRACING_ENV_VAR: "1"}):
                with pytest.warns(UserWarning, match=r"tracing dependencies are missing"):
                    assert tracing.tracing_enabled() is False
                # Second call must not warn again.
                import warnings as _w

                with _w.catch_warnings():
                    _w.simplefilter("error")
                    assert tracing.tracing_enabled() is False

    def test_no_warning_when_env_unset(self):
        with mock.patch.object(tracing, "OTEL_AVAILABLE", False):
            with mock.patch.dict(os.environ, {}, clear=True):
                import warnings as _w

                with _w.catch_warnings():
                    _w.simplefilter("error")
                    assert tracing.tracing_enabled() is False


class TestTracingEnabled:
    def test_disabled_by_default(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            assert tracing.tracing_enabled() is False

    @pytest.mark.parametrize("val", ["", "0", "false", "FALSE", "no", "off"])
    def test_falsy_disables(self, val):
        with mock.patch.dict(os.environ, {tracing.TRACING_ENV_VAR: val}):
            assert tracing.tracing_enabled() is False

    @pytest.mark.parametrize("val", ["1", "true", "yes", "on", "anything"])
    def test_truthy_enables(self, val):
        with mock.patch.dict(os.environ, {tracing.TRACING_ENV_VAR: val}):
            assert tracing.tracing_enabled() is True


class TestContextPropagation:
    def test_inject_writes_traceparent_when_active_span(self, _global_tracer_provider):
        tracing._force_installed_for_tests()
        tracer = trace.get_tracer("test")
        with tracer.start_as_current_span("outer"):
            md: dict = {}
            tracing.inject_trace_context(md)
            assert "traceparent" in md
            traceparent = md["traceparent"]

        extracted = tracing.extract_trace_context({"traceparent": traceparent})
        span_ctx = trace.get_current_span(extracted).get_span_context()
        assert span_ctx.is_valid

    def test_extract_handles_bytes_values(self, _global_tracer_provider):
        tracing._force_installed_for_tests()
        tracer = trace.get_tracer("test")
        with tracer.start_as_current_span("outer"):
            md: dict = {}
            tracing.inject_trace_context(md)
            tp = md["traceparent"]

        extracted = tracing.extract_trace_context({"traceparent": tp.encode("ascii")})
        span_ctx = trace.get_current_span(extracted).get_span_context()
        assert span_ctx.is_valid

    def test_inject_noop_when_not_installed(self, _global_tracer_provider):
        tracer = trace.get_tracer("test")
        with tracer.start_as_current_span("outer"):
            md: dict = {}
            tracing.inject_trace_context(md)
            assert md == {}


class TestStartServerSpan:
    def test_no_provider_yields_none(self):
        # _reset_tracing_state cleared the sentinel; should be no-op.
        with tracing.start_server_span("Foo", {}) as span:
            assert span is None

    def test_with_provider_creates_span_and_extracts_parent(self, memory_exporter):
        tracing._force_installed_for_tests()

        tracer = trace.get_tracer("test")
        with tracer.start_as_current_span("parent") as parent:
            md: dict = {}
            tracing.inject_trace_context(md)
            parent_trace_id = parent.get_span_context().trace_id

        with tracing.start_server_span("DoThing", md) as span:
            assert span is not None
            assert span.is_recording()
            assert span.get_span_context().trace_id == parent_trace_id

        spans = memory_exporter.get_finished_spans()
        server_spans = [s for s in spans if s.name == "DoThing"]
        assert len(server_spans) == 1
        s = server_spans[0]
        assert s.kind == trace.SpanKind.SERVER
        assert s.attributes["rpc.system"] == "grpc"
        assert s.attributes["rpc.method"] == "DoThing"

    def test_records_exception(self, memory_exporter):
        tracing._force_installed_for_tests()

        with pytest.raises(ValueError):
            with tracing.start_server_span("Bad", {}):
                raise ValueError("boom")

        spans = memory_exporter.get_finished_spans()
        bad = [s for s in spans if s.name == "Bad"]
        assert len(bad) == 1
        assert bad[0].status.status_code == trace.StatusCode.ERROR
        assert any(ev.name == "exception" for ev in bad[0].events)


class TestInstallExporter:
    def test_noop_when_disabled(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            assert tracing.install_parent_send_exporter(mock.Mock()) is False

    def test_noop_when_already_installed(self):
        with mock.patch.dict(os.environ, {tracing.TRACING_ENV_VAR: "1"}):
            tracing._force_installed_for_tests()
            assert tracing.install_parent_send_exporter(mock.Mock()) is False


def _start_background_loop():
    """Spin up an asyncio loop on a worker thread; return (loop, stop_fn)."""
    loop_ready = threading.Event()
    loop_holder: dict = {}

    def run_loop():
        loop = asyncio.new_event_loop()
        loop_holder["loop"] = loop
        asyncio.set_event_loop(loop)
        loop_ready.set()
        try:
            loop.run_forever()
        finally:
            loop.close()

    thread = threading.Thread(target=run_loop, daemon=True)
    thread.start()
    loop_ready.wait()
    loop = loop_holder["loop"]

    def stop():
        loop.call_soon_threadsafe(loop.stop)
        thread.join(timeout=2)

    return loop, stop


class TestParentSendExporter:
    def test_export_dispatches_to_captured_loop(self, _global_tracer_provider):
        captured_loops: list = []

        async def fake_send_traces(req):
            captured_loops.append(asyncio.get_running_loop())
            return mock.Mock()

        loop, stop = _start_background_loop()
        try:
            robot_client = mock.Mock()
            robot_client._client.SendTraces = fake_send_traces
            exporter = tracing.ParentSendTracesExporter(robot_client, loop)

            tracer = trace.get_tracer("test-export")
            sink = InMemorySpanExporter()
            proc = SimpleSpanProcessor(sink)
            _global_tracer_provider.add_span_processor(proc)
            with tracer.start_as_current_span("export-me"):
                pass
            readable = [s for s in sink.get_finished_spans() if s.name == "export-me"]

            assert exporter.export(readable) == SpanExportResult.SUCCESS
            assert captured_loops == [loop]
        finally:
            stop()

    def test_export_cancels_on_timeout(self, _global_tracer_provider):
        cancelled = threading.Event()

        async def slow_send_traces(req):
            try:
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                cancelled.set()
                raise

        loop, stop = _start_background_loop()
        try:
            robot_client = mock.Mock()
            robot_client._client.SendTraces = slow_send_traces
            exporter = tracing.ParentSendTracesExporter(robot_client, loop)

            tracer = trace.get_tracer("test-timeout")
            sink = InMemorySpanExporter()
            _global_tracer_provider.add_span_processor(SimpleSpanProcessor(sink))
            with tracer.start_as_current_span("timeout-me"):
                pass
            readable = [s for s in sink.get_finished_spans() if s.name == "timeout-me"]

            with mock.patch.object(tracing, "_EXPORT_TIMEOUT_SEC", 0.05):
                assert exporter.export(readable) == SpanExportResult.FAILURE
            assert cancelled.wait(timeout=2), "in-flight RPC should have been cancelled"
        finally:
            stop()

    def test_export_noop_on_empty(self):
        exporter = tracing.ParentSendTracesExporter(mock.Mock(), mock.Mock())
        assert exporter.export([]) == SpanExportResult.SUCCESS

    def test_export_failure_after_shutdown(self):
        exporter = tracing.ParentSendTracesExporter(mock.Mock(), mock.Mock())
        exporter.shutdown()
        assert exporter.export([mock.Mock()]) == SpanExportResult.FAILURE


class TestSpansToResourceSpans:
    def test_encodes_span_attributes_and_status(self, _global_tracer_provider):
        tracer = trace.get_tracer("scope-x")
        with tracer.start_as_current_span("op", attributes={"a": 1, "b": "two"}) as span:
            span.set_status(trace.Status(trace.StatusCode.ERROR, "nope"))

        from opentelemetry.sdk.trace import ReadableSpan

        # Build a ReadableSpan from the just-ended span by exporting via a private collector.
        exporter = InMemorySpanExporter()
        proc = SimpleSpanProcessor(exporter)
        _global_tracer_provider.add_span_processor(proc)
        with tracer.start_as_current_span("op2", attributes={"k": True}) as s2:
            s2.set_status(trace.Status(trace.StatusCode.ERROR, "x"))
        readable: ReadableSpan = exporter.get_finished_spans()[0]

        out = tracing._spans_to_resource_spans([readable])
        assert len(out) == 1
        rs = out[0]
        assert len(rs.scope_spans) == 1
        ss = rs.scope_spans[0]
        assert ss.scope.name == "scope-x"
        assert len(ss.spans) == 1
        pb = ss.spans[0]
        assert pb.name == "op2"
        assert any(kv.key == "k" and kv.value.bool_value is True for kv in pb.attributes)
        assert pb.status.code == pb.status.STATUS_CODE_ERROR

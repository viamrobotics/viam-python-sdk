# pyright: reportPossiblyUnboundVariable=false, reportRedeclaration=false, reportOptionalMemberAccess=false, reportAttributeAccessIssue=false, reportGeneralTypeIssues=false
"""Automated OpenTelemetry tracing for gRPC RPCs in the Viam Python SDK.

Tracing is an *optional* feature. Install the ``tracing`` extra to enable
it::

    pip install "viam-sdk[tracing]"

Without the extra, every function in this module is a safe no-op so the
rest of the SDK works unchanged. With the extra, spans are emitted only
when the ``VIAM_MODULE_TRACING`` environment variable is set to a truthy
value, mirroring viam-cpp-sdk.

When enabled, the W3C Trace Context propagator is installed so incoming
trace context is honored, and a custom exporter ships spans to the parent
``viam-server`` via the ``RobotService.SendTraces`` RPC.

OTLP encoding is implemented locally against the protobuf types bundled
under ``viam.gen.opentelemetry`` so that the SDK does not depend on the
PyPI ``opentelemetry-proto`` package, which would conflict with those
bundled types in the protobuf descriptor pool.
"""

import asyncio
import concurrent.futures
import os
import warnings
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, List, Mapping, MutableMapping

from viam import logging

if TYPE_CHECKING:
    from viam.robot.client import RobotClient

LOGGER = logging.getLogger(__name__)

TRACING_ENV_VAR = "VIAM_MODULE_TRACING"
INSTRUMENTATION_SCOPE = "viam-python-sdk"
SERVICE_NAME_VALUE = "viam-python-sdk"
_FALSY = {"", "0", "false", "no", "off"}
_EXPORT_TIMEOUT_SEC = 5

try:
    from opentelemetry import propagate, trace
    from opentelemetry.propagators.textmap import Getter, Setter
    from opentelemetry.sdk.resources import SERVICE_NAME, Resource
    from opentelemetry.sdk.trace import ReadableSpan, TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter, SpanExportResult
    from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

    OTEL_AVAILABLE = True
except ImportError:
    OTEL_AVAILABLE = False


_missing_extra_warned = False


def tracing_enabled() -> bool:
    """Return whether tracing is enabled via the ``VIAM_MODULE_TRACING`` env var.

    Returns ``False`` when the ``tracing`` extra is not installed, warning
    once if the env var is set but the extra is missing.
    """
    env_set = os.environ.get(TRACING_ENV_VAR, "").strip().lower() not in _FALSY
    if not env_set:
        return False
    if not OTEL_AVAILABLE:
        global _missing_extra_warned
        if not _missing_extra_warned:
            warnings.warn(
                f"{TRACING_ENV_VAR} is set but tracing dependencies are missing. "
                "Install the [tracing] extra, e.g. `pip install 'viam-sdk[tracing]'`."
            )
            _missing_extra_warned = True
        return False
    return True


_provider_installed = False


if OTEL_AVAILABLE:
    from viam.gen.opentelemetry.proto.common.v1.common_pb2 import (
        AnyValue,
        InstrumentationScope,
        KeyValue,
    )
    from viam.gen.opentelemetry.proto.resource.v1.resource_pb2 import Resource as PbResource
    from viam.gen.opentelemetry.proto.trace.v1.trace_pb2 import (
        ResourceSpans as ViamResourceSpans,
    )
    from viam.gen.opentelemetry.proto.trace.v1.trace_pb2 import (
        ScopeSpans,
        Span,
        Status as PbStatus,
    )
    from viam.proto.robot import SendTracesRequest

    class _MetadataSetter(Setter[MutableMapping[str, Any]]):
        def set(self, carrier: MutableMapping[str, Any], key: str, value: str) -> None:
            carrier[key] = value

    class _MetadataGetter(Getter[Mapping[str, Any]]):
        def get(self, carrier: Mapping[str, Any], key: str):
            value = carrier.get(key)
            if value is None:
                value = carrier.get(key.lower())
            if value is None:
                return None
            if isinstance(value, (bytes, bytearray)):
                return [value.decode("ascii", errors="replace")]
            if isinstance(value, str):
                return [value]
            return [str(value)]

        def keys(self, carrier: Mapping[str, Any]):
            return list(carrier.keys())

    _SETTER = _MetadataSetter()
    _GETTER = _MetadataGetter()

    def inject_trace_context(metadata: MutableMapping[str, Any]) -> None:
        """Inject the active trace context into outgoing gRPC metadata.

        No-op until ``install_parent_send_exporter`` has installed the W3C
        propagator, so import-time installation doesn't override a user's
        own global propagator.
        """
        if not _provider_installed:
            return
        propagate.inject(metadata, setter=_SETTER)

    def extract_trace_context(metadata: Mapping[str, Any]):
        """Extract trace context from incoming gRPC metadata."""
        return propagate.extract(metadata, getter=_GETTER)

    def get_tracer():
        """Return the tracer for the Viam Python SDK instrumentation scope."""
        return trace.get_tracer(INSTRUMENTATION_SCOPE)

    @contextmanager
    def start_server_span(method_name: str, metadata: Mapping[str, Any]):
        """Context manager that opens a SERVER span for an incoming RPC.

        On exception inside the ``with`` block, records the exception and
        marks the span ERROR before re-raising.
        """
        if not _provider_installed:
            yield None
            return
        parent_ctx = extract_trace_context(metadata)
        tracer = get_tracer()
        with tracer.start_as_current_span(
            method_name,
            context=parent_ctx,
            kind=trace.SpanKind.SERVER,
            attributes={"rpc.system": "grpc", "rpc.method": method_name},
        ) as span:
            try:
                yield span
            except Exception as e:
                span.record_exception(e)
                span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
                raise

    def _any_value(v) -> AnyValue:
        # bool must precede int: bool is a subclass of int.
        if isinstance(v, bool):
            return AnyValue(bool_value=v)
        if isinstance(v, int):
            return AnyValue(int_value=v)
        if isinstance(v, float):
            return AnyValue(double_value=v)
        if isinstance(v, bytes):
            return AnyValue(bytes_value=v)
        return AnyValue(string_value=str(v))

    def _kvs(attrs: Mapping[str, Any]) -> List[KeyValue]:
        return [KeyValue(key=k, value=_any_value(v)) for k, v in (attrs or {}).items()]

    _OTEL_SPAN_KIND_TO_PB = {
        trace.SpanKind.INTERNAL: Span.SPAN_KIND_INTERNAL,
        trace.SpanKind.SERVER: Span.SPAN_KIND_SERVER,
        trace.SpanKind.CLIENT: Span.SPAN_KIND_CLIENT,
        trace.SpanKind.PRODUCER: Span.SPAN_KIND_PRODUCER,
        trace.SpanKind.CONSUMER: Span.SPAN_KIND_CONSUMER,
    }

    def _status_to_pb(status) -> PbStatus:
        code_map = {
            trace.StatusCode.UNSET: PbStatus.STATUS_CODE_UNSET,
            trace.StatusCode.OK: PbStatus.STATUS_CODE_OK,
            trace.StatusCode.ERROR: PbStatus.STATUS_CODE_ERROR,
        }
        return PbStatus(code=code_map.get(status.status_code, PbStatus.STATUS_CODE_UNSET), message=status.description or "")

    def _span_to_pb(span: "ReadableSpan") -> Span:
        ctx = span.get_span_context()
        parent = span.parent
        events = [
            Span.Event(
                time_unix_nano=ev.timestamp,
                name=ev.name,
                attributes=_kvs(dict(ev.attributes or {})),
            )
            for ev in (span.events or [])
        ]
        links = [
            Span.Link(
                trace_id=link.context.trace_id.to_bytes(16, "big"),
                span_id=link.context.span_id.to_bytes(8, "big"),
                attributes=_kvs(dict(link.attributes or {})),
            )
            for link in (span.links or [])
        ]
        return Span(
            trace_id=ctx.trace_id.to_bytes(16, "big"),
            span_id=ctx.span_id.to_bytes(8, "big"),
            parent_span_id=parent.span_id.to_bytes(8, "big") if parent else b"",
            name=span.name,
            kind=_OTEL_SPAN_KIND_TO_PB.get(span.kind, Span.SPAN_KIND_INTERNAL),
            start_time_unix_nano=span.start_time or 0,
            end_time_unix_nano=span.end_time or 0,
            attributes=_kvs(dict(span.attributes or {})),
            events=events,
            links=links,
            status=_status_to_pb(span.status),
        )

    def _spans_to_resource_spans(spans: Iterable["ReadableSpan"]) -> List[ViamResourceSpans]:
        """Group ``ReadableSpan``s into ``ResourceSpans`` by resource and scope."""
        # resource_key -> (PbResource, {scope_key: (InstrumentationScope, [Span])})
        by_resource: dict = {}
        for span in spans:
            res = span.resource
            res_attrs = tuple(sorted((res.attributes or {}).items())) if res else ()
            if res_attrs not in by_resource:
                pb_res = PbResource(attributes=_kvs(dict(res.attributes) if res else {}))
                by_resource[res_attrs] = (pb_res, {})
            _, scopes = by_resource[res_attrs]

            inst = span.instrumentation_scope
            scope_name = inst.name if inst else ""
            scope_version = inst.version if inst and inst.version else ""
            scope_key = (scope_name, scope_version)
            if scope_key not in scopes:
                scopes[scope_key] = (InstrumentationScope(name=scope_name, version=scope_version), [])
            scopes[scope_key][1].append(_span_to_pb(span))

        out: List[ViamResourceSpans] = []
        for pb_res, scopes in by_resource.values():
            scope_spans = [ScopeSpans(scope=scope, spans=spans_pb) for scope, spans_pb in scopes.values()]
            out.append(ViamResourceSpans(resource=pb_res, scope_spans=scope_spans))
        return out

    class ParentSendTracesExporter(SpanExporter):
        """Exporter that ships spans to the parent robot via ``SendTraces``.

        Mirrors viam-cpp-sdk's ``ParentSendTracesExporter``.
        """

        def __init__(self, robot_client: "RobotClient", loop: asyncio.AbstractEventLoop) -> None:
            """Capture the parent module's event loop for cross-thread dispatch.

            ``BatchSpanProcessor`` calls ``export`` from a worker thread, so
            the RPC must be scheduled back onto the loop that owns
            ``robot_client``'s gRPC channel.
            """
            self._robot_client = robot_client
            self._loop = loop
            self._shutdown = False

        def export(self, spans) -> "SpanExportResult":
            if self._shutdown:
                return SpanExportResult.FAILURE
            if not spans:
                return SpanExportResult.SUCCESS
            try:
                req = SendTracesRequest(resource_spans=_spans_to_resource_spans(spans))
                coro = self._robot_client._client.SendTraces(req)
                fut = asyncio.run_coroutine_threadsafe(coro, self._loop)
                try:
                    fut.result(timeout=_EXPORT_TIMEOUT_SEC)
                except concurrent.futures.TimeoutError:
                    # Don't leak the in-flight RPC on the parent loop.
                    fut.cancel()
                    raise
                return SpanExportResult.SUCCESS
            except Exception as e:
                LOGGER.debug(f"Failed to export traces to parent: {e}")
                return SpanExportResult.FAILURE

        def shutdown(self) -> None:
            self._shutdown = True

        def force_flush(self, timeout_millis: int = 30000) -> bool:
            return True

    def install_parent_send_exporter(robot_client: "RobotClient") -> bool:
        """Install a ``TracerProvider`` that exports spans to ``robot_client``.

        Must be called from the event loop that owns ``robot_client``'s gRPC
        channel; that loop is captured for cross-thread dispatch from the
        ``BatchSpanProcessor`` worker.

        No-op if tracing is disabled or already installed. Returns ``True``
        only when the provider was installed in this call.
        """
        global _provider_installed
        if _provider_installed:
            return False
        if not tracing_enabled():
            return False
        loop = asyncio.get_running_loop()
        # Install the W3C propagator here rather than at import so we don't
        # clobber a user's own propagator unless they opted into tracing.
        propagate.set_global_textmap(TraceContextTextMapPropagator())
        resource = Resource.create({SERVICE_NAME: SERVICE_NAME_VALUE})
        provider = TracerProvider(resource=resource)
        provider.add_span_processor(BatchSpanProcessor(ParentSendTracesExporter(robot_client, loop)))
        trace.set_tracer_provider(provider)
        _provider_installed = True
        LOGGER.debug("Viam tracing enabled; spans will be forwarded to parent robot")
        return True

else:
    # No-op fallbacks when opentelemetry is not installed.

    def inject_trace_context(metadata: MutableMapping[str, Any]) -> None:  # type: ignore[misc]
        return

    def extract_trace_context(metadata: Mapping[str, Any]):  # type: ignore[misc]
        return None

    def get_tracer():  # type: ignore[misc]
        return None

    @contextmanager
    def start_server_span(method_name: str, metadata: Mapping[str, Any]):  # type: ignore[misc]
        yield None

    def install_parent_send_exporter(robot_client: "RobotClient") -> bool:  # type: ignore[misc]
        return False


def _reset_for_tests() -> None:
    """Test-only helper: clear the installed-provider sentinel."""
    global _provider_installed
    _provider_installed = False


def _force_installed_for_tests() -> None:
    """Test-only helper: mark the provider as installed without wiring exporter."""
    global _provider_installed
    _provider_installed = True

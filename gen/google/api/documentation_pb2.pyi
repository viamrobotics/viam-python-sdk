"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Documentation(google.protobuf.message.Message):
    """`Documentation` provides the information for describing a service.

    Example:
    <pre><code>documentation:
      summary: >
        The Google Calendar API gives access
        to most calendar features.
      pages:
      - name: Overview
        content: &#40;== include google/foo/overview.md ==&#41;
      - name: Tutorial
        content: &#40;== include google/foo/tutorial.md ==&#41;
        subpages;
        - name: Java
          content: &#40;== include google/foo/tutorial_java.md ==&#41;
      rules:
      - selector: google.calendar.Calendar.Get
        description: >
          ...
      - selector: google.calendar.Calendar.Put
        description: >
          ...
    </code></pre>
    Documentation is provided in markdown syntax. In addition to
    standard markdown features, definition lists, tables and fenced
    code blocks are supported. Section headers can be provided and are
    interpreted relative to the section nesting of the context where
    a documentation fragment is embedded.

    Documentation from the IDL is merged with documentation defined
    via the config at normalization time, where documentation provided
    by config rules overrides IDL provided.

    A number of constructs specific to the API platform are supported
    in documentation text.

    In order to reference a proto element, the following
    notation can be used:
    <pre><code>&#91;fully.qualified.proto.name]&#91;]</code></pre>
    To override the display text used for the link, this can be used:
    <pre><code>&#91;display text]&#91;fully.qualified.proto.name]</code></pre>
    Text can be excluded from doc using the following notation:
    <pre><code>&#40;-- internal comment --&#41;</code></pre>

    A few directives are available in documentation. Note that
    directives must appear on a single line to be properly
    identified. The `include` directive includes a markdown file from
    an external source:
    <pre><code>&#40;== include path/to/file ==&#41;</code></pre>
    The `resource_for` directive marks a message to be the resource of
    a collection in REST view. If it is not specified, tools attempt
    to infer the resource from the operations in a collection:
    <pre><code>&#40;== resource_for v1.shelves.books ==&#41;</code></pre>
    The directive `suppress_warning` does not directly affect documentation
    and is documented together with service config validation.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUMMARY_FIELD_NUMBER: builtins.int
    PAGES_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    DOCUMENTATION_ROOT_URL_FIELD_NUMBER: builtins.int
    SERVICE_ROOT_URL_FIELD_NUMBER: builtins.int
    OVERVIEW_FIELD_NUMBER: builtins.int
    summary: typing.Text = ...
    """A short summary of what the service does. Can only be provided by
    plain text.
    """

    @property
    def pages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Page]:
        """The top level pages for the documentation set."""
        pass
    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DocumentationRule]:
        """A list of documentation rules that apply to individual API elements.

        **NOTE:** All service configuration rules follow "last one wins" order.
        """
        pass
    documentation_root_url: typing.Text = ...
    """The URL to the root of documentation."""

    service_root_url: typing.Text = ...
    """Specifies the service root url if the default one (the service name
    from the yaml file) is not suitable. This can be seen in any fully
    specified service urls as well as sections that show a base that other
    urls are relative to.
    """

    overview: typing.Text = ...
    """Declares a single overview page. For example:
    <pre><code>documentation:
      summary: ...
      overview: &#40;== include overview.md ==&#41;
    </code></pre>
    This is a shortcut for the following declaration (using pages style):
    <pre><code>documentation:
      summary: ...
      pages:
      - name: Overview
        content: &#40;== include overview.md ==&#41;
    </code></pre>
    Note: you cannot specify both `overview` field and `pages` field.
    """

    def __init__(self,
        *,
        summary : typing.Text = ...,
        pages : typing.Optional[typing.Iterable[global___Page]] = ...,
        rules : typing.Optional[typing.Iterable[global___DocumentationRule]] = ...,
        documentation_root_url : typing.Text = ...,
        service_root_url : typing.Text = ...,
        overview : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["documentation_root_url",b"documentation_root_url","overview",b"overview","pages",b"pages","rules",b"rules","service_root_url",b"service_root_url","summary",b"summary"]) -> None: ...
global___Documentation = Documentation

class DocumentationRule(google.protobuf.message.Message):
    """A documentation rule provides information about individual API elements."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SELECTOR_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEPRECATION_DESCRIPTION_FIELD_NUMBER: builtins.int
    selector: typing.Text = ...
    """The selector is a comma-separated list of patterns. Each pattern is a
    qualified name of the element which may end in "*", indicating a wildcard.
    Wildcards are only allowed at the end and for a whole component of the
    qualified name, i.e. "foo.*" is ok, but not "foo.b*" or "foo.*.bar". A
    wildcard will match one or more components. To specify a default for all
    applicable elements, the whole pattern "*" is used.
    """

    description: typing.Text = ...
    """Description of the selected API(s)."""

    deprecation_description: typing.Text = ...
    """Deprecation description of the selected element(s). It can be provided if
    an element is marked as `deprecated`.
    """

    def __init__(self,
        *,
        selector : typing.Text = ...,
        description : typing.Text = ...,
        deprecation_description : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deprecation_description",b"deprecation_description","description",b"description","selector",b"selector"]) -> None: ...
global___DocumentationRule = DocumentationRule

class Page(google.protobuf.message.Message):
    """Represents a documentation page. A page can contain subpages to represent
    nested documentation set structure.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    SUBPAGES_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the page. It will be used as an identity of the page to
    generate URI of the page, text of the link to this page in navigation,
    etc. The full page name (start from the root page name to this page
    concatenated with `.`) can be used as reference to the page in your
    documentation. For example:
    <pre><code>pages:
    - name: Tutorial
      content: &#40;== include tutorial.md ==&#41;
      subpages:
      - name: Java
        content: &#40;== include tutorial_java.md ==&#41;
    </code></pre>
    You can reference `Java` page using Markdown reference link syntax:
    `[Java][Tutorial.Java]`.
    """

    content: typing.Text = ...
    """The Markdown content of the page. You can use <code>&#40;== include {path}
    ==&#41;</code> to include content from a Markdown file.
    """

    @property
    def subpages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Page]:
        """Subpages of this page. The order of subpages specified here will be
        honored in the generated docset.
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        content : typing.Text = ...,
        subpages : typing.Optional[typing.Iterable[global___Page]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","name",b"name","subpages",b"subpages"]) -> None: ...
global___Page = Page

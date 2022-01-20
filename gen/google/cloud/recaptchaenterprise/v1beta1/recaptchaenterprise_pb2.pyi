"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateAssessmentRequest(google.protobuf.message.Message):
    """The create assessment request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    ASSESSMENT_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the project in which the assessment will be created,
    in the format "projects/{project_number}".
    """

    @property
    def assessment(self) -> global___Assessment:
        """Required. The assessment details."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        assessment : typing.Optional[global___Assessment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["assessment",b"assessment"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assessment",b"assessment","parent",b"parent"]) -> None: ...
global___CreateAssessmentRequest = CreateAssessmentRequest

class AnnotateAssessmentRequest(google.protobuf.message.Message):
    """The request message to annotate an Assessment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _Annotation:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AnnotationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Annotation.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ANNOTATION_UNSPECIFIED: AnnotateAssessmentRequest.Annotation.ValueType = ...  # 0
        """Default unspecified type."""

        LEGITIMATE: AnnotateAssessmentRequest.Annotation.ValueType = ...  # 1
        """Provides information that the event turned out to be legitimate."""

        FRAUDULENT: AnnotateAssessmentRequest.Annotation.ValueType = ...  # 2
        """Provides information that the event turned out to be fraudulent."""

    class Annotation(_Annotation, metaclass=_AnnotationEnumTypeWrapper):
        """Enum that reprensents the types of annotations."""
        pass

    ANNOTATION_UNSPECIFIED: AnnotateAssessmentRequest.Annotation.ValueType = ...  # 0
    """Default unspecified type."""

    LEGITIMATE: AnnotateAssessmentRequest.Annotation.ValueType = ...  # 1
    """Provides information that the event turned out to be legitimate."""

    FRAUDULENT: AnnotateAssessmentRequest.Annotation.ValueType = ...  # 2
    """Provides information that the event turned out to be fraudulent."""


    NAME_FIELD_NUMBER: builtins.int
    ANNOTATION_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The resource name of the Assessment, in the format
    "projects/{project_number}/assessments/{assessment_id}".
    """

    annotation: global___AnnotateAssessmentRequest.Annotation.ValueType = ...
    """Required. The annotation that will be assigned to the Event."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        annotation : global___AnnotateAssessmentRequest.Annotation.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["annotation",b"annotation","name",b"name"]) -> None: ...
global___AnnotateAssessmentRequest = AnnotateAssessmentRequest

class AnnotateAssessmentResponse(google.protobuf.message.Message):
    """Empty response for AnnotateAssessment."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___AnnotateAssessmentResponse = AnnotateAssessmentResponse

class Assessment(google.protobuf.message.Message):
    """A recaptcha assessment resource."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ClassificationReason:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ClassificationReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ClassificationReason.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CLASSIFICATION_REASON_UNSPECIFIED: Assessment.ClassificationReason.ValueType = ...  # 0
        """Default unspecified type."""

        AUTOMATION: Assessment.ClassificationReason.ValueType = ...  # 1
        """Interactions matched the behavior of an automated agent."""

        UNEXPECTED_ENVIRONMENT: Assessment.ClassificationReason.ValueType = ...  # 2
        """The event originated from an illegitimate environment."""

        TOO_MUCH_TRAFFIC: Assessment.ClassificationReason.ValueType = ...  # 3
        """Traffic volume from the event source is higher than normal."""

        UNEXPECTED_USAGE_PATTERNS: Assessment.ClassificationReason.ValueType = ...  # 4
        """Interactions with the site were significantly different than expected
        patterns.
        """

        LOW_CONFIDENCE_SCORE: Assessment.ClassificationReason.ValueType = ...  # 5
        """Too little traffic has been received from this site thus far to generate
        quality risk analysis.
        """

    class ClassificationReason(_ClassificationReason, metaclass=_ClassificationReasonEnumTypeWrapper):
        """LINT.IfChange(classification_reason)
        Reasons contributing to the risk analysis verdict.
        """
        pass

    CLASSIFICATION_REASON_UNSPECIFIED: Assessment.ClassificationReason.ValueType = ...  # 0
    """Default unspecified type."""

    AUTOMATION: Assessment.ClassificationReason.ValueType = ...  # 1
    """Interactions matched the behavior of an automated agent."""

    UNEXPECTED_ENVIRONMENT: Assessment.ClassificationReason.ValueType = ...  # 2
    """The event originated from an illegitimate environment."""

    TOO_MUCH_TRAFFIC: Assessment.ClassificationReason.ValueType = ...  # 3
    """Traffic volume from the event source is higher than normal."""

    UNEXPECTED_USAGE_PATTERNS: Assessment.ClassificationReason.ValueType = ...  # 4
    """Interactions with the site were significantly different than expected
    patterns.
    """

    LOW_CONFIDENCE_SCORE: Assessment.ClassificationReason.ValueType = ...  # 5
    """Too little traffic has been received from this site thus far to generate
    quality risk analysis.
    """


    NAME_FIELD_NUMBER: builtins.int
    EVENT_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    TOKEN_PROPERTIES_FIELD_NUMBER: builtins.int
    REASONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name for the Assessment in the format
    "projects/{project_number}/assessments/{assessment_id}".
    """

    @property
    def event(self) -> global___Event:
        """The event being assessed."""
        pass
    score: builtins.float = ...
    """Output only. Legitimate event score from 0.0 to 1.0.
    (1.0 means very likely legitimate traffic while 0.0 means very likely
    non-legitimate traffic).
    """

    @property
    def token_properties(self) -> global___TokenProperties:
        """Output only. Properties of the provided event token."""
        pass
    @property
    def reasons(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Assessment.ClassificationReason.ValueType]:
        """Output only. Reasons contributing to the risk analysis verdict."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        event : typing.Optional[global___Event] = ...,
        score : builtins.float = ...,
        token_properties : typing.Optional[global___TokenProperties] = ...,
        reasons : typing.Optional[typing.Iterable[global___Assessment.ClassificationReason.ValueType]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["event",b"event","token_properties",b"token_properties"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["event",b"event","name",b"name","reasons",b"reasons","score",b"score","token_properties",b"token_properties"]) -> None: ...
global___Assessment = Assessment

class Event(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOKEN_FIELD_NUMBER: builtins.int
    SITE_KEY_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    USER_IP_ADDRESS_FIELD_NUMBER: builtins.int
    EXPECTED_ACTION_FIELD_NUMBER: builtins.int
    token: typing.Text = ...
    """Optional. The user response token provided by the reCAPTCHA client-side integration
    on your site.
    """

    site_key: typing.Text = ...
    """Optional. The site key that was used to invoke reCAPTCHA on your site and generate
    the token.
    """

    user_agent: typing.Text = ...
    """Optional. The user agent present in the request from the user's device related to
    this event.
    """

    user_ip_address: typing.Text = ...
    """Optional. The IP address in the request from the user's device related to this event."""

    expected_action: typing.Text = ...
    """Optional. The expected action for this type of event. This should be the same action
    provided at token generation time on client-side platforms already
    integrated with recaptcha enterprise.
    """

    def __init__(self,
        *,
        token : typing.Text = ...,
        site_key : typing.Text = ...,
        user_agent : typing.Text = ...,
        user_ip_address : typing.Text = ...,
        expected_action : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expected_action",b"expected_action","site_key",b"site_key","token",b"token","user_agent",b"user_agent","user_ip_address",b"user_ip_address"]) -> None: ...
global___Event = Event

class TokenProperties(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _InvalidReason:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _InvalidReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_InvalidReason.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INVALID_REASON_UNSPECIFIED: TokenProperties.InvalidReason.ValueType = ...  # 0
        """Default unspecified type."""

        UNKNOWN_INVALID_REASON: TokenProperties.InvalidReason.ValueType = ...  # 1
        """If the failure reason was not accounted for."""

        MALFORMED: TokenProperties.InvalidReason.ValueType = ...  # 2
        """The provided user verification token was malformed."""

        EXPIRED: TokenProperties.InvalidReason.ValueType = ...  # 3
        """The user verification token had expired."""

        DUPE: TokenProperties.InvalidReason.ValueType = ...  # 4
        """The user verification had already been seen."""

        SITE_MISMATCH: TokenProperties.InvalidReason.ValueType = ...  # 5
        """The user verification token did not match the provided site key.
        This may be a configuration error (e.g. development keys used in
        production) or end users trying to use verification tokens from other
        sites.
        """

        MISSING: TokenProperties.InvalidReason.ValueType = ...  # 6
        """The user verification token was not present.  It is a required input."""

    class InvalidReason(_InvalidReason, metaclass=_InvalidReasonEnumTypeWrapper):
        """LINT.IfChange
        Enum that represents the types of invalid token reasons.
        """
        pass

    INVALID_REASON_UNSPECIFIED: TokenProperties.InvalidReason.ValueType = ...  # 0
    """Default unspecified type."""

    UNKNOWN_INVALID_REASON: TokenProperties.InvalidReason.ValueType = ...  # 1
    """If the failure reason was not accounted for."""

    MALFORMED: TokenProperties.InvalidReason.ValueType = ...  # 2
    """The provided user verification token was malformed."""

    EXPIRED: TokenProperties.InvalidReason.ValueType = ...  # 3
    """The user verification token had expired."""

    DUPE: TokenProperties.InvalidReason.ValueType = ...  # 4
    """The user verification had already been seen."""

    SITE_MISMATCH: TokenProperties.InvalidReason.ValueType = ...  # 5
    """The user verification token did not match the provided site key.
    This may be a configuration error (e.g. development keys used in
    production) or end users trying to use verification tokens from other
    sites.
    """

    MISSING: TokenProperties.InvalidReason.ValueType = ...  # 6
    """The user verification token was not present.  It is a required input."""


    VALID_FIELD_NUMBER: builtins.int
    INVALID_REASON_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    HOSTNAME_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    valid: builtins.bool = ...
    """Whether the provided user response token is valid."""

    invalid_reason: global___TokenProperties.InvalidReason.ValueType = ...
    """Reason associated with the response when valid = false."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp corresponding to the generation of the token."""
        pass
    hostname: typing.Text = ...
    """The hostname of the page on which the token was generated."""

    action: typing.Text = ...
    """Action name provided at token generation."""

    def __init__(self,
        *,
        valid : builtins.bool = ...,
        invalid_reason : global___TokenProperties.InvalidReason.ValueType = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        hostname : typing.Text = ...,
        action : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action","create_time",b"create_time","hostname",b"hostname","invalid_reason",b"invalid_reason","valid",b"valid"]) -> None: ...
global___TokenProperties = TokenProperties

class CreateKeyRequest(google.protobuf.message.Message):
    """The create key request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the project in which the key will be created, in the
    format "projects/{project_number}".
    """

    @property
    def key(self) -> global___Key:
        """Required. Information to create a reCAPTCHA Enterprise key."""
        pass
    def __init__(self,
        *,
        parent : typing.Text = ...,
        key : typing.Optional[global___Key] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["key",b"key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","parent",b"parent"]) -> None: ...
global___CreateKeyRequest = CreateKeyRequest

class ListKeysRequest(google.protobuf.message.Message):
    """The list keys request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARENT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    parent: typing.Text = ...
    """Required. The name of the project that contains the keys that will be
    listed, in the format "projects/{project_number}".
    """

    page_size: builtins.int = ...
    """Optional. The maximum number of keys to return. Default is 10. Max limit is
    1000.
    """

    page_token: typing.Text = ...
    """Optional. The next_page_token value returned from a previous.
    ListKeysRequest, if any.
    """

    def __init__(self,
        *,
        parent : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","parent",b"parent"]) -> None: ...
global___ListKeysRequest = ListKeysRequest

class ListKeysResponse(google.protobuf.message.Message):
    """Response to request to list keys in a project."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEYS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def keys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Key]:
        """Key details."""
        pass
    next_page_token: typing.Text = ...
    """Token to retrieve the next page of results. It is set to empty if no keys
    remain in results.
    """

    def __init__(self,
        *,
        keys : typing.Optional[typing.Iterable[global___Key]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keys",b"keys","next_page_token",b"next_page_token"]) -> None: ...
global___ListKeysResponse = ListKeysResponse

class GetKeyRequest(google.protobuf.message.Message):
    """The get key request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the requested key, in the format
    "projects/{project_number}/keys/{key_id}".
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___GetKeyRequest = GetKeyRequest

class UpdateKeyRequest(google.protobuf.message.Message):
    """The update key request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___Key:
        """Required. The key to update."""
        pass
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Optional. The mask to control which field of the key get updated. If the mask is not
        present, all fields will be updated.
        """
        pass
    def __init__(self,
        *,
        key : typing.Optional[global___Key] = ...,
        update_mask : typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["key",b"key","update_mask",b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","update_mask",b"update_mask"]) -> None: ...
global___UpdateKeyRequest = UpdateKeyRequest

class DeleteKeyRequest(google.protobuf.message.Message):
    """The delete key request message."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Required. The name of the key to be deleted, in the format
    "projects/{project_number}/keys/{key_id}".
    """

    def __init__(self,
        *,
        name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___DeleteKeyRequest = DeleteKeyRequest

class Key(google.protobuf.message.Message):
    """A key used to identify and configure applications (web and/or mobile) that
    use reCAPTCHA Enterprise.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    WEB_SETTINGS_FIELD_NUMBER: builtins.int
    ANDROID_SETTINGS_FIELD_NUMBER: builtins.int
    IOS_SETTINGS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The resource name for the Key in the format
    "projects/{project_number}/keys/{key_id}".
    """

    display_name: typing.Text = ...
    """Human-readable display name of this key. Modifiable by user."""

    @property
    def web_settings(self) -> global___WebKeySettings:
        """Settings for keys that can be used by websites."""
        pass
    @property
    def android_settings(self) -> global___AndroidKeySettings:
        """Settings for keys that can be used by Android apps."""
        pass
    @property
    def ios_settings(self) -> global___IOSKeySettings:
        """Settings for keys that can be used by iOS apps."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        web_settings : typing.Optional[global___WebKeySettings] = ...,
        android_settings : typing.Optional[global___AndroidKeySettings] = ...,
        ios_settings : typing.Optional[global___IOSKeySettings] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["android_settings",b"android_settings","ios_settings",b"ios_settings","platform_settings",b"platform_settings","web_settings",b"web_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["android_settings",b"android_settings","display_name",b"display_name","ios_settings",b"ios_settings","name",b"name","platform_settings",b"platform_settings","web_settings",b"web_settings"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["platform_settings",b"platform_settings"]) -> typing.Optional[typing_extensions.Literal["web_settings","android_settings","ios_settings"]]: ...
global___Key = Key

class WebKeySettings(google.protobuf.message.Message):
    """Settings specific to keys that can be used by websites."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _IntegrationType:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _IntegrationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IntegrationType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INTEGRATION_TYPE_UNSPECIFIED: WebKeySettings.IntegrationType.ValueType = ...  # 0
        """Default type that indicates this enum hasn't been specified. This is not
        a valid IntegrationType, one of the other types must be specified
        instead.
        """

        SCORE_ONLY: WebKeySettings.IntegrationType.ValueType = ...  # 1
        """Only used to produce scores. It doesn't display the "I'm not a robot"
        checkbox and never shows captcha challenges.
        """

        CHECKBOX_CHALLENGE: WebKeySettings.IntegrationType.ValueType = ...  # 2
        """Displays the "I'm not a robot" checkbox and may show captcha challenges
        after it is checked.
        """

        INVISIBLE_CHALLENGE: WebKeySettings.IntegrationType.ValueType = ...  # 3
        """Doesn't display the "I'm not a robot" checkbox, but may show captcha
        challenges after risk analysis.
        """

    class IntegrationType(_IntegrationType, metaclass=_IntegrationTypeEnumTypeWrapper):
        """Enum that represents the integration types for web keys."""
        pass

    INTEGRATION_TYPE_UNSPECIFIED: WebKeySettings.IntegrationType.ValueType = ...  # 0
    """Default type that indicates this enum hasn't been specified. This is not
    a valid IntegrationType, one of the other types must be specified
    instead.
    """

    SCORE_ONLY: WebKeySettings.IntegrationType.ValueType = ...  # 1
    """Only used to produce scores. It doesn't display the "I'm not a robot"
    checkbox and never shows captcha challenges.
    """

    CHECKBOX_CHALLENGE: WebKeySettings.IntegrationType.ValueType = ...  # 2
    """Displays the "I'm not a robot" checkbox and may show captcha challenges
    after it is checked.
    """

    INVISIBLE_CHALLENGE: WebKeySettings.IntegrationType.ValueType = ...  # 3
    """Doesn't display the "I'm not a robot" checkbox, but may show captcha
    challenges after risk analysis.
    """


    class _ChallengeSecurityPreference:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _ChallengeSecurityPreferenceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ChallengeSecurityPreference.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 0
        """Default type that indicates this enum hasn't been specified."""

        USABILITY: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 1
        """Key tends to show fewer and easier challenges."""

        BALANCED: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 2
        """Key tends to show balanced (in amount and difficulty) challenges."""

        SECURITY: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 3
        """Key tends to show more and harder challenges."""

    class ChallengeSecurityPreference(_ChallengeSecurityPreference, metaclass=_ChallengeSecurityPreferenceEnumTypeWrapper):
        """Enum that represents the possible challenge frequency and difficulty
        configurations for a web key.
        """
        pass

    CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 0
    """Default type that indicates this enum hasn't been specified."""

    USABILITY: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 1
    """Key tends to show fewer and easier challenges."""

    BALANCED: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 2
    """Key tends to show balanced (in amount and difficulty) challenges."""

    SECURITY: WebKeySettings.ChallengeSecurityPreference.ValueType = ...  # 3
    """Key tends to show more and harder challenges."""


    ENFORCE_ALLOWED_DOMAINS_FIELD_NUMBER: builtins.int
    ALLOWED_DOMAINS_FIELD_NUMBER: builtins.int
    ALLOW_AMP_TRAFFIC_FIELD_NUMBER: builtins.int
    INTEGRATION_TYPE_FIELD_NUMBER: builtins.int
    CHALLENGE_SECURITY_PREFERENCE_FIELD_NUMBER: builtins.int
    enforce_allowed_domains: builtins.bool = ...
    """Whether allowed_domains is enforced or not."""

    @property
    def allowed_domains(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Domains or subdomains of websites allowed to use the key. All subdomains
        of an allowed domain are automatically allowed. A valid domain requires a
        host and must not include any path, port, query or fragment.
        Examples: 'example.com' or 'subdomain.example.com'
        """
        pass
    allow_amp_traffic: builtins.bool = ...
    """Whether this key can be used on AMP (Accelerated Mobile Pages) websites."""

    integration_type: global___WebKeySettings.IntegrationType.ValueType = ...
    """Required. Describes how this key is integrated with the website."""

    challenge_security_preference: global___WebKeySettings.ChallengeSecurityPreference.ValueType = ...
    """Settings for the frequency and difficulty at which this key triggers
    captcha challenges. This should only be specified for IntegrationTypes
    CHECKBOX_CHALLENGE and INVISIBLE_CHALLENGE.
    """

    def __init__(self,
        *,
        enforce_allowed_domains : builtins.bool = ...,
        allowed_domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        allow_amp_traffic : builtins.bool = ...,
        integration_type : global___WebKeySettings.IntegrationType.ValueType = ...,
        challenge_security_preference : global___WebKeySettings.ChallengeSecurityPreference.ValueType = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_amp_traffic",b"allow_amp_traffic","allowed_domains",b"allowed_domains","challenge_security_preference",b"challenge_security_preference","enforce_allowed_domains",b"enforce_allowed_domains","integration_type",b"integration_type"]) -> None: ...
global___WebKeySettings = WebKeySettings

class AndroidKeySettings(google.protobuf.message.Message):
    """Settings specific to keys that can be used by Android apps."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ALLOWED_PACKAGE_NAMES_FIELD_NUMBER: builtins.int
    @property
    def allowed_package_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Android package names of apps allowed to use the key.
        Example: 'com.companyname.appname'
        """
        pass
    def __init__(self,
        *,
        allowed_package_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowed_package_names",b"allowed_package_names"]) -> None: ...
global___AndroidKeySettings = AndroidKeySettings

class IOSKeySettings(google.protobuf.message.Message):
    """Settings specific to keys that can be used by iOS apps."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ALLOWED_BUNDLE_IDS_FIELD_NUMBER: builtins.int
    @property
    def allowed_bundle_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """iOS bundle ids of apps allowed to use the key.
        Example: 'com.companyname.productname.appname'
        """
        pass
    def __init__(self,
        *,
        allowed_bundle_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowed_bundle_ids",b"allowed_bundle_ids"]) -> None: ...
global___IOSKeySettings = IOSKeySettings

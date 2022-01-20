"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.longrunning.operations_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SearchCatalogsRequest(google.protobuf.message.Message):
    """Request message for [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    resource: typing.Text = ...
    """Required. The name of the resource context. It can be in following formats:

    * `projects/{project}`
    * `folders/{folder}`
    * `organizations/{organization}`
    """

    query: typing.Text = ...
    """The query to filter the catalogs. The supported queries are:

    * Get a single catalog: `name=catalogs/{catalog}`
    """

    page_size: builtins.int = ...
    """The maximum number of entries that are requested."""

    page_token: typing.Text = ...
    """A pagination token returned from a previous call to SearchCatalogs that
    indicates where this listing should continue from.
    """

    def __init__(self,
        *,
        resource : typing.Text = ...,
        query : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","query",b"query","resource",b"resource"]) -> None: ...
global___SearchCatalogsRequest = SearchCatalogsRequest

class SearchCatalogsResponse(google.protobuf.message.Message):
    """Response message for [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CATALOGS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def catalogs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Catalog]:
        """The `Catalog`s computed from the resource context."""
        pass
    next_page_token: typing.Text = ...
    """A pagination token returned from a previous call to SearchCatalogs that
    indicates from where listing should continue.
    """

    def __init__(self,
        *,
        catalogs : typing.Optional[typing.Iterable[global___Catalog]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalogs",b"catalogs","next_page_token",b"next_page_token"]) -> None: ...
global___SearchCatalogsResponse = SearchCatalogsResponse

class SearchProductsRequest(google.protobuf.message.Message):
    """Request message for [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    resource: typing.Text = ...
    """Required. The name of the resource context. See [SearchCatalogsRequest.resource][google.cloud.privatecatalog.v1beta1.SearchCatalogsRequest.resource]
    for details.
    """

    query: typing.Text = ...
    """The query to filter the products.

    The supported queries are:
    * List products of all catalogs: empty
    * List products under a catalog: `parent=catalogs/{catalog}`
    * Get a product by name:
    `name=catalogs/{catalog}/products/{product}`
    """

    page_size: builtins.int = ...
    """The maximum number of entries that are requested."""

    page_token: typing.Text = ...
    """A pagination token returned from a previous call to SearchProducts that
    indicates where this listing should continue from.
    """

    def __init__(self,
        *,
        resource : typing.Text = ...,
        query : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","query",b"query","resource",b"resource"]) -> None: ...
global___SearchProductsRequest = SearchProductsRequest

class SearchProductsResponse(google.protobuf.message.Message):
    """Response message for [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PRODUCTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def products(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Product]:
        """The `Product` resources computed from the resource context."""
        pass
    next_page_token: typing.Text = ...
    """A pagination token returned from a previous call to SearchProducts that
    indicates from where listing should continue.
    """

    def __init__(self,
        *,
        products : typing.Optional[typing.Iterable[global___Product]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","products",b"products"]) -> None: ...
global___SearchProductsResponse = SearchProductsResponse

class SearchVersionsRequest(google.protobuf.message.Message):
    """Request message for [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    resource: typing.Text = ...
    """Required. The name of the resource context. See [SearchCatalogsRequest.resource][google.cloud.privatecatalog.v1beta1.SearchCatalogsRequest.resource]
    for details.
    """

    query: typing.Text = ...
    """Required. The query to filter the versions.

    The supported queries are:
    * List versions under a product:
    `parent=catalogs/{catalog}/products/{product}`
    * Get a version by name:
    `name=catalogs/{catalog}/products/{product}/versions/{version}`
    """

    page_size: builtins.int = ...
    """The maximum number of entries that are requested."""

    page_token: typing.Text = ...
    """A pagination token returned from a previous call to SearchVersions
    that indicates where this listing should continue from.
    """

    def __init__(self,
        *,
        resource : typing.Text = ...,
        query : typing.Text = ...,
        page_size : builtins.int = ...,
        page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token","query",b"query","resource",b"resource"]) -> None: ...
global___SearchVersionsRequest = SearchVersionsRequest

class SearchVersionsResponse(google.protobuf.message.Message):
    """Response message for [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def versions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Version]:
        """The `Version` resources computed from the resource context."""
        pass
    next_page_token: typing.Text = ...
    """A pagination token returned from a previous call to SearchVersions that
    indicates from where the listing should continue.
    """

    def __init__(self,
        *,
        versions : typing.Optional[typing.Iterable[global___Version]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","versions",b"versions"]) -> None: ...
global___SearchVersionsResponse = SearchVersionsResponse

class Catalog(google.protobuf.message.Message):
    """The readonly representation of a catalog computed with a given resource
    context.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the target catalog, in the format of
    `catalogs/{catalog}'.
    """

    display_name: typing.Text = ...
    """Output only. The descriptive name of the catalog as it appears in UIs."""

    description: typing.Text = ...
    """Output only. The description of the catalog."""

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the catalog was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the catalog was last updated."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        display_name : typing.Text = ...,
        description : typing.Text = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["create_time",b"create_time","description",b"description","display_name",b"display_name","name",b"name","update_time",b"update_time"]) -> None: ...
global___Catalog = Catalog

class Product(google.protobuf.message.Message):
    """The readonly representation of a product computed with a given resource
    context.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    ASSET_TYPE_FIELD_NUMBER: builtins.int
    DISPLAY_METADATA_FIELD_NUMBER: builtins.int
    ICON_URI_FIELD_NUMBER: builtins.int
    ASSET_REFERENCES_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the target product, in the format of
    `products/[a-z][-a-z0-9]*[a-z0-9]'.

    A unique identifier for the product under a catalog.
    """

    asset_type: typing.Text = ...
    """Output only. The type of the product asset. It can be one of the following values:

    * `google.deploymentmanager.Template`
    * `google.cloudprivatecatalog.ListingOnly`
    * `google.cloudprivatecatalog.Terraform`
    """

    @property
    def display_metadata(self) -> google.protobuf.struct_pb2.Struct:
        """Required. Output only. The display metadata to describe the product. The JSON schema of the
        metadata differs by [Product.asset_type][google.cloud.privatecatalog.v1beta1.Product.asset_type].
        When the type is `google.deploymentmanager.Template`, the schema is as
        follows:

        ```
        "$schema": http://json-schema.org/draft-04/schema#
        type: object
        properties:
          name:
            type: string
            minLength: 1
            maxLength: 64
          description:
            type: string
            minLength: 1
            maxLength: 2048
          tagline:
            type: string
            minLength: 1
            maxLength: 100
          support_info:
            type: string
            minLength: 1
            maxLength: 2048
          creator:
            type: string
            minLength: 1
            maxLength: 100
          documentations:
            type: array
            items:
              type: object
              properties:
                url:
                  type: string
                  pattern:
                  "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
                title:
                  type: string
                  minLength: 1
                  maxLength: 64
                description:
                  type: string
                  minLength: 1
                  maxLength: 2048
        required:
        - name
        - description
        additionalProperties: false

        ```

        When the asset type is `google.cloudprivatecatalog.ListingOnly`, the schema
        is as follows:

        ```
        "$schema": http://json-schema.org/draft-04/schema#
        type: object
        properties:
          name:
            type: string
            minLength: 1
            maxLength: 64
          description:
            type: string
            minLength: 1
            maxLength: 2048
          tagline:
            type: string
            minLength: 1
            maxLength: 100
          support_info:
            type: string
            minLength: 1
            maxLength: 2048
          creator:
            type: string
            minLength: 1
            maxLength: 100
          documentations:
            type: array
            items:
              type: object
              properties:
                url:
                  type: string
                  pattern:
                  "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
                title:
                  type: string
                  minLength: 1
                  maxLength: 64
                description:
                  type: string
                  minLength: 1
                  maxLength: 2048
          signup_url:
            type: string
            pattern:
            "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
        required:
        - name
        - description
        - signup_url
        additionalProperties: false

        ```

        When the asset type is `google.cloudprivatecatalog.Terraform`, the schema
        is as follows:

        ```
        "$schema": http://json-schema.org/draft-04/schema#
        type: object
        properties:
          name:
            type: string
            minLength: 1
            maxLength: 64
          description:
            type: string
            minLength: 1
            maxLength: 2048
          tagline:
            type: string
            minLength: 1
            maxLength: 100
          support_info:
            type: string
            minLength: 1
            maxLength: 2048
          creator:
            type: string
            minLength: 1
            maxLength: 100
          documentations:
            type: array
            items:
              type: object
              properties:
                url:
                  type: string
                  pattern:
                  "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
                title:
                  type: string
                  minLength: 1
                  maxLength: 64
                description:
                  type: string
                  minLength: 1
                  maxLength: 2048
        required:
        - name
        - description
        additionalProperties: true
        """
        pass
    icon_uri: typing.Text = ...
    """Output only. The icon URI of the product."""

    @property
    def asset_references(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___AssetReference]:
        """Output only. A collection of assets referred by a product.
        This field is set for Terraform Products only.
        """
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the product was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the product was last updated."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        asset_type : typing.Text = ...,
        display_metadata : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        icon_uri : typing.Text = ...,
        asset_references : typing.Optional[typing.Iterable[global___AssetReference]] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time",b"create_time","display_metadata",b"display_metadata","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_references",b"asset_references","asset_type",b"asset_type","create_time",b"create_time","display_metadata",b"display_metadata","icon_uri",b"icon_uri","name",b"name","update_time",b"update_time"]) -> None: ...
global___Product = Product

class AssetReference(google.protobuf.message.Message):
    """Defines the reference of an asset belonging to a product."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AssetValidationState:
        ValueType = typing.NewType('ValueType', builtins.int)
        V: typing_extensions.TypeAlias = ValueType
    class _AssetValidationStateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AssetValidationState.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        ASSET_VALIDATION_STATE_UNSPECIFIED: AssetReference.AssetValidationState.ValueType = ...  # 0
        """Unknown state."""

        PENDING: AssetReference.AssetValidationState.ValueType = ...  # 1
        """The validation is still in process."""

        VALID: AssetReference.AssetValidationState.ValueType = ...  # 2
        """The validation is done and the asset reference is valid."""

        INVALID: AssetReference.AssetValidationState.ValueType = ...  # 3
        """The validation is done and the asset reference is invalid."""

    class AssetValidationState(_AssetValidationState, metaclass=_AssetValidationStateEnumTypeWrapper):
        """Possible validation steates of an asset reference."""
        pass

    ASSET_VALIDATION_STATE_UNSPECIFIED: AssetReference.AssetValidationState.ValueType = ...  # 0
    """Unknown state."""

    PENDING: AssetReference.AssetValidationState.ValueType = ...  # 1
    """The validation is still in process."""

    VALID: AssetReference.AssetValidationState.ValueType = ...  # 2
    """The validation is done and the asset reference is valid."""

    INVALID: AssetReference.AssetValidationState.ValueType = ...  # 3
    """The validation is done and the asset reference is invalid."""


    ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    VALIDATION_STATUS_FIELD_NUMBER: builtins.int
    VALIDATION_OPERATION_FIELD_NUMBER: builtins.int
    ASSET_FIELD_NUMBER: builtins.int
    GCS_PATH_FIELD_NUMBER: builtins.int
    GIT_SOURCE_FIELD_NUMBER: builtins.int
    GCS_SOURCE_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    """Output only. A unique identifier among asset references in a product."""

    description: typing.Text = ...
    """Output only. The human-readable description of the referenced asset. Maximum 256
    characters in length.
    """

    @property
    def inputs(self) -> global___Inputs:
        """Output only. The definition of input parameters to hydrate the asset template."""
        pass
    validation_status: global___AssetReference.AssetValidationState.ValueType = ...
    """Output only. The current state of the asset reference."""

    @property
    def validation_operation(self) -> google.longrunning.operations_pb2.Operation:
        """Output only. The validation process metadata."""
        pass
    asset: typing.Text = ...
    """Output only. The asset resource name if an asset is hosted by Private Catalog."""

    gcs_path: typing.Text = ...
    """Output only. The cloud storage object path."""

    @property
    def git_source(self) -> global___GitSource:
        """Output only. The git source."""
        pass
    @property
    def gcs_source(self) -> global___GcsSource:
        """Output only. The cloud storage source."""
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The creation timestamp of the asset reference."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The last update timestamp of the asset reference."""
        pass
    version: typing.Text = ...
    """The version of the source used for this asset reference."""

    def __init__(self,
        *,
        id : typing.Text = ...,
        description : typing.Text = ...,
        inputs : typing.Optional[global___Inputs] = ...,
        validation_status : global___AssetReference.AssetValidationState.ValueType = ...,
        validation_operation : typing.Optional[google.longrunning.operations_pb2.Operation] = ...,
        asset : typing.Text = ...,
        gcs_path : typing.Text = ...,
        git_source : typing.Optional[global___GitSource] = ...,
        gcs_source : typing.Optional[global___GcsSource] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        version : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asset",b"asset","create_time",b"create_time","gcs_path",b"gcs_path","gcs_source",b"gcs_source","git_source",b"git_source","inputs",b"inputs","source",b"source","update_time",b"update_time","validation_operation",b"validation_operation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset",b"asset","create_time",b"create_time","description",b"description","gcs_path",b"gcs_path","gcs_source",b"gcs_source","git_source",b"git_source","id",b"id","inputs",b"inputs","source",b"source","update_time",b"update_time","validation_operation",b"validation_operation","validation_status",b"validation_status","version",b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["source",b"source"]) -> typing.Optional[typing_extensions.Literal["asset","gcs_path","git_source"]]: ...
global___AssetReference = AssetReference

class Inputs(google.protobuf.message.Message):
    """Defines definition of input parameters of asset templates."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMETERS_FIELD_NUMBER: builtins.int
    @property
    def parameters(self) -> google.protobuf.struct_pb2.Struct:
        """Output only. The JSON schema defining the inputs and their formats."""
        pass
    def __init__(self,
        *,
        parameters : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parameters",b"parameters"]) -> None: ...
global___Inputs = Inputs

class GcsSource(google.protobuf.message.Message):
    """Defines how to access Cloud Storage source."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GCS_PATH_FIELD_NUMBER: builtins.int
    GENERATION_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    gcs_path: typing.Text = ...
    """Output only. the cloud storage object path."""

    generation: builtins.int = ...
    """Output only. Generation of the object, which is set when the content of an object starts
    being written.
    """

    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the object metadata was last changed."""
        pass
    def __init__(self,
        *,
        gcs_path : typing.Text = ...,
        generation : builtins.int = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gcs_path",b"gcs_path","generation",b"generation","update_time",b"update_time"]) -> None: ...
global___GcsSource = GcsSource

class GitSource(google.protobuf.message.Message):
    """Defines how to access a Git Source."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REPO_FIELD_NUMBER: builtins.int
    DIR_FIELD_NUMBER: builtins.int
    COMMIT_FIELD_NUMBER: builtins.int
    BRANCH_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    repo: typing.Text = ...
    """Location of the Git repo to build."""

    dir: typing.Text = ...
    """Directory, relative to the source root, in which to run the build.

    This must be a relative path. If a step's `dir` is specified and is an
    absolute path, this value is ignored for that step's execution.
    """

    commit: typing.Text = ...
    """The revision commit to use."""

    branch: typing.Text = ...
    """The revision branch to use."""

    tag: typing.Text = ...
    """The revision tag to use."""

    def __init__(self,
        *,
        repo : typing.Text = ...,
        dir : typing.Text = ...,
        commit : typing.Text = ...,
        branch : typing.Text = ...,
        tag : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["branch",b"branch","commit",b"commit","ref",b"ref","tag",b"tag"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["branch",b"branch","commit",b"commit","dir",b"dir","ref",b"ref","repo",b"repo","tag",b"tag"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["ref",b"ref"]) -> typing.Optional[typing_extensions.Literal["commit","branch","tag"]]: ...
global___GitSource = GitSource

class Version(google.protobuf.message.Message):
    """The consumer representation of a version which is a child resource under a
    `Product` with asset data.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ASSET_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Output only. The resource name of the version, in the format
    `catalogs/{catalog}/products/{product}/versions/[a-z][-a-z0-9]*[a-z0-9]'.

    A unique identifier for the version under a product.
    """

    description: typing.Text = ...
    """Output only. The user-supplied description of the version. Maximum of 256
    characters.
    """

    @property
    def asset(self) -> google.protobuf.struct_pb2.Struct:
        """Output only. The asset which has been validated and is ready to be
        provisioned. See
        [google.cloud.privatecatalogproducer.v1beta.Version.asset][] for details.
        """
        pass
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the version was created."""
        pass
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The time when the version was last updated."""
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        description : typing.Text = ...,
        asset : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        create_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        update_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asset",b"asset","create_time",b"create_time","update_time",b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset",b"asset","create_time",b"create_time","description",b"description","name",b"name","update_time",b"update_time"]) -> None: ...
global___Version = Version

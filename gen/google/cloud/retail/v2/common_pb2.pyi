"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Audience(google.protobuf.message.Message):
    """An intended audience of the [Product][google.cloud.retail.v2.Product] for
    whom it's sold.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GENDERS_FIELD_NUMBER: builtins.int
    AGE_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def genders(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The genders of the audience. Strongly encouraged to use the standard
        values: "male", "female", "unisex".

        At most 5 values are allowed. Each value must be a UTF-8 encoded string
        with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error
        is returned.

        Google Merchant Center property
        [gender](https://support.google.com/merchants/answer/6324479). Schema.org
        property
        [Product.audience.suggestedGender](https://schema.org/suggestedGender).
        """
        pass
    @property
    def age_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The age groups of the audience. Strongly encouraged to use the standard
        values: "newborn" (up to 3 months old), "infant" (3–12 months old),
        "toddler" (1–5 years old), "kids" (5–13 years old), "adult" (typically
        teens or older).

        At most 5 values are allowed. Each value must be a UTF-8 encoded string
        with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error
        is returned.

        Google Merchant Center property
        [age_group](https://support.google.com/merchants/answer/6324463).
        Schema.org property
        [Product.audience.suggestedMinAge](https://schema.org/suggestedMinAge) and
        [Product.audience.suggestedMaxAge](https://schema.org/suggestedMaxAge).
        """
        pass
    def __init__(self,
        *,
        genders : typing.Optional[typing.Iterable[typing.Text]] = ...,
        age_groups : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["age_groups",b"age_groups","genders",b"genders"]) -> None: ...
global___Audience = Audience

class ColorInfo(google.protobuf.message.Message):
    """The color information of a [Product][google.cloud.retail.v2.Product]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COLOR_FAMILIES_FIELD_NUMBER: builtins.int
    COLORS_FIELD_NUMBER: builtins.int
    @property
    def color_families(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The standard color families. Strongly recommended to use the following
        standard color groups: "Red", "Pink", "Orange", "Yellow", "Purple",
        "Green", "Cyan", "Blue", "Brown", "White", "Gray", "Black" and
        "Mixed". Normally it is expected to have only 1 color family. May consider
        using single "Mixed" instead of multiple values.

        A maximum of 5 values are allowed. Each value must be a UTF-8 encoded
        string with a length limit of 128 characters. Otherwise, an
        INVALID_ARGUMENT error is returned.

        Google Merchant Center property
        [color](https://support.google.com/merchants/answer/6324487). Schema.org
        property [Product.color](https://schema.org/color).
        """
        pass
    @property
    def colors(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The color display names, which may be different from standard color family
        names, such as the color aliases used in the website frontend. Normally
        it is expected to have only 1 color. May consider using single "Mixed"
        instead of multiple values.

        A maximum of 25 colors are allowed. Each value must be a UTF-8 encoded
        string with a length limit of 128 characters. Otherwise, an
        INVALID_ARGUMENT error is returned.

        Google Merchant Center property
        [color](https://support.google.com/merchants/answer/6324487). Schema.org
        property [Product.color](https://schema.org/color).
        """
        pass
    def __init__(self,
        *,
        color_families : typing.Optional[typing.Iterable[typing.Text]] = ...,
        colors : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["color_families",b"color_families","colors",b"colors"]) -> None: ...
global___ColorInfo = ColorInfo

class CustomAttribute(google.protobuf.message.Message):
    """A custom attribute that is not explicitly modeled in
    [Product][google.cloud.retail.v2.Product].
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TEXT_FIELD_NUMBER: builtins.int
    NUMBERS_FIELD_NUMBER: builtins.int
    SEARCHABLE_FIELD_NUMBER: builtins.int
    INDEXABLE_FIELD_NUMBER: builtins.int
    @property
    def text(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The textual values of this custom attribute. For example, `["yellow",
        "green"]` when the key is "color".

        At most 400 values are allowed. Empty values are not allowed. Each value
        must be a UTF-8 encoded string with a length limit of 256 characters.
        Otherwise, an INVALID_ARGUMENT error is returned.

        Exactly one of [text][google.cloud.retail.v2.CustomAttribute.text] or
        [numbers][google.cloud.retail.v2.CustomAttribute.numbers] should be set.
        Otherwise, an INVALID_ARGUMENT error is returned.
        """
        pass
    @property
    def numbers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """The numerical values of this custom attribute. For example, `[2.3, 15.4]`
        when the key is "lengths_cm".

        At most 400 values are allowed.Otherwise, an INVALID_ARGUMENT error is
        returned.

        Exactly one of [text][google.cloud.retail.v2.CustomAttribute.text] or
        [numbers][google.cloud.retail.v2.CustomAttribute.numbers] should be set.
        Otherwise, an INVALID_ARGUMENT error is returned.
        """
        pass
    searchable: builtins.bool = ...
    """If true, custom attribute values are searchable by text queries in
    [SearchService.Search][google.cloud.retail.v2.SearchService.Search].

    This field is ignored in a [UserEvent][google.cloud.retail.v2.UserEvent].

    Only set if type [text][google.cloud.retail.v2.CustomAttribute.text] is
    set. Otherwise, a INVALID_ARGUMENT error is returned.
    """

    indexable: builtins.bool = ...
    """If true, custom attribute values are indexed, so that it can be filtered,
    faceted or boosted in
    [SearchService.Search][google.cloud.retail.v2.SearchService.Search].

    This field is ignored in a [UserEvent][google.cloud.retail.v2.UserEvent].

    See [SearchRequest.filter][google.cloud.retail.v2.SearchRequest.filter],
    [SearchRequest.facet_specs][google.cloud.retail.v2.SearchRequest.facet_specs]
    and
    [SearchRequest.boost_spec][google.cloud.retail.v2.SearchRequest.boost_spec]
    for more details.
    """

    def __init__(self,
        *,
        text : typing.Optional[typing.Iterable[typing.Text]] = ...,
        numbers : typing.Optional[typing.Iterable[builtins.float]] = ...,
        searchable : typing.Optional[builtins.bool] = ...,
        indexable : typing.Optional[builtins.bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_indexable",b"_indexable","_searchable",b"_searchable","indexable",b"indexable","searchable",b"searchable"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_indexable",b"_indexable","_searchable",b"_searchable","indexable",b"indexable","numbers",b"numbers","searchable",b"searchable","text",b"text"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_indexable",b"_indexable"]) -> typing.Optional[typing_extensions.Literal["indexable"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_searchable",b"_searchable"]) -> typing.Optional[typing_extensions.Literal["searchable"]]: ...
global___CustomAttribute = CustomAttribute

class FulfillmentInfo(google.protobuf.message.Message):
    """Fulfillment information, such as the store IDs for in-store pickup or region
    IDs for different shipping methods.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_FIELD_NUMBER: builtins.int
    PLACE_IDS_FIELD_NUMBER: builtins.int
    type: typing.Text = ...
    """The fulfillment type, including commonly used types (such as pickup in
    store and same day delivery), and custom types. Customers have to map
    custom types to their display names before rendering UI.

    Supported values:

    * "pickup-in-store"
    * "ship-to-store"
    * "same-day-delivery"
    * "next-day-delivery"
    * "custom-type-1"
    * "custom-type-2"
    * "custom-type-3"
    * "custom-type-4"
    * "custom-type-5"

    If this field is set to an invalid value other than these, an
    INVALID_ARGUMENT error is returned.
    """

    @property
    def place_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The IDs for this [type][google.cloud.retail.v2.FulfillmentInfo.type], such
        as the store IDs for
        [FulfillmentInfo.type.pickup-in-store][google.cloud.retail.v2.FulfillmentInfo.type]
        or the region IDs for
        [FulfillmentInfo.type.same-day-delivery][google.cloud.retail.v2.FulfillmentInfo.type].

        A maximum of 3000 values are allowed. Each value must be a string with a
        length limit of 30 characters, matching the pattern `[a-zA-Z0-9_-]+`, such
        as "store1" or "REGION-2". Otherwise, an INVALID_ARGUMENT error is
        returned.
        """
        pass
    def __init__(self,
        *,
        type : typing.Text = ...,
        place_ids : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["place_ids",b"place_ids","type",b"type"]) -> None: ...
global___FulfillmentInfo = FulfillmentInfo

class Image(google.protobuf.message.Message):
    """[Product][google.cloud.retail.v2.Product] thumbnail/detail image."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    URI_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    uri: typing.Text = ...
    """Required. URI of the image.

    This field must be a valid UTF-8 encoded URI with a length limit of 5,000
    characters. Otherwise, an INVALID_ARGUMENT error is returned.

    Google Merchant Center property
    [image_link](https://support.google.com/merchants/answer/6324350).
    Schema.org property [Product.image](https://schema.org/image).
    """

    height: builtins.int = ...
    """Height of the image in number of pixels.

    This field must be nonnegative. Otherwise, an INVALID_ARGUMENT error is
    returned.
    """

    width: builtins.int = ...
    """Width of the image in number of pixels.

    This field must be nonnegative. Otherwise, an INVALID_ARGUMENT error is
    returned.
    """

    def __init__(self,
        *,
        uri : typing.Text = ...,
        height : builtins.int = ...,
        width : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height",b"height","uri",b"uri","width",b"width"]) -> None: ...
global___Image = Image

class Interval(google.protobuf.message.Message):
    """A floating point interval."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MINIMUM_FIELD_NUMBER: builtins.int
    EXCLUSIVE_MINIMUM_FIELD_NUMBER: builtins.int
    MAXIMUM_FIELD_NUMBER: builtins.int
    EXCLUSIVE_MAXIMUM_FIELD_NUMBER: builtins.int
    minimum: builtins.float = ...
    """Inclusive lower bound."""

    exclusive_minimum: builtins.float = ...
    """Exclusive lower bound."""

    maximum: builtins.float = ...
    """Inclusive upper bound."""

    exclusive_maximum: builtins.float = ...
    """Exclusive upper bound."""

    def __init__(self,
        *,
        minimum : builtins.float = ...,
        exclusive_minimum : builtins.float = ...,
        maximum : builtins.float = ...,
        exclusive_maximum : builtins.float = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exclusive_maximum",b"exclusive_maximum","exclusive_minimum",b"exclusive_minimum","max",b"max","maximum",b"maximum","min",b"min","minimum",b"minimum"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exclusive_maximum",b"exclusive_maximum","exclusive_minimum",b"exclusive_minimum","max",b"max","maximum",b"maximum","min",b"min","minimum",b"minimum"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["max",b"max"]) -> typing.Optional[typing_extensions.Literal["maximum","exclusive_maximum"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["min",b"min"]) -> typing.Optional[typing_extensions.Literal["minimum","exclusive_minimum"]]: ...
global___Interval = Interval

class PriceInfo(google.protobuf.message.Message):
    """The price information of a [Product][google.cloud.retail.v2.Product]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PriceRange(google.protobuf.message.Message):
        """The price range of all
        [variant][google.cloud.retail.v2.Product.Type.VARIANT]
        [Product][google.cloud.retail.v2.Product] having the same
        [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id].
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        PRICE_FIELD_NUMBER: builtins.int
        ORIGINAL_PRICE_FIELD_NUMBER: builtins.int
        @property
        def price(self) -> global___Interval:
            """The inclusive
            [Product.pricing_info.price][google.cloud.retail.v2.PriceInfo.price]
            interval of all [variant][google.cloud.retail.v2.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2.Product] having the same
            [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id].
            """
            pass
        @property
        def original_price(self) -> global___Interval:
            """The inclusive
            [Product.pricing_info.original_price][google.cloud.retail.v2.PriceInfo.original_price]
            internal of all [variant][google.cloud.retail.v2.Product.Type.VARIANT]
            [Product][google.cloud.retail.v2.Product] having the same
            [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id].
            """
            pass
        def __init__(self,
            *,
            price : typing.Optional[global___Interval] = ...,
            original_price : typing.Optional[global___Interval] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["original_price",b"original_price","price",b"price"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["original_price",b"original_price","price",b"price"]) -> None: ...

    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    ORIGINAL_PRICE_FIELD_NUMBER: builtins.int
    COST_FIELD_NUMBER: builtins.int
    PRICE_EFFECTIVE_TIME_FIELD_NUMBER: builtins.int
    PRICE_EXPIRE_TIME_FIELD_NUMBER: builtins.int
    PRICE_RANGE_FIELD_NUMBER: builtins.int
    currency_code: typing.Text = ...
    """The 3-letter currency code defined in [ISO
    4217](https://www.iso.org/iso-4217-currency-codes.html).

    If this field is an unrecognizable currency code, an INVALID_ARGUMENT
    error is returned.

    The [Product.Type.VARIANT][google.cloud.retail.v2.Product.Type.VARIANT]
    [Product][google.cloud.retail.v2.Product]s with the same
    [Product.primary_product_id][google.cloud.retail.v2.Product.primary_product_id]
    must share the same
    [currency_code][google.cloud.retail.v2.PriceInfo.currency_code]. Otherwise,
    a FAILED_PRECONDITION error is returned.
    """

    price: builtins.float = ...
    """Price of the product.

    Google Merchant Center property
    [price](https://support.google.com/merchants/answer/6324371). Schema.org
    property [Offer.priceSpecification](https://schema.org/priceSpecification).
    """

    original_price: builtins.float = ...
    """Price of the product without any discount. If zero, by default set to be
    the [price][google.cloud.retail.v2.PriceInfo.price].
    """

    cost: builtins.float = ...
    """The costs associated with the sale of a particular product. Used for gross
    profit reporting.

    * Profit = [price][google.cloud.retail.v2.PriceInfo.price] -
    [cost][google.cloud.retail.v2.PriceInfo.cost]

    Google Merchant Center property
    [cost_of_goods_sold](https://support.google.com/merchants/answer/9017895).
    """

    @property
    def price_effective_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp when the [price][google.cloud.retail.v2.PriceInfo.price]
        starts to be effective. This can be set as a future timestamp, and the
        [price][google.cloud.retail.v2.PriceInfo.price] is only used for search
        after
        [price_effective_time][google.cloud.retail.v2.PriceInfo.price_effective_time].
        If so, the
        [original_price][google.cloud.retail.v2.PriceInfo.original_price] must be
        set and [original_price][google.cloud.retail.v2.PriceInfo.original_price]
        is used before
        [price_effective_time][google.cloud.retail.v2.PriceInfo.price_effective_time].

        Do not set if [price][google.cloud.retail.v2.PriceInfo.price] is always
        effective because it will cause additional latency during search.
        """
        pass
    @property
    def price_expire_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp when the [price][google.cloud.retail.v2.PriceInfo.price]
        stops to be effective. The [price][google.cloud.retail.v2.PriceInfo.price]
        is used for search before
        [price_expire_time][google.cloud.retail.v2.PriceInfo.price_expire_time]. If
        this field is set, the
        [original_price][google.cloud.retail.v2.PriceInfo.original_price] must be
        set and [original_price][google.cloud.retail.v2.PriceInfo.original_price]
        is used after
        [price_expire_time][google.cloud.retail.v2.PriceInfo.price_expire_time].

        Do not set if [price][google.cloud.retail.v2.PriceInfo.price] is always
        effective because it will cause additional latency during search.
        """
        pass
    @property
    def price_range(self) -> global___PriceInfo.PriceRange:
        """Output only. The price range of all the child
        [Product.Type.VARIANT][google.cloud.retail.v2.Product.Type.VARIANT]
        [Product][google.cloud.retail.v2.Product]s grouped together on the
        [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
        [Product][google.cloud.retail.v2.Product]. Only populated for
        [Product.Type.PRIMARY][google.cloud.retail.v2.Product.Type.PRIMARY]
        [Product][google.cloud.retail.v2.Product]s.

        Note: This field is OUTPUT_ONLY for
        [ProductService.GetProduct][google.cloud.retail.v2.ProductService.GetProduct].
        Do not set this field in API requests.
        """
        pass
    def __init__(self,
        *,
        currency_code : typing.Text = ...,
        price : builtins.float = ...,
        original_price : builtins.float = ...,
        cost : builtins.float = ...,
        price_effective_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        price_expire_time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        price_range : typing.Optional[global___PriceInfo.PriceRange] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["price_effective_time",b"price_effective_time","price_expire_time",b"price_expire_time","price_range",b"price_range"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cost",b"cost","currency_code",b"currency_code","original_price",b"original_price","price",b"price","price_effective_time",b"price_effective_time","price_expire_time",b"price_expire_time","price_range",b"price_range"]) -> None: ...
global___PriceInfo = PriceInfo

class Rating(google.protobuf.message.Message):
    """The rating of a [Product][google.cloud.retail.v2.Product]."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RATING_COUNT_FIELD_NUMBER: builtins.int
    AVERAGE_RATING_FIELD_NUMBER: builtins.int
    RATING_HISTOGRAM_FIELD_NUMBER: builtins.int
    rating_count: builtins.int = ...
    """The total number of ratings. This value is independent of the value of
    [rating_histogram][google.cloud.retail.v2.Rating.rating_histogram].

    This value must be nonnegative. Otherwise, an INVALID_ARGUMENT error is
    returned.
    """

    average_rating: builtins.float = ...
    """The average rating of the [Product][google.cloud.retail.v2.Product].

    The rating is scaled at 1-5. Otherwise, an INVALID_ARGUMENT error is
    returned.
    """

    @property
    def rating_histogram(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """List of rating counts per rating value (index = rating - 1). The list is
        empty if there is no rating. If the list is non-empty, its size is
        always 5. Otherwise, an INVALID_ARGUMENT error is returned.

        For example, [41, 14, 13, 47, 303]. It means that the
        [Product][google.cloud.retail.v2.Product] got 41 ratings with 1 star, 14
        ratings with 2 star, and so on.
        """
        pass
    def __init__(self,
        *,
        rating_count : builtins.int = ...,
        average_rating : builtins.float = ...,
        rating_histogram : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["average_rating",b"average_rating","rating_count",b"rating_count","rating_histogram",b"rating_histogram"]) -> None: ...
global___Rating = Rating

class UserInfo(google.protobuf.message.Message):
    """Information of an end user."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_ID_FIELD_NUMBER: builtins.int
    IP_ADDRESS_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    DIRECT_USER_REQUEST_FIELD_NUMBER: builtins.int
    user_id: typing.Text = ...
    """Highly recommended for logged-in users. Unique identifier for logged-in
    user, such as a user name.

    The field must be a UTF-8 encoded string with a length limit of 128
    characters. Otherwise, an INVALID_ARGUMENT error is returned.
    """

    ip_address: typing.Text = ...
    """The end user's IP address. Required for getting
    [SearchResponse.sponsored_results][google.cloud.retail.v2.SearchResponse.sponsored_results].
    This field is used to extract location information for personalization.

    This field must be either an IPv4 address (e.g. "104.133.9.80") or an IPv6
    address (e.g. "2001:0db8:85a3:0000:0000:8a2e:0370:7334"). Otherwise, an
    INVALID_ARGUMENT error is returned.

    This should not be set when using the JavaScript tag in
    [UserEventService.CollectUserEvent][google.cloud.retail.v2.UserEventService.CollectUserEvent]
    or if
    [direct_user_request][google.cloud.retail.v2.UserInfo.direct_user_request]
    is set.
    """

    user_agent: typing.Text = ...
    """User agent as included in the HTTP header. Required for getting
    [SearchResponse.sponsored_results][google.cloud.retail.v2.SearchResponse.sponsored_results].

    The field must be a UTF-8 encoded string with a length limit of 1,000
    characters. Otherwise, an INVALID_ARGUMENT error is returned.

    This should not be set when using the client side event reporting with
    GTM or JavaScript tag in
    [UserEventService.CollectUserEvent][google.cloud.retail.v2.UserEventService.CollectUserEvent]
    or if
    [direct_user_request][google.cloud.retail.v2.UserInfo.direct_user_request]
    is set.
    """

    direct_user_request: builtins.bool = ...
    """True if the request is made directly from the end user, in which case the
    [ip_address][google.cloud.retail.v2.UserInfo.ip_address] and
    [user_agent][google.cloud.retail.v2.UserInfo.user_agent] can be populated
    from the HTTP request. This flag should be set only if the API request is
    made directly from the end user such as a mobile app (and not if a gateway
    or a server is processing and pushing the user events).

    This should not be set when using the JavaScript tag in
    [UserEventService.CollectUserEvent][google.cloud.retail.v2.UserEventService.CollectUserEvent].
    """

    def __init__(self,
        *,
        user_id : typing.Text = ...,
        ip_address : typing.Text = ...,
        user_agent : typing.Text = ...,
        direct_user_request : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["direct_user_request",b"direct_user_request","ip_address",b"ip_address","user_agent",b"user_agent","user_id",b"user_id"]) -> None: ...
global___UserInfo = UserInfo

class Promotion(google.protobuf.message.Message):
    """Promotion information."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROMOTION_ID_FIELD_NUMBER: builtins.int
    promotion_id: typing.Text = ...
    """ID of the promotion. For example, "free gift".

    The value value must be a UTF-8 encoded string with a length limit of 128
    characters, and match the pattern: `[a-zA-Z][a-zA-Z0-9_]*`. For example,
    id0LikeThis or ID_1_LIKE_THIS. Otherwise, an INVALID_ARGUMENT error is
    returned.

    Google Merchant Center property
    [promotion](https://support.google.com/merchants/answer/7050148).
    """

    def __init__(self,
        *,
        promotion_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["promotion_id",b"promotion_id"]) -> None: ...
global___Promotion = Promotion

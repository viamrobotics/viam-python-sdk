# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/recommendationengine/v1beta1/catalog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.recommendationengine.v1beta1 import common_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_common__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/recommendationengine/v1beta1/catalog.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x36google/cloud/recommendationengine/v1beta1/common.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\"\x84\x05\n\x0b\x43\x61talogItem\x12\x14\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x02id\x12\x81\x01\n\x14\x63\x61tegory_hierarchies\x18\x02 \x03(\x0b\x32H.google.cloud.recommendationengine.v1beta1.CatalogItem.CategoryHierarchyB\x04\xe2\x41\x01\x02R\x13\x63\x61tegoryHierarchies\x12\x1a\n\x05title\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x05title\x12&\n\x0b\x64\x65scription\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x0b\x64\x65scription\x12\x64\n\x0fitem_attributes\x18\x05 \x01(\x0b\x32\x35.google.cloud.recommendationengine.v1beta1.FeatureMapB\x04\xe2\x41\x01\x01R\x0eitemAttributes\x12)\n\rlanguage_code\x18\x06 \x01(\tB\x04\xe2\x41\x01\x01R\x0clanguageCode\x12\x18\n\x04tags\x18\x08 \x03(\tB\x04\xe2\x41\x01\x01R\x04tags\x12(\n\ritem_group_id\x18\t \x01(\tB\x04\xe2\x41\x01\x01R\x0bitemGroupId\x12p\n\x10product_metadata\x18\n \x01(\x0b\x32=.google.cloud.recommendationengine.v1beta1.ProductCatalogItemB\x04\xe2\x41\x01\x01H\x00R\x0fproductMetadata\x1a\x39\n\x11\x43\x61tegoryHierarchy\x12$\n\ncategories\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\ncategoriesB\x15\n\x13recommendation_type\"\x8e\x08\n\x12ProductCatalogItem\x12q\n\x0b\x65xact_price\x18\x01 \x01(\x0b\x32H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.ExactPriceB\x04\xe2\x41\x01\x01H\x00R\nexactPrice\x12q\n\x0bprice_range\x18\x02 \x01(\x0b\x32H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.PriceRangeB\x04\xe2\x41\x01\x01H\x00R\npriceRange\x12\x64\n\x05\x63osts\x18\x03 \x03(\x0b\x32H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.CostsEntryB\x04\xe2\x41\x01\x01R\x05\x63osts\x12)\n\rcurrency_code\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\x0c\x63urrencyCode\x12o\n\x0bstock_state\x18\x05 \x01(\x0e\x32H.google.cloud.recommendationengine.v1beta1.ProductCatalogItem.StockStateB\x04\xe2\x41\x01\x01R\nstockState\x12\x33\n\x12\x61vailable_quantity\x18\x06 \x01(\x03\x42\x04\xe2\x41\x01\x01R\x11\x61vailableQuantity\x12\x38\n\x15\x63\x61nonical_product_uri\x18\x07 \x01(\tB\x04\xe2\x41\x01\x01R\x13\x63\x61nonicalProductUri\x12N\n\x06images\x18\x08 \x03(\x0b\x32\x30.google.cloud.recommendationengine.v1beta1.ImageB\x04\xe2\x41\x01\x01R\x06images\x1a\x64\n\nExactPrice\x12)\n\rdisplay_price\x18\x01 \x01(\x02\x42\x04\xe2\x41\x01\x01R\x0c\x64isplayPrice\x12+\n\x0eoriginal_price\x18\x02 \x01(\x02\x42\x04\xe2\x41\x01\x01R\roriginalPrice\x1a<\n\nPriceRange\x12\x16\n\x03min\x18\x01 \x01(\x02\x42\x04\xe2\x41\x01\x02R\x03min\x12\x16\n\x03max\x18\x02 \x01(\x02\x42\x04\xe2\x41\x01\x02R\x03max\x1a\x38\n\nCostsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x02R\x05value:\x02\x38\x01\"j\n\nStockState\x12\x1b\n\x17STOCK_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_STOCK\x10\x00\x12\x10\n\x0cOUT_OF_STOCK\x10\x01\x12\x0c\n\x08PREORDER\x10\x02\x12\r\n\tBACKORDER\x10\x03\x1a\x02\x10\x01\x42\x07\n\x05price\"Y\n\x05Image\x12\x16\n\x03uri\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x03uri\x12\x1c\n\x06height\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x06height\x12\x1a\n\x05width\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x05widthB\x9f\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Z]google.golang.org/genproto/googleapis/cloud/recommendationengine/v1beta1;recommendationengine\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')



_CATALOGITEM = DESCRIPTOR.message_types_by_name['CatalogItem']
_CATALOGITEM_CATEGORYHIERARCHY = _CATALOGITEM.nested_types_by_name['CategoryHierarchy']
_PRODUCTCATALOGITEM = DESCRIPTOR.message_types_by_name['ProductCatalogItem']
_PRODUCTCATALOGITEM_EXACTPRICE = _PRODUCTCATALOGITEM.nested_types_by_name['ExactPrice']
_PRODUCTCATALOGITEM_PRICERANGE = _PRODUCTCATALOGITEM.nested_types_by_name['PriceRange']
_PRODUCTCATALOGITEM_COSTSENTRY = _PRODUCTCATALOGITEM.nested_types_by_name['CostsEntry']
_IMAGE = DESCRIPTOR.message_types_by_name['Image']
_PRODUCTCATALOGITEM_STOCKSTATE = _PRODUCTCATALOGITEM.enum_types_by_name['StockState']
CatalogItem = _reflection.GeneratedProtocolMessageType('CatalogItem', (_message.Message,), {

  'CategoryHierarchy' : _reflection.GeneratedProtocolMessageType('CategoryHierarchy', (_message.Message,), {
    'DESCRIPTOR' : _CATALOGITEM_CATEGORYHIERARCHY,
    '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.CatalogItem.CategoryHierarchy)
    })
  ,
  'DESCRIPTOR' : _CATALOGITEM,
  '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.CatalogItem)
  })
_sym_db.RegisterMessage(CatalogItem)
_sym_db.RegisterMessage(CatalogItem.CategoryHierarchy)

ProductCatalogItem = _reflection.GeneratedProtocolMessageType('ProductCatalogItem', (_message.Message,), {

  'ExactPrice' : _reflection.GeneratedProtocolMessageType('ExactPrice', (_message.Message,), {
    'DESCRIPTOR' : _PRODUCTCATALOGITEM_EXACTPRICE,
    '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.ProductCatalogItem.ExactPrice)
    })
  ,

  'PriceRange' : _reflection.GeneratedProtocolMessageType('PriceRange', (_message.Message,), {
    'DESCRIPTOR' : _PRODUCTCATALOGITEM_PRICERANGE,
    '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.ProductCatalogItem.PriceRange)
    })
  ,

  'CostsEntry' : _reflection.GeneratedProtocolMessageType('CostsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PRODUCTCATALOGITEM_COSTSENTRY,
    '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.ProductCatalogItem.CostsEntry)
    })
  ,
  'DESCRIPTOR' : _PRODUCTCATALOGITEM,
  '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.ProductCatalogItem)
  })
_sym_db.RegisterMessage(ProductCatalogItem)
_sym_db.RegisterMessage(ProductCatalogItem.ExactPrice)
_sym_db.RegisterMessage(ProductCatalogItem.PriceRange)
_sym_db.RegisterMessage(ProductCatalogItem.CostsEntry)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'google.cloud.recommendationengine.v1beta1.catalog_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.recommendationengine.v1beta1.Image)
  })
_sym_db.RegisterMessage(Image)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\001Z]google.golang.org/genproto/googleapis/cloud/recommendationengine/v1beta1;recommendationengine\242\002\005RECAI\252\002)Google.Cloud.RecommendationEngine.V1Beta1\312\002)Google\\Cloud\\RecommendationEngine\\V1beta1\352\002,Google::Cloud::RecommendationEngine::V1beta1'
  _CATALOGITEM_CATEGORYHIERARCHY.fields_by_name['categories']._options = None
  _CATALOGITEM_CATEGORYHIERARCHY.fields_by_name['categories']._serialized_options = b'\342A\001\002'
  _CATALOGITEM.fields_by_name['id']._options = None
  _CATALOGITEM.fields_by_name['id']._serialized_options = b'\342A\001\002'
  _CATALOGITEM.fields_by_name['category_hierarchies']._options = None
  _CATALOGITEM.fields_by_name['category_hierarchies']._serialized_options = b'\342A\001\002'
  _CATALOGITEM.fields_by_name['title']._options = None
  _CATALOGITEM.fields_by_name['title']._serialized_options = b'\342A\001\002'
  _CATALOGITEM.fields_by_name['description']._options = None
  _CATALOGITEM.fields_by_name['description']._serialized_options = b'\342A\001\001'
  _CATALOGITEM.fields_by_name['item_attributes']._options = None
  _CATALOGITEM.fields_by_name['item_attributes']._serialized_options = b'\342A\001\001'
  _CATALOGITEM.fields_by_name['language_code']._options = None
  _CATALOGITEM.fields_by_name['language_code']._serialized_options = b'\342A\001\001'
  _CATALOGITEM.fields_by_name['tags']._options = None
  _CATALOGITEM.fields_by_name['tags']._serialized_options = b'\342A\001\001'
  _CATALOGITEM.fields_by_name['item_group_id']._options = None
  _CATALOGITEM.fields_by_name['item_group_id']._serialized_options = b'\342A\001\001'
  _CATALOGITEM.fields_by_name['product_metadata']._options = None
  _CATALOGITEM.fields_by_name['product_metadata']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM_EXACTPRICE.fields_by_name['display_price']._options = None
  _PRODUCTCATALOGITEM_EXACTPRICE.fields_by_name['display_price']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM_EXACTPRICE.fields_by_name['original_price']._options = None
  _PRODUCTCATALOGITEM_EXACTPRICE.fields_by_name['original_price']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM_PRICERANGE.fields_by_name['min']._options = None
  _PRODUCTCATALOGITEM_PRICERANGE.fields_by_name['min']._serialized_options = b'\342A\001\002'
  _PRODUCTCATALOGITEM_PRICERANGE.fields_by_name['max']._options = None
  _PRODUCTCATALOGITEM_PRICERANGE.fields_by_name['max']._serialized_options = b'\342A\001\002'
  _PRODUCTCATALOGITEM_COSTSENTRY._options = None
  _PRODUCTCATALOGITEM_COSTSENTRY._serialized_options = b'8\001'
  _PRODUCTCATALOGITEM_STOCKSTATE._options = None
  _PRODUCTCATALOGITEM_STOCKSTATE._serialized_options = b'\020\001'
  _PRODUCTCATALOGITEM.fields_by_name['exact_price']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['exact_price']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['price_range']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['price_range']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['costs']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['costs']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['currency_code']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['currency_code']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['stock_state']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['stock_state']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['available_quantity']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['available_quantity']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['canonical_product_uri']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['canonical_product_uri']._serialized_options = b'\342A\001\001'
  _PRODUCTCATALOGITEM.fields_by_name['images']._options = None
  _PRODUCTCATALOGITEM.fields_by_name['images']._serialized_options = b'\342A\001\001'
  _IMAGE.fields_by_name['uri']._options = None
  _IMAGE.fields_by_name['uri']._serialized_options = b'\342A\001\002'
  _IMAGE.fields_by_name['height']._options = None
  _IMAGE.fields_by_name['height']._serialized_options = b'\342A\001\001'
  _IMAGE.fields_by_name['width']._options = None
  _IMAGE.fields_by_name['width']._serialized_options = b'\342A\001\001'
  _CATALOGITEM._serialized_start=252
  _CATALOGITEM._serialized_end=896
  _CATALOGITEM_CATEGORYHIERARCHY._serialized_start=816
  _CATALOGITEM_CATEGORYHIERARCHY._serialized_end=873
  _PRODUCTCATALOGITEM._serialized_start=899
  _PRODUCTCATALOGITEM._serialized_end=1937
  _PRODUCTCATALOGITEM_EXACTPRICE._serialized_start=1600
  _PRODUCTCATALOGITEM_EXACTPRICE._serialized_end=1700
  _PRODUCTCATALOGITEM_PRICERANGE._serialized_start=1702
  _PRODUCTCATALOGITEM_PRICERANGE._serialized_end=1762
  _PRODUCTCATALOGITEM_COSTSENTRY._serialized_start=1764
  _PRODUCTCATALOGITEM_COSTSENTRY._serialized_end=1820
  _PRODUCTCATALOGITEM_STOCKSTATE._serialized_start=1822
  _PRODUCTCATALOGITEM_STOCKSTATE._serialized_end=1928
  _IMAGE._serialized_start=1939
  _IMAGE._serialized_end=2028
# @@protoc_insertion_point(module_scope)

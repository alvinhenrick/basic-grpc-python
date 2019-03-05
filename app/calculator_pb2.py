# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/calculator.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x14\x61pp/calculator.proto\"\x1e\n\rNumberRequest\x12\r\n\x05value\x18\x01 \x01(\x02\"\x1f\n\x0eNumberResponse\x12\r\n\x05value\x18\x01 \x01(\x02\x32=\n\nCalculator\x12/\n\nSquareRoot\x12\x0e.NumberRequest\x1a\x0f.NumberResponse\"\x00\x62\x06proto3')
)




_NUMBERREQUEST = _descriptor.Descriptor(
  name='NumberRequest',
  full_name='NumberRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='NumberRequest.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=54,
)


_NUMBERRESPONSE = _descriptor.Descriptor(
  name='NumberResponse',
  full_name='NumberResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='NumberResponse.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['NumberRequest'] = _NUMBERREQUEST
DESCRIPTOR.message_types_by_name['NumberResponse'] = _NUMBERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumberRequest = _reflection.GeneratedProtocolMessageType('NumberRequest', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERREQUEST,
  __module__ = 'app.calculator_pb2'
  # @@protoc_insertion_point(class_scope:NumberRequest)
  ))
_sym_db.RegisterMessage(NumberRequest)

NumberResponse = _reflection.GeneratedProtocolMessageType('NumberResponse', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERRESPONSE,
  __module__ = 'app.calculator_pb2'
  # @@protoc_insertion_point(class_scope:NumberResponse)
  ))
_sym_db.RegisterMessage(NumberResponse)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=89,
  serialized_end=150,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBERREQUEST,
    output_type=_NUMBERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class CalculatorStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.SquareRoot = channel.unary_unary(
          '/Calculator/SquareRoot',
          request_serializer=NumberRequest.SerializeToString,
          response_deserializer=NumberResponse.FromString,
          )


  class CalculatorServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def SquareRoot(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SquareRoot': grpc.unary_unary_rpc_method_handler(
            servicer.SquareRoot,
            request_deserializer=NumberRequest.FromString,
            response_serializer=NumberResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaCalculatorServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def SquareRoot(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaCalculatorStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def SquareRoot(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    SquareRoot.future = None


  def beta_create_Calculator_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Calculator', 'SquareRoot'): NumberRequest.FromString,
    }
    response_serializers = {
      ('Calculator', 'SquareRoot'): NumberResponse.SerializeToString,
    }
    method_implementations = {
      ('Calculator', 'SquareRoot'): face_utilities.unary_unary_inline(servicer.SquareRoot),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Calculator_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Calculator', 'SquareRoot'): NumberRequest.SerializeToString,
    }
    response_deserializers = {
      ('Calculator', 'SquareRoot'): NumberResponse.FromString,
    }
    cardinalities = {
      'SquareRoot': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Calculator', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
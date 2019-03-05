import grpc

# import the generated classes
from app import calculator_pb2, calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:9090')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.NumberRequest(value=16)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)

#/usr/bin/python3
from concurrent import futures
import time
import grpc
import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
from grpc_controllers.charges import * 
from grpc_controllers.customers import *


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payments_bills_service_pb2_grpc.add_ChargesServicer_to_server(
        ChargesServicer(), server)
    payments_bills_service_pb2_grpc.add_CustomersServicer_to_server(
        CustomersServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS) # vive infinitamente
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()



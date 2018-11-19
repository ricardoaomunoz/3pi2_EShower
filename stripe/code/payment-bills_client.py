#/usr/bin/python3
import grpc
import payments_bills_service_pb2
import payments_bills_service_pb2_grpc


def create_a_charge(stub):
    chargeobject= payments_bills_service_pb2.ChargeObject(amount=200, currency="usd", source="tok_visa", description="first charge", customer="Juan", receipt_email="ricardoaomunoz@gmail.com")
    print("resultado", chargeobject)
    return_charge = stub.CreateCharge(chargeobject)
    print("resultado", return_charge)
    if not return_charge.id:
        print("server error", return_charge.description)

    else:
        print("object returned", return_charge)
        print("id: ", return_charge.id)


def get_customer(stub):
        getid = payments_bills_service_pb2.GetByIdCharge(id="cus_E05uw5emgkEtwi")#"ch_1DY40t2eZvKYlo2CBcSeU9CC")
        return_customer = stub.GetCustomerById(getid)
        print("object returned", return_customer)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = payments_bills_service_pb2_grpc.ChargesStub(channel)
        stub1 = payments_bills_service_pb2_grpc.CustomersStub(channel)
        print("-------------- Make a Charge --------------")
        # create_a_charge(stub)
        print("-------------- get customer --------------")
        get_customer(stub1)
        # print("-------------- RecordRoute --------------")
        # guide_record_route(stub)
        # print("-------------- RouteChat --------------")
        # guide_route_chat(stub)


if __name__ == '__main__':
    run()

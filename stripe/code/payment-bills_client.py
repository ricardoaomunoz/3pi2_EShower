#/usr/bin/python3
import grpc
import payments_bills_service_pb2
import payments_bills_service_pb2_grpc


def create_a_charge(stub):
    chargeobject= payments_bills_service_pb2.ChargeObject(amount=200, currency="usd", source="tok_visa", description="first charge", customer="Juan", receipt_email="ricardoaomunoz@gmail.com")
    print("resultado", chargeobject)
    return_charge = stub.CreateChargeToSource(chargeobject)
    print("resultado", return_charge)
    if not return_charge.id:
        print("server error", return_charge.description)

    else:
        print("object returned", return_charge)
        print("id: ", return_charge.id)
        return return_charge.id

def get_charge(stub, id_charge):
        getChar = payments_bills_service_pb2.GetByIdCharge(id = id_charge)
        retun_char = stub.GetChargeById(getChar)
        print("charge returned: ", retun_char)
        print("id: ", str(retun_char.id))

def get_customer(stub):
        getid = payments_bills_service_pb2.GetByIdCharge(
                id="cus_E0RNACg0")#"ch_1DY40t2eZvKYlo2CBcSeU9CC")
        try:
                return_customer = stub.GetCustomerById(getid)
                print("object returned", return_customer)
        except grpc.RpcError as e:
                print("error", e)
                print ("details", e.details())
                status_code = e.code()
                print("name: ", status_code.name)
                print("value: ", status_code.value)

def Create_customer(stub):
        cus = payments_bills_service_pb2.CustomerObject(
               email="prueba@prueba.com",
               source="tok_visa",
               description= "prueba client crear customer"
        )
        try:
                create_cus = stub.CreateCustomer(cus)
                print ("Se creo usuario con id: ", create_cus.id)
                return str(create_cus.id)
        except grpc.RpcError as e:
                print("error", e)
                print ("details", e.details())
                print(status_code = e.code())
                print(status_code.name)
                print(status_code.value)
        


def Delete_cus(stub, id_cus):
        cus = payments_bills_service_pb2.GetByIdCharge(
                id = id_cus
        )
        delet_cus = stub.DeleteCustomer(cus)
        print ("The deleted customer: ", delet_cus)

def create_subs(stub, dict_format):
        subs = payments_bills_service_pb2.SubscriptionsObject(
                customerId=dict_format["customerId"],
                plan=payments_bills_service_pb2.PlansObject(
                        id=dict_format["planid"]
                ))
        createsubs = stub.CreateSubscription(subs)
        print ("susbscription: ",createsubs)

def get_cutomer_list(stub):
        argument = payments_bills_service_pb2.ListRequest(
                limit = 1
        )
        get_list = stub.GetCustomesList(argument)
        for list_get in get_list:
                print ("Customer: ....", list_get)
        

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = payments_bills_service_pb2_grpc.ChargesStub(channel)
        stub1 = payments_bills_service_pb2_grpc.CustomersStub(channel)
        stub3 = payments_bills_service_pb2_grpc.SubscriptionStub(channel)
        #print("-------------- Make a Charge --------------")
        #char = create_a_charge(stub)
        #print("-------------- Get a Charge --------------")
        #get_charge(stub, char)
        print("-------------- get customer --------------")
        get_customer(stub1)
        #print("-------------- create customer --------------")
        #cusCreated = Create_customer(stub1)
        #print("-------------- delete customer --------------")
        #Delete_cus(stub1, cusCreated)
        #print("--------------create subscription --------------")
        #create_subs(stub3, ({"customerId": cusCreated, "planid":"plan_E0erUB9TWBz30r"}))
        #print("-------------- Get customer list --------------")
        #get_cutomer_list(stub1)
        # print("-------------- RouteChat --------------")
        # guide_route_chat(stub)


if __name__ == '__main__':
    run()

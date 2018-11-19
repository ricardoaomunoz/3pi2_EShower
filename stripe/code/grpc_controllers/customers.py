import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *

class CustomersServicer(payments_bills_service_pb2_grpc.CustomersServicer):
    def __init__(self):
        self.customer = Customers()

    def GetCustomerById(self, request, context):
        try:
            ans = self.customer.GetById(request.id)
            return json_to_grpc(str(ans))
        except stripe.error.CardError as e:
            print(e)
            

    def GetCustomesList(self, request, context):
        pass

    def CreateCustomer(self, request, context):
        pass

    def DeleteCustomer(self, request, context):
        pass
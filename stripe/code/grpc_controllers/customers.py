import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
import grpc
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *

class CustomersServicer(payments_bills_service_pb2_grpc.CustomersServicer):
    def __init__(self):
        self.customer = Customers()

    def GetCustomerById(self, request, context):
        
        ans = self.customer.GetById(request.id)
        try:
            return json_to_grpc_customer(str(ans))
        except Exception as e:
            print("hubo un error se devuelve none", ans)
            context.set_details(str(ans))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return context
    
            

    def GetCustomesList(self, request, context):
        ans = self.customer.GetList()
        for item in ans:
            customer_details = {
                "id": item["id"],
                "created": item["created"],
                "object": item["object"],
                "description": item["description"],
                "subscriptions":item["subscriptions"]
                }
            print("yields", customer_details)
            json_details = json.dumps(customer_details)
            yield json_to_grpc_customer(str(json_details))

            


        

    def CreateCustomer(self, request, context):
        request_dic = {
            "email":request.email,
            "source":request.source,
            "description":request.description
        }
        try:
            ans = self.customer.Add(request_dic)
            return json_to_grpc_grtbyid(str(ans))

        except stripe.error.CardError as e:
            print(e)    
        pass

    def DeleteCustomer(self, request, context):
        try:
            ans = self.customer.Delete(request.id)
            return json_to_grpc_deleted(str(ans))
        except stripe.error.CardError as e:
            print(e)
            pass
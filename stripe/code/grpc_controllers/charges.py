# /usr/bin/python3
import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
import grpc
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *


class ChargesServicer(payments_bills_service_pb2_grpc.ChargesServicer):
    
    def __init__(self):
        #  stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
         self.charges = Charges()
    
    def CreateChargeToCustomer(self, request, context):
        Chargeparameters = {
            "cutomer_id":request.customer,
            "amount":request.amount,
            "currency":request.currency,
            "description":request.description
        }
        
        ans = self.charges.AddToCustomer(Chargeparameters)
        try:
            return json_to_grpc_charge(str(ans))
        except Exception as e:
            context.set_details(str(ans))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return None


        

    def CreateChargeToSource(self, request, context):
        Chargeparameters = {
            "email":request.receipt_email,
            "source":request.source,
            "amount":request.amount,
            "currency":request.currency,
            "description":request.description
        }
        try:
            ans = self.charges.AddCharge(Chargeparameters)
            return json_to_grpc_charge(str(ans))
        except stripe.error.CardError as e:
            print (e)
   

    def GetChargeById(self, request, context):
        try:
            charge = self.charges.GetById(request.id)
            print("respuesta del get charge by id: ",json_to_grpc_charge(str(charge)))
            return json_to_grpc_charge(str(charge))
        except stripe.error.CardError as e:
            print ("this is the get charge error", e)
            

    def EditChargeById(self, request, context):
        try:
            ans = self.charges.EditById(request.id, request.description)
            # ch = stripe.Charge.retrieve(request.id)
            # ch.description = request.description
            # ch.save()
            return json_to_grpc_charge(str(ans))
        except stripe.error.CardError as e:
            print("this is the edit charge error", e)
            return payments_bills_service_pb2.ChargeObject(id="", description=e)

    def GetChargeList(self, request, context):
        try:
            ans_list = stripe.Charge.list()
            # return ans_list
            #for 
        except stripe.error.CardError as e:
            print("this is the get list charge error", e)

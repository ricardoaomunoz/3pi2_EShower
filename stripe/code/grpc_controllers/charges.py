# /usr/bin/python3
import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *


class ChargesServicer(payments_bills_service_pb2_grpc.ChargesServicer):
    
    def __init__(self):
         stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    def CreateCharge(self, request, context):
        print("Charge created into")
        try:
            ans = stripe.Charge.create(
                amount=request.amount,
                currency=request.currency,
                source=request.source,  # obtained with Stripe.js
                description=request.description,
                receipt_email=request.receipt_email

            )
            print("register ok")
            print("ans: ", ans)
            data = json_to_grpc_charge(str(ans))

            print("data: ", data)
            return data
        except stripe.error.CardError as e:
            print("this is the charge error", e)
            return payments_bills_service_pb2.GetByIdCharge(id="", object="charge", customer=request.customer,
                                                           descrption=e)

    def GetChargeById(self, request, context):
        try:
            ans = stripe.Charge.retrieve(request.id)
            print("getChargebyID ok")
            return ans
        except stripe.error.CardError as e:
            print ("this is the get charge error", e)
            return payments_bills_service_pb2.ChargeObject(id="", description=e)

    def EditChargeById(self, request, context):
        try:
            ch = stripe.Charge.retrieve(request.id)
            ch.description = request.description
            ch.save()
            return ch
        except stripe.error.CardError as e:
            print("this is the edit charge error", e)
            return payments_bills_service_pb2.ChargeObject(id="", description=e)

    def GetChargeList(self, request, context):
        try:
            ans_list = stripe.Charge.list(request)
            return ans_list
        except stripe.error.CardError as e:
            print("this is the get list charge error", e)

import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *

class SubscriptionServicer(payments_bills_service_pb2_grpc.SubscriptionServicer):
    def __init__(self):
        self.subscription = Subscriptions()

    def GetSubscriptionById(self, request, context):
        try:
            ans = self.subscription.GetById(request.id)
            return json_to_grpc_subscription(str(ans))
        except stripe.error.CardError as e:
            print(e)
    
    def GetSubscriptionList(self, request, context):
        try:
            pass
        except stripe.error.CardError as e:
            print(e)

    def CreateSubscription(self, request, context):
        request_dic = {
            "customer":request.customerId,
            "id_plan":request.plan.id, 
        }
        try:
            print(request_dic)
            ans = self.subscription.Add(request_dic)
            return json_to_grpc_subscription(str(ans))
            
            
        except stripe.error.CardError as e:
            print(e)

    def CancelSubscription(self, request, context):
        try:
            ans = self.subscription.Cancel(request.id)
            return json_to_grpc_subscription(str(ans))
            
        except stripe.error.CardError as e:
            print(e)

    def UpdateSubscription(self, request, context):
        try:
            pass
        except stripe.error.CardError as e:
            print(e)
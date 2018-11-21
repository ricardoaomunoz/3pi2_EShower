import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *

class PlansServicer(payments_bills_service_pb2_grpc.PlansServicer):
    def __init__(self):
        self.plan = Plans()

    def GetPlanById(self, request, context):
        ans = self.plan.GetById(request.id)
        return json_to_grpc_plan(str(ans))

    def GetPlansList(self, request, context):
        pass
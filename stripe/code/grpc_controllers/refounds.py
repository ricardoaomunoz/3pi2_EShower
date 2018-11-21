import payments_bills_service_pb2
import payments_bills_service_pb2_grpc
import stripe
from stripe_models.stripe_api import *
from stripe_models.stripe_resources import *

class RefoundsServicer(payments_bills_service_pb2_grpc.RefoundsServicer):
    def __init__(self):
        self.refound = Refounds()

    def GetRefoundById(self, request, context):
        ans = self.refound.GetByID(request.id)
        return json_to_grpc_refound(str(ans))
        

    def GetRefounsList(self, request, context):
        pass

    def CreateRefound(self, request, context):
        ans = self.refound.Add(request.charge)
        return json_to_grpc_refound(str(ans))
        
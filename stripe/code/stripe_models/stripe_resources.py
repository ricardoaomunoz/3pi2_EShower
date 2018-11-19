import json
import payments_bills_service_pb2

def json_to_grpc_charge(stripe_ans):
    # feature_list = []
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.GetByIdCharge(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            customer=item["customer"],
            description=item["description"])
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge

def json_to_grpc_customer(stripe_ans):
    # feature_list = []
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.ChargeObject(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            customer=item["customer"],
            description=item["description"])
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge
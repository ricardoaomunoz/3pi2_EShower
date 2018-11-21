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
    if item["subscriptions"]["total_count"] == 0:
        supscrip = payments_bills_service_pb2.SubscriptionsObject(
            id="")
    else:
        supscrip = payments_bills_service_pb2.SubscriptionsObject(
            id=item["subscriptions"]["data"][0]["id"])
    ans_charge = payments_bills_service_pb2.CustomerObject(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            description=item["description"],
            suscriptions = supscrip )
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge

def json_to_grpc_grtbyid(stripe_ans):
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.GetByIdCharge(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            description=item["description"])
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge

def json_to_grpc_deleted(stripe_ans):
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.DeleteObject(
            id=item["id"],
            object=item["object"],
            deleted=item["deleted"])
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge


def json_to_grpc_subscription(stripe_ans):
    # feature_list = []
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.SubscriptionsObject(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            customerId= item["customer"],
            plan = payments_bills_service_pb2.PlansObject(
                id=item["plan"]["id"]))
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge

def json_to_grpc_plan(stripe_ans):
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.PlansObject(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            currency= item["currency"],
            interval=item["interval"],
            active = item["active"]
            )
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge

def json_to_grpc_refound(stripe_ans):
    item = json.loads(stripe_ans)
    print ("item: ", item)
    ans_charge = payments_bills_service_pb2.RefoundObject(
            id=item["id"],
            object=item["object"],
            created=item["created"],
            currency= item["currency"],
            charge=item["charge"],
            amount = item["amount"]
            )
    # feature_list.append(ans_charge)
    print("return: ", ans_charge)
    return ans_charge





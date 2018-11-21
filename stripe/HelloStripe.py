import stripe
import os
import json
import exceptionStripe

# a = os.environ.get('STRIPE_PUBLISHABLE')
# print (a)
# stripe.api_key = os.getenv('STRIPE_SECRET')


stripe.api_key = "sk_test_n3vaKoIJeX33JmgMtFT49D7o"
# print ("first: ", stripe.Charge.retrieve("ch_1DVf9y2eZvKYlo2CdNCnredz", expand=['customer']))


def createcharge(cantidad, moneda, fuente, descripcion):
    try:
        ans = (stripe.Charge.create(
            amount=cantidad,
            currency=moneda,
            source=fuente,  # obtained with Stripe.js
            description=descripcion
            ))
        print("register ok")
        return ans
    except stripe.error.CardError as e:
        print("this is the error", e)
        # print("Second: ", stripe.Customer.list(limit=3))
# print(stripe.Balance.retrieve())


# charge = createcharge(100, "usd", "tok_visa", "Carga example")
# list_arguments=dict(limit=3)
# print(list_arguments)
# print (type(list_arguments))
# #print("id de carga: ", charge.id)
# for key in list_arguments:
#      print (key, type(key))
#      print (list_arguments[key], type(list_arguments[key]))
##customerById = stripe.Customer.list()
##print("Customers: ", customerById)
##
##dict_obj = json.loads(str(customerById))
##print("#############################333333")
##customer_list = []
##
##for item in customerById:
##    # print(item["id"][0])
##    store_details = {"id": None, "created": None, "object": None, "description": None, "subscription": None}
##    store_details["id"] = item["id"]
##    store_details["created"] = item["created"]
##    store_details["object"] = item['object']
##    store_details["description"] = item['description']
##    store_details["subscriptions"] = item['subscriptions']
##    customer_list.append(store_details)
##print (customer_list)
# for i in dict_obj:

# print(type(customerById))
# #Return the details of a specific charge_id
# print(stripe.Charge.retrieve("ch_1DVlVvKW8zB7kwRq92Gwav2F"))
#
# #Change a specific parameter of a specific charge_id
# ch = stripe.Charge.retrieve("ch_1DVf9y2eZvKYlo2CdNCnredz")
# ch.description = "Charge for jenny.rosen@example.com"
# ch.save()
#
# #When the capture options is false, this pass true (remeber the Uncaptured payments expire exactly seven days after they are created)
# ch = stripe.Charge.retrieve("ch_1DVf9y2eZvKYlo2CdNCnredz")
# ch.capture()

# Returns a list of charges you’ve previously created
try:
    print("list: ", stripe.Charge.list(customer="cus"))
except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
    body = e.json_body
    err  = body.get('error', {})
    print ("Status is: %s" % e.http_status)
    print ("Type is: %s" % err.get('type'))
    print ("Code is: %s" % err.get('code'))
  # param is '' in this case
    print ("Param is: %s" % err.get('param'))
    print ("Message is: %s" % err.get('message'))
    
        
        

    
  # Since it's a decline, stripe.error.CardError will be caught
##  body = e.json_body
##  err  = body.get('error', {})
##
##  print ("Status is: %s" % e.http_status)
##  print ("Type is: %s" % err.get('type'))
##  print ("Code is: %s" % err.get('code'))
##  print ("Param is: %s" % err.get('param'))
##  print ("Message is: %s" % err.get('message'))

# stripe.Plan.create(
#   amount=5000,
#   interval="month",
#   product={
#     "name": "Primer-123"
#   },
#   currency="usd",
# )

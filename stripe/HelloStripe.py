import stripe
import os

#a = os.environ.get('STRIPE_PUBLISHABLE')
#print (a)
#stripe.api_key = os.getenv('STRIPE_SECRET')


stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
#print ("first: ", stripe.Charge.retrieve("ch_1DVf9y2eZvKYlo2CdNCnredz", expand=['customer']))

def createcharge(cantidad, moneda, fuente, descripcion):
    try:
        ans=(stripe.Charge.create(
            amount=cantidad,
            currency=moneda,
            source=fuente, # obtained with Stripe.js
            description=descripcion
            ))
        print("register ok")
        return ans
    except stripe.error.CardError as e:
        print("this is the error", e)
        #print("Second: ", stripe.Customer.list(limit=3))
#print(stripe.Balance.retrieve())

#charge = createcharge(100, "usd", "tok_visa", "Carga example")
list_arguments=dict(limit=3)
print(list_arguments)
print (type(list_arguments))
#print("id de carga: ", charge.id)
for key in list_arguments:  
     print (key, type(key))
     print (list_arguments[key], type(list_arguments[key]))
customerById = stripe.Customer.list(limit='')
print("Customers: ", customerById)
print(type(customerById))
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

#Returns a list of charges you’ve previously created
#print("list: ", stripe.Charge.list(limit=3))

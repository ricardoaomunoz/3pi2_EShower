from stripe_models.stripe_api import *

# x = Customers()
# print (x.GetList())  
charge_params= {
'customer_id':'cus_DzxC8mu133bA9h', 
'amount':200, 
'description':'probando stripe api', 
'currency':'usd'}

y = Charges()
print (y.AddToCustomer(charge_params))
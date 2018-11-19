import stripe
import os

#a = os.environ.get('STRIPE_PUBLISHABLE')
#print (a)
#stripe.api_key = os.getenv('STRIPE_SECRET')


# stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
#print ("first: ", stripe.Charge.retrieve("ch_1DVf9y2eZvKYlo2CdNCnredz", expand=['customer']))
class Stripe():
    def __init__(self):
        stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


class Charges(Stripe):

    def AddToCustomer(self, parameter_dict):
        charge = stripe.Charge.create(
            customer=parameter_dict['customer_id'],
            amount=parameter_dict['amount'],
            currency=parameter_dict['currency'],
            description=parameter_dict['description']
        )
        return charge

    def AddCharge(self, parameter_dict):
        # if parameter_dict['customer_id'] == "none":
        customer = stripe.Customer.create(
            email=parameter_dict['email'],
            source=parameter_dict['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer.id,
            amount=parameter_dict['amount'],
            currency=parameter_dict['usd'],
            description=parameter_dict['description']
        )
        return charge

class Customers(Stripe):
    def GetById(self, customer_id):
        return stripe.Customer.retrieve(customer_id)

    def GetList(self):
        return stripe.Customer.list()

    def Add(self, parameter_dict):
        customer = stripe.Customer.create(
            email=parameter_dict['email'],
            source=parameter_dict['stripeToken'],
            description = parameter_dict['description']
        )

        return customer

    def Delete(self, customer_id):
        cu = stripe.Customer.retrieve(customer_id)
        return cu.delete()

class Suscriptions(Stripe):
    def GetById(self, sub_id):
        return stripe.Subscription.retrieve(sub_id)

    def GetList(self, parameter_sublist):
        return stripe.Subscription.list(parameter_sublist)

    def Add(self, parameter_dict):
        suscription = stripe.Subscription.create(
            customer=parameter_dict['customer_id'],
            items=parameter_dict['items']
        )
        return suscription

    def Cancel(self, sub_id):
        sub = stripe.Subscription.retrieve(sub_id)
        return sub.delete()

    def Update(self, sub_id, newValue):
        subscription = stripe.Subscription.retrieve(sub_id)
        subscription.tax_percent = 10
        subscription.save()
        pass

class Plans(Stripe):

    def GetById(self, plan_name):
        return stripe.Plan.retrieve(plan_name)


    def GetList(self, parameter_list):
        return stripe.Plan.list(parameter_list)

class Refounds(Stripe):
    def GetByID(self, refound_id):
        return stripe.Refund.retrieve(refound_id)

    def GetList(self, parameter_list):
        return stripe.Refund.list(parameter_list)

    def Add(self, charge_id):
        re = stripe.Refund.create(
            charge=charge_id        )



# x = Customers()
# print (x.GetList())      



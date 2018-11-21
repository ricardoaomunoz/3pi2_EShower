import stripe
import os

#a = os.environ.get('STRIPE_PUBLISHABLE')
#print (a)
#stripe.api_key = os.getenv('STRIPE_SECRET')


# stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
#print ("first: ", stripe.Charge.retrieve("ch_1DVf9y2eZvKYlo2CdNCnredz", expand=['customer']))
class Stripe():
    def __init__(self):
        
        # stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
        stripe.api_key ="sk_test_n3vaKoIJeX33JmgMtFT49D7o"


class Charges(Stripe):

    def AddToCustomer(self, parameter_dict):
        try:
            charge = stripe.Charge.create(
                customer=parameter_dict['customer_id'],
                amount=parameter_dict['amount'],
                currency=parameter_dict['currency'],
                description=parameter_dict['description']
            )
            return charge
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))
            back = "Type is: %s and Message is: %s" %(err.get('type'),err.get('message'))
            print (back)
            return (back)
    def AddCharge(self, parameter_dict):
        # if parameter_dict['customer_id'] == "none":
        try:
            customer = stripe.Customer.create(
                email=parameter_dict['email'],
                source=parameter_dict['source']
            )

            charge = stripe.Charge.create(
                customer=customer.id,
                amount=parameter_dict['amount'],
                currency=parameter_dict['currency'],
                description=parameter_dict['description']
            )
            return charge
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def GetById(self, reques_id):
        try:
            ans = stripe.Charge.retrieve(reques_id)
            # print("getChargebyID ok")
            return ans
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))
            back = "Type is: %s and Message is: %s" %(err.get('type'),err.get('message'))
            return (back)

    def EditById(self, reques_id, parameter_dict):
        try:
            ch = stripe.Charge.retrieve(reques_id)
            ch.description = parameter_dict
            return ch.save()
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def GetList(self):
        try:
            ans_list = stripe.Charge.list()
            return ans_list
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

class Customers(Stripe):
    def GetById(self, customer_id):
        try:
            return stripe.Customer.retrieve(customer_id)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))
            back = "Type is: %s and Message is: %s" % (err.get('type'),err.get('message'))
            return (back)


    def GetList(self):
        try:
            return stripe.Customer.list()
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def Add(self, parameter_dict):
        try:
            customer = stripe.Customer.create(
                email=parameter_dict['email'],
                source=parameter_dict['source'],
                description = parameter_dict['description']
            )

            return customer
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def Delete(self, customer_id):
        try:
            cu = stripe.Customer.retrieve(customer_id)
            return cu.delete()
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

class Subscriptions(Stripe):
    def GetById(self, sub_id):
        try:
            return stripe.Subscription.retrieve(sub_id)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def GetList(self, parameter_sublist):
        try:
            return stripe.Subscription.list(parameter_sublist)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def Add(self, parameter_dict):
        try:
            suscription = stripe.Subscription.create(
                customer=parameter_dict['customer'],
                items=[
                    {
                        "plan": parameter_dict['id_plan']
                    },
                ]
            )
            return suscription
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def Cancel(self, sub_id):
        try:
            sub = stripe.Subscription.retrieve(sub_id)
            return sub.delete()
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def Update(self, sub_id, newValue):
        try:
            subscription = stripe.Subscription.retrieve(sub_id)
            subscription.tax_percent = 10
            return subscription.save()
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))
        

class Plans(Stripe):

    def GetById(self, plan_name):
        try:
            return stripe.Plan.retrieve(plan_name)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))


    def GetList(self, parameter_list):
        try:
            return stripe.Plan.list(parameter_list)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

class Refounds(Stripe):
    def GetByID(self, refound_id):
        try:
            return stripe.Refund.retrieve(refound_id)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def GetList(self, parameter_list):
        try:
            return stripe.Refund.list(parameter_list)
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))

    def Add(self, charge_id):
        try:
            re = stripe.Refund.create(
                charge=charge_id        )
            return re
        except (stripe.error.RateLimitError, stripe.error.InvalidRequestError, stripe.error.APIConnectionError, stripe.error.StripeError, stripe.error.CardError) as e:
            body = e.json_body
            err  = body.get('error', {})
            print ("Status is: %s" % e.http_status)
            print ("Type is: %s" % err.get('type'))
            print ("Code is: %s" % err.get('code'))
            print ("Param is: %s" % err.get('param'))
            print ("Message is: %s" % err.get('message'))



# x = Customers()
# print (x.GetList())      



import os
from flask import Flask, render_template, request
from flask_restful import reqparse, abort, Api, Resource
import stripe
import json


stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument('cus_description')
parser.add_argument('cus_source')

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    print(request.form)
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

class Cutomers(Resource):
    def get(self):
        customerById = stripe.Customer.list()
        print("Customers....!!!!!!", customerById)
        customer_json=json.loads(str(customerById))
        print(customer_json)
        return str(customer_json)
    def post(self):
        args = parser.parse_args()
        # print("este es request", request.form)
        # print("argumentos", args)
        create_customer= stripe.Customer.create(
            description=args['cus_description'],
            source=args['cus_source'] # obtained with Stripe.js
        )
        return json.loads(str(create_customer))


api.add_resource(Cutomers, '/all')


if __name__ == '__main__':
    app.run(debug=True)

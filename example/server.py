from flask import Flask
from flask_restx import Api, Resource, fields, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='CIR API',
    description='Cloud Impact Rating API', prefix='/v1'
)

from cloudant.client import Cloudant

# Overwrite the values in api_access below with those form your service credential, that you created in IBM Cloud IAM for Cloudant
api_access = {
  "apikey": "-OPMa01VOo5YhaHqHatlzNQiNFF1b31fqlY3hRpc720H",
  "host": "c5abe484-83a8-407e-92f8-b3be0f8f0afe-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key 1547206e-bf1b-466e-b797-7afabfc9b29e",
  "iam_apikey_name": "apiaccess",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/4a35fbbd385a17dc3178b6dc66949178::serviceid:ServiceId-c6da6f0d-c24c-4d28-b15e-ea426501b8d1",
  "url": "https://c5abe484-83a8-407e-92f8-b3be0f8f0afe-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "c5abe484-83a8-407e-92f8-b3be0f8f0afe-bluemix"
}

client = Cloudant.iam(
    api_access['username'],
    api_access['apikey'],
    connect=True
)

cir_db = client['cir-db']

cir_ns = api.namespace('cir', description='User CIR operations')

rating = api.model('Rating', {
    'efficiency': fields.String(required=False, description='The efficiency of this item when in use'),
    'CO2': fields.Integer(required=False, description='The CO2 released to produce this item'),
    'otherGG': fields.Integer(required=False, description='The Other Green House gases released to produce this item'),
    'water': fields.Integer(required=False, description='The volume of water to produce this item'),
    'lifetime': fields.Integer(required=False, description='The expected lifetime of this item')
})

cir = api.model('CIR', {
    'id': fields.String(readonly=True, description='The unique product identifier registered with this CIR'),
    'barcode_id': fields.String(required=True, description='The barcode for this product id, in EAN-13 format'),
    'name': fields.String(required=True, description='The general name for this item'),
    'vendor_id': fields.String(required=True, description='The venfor of this item'),
    'rating': fields.Nested(rating)
})

@cir_ns.route('/')
class CIR(Resource):
    @api.marshal_with(cir)
    @api.doc("Get the ratings for a given product by barcode")
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('barcode_id', required=True, location='args')
        args = parser.parse_args()
        my_document = cir_db[args['barcode_id']]
        return my_document

    @api.marshal_with(cir, code=201)
    def post(self):
        # For now, we'll set the id to be the same as the barcode_id. For production systems, we would
        # probably want these seperate, and to implement more indexed searching by barcode_id for GET.
        api.payload['_id'] = api.payload['barcode_id']
        my_document = cir_db.create_document(api.payload)
        my_document['id'] = my_document['barcode_id']
        return my_document

if __name__ == '__main__':
	app.run()

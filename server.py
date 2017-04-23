from flask import Flask
from pymongo import MongoClient
from flask_restful import Api
from loupe_query import LoupeQuery
from loinc_code import LoincCode
from patient import Patient

app = Flask(__name__)
api = Api(app)

client = None

@app.route("/")
def main():
    return """<b>HII-C Mongo Proxy.</b><br><br>
              You must supply a valid username and password to use this API.
              """

api.add_resource(LoupeQuery, '/loupe_query', '/loupe_query/<string:hash_code>')
api.add_resource(LoincCode, '/loinc_code/<string:code>')
api.add_resource(Patient, '/Patient/<string:patient_id>')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from flask import Flask
from flask_restful import Api
from loupe_query import LoupeQuery
from loinc_code import LoincCode
from patient import Patient
from observation import Observation
from condition import Condition

app = Flask(__name__)
api = Api(app)

client = None


@app.route("/")
def main():
    return """<b>HII-C Mongo Proxy.</b><br><br>
              You must supply a valid username and password to use this API.
              """


api.add_resource(LoupeQuery, '/loupe_query', '/loupe_query/<string:hash_code>', '/loupe_query/<string:hash_code>/')
api.add_resource(LoincCode, '/loinc_code/<string:code>', '/loinc_code/<string:code>/')
api.add_resource(Patient, '/Patient')
api.add_resource(Observation, '/Observation')
api.add_resource(Condition, '/Condition', '/Condition/')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

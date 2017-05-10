from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL
from auth import requires_auth
import json


class Condition(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.Patient

    @requires_auth
    def get(self):
        patient_id = request.args.get('Patient')
        res = self.collection.find_one({'Patient.id': patient_id})
        if res is None:
            print("why")
            return "This patient does not exist"
        else:
            res.pop('_id', None)
            return json.dumps(res['Patient'][0]['resource']['Conditions'])

    @requires_auth
    def post(self):
        patient_id = request.args.get('Patient')
        patient_data = request.get_json(force=True)
        res = self.collection.find_one({'Patient.id': patient_id})
        patientIndex = self.collection.find({'id': {'$lt': patient_id}}).count()
        if (patient_data not in res['Patient'][0]['resource']['Conditions']):
            self.collection.update_one({'Patient.id': patient_id}, {'$addToSet': {('Patient.{}.resource.Conditions').format(patientIndex): patient_data}})
            return "Condition Added"
        else:
            return "This already exists in the Conditions list"
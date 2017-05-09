from flask_restful import Resource
from flask import jsonify, request
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

    def post(self):
        patient_data = request.get_json(force=True)
        if (request.args.get('Condition') not in patient_data['Patient'][0]['Conditions']):
            self.collection.insert_one(patient_data)
            return "Patient Successfully inserted"
        else:
            return "That condition is already been added"

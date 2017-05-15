from flask_restful import Resource
from flask import jsonify, request
from pymongo import MongoClient
from helpers import loadMongoURL
from auth import requires_auth
from bson.json_util import dumps


class OnePatient(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.Patient

    @requires_auth
    def get(self, patient_id):
        if (patient_id is not None):
            res = self.collection.find_one({'Patient.id': patient_id})
            if res is None:
                return "This patient does not exist"
            else:
                res.pop('_id', None)
                return res
        else:
            return "Invalid query"

    @requires_auth
    def post(self):
        patient_data = request.get_json(force=True)
        patient_id = patient_data['Patient'][0]['id']
        # TODO
        if (self.collection.find_one({'Patient.id': patient_id}) is None):
            self.collection.insert_one(patient_data)
            return "Patient Successfully inserted"
        else:
            return "That patient already exists in this database"

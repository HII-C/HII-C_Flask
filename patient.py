from flask_restful import Resource
from flask import jsonify, request
from pymongo import MongoClient
from helpers import loadMongoURL
from auth import requires_auth
from bson.json_util import dumps


class Patient(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.Patient

    @requires_auth
    def get(self):
        patient_id = request.args.get('Patient')
        print(patient_id)
        if (patient_id is not None):
            res = self.collection.find_one({'patient_id': patient_id})
            if res is None:
                print("This patient does not exist")
                return "This patient does not exist"
            else:
                print("This Patient exists")
                res.pop('_id', None)
                return jsonify(dumps(res))
        else:
            res = self.collection.find({})
            if res is None:
                return "There are no patients in the database"
            else:
                return jsonify(dumps(res))

    @requires_auth
    def post(self):
        patient_data = request.get_json(force=True)
        patient_id = patient_data['Patient'][0]['id']
        print(patient_id)
        # TODO
        if (self.collection.find_one({'Patient.id': patient_id}) is None):
            self.collection.insert_one(patient_data)
            return "Patient Successfully inserted"

        else:
            return "That patient already exists in this database"

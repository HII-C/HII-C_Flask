from flask_restful import Resource
from flask import request, jsonify
from pymongo import MongoClient
from helpers import loadMongoURL
from auth import requires_auth


class Observation(Resource):

    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.Patient

    @requires_auth
    def get(self):
        patient_id = request.args.get('Patient')
        res = self.collection.find_one({'Patient.id': patient_id})

        if res is None:
            return "This patient does not exist"

        else:
            res.pop('_id', None)
            return jsonify(res['Patient'][0]['resource']['Observations'])

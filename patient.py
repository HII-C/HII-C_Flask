from flask_restful import Resource
from flask import jsonify
from pymongo import MongoClient
from helpers import loadMongoURL
# from auth import requires_auth


class PatientAll(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.Patient

    # @requires_auth
    def get(self):
        res = self.collection.find({})
        if res is None:
            return "There are no patients in the database"
        else:
            returnDict = list()
            for item in res:
                item.pop('_id', None)
                returnDict.append(item)
            return returnDict

from flask_restful import Resource
from pymongo import MongoClient
from helpers import loadMongoURL
from auth import authenticate


class LoincCode(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.loinc


    def get(self, code):
        res = self.collection.find_one({'LOINC_NUM': code})

        if res is None:
            return {}

        res.pop('_id', None)

        return res

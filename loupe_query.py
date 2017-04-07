from flask_restful import Resource
from pymongo import MongoClient
from helpers import loadMongoURL

class LoupeQuery(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.outputs
    def get(self, hash_code):
        return str(self.collection.find_one({'hash': hash_code}))

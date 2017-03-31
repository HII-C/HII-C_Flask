from flask_restful import Resource
from pymongo import MongoClient

class LoupeQuery(Resource):
    def __init__(self):
        self.client = MongoClient()
        self.collection = client.test.outputs
    def get(self, hash_code):
        return self.collection.find_one({'hash': hash_code})

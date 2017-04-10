from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL

import json

class LoupeQuery(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.outputs
    def get(self, hash_code):
        res = self.collection.find_one({'hash': hash_code})

        if res == None:
            return json.dumps({})

        res.pop('_id', None)

        return json.dumps(res)

    def post(self):
        body = request.get_json(force=True)
        self.collection.insert_one(body)

        res = {'success': True, 'message': 'The loupe query was successfully inserted.'}

        return json.dumps(res)

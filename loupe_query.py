from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL

import json

def validate_post(json):
    return (json != None) and ('hash' in json) and ('output' in json)

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
        json = request.get_json(force=True)

        message = ''

        if validate_post(json):
            if self.collection.find_one({'hash': json['hash']}) != None:
                message = 'A loupe query with the provided hash already exists.'
            else:
                self.collection.insert_one(json)
                message = 'The loupe query was successfully inserted.'
        else:
            message = 'The POST request is malformed.'

        res = {'success': True, 'message': message}

        return json.dumps(res)

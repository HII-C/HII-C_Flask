from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL

import json

def validate_post(body):
    return (body != None) and ('hash' in body) and ('output' in body)

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

        message = ''
        success = False

        if validate_post(body):
            if self.collection.find_one({'hash': body['hash']}) != None:
                message = 'A loupe query with the provided hash already exists.'
            else:
                self.collection.insert_one(body)
                message = 'The loupe query was successfully inserted.'
                success = True
        else:
            message = 'The POST request is malformed.'

        res = {'success': success, 'message': message}
        
        return json.dumps(res)

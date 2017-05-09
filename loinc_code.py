from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL
from auth import authenticate
import json

class LoincCode(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.loinc

    @authenticate
    def get(self, code):
        res = self.collection.find_one({'LOINC_NUM': code})

        if res == None:
            return {}

        res.pop('_id', None)

        return res

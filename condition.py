from flask_restful import Resource
from flask import request
import os
import pprint
from pymongo import MongoClient
from helpers import loadMongoURL
import json

class Condition(Resource):
	def __init__(self):
		self.client = MongoClient(loadMongoURL())
		self.collection = self.client.test.Patient

	def get(self):
		patient_id = request.args.get('Patient')
		res = self.collection.find_one({'Patient.id': patient_id})

		if res == None:
			return "This patient does not exist"

		else:
			res.pop('_id', None)
			return res['Patient'][0]['resource']['Conditions']

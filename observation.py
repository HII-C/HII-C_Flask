from flask_restful import Resource
from flask import request
import os
import pprint
from pymongo import MongoClient
from helpers import loadMongoURL
import json

class Observation(Resource):
	def __init__(self):
		self.client = MongoClient(loadMongoURL())
		self.collection = self.client.test.Patient

	def get(self):
		patient_id = request.args.get('Patient')
		res = self.collection.find_one({'Patient.id': patient_id})

		print(patient_id)

		if res == None:
			print("This patient does not exist")
			return "This patient does not exist"

		else:
			print("This Patient exists")
			res.pop('_id', None)
			return res['Patient'][0]['resource']['Observations']

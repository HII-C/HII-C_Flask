from flask_restful import Resource
import os
import pprint
from pymongo import MongoClient
from helpers import loadMongoURL
import json

class Patient(Resource):
	def __init__(self):
		self.client = MongoClient(loadMongoURL())
		self.collection = self.client.test.Patient


	def get(self, patient_id):
		res = self.collection.find_one({'patient_id': patient_id})

		if res == None:
			print("This patient does not exist")
			return "This patient does not exist"

		else:
			print("This Patient exists")
			res.pop('_id', None)
			return res

	def post(self):

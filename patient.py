import os
import pprint
from pymongo import MongoClient
from helpers import loadMongoURL
import json

class Patient(Resource):
	def __init__(self):
		self.client = MongoClient(loadMongoURL())
		connection = client.test.loinc

	def get(self, patient_id):
		res = self.collection.find_one({''})
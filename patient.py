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
		res = self.collection.find_one({'patientId': patient_id})

		if res == None:
			print "That Patient does not exist in the system"
			return {}

		else:
			print "This Patient exists"
			return res
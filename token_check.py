from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL
#TODO Get rid of requests in favor of flask/request
import requests


class TokenCheck(Resource):
    def __init__(self):
        self.client = MongoClient(loadMongoURL())
        self.collection = self.client.test.Patient

    def post(self):
        code = request.form['code']
        redirect_uri = request.form['redirect_uri']
        token_url = request.form['token_url']
        data = 'grant_type=authorization_code&code=' + code + '&redirect_uri=' + redirect_uri
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        client = '160324a1-e8fa-440c-8068-0f482701f1e8'
        client_secret = 'HNjyMOK6SkdVFuilQSuORvQ8duqg4DD7yJ0weZE3Vfffsfl3nY9JLOQewg-arYxSlnLkDh9c3Ldj5hfUQ2zUoA'
        res = requests.post(token_url, headers=headers, auth=(client, client_secret), data=data)
        return res.json()

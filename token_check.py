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
        client = 'e848c885-be81-45e3-a441-14ab1cc6ad55'
        client_secret = 'AfqgsKVOtE2VcasgXUZu4M_JCkNee1yvkaryDsjSoyoxQRPqmQrgyHePppPn2oAEg-BJvxKgQErYnHZaeYLUiA'
        res = requests.post(token_url, headers=headers, auth=(client, client_secret), data=data)
        return res.json()

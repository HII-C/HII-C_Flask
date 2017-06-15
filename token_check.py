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
        client = '82b330f7-1186-4059-8c31-62dce4b18d77'
        client_secret = 'AKgTeRtUGHrr3Eu7HF0fJf6DfbrLTk2ieyeSpR0KUweizQWfqZICOYjHjUbXegMajNhTgQEKt5AZryb_5KAZTIs'

        res = requests.post(token_url, headers=headers, auth=(client, client_secret), data=data)
        return res.json()

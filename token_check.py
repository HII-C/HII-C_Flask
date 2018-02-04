from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL
#TODO Get rid of requests in favor of flask/request
import requests


class TokenCheck(Resource):
    def __init__(self):
        pass
        # self.client = MongoClient(loadMongoURL())
        # self.collection = self.client.test.Patient

    def post(self):
        code = request.form['code']
        redirect_uri = request.form['redirect_uri']
        token_url = request.form['token_url']
        data = 'grant_type=authorization_code&code=' + code + '&redirect_uri=' + redirect_uri
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        client = '2c304df8-711d-4de9-afbe-330c01a5ca8e'
        client_secret = 'O7mfO8pNJMLC6Sm34OYIjgFYiips-1H2uKHuGqC0nVDIOA_N3Ec-bm4y6-nIyGVLZuL1b5UawPBgrXn-njUw_w'#'AKgTeRtUGHrr3Eu7HF0fJf6DfbrLTk2ieyeSpR0KUweizQWfqZICOYjHjUbXegMajNhTgQEKt5AZryb_5KAZTIs'

        res = requests.post(token_url, headers=headers, auth=(client, client_secret), data=data)
        return res.json()

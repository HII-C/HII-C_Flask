from flask_restful import Resource
from flask import request
from pymongo import MongoClient
from helpers import loadMongoURL
import requests


class ProdTokenCheck(Resource):
    def __init__(self):
        pass

    def post(self):
        code = request.form['code']
        redirect_uri = request.form['redirect_uri']
        token_url = request.form['token_url']
        data = 'grant_type=authorization_code&code=' + code + '&redirect_uri=' + redirect_uri
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        client = 'cff2305a-a6ec-4885-bc64-8b76a1425229'
        client_secret = 'AMdda7TDW5cL6cXTVcAjivVQ4JVfznxN0blMniZAu4HLHqQ6IhdMY1vW5YrY3IIJi0PTVZWCqhbwDDEWdYLF_a8'

        res = requests.post(token_url, headers=headers, auth=(client, client_secret), data=data)
        return res.json()

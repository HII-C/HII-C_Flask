from flask import Flask
from pymongo import MongoClient
from flask_restful import Api
from loupe_query import LoupeQuery

app = Flask(__name__)
api = Api(app)

client = None

@app.route("/")
def main():
    return "HII-C MongoDB Interface"

api.add_resource(LoupeQuery, '/loupe_query')

if __name__ == "__main__":
    #client = MongoDB('mongodb://localhost:27017/')
    app.run()

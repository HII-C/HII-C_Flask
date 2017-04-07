from flask import Flask
from pymongo import MongoClient
from flask_restful import Api
from loupe_query import LoupeQuery

app = Flask(__name__)
api = Api(app)

client = None

f = open('mongo.txt')
MONGO_URL = f.readline().strip('\n')
f.close()

@app.route("/")
def main():
    return "HII-C MongoDB Interface"

api.add_resource(LoupeQuery, '/loupe_query/<string:hash_code>')

if __name__ == "__main__":
    app.debug = True
    app.run()

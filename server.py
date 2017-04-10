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

api.add_resource(LoupeQuery, '/loupe_query', '/loupe_query/<string:hash_code>')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

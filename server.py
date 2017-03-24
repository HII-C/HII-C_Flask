from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = None

@app.route("/")
def main():
    return "HII-C MongoDB Interface"

if __name__ == "__main__":
    client = MongoDB('mongodb://localhost:27017/')
    app.run()

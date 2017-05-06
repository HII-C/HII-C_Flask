import os
import csv
import pprint
from pymongo import MongoClient
from helpers import loadMongoURL

LOINC_NUM = 0
COMPONENT = 1
SYSTEM = 4
ROWS = 83377

if __name__ == '__main__':
    client = MongoClient(loadMongoURL())
    collection = client.test.loinc

    #Delete previous LOINC documents.
    collection.delete_many({})

    with open('loinc.csv') as f:
        reader = csv.reader(f)

        #Skip over the first row, which contains the column names.
        reader.__next__()

        for i in range(0, ROWS):
            res = reader.__next__()
            doc = {
                'LOINC_NUM': res[LOINC_NUM],
                'COMPONENT': res[COMPONENT],
                'SYSTEM': res[SYSTEM]
            }

            collection.insert_one(doc)

            if i % 1000 == 0:
                print("Inserted " + str(i) + " documents.")

    client.close()

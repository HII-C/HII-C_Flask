from flask_restful import Resource

class LoupeQuery(Resource):
    def get(self):
        return {'data': 'LoupeQuery'}

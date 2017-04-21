from flask import request, Response
import os

def authenticate(func):
    def wrapper(*args, **kwargs):
        username = os.environ.get('USER') or 'user'
        password = os.environ.get('PASS') or 'pass'

        auth = request.authorization

        if not auth or username != auth.username or password != auth.password:
            return {'error': 'You are not authorized to access this resource.'}

        func(*args, **kwargs)

    return wrapper

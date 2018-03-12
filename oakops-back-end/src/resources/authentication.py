from flask_restful import Resource, abort, reqparse
from flask import request, g
import pprint, json, md5, re, time, os


class Authentication(Resource):
    def __init__(self):
        super(Authentication, self).__init__()

    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('username', location='args', required=True)
        # parser.add_argument('password', location='args', required=True)

        return {'ok': 200 }


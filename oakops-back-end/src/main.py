from flask import Flask, g
from flask_restful import Api
import sqlite3, re
from pprint import pprint

application = Flask(__name__)
api = Api(application)

from resources import Authentication

api.add_resource(Authentication, "/oakops/v0/login")

if __name__ == "__main__":
    application.run(host='0.0.0.0')


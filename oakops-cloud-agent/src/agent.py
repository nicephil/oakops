from flask import Flask, g
from flask_restful import Api
from pprint import pprint

from organization import OrganizationList

application = Flask(__name__)
api = Api(application)

ROOT_URL_v0 = "/cloud/agent/v0/"

api.add_resource(OrganizationList,  ROOT_URL_v0+"organization")

@application.route("/")
def app():
     return "cloud agent!"

if __name__ == "__main__":
    application.run(host='0.0.0.0')


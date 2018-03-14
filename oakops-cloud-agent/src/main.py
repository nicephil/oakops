#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, g
from flask_restful import Api
from pprint import pprint

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from organization import OrganizationList



application = Flask(__name__)
application.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(application)

ROOT_URL_v0 = "/agent/cloud/v1/"

api.add_resource(OrganizationList,  ROOT_URL_v0+"organization")

@application.route("/")
def app():
     return "cloud agent!"

if __name__ == "__main__":
    application.run(host='0.0.0.0')


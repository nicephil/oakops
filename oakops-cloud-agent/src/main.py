#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, g
from flask_restful import Api
from pprint import pprint

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

from resources import OrganizationList



app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)

ROOT_URL_v0 = "/agent/cloud/v1/"

api.add_resource(OrganizationList,  ROOT_URL_v0+"organizations/sites")

@app.route("/")
def agent():
     return "cloud agent!"

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--port', type=int, default = 5001)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)


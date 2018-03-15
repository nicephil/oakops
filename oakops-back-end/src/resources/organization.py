# -*- coding: UTF-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required)
import requests

cloud_agent_root_url='http://cloud.oakridge.io/agent/cloud/v1'

class OrganizationList(Resource):
    def __init__(self):
        super(OrganizationList,self).__init__()

    # @jwt_required
    def get(self):
        res = requests.get(cloud_agent_root_url + "/organizations")
        return res.json()


class SiteList(Resource):
    def get(self):
        return {
            
        }
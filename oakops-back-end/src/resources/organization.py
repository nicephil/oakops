# -*- coding: UTF-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required)
import requests
from flask import request

cloud_agent_root_url='http://cloud.oakridge.io/agent/cloud/v1'

class OrganizationList(Resource):
    def __init__(self):
        super(OrganizationList,self).__init__()

    @jwt_required
    def get(self):
        url = cloud_agent_root_url + "/organizations/sites"
        full_path = request.full_path
        index = full_path.find('?')
        if index != -1:
            url = url + full_path[index:]
        print(url)
        res = requests.get(url)
        return res.json()

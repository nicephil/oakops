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
            "error_code": 0,
            "total": 4,
            "list": [
                {
                "device_total": 2,
                "device_offline": 0,
                "zone_id": "Asia/Shanghai",
                "parent_name": "Oak-xxia",
                "country": "CN",
                "device_unused": 0,
                "name": "Oak-xxia-hz",
                "parent_id": 2,
                "customer_type": 1,
                "total_bytes": 0,
                "address": "杭州市",
                "client_online": 1,
                "id": 3,
                "device_online": 2
                },
                {
                "device_total": 99,
                "device_offline": 10,
                "zone_id": "Asia/Shanghai",
                "parent_name": "Oak-xxia",
                "country": "CN",
                "device_unused": 2,
                "name": "Oak-xxia-test1",
                "parent_id": 2,
                "customer_type": 2,
                "total_bytes": 0,
                "address": "大星海纯k.高新店",
                "client_online": 188,
                "id": 32,
                "device_online": 0
                },
                {
                "device_total": 10,
                "device_offline": 10,
                "zone_id": "Asia/Shanghai",
                "parent_name": "hh-oak-hz",
                "country": "CN",
                "device_unused": 0,
                "name": "hh-oak-hz",
                "parent_id": 33,
                "customer_type": 2,
                "total_bytes": 0,
                "address": "红河哈尼族彝族自治州",
                "client_online": 0,
                "id": 34,
                "device_online": 0
                },
                {
                "device_total": 0,
                "device_offline": 0,
                "zone_id": "Asia/Shanghai",
                "parent_name": "test",
                "country": "CN",
                "device_unused": 0,
                "name": "test",
                "parent_id": 49,
                "customer_type": 2,
                "total_bytes": 0,
                "address": "爱丝特(esther)甜品烘焙",
                "client_online": 0,
                "id": 50,
                "device_online": 0
                }
            ]
        }
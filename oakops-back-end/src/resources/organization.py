#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_restful import Resource
import requests

class OrganizationList(Resource):
    def __init__(self):
        super(OrganizationList,self).__init__()

    def get(self):
        res = requests.get("http://cloud.oakridge.io:5000/agent/cloud/v1/organizations")
        return res.json()
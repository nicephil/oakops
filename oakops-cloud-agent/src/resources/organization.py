#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_restful import Resource
import json

from common import DBUtils


class OrganizationList(Resource):
    def __init__(self):
        self.dbutils = DBUtils()
        super(OrganizationList,self).__init__()

    def get(self):
        res = dict()
        res["error_code"] = 0
        orgs = []
        dbResult = self.dbutils.executeQuery("select id,name,address,country,zone_id,parent_id,customer_type,type from organization_info where parent_id > 0 order by id",None)
        for row in dbResult:
            item = dict()
            item["id"] = row[0]
            item["name"] = row[1]
            if row[2] is not None:
                item["address"] = row[2]
            item["country"] = row[3]
            item["zone_id"] = row[4]
            item["parent_id"] = row[5]
            item["customer_type"] = row[6]
            item["children"] = []
            if row[7] == 1:
                orgs.append(item)#business
            else:
                for parent in orgs:
                    if parent["id"] == item["parent_id"]:
                        parent["children"].append(item)#site
        res["list"] = orgs    
        
        return res
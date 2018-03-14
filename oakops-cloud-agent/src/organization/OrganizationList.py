#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_restful import Resource
import json

from db import DBUtils


class OrganizationList(Resource):
    def __init__(self):
        self.dbutils = DBUtils()
        super(OrganizationList,self).__init__()

    def get(self):
        result = []
        res = self.dbutils.executeQuery("select id, name, address, type, parent_id, customer_type from organization_info where parent_id > 0 order by id",None)
        for row in res:
            item = dict()
            item["id"] = row[0]
            item["name"] = row[1]
            if row[2] is not None:
                item["address"] = row[2]
            item["parent_id"] = row[4]
            item["customer_type"] = row[5]
            item["children"] = []
            if row[3] == 1:
                # business
                result.append(item)
            else:
                for parent in result:
                    if parent["id"] == row[4]:
                        parent["children"].append(item)
            
        
        return result
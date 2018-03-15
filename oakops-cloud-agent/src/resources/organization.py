#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask_restful import Resource
import json
from flask_restful import reqparse

from common import DBUtils


class OrganizationList(Resource):
    def __init__(self):
        self.dbutils = DBUtils()
        super(OrganizationList,self).__init__()

    def get(self):
        # parse parameter
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, location='args', required=False, default = 1)
        parser.add_argument('page_size', type =int,location='args', required=False, default = 10)
        parser.add_argument('sort', type=str, location='args', required=False, default = 'id')
        parser.add_argument('cond', type=str, location='args', required=False)
        args = parser.parse_args()
        page = args['page']
        page_size = args['page_size']
        sort = args['sort']
        cond = args['cond']
        
        res = dict()
        res['error_code'] = 0
        orgs = []

        fields = "type,id,name,address,country,zone_id,parent_id,customer_type,client_online,device_total,device_online,device_offline,device_unused,total_bytes"
        condSql = ""
        if cond is not None :
            condSql = " and " + cond
        orderSql = " order by " + sort
        limitSql = ' limit ' + str(page_size) + ' offset ' + str((page-1) * page_size)

        # get total 
        sql = "select count(1) from organization_info where type = 2 " + condSql
        dbResult = self.dbutils.executeQuery(sql,None)
        for row in dbResult:
            res["total"] = row[0]
            break

        sql = "select " + fields + " from organization_info where type = 2 " + condSql + orderSql + limitSql
        dbResult = self.dbutils.executeQuery(sql,None)

        for row in dbResult:
            item = dict()
            item["id"] = row[1]
            item["name"] = row[2]
            if row[3] is not None:
                item["address"] = row[3]
            item["country"] = row[4]
            item["zone_id"] = row[5]
            item["parent_id"] = row[6]
            item["customer_type"] = row[7]
            item["client_online"] = row[8]
            item["device_total"] = row[9]
            item["device_online"] = row[10]
            item["device_offline"] = row[11]
            item["device_unused"] = row[12]
            item["total_bytes"] = row[13]
            orgs.append(item)

        # get parent name
        dbResult = self.dbutils.executeQuery("select id, name from organization_info where type = 1",None)
        for row in dbResult:
            for item in orgs:
                if item["parent_id"] == row[0]: item["parent_name"] = row[1]
            
        res["list"] = orgs    
        
        return res
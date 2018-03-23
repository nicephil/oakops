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
        parser.add_argument('search', type =str,location='args', required=False, default = '')
        parser.add_argument('sort', type=str, location='args', required=False, default = 'id')
        parser.add_argument('status', type=int, location='args', required=False, default = None, action='append')
        parser.add_argument('customer_types', type=int, location='args', required=False, default = None, action='append')
        args = parser.parse_args()
        page = args['page']
        page_size = args['page_size']
        search = args['search']
        sort = args['sort']
        status = args['status']
        customer_types = args['customer_types']
        
        res = dict()
        res['error_code'] = 0
        orgs = []

        fields = '''o.type as type,o.id as id,o.name as name,o.address as address,o.country as country,o.zone_id as zone_id,o.parent_id as parent_id, 
            p.name as parent_name,o.customer_type as customer_type,o.client_online as client_online,o.device_total as device_total,o.device_online as device_online,
            o.device_offline as device_offline,o.device_unused as device_unused,o.total_bytes as total_bytes, o.status as status, oci.name as nms,
            ui.email as owner, o.sponsor as sponsor'''
        condParams = []
        condSql = " where o.type = 2 "
        if (search is not None and search.strip() != ''):
            condSql += " and (o.name like  %s or p.name like %s or ui.email like %s)"
            condParams.append('%'+search+'%')
            condParams.append('%'+search+'%')
            condParams.append('%'+search+'%')
        if (status is not None and len(status) > 0):
            arg_list = ','.join(['%s'] * len(status))
            condSql += " and o.status in (" + arg_list + ")"
            for value in status:
                condParams.append(value)
        if (customer_types is not None and len(customer_types) > 0):
            arg_list = ','.join(['%s'] * len(customer_types))
            condSql += " and o.customer_type in (" + arg_list + ")"
            for value in customer_types:
                condParams.append(value)
        print(condSql)
        orderSql = " order by " + sort
        limitSql = ' limit ' + str(page_size) + ' offset ' + str((page-1) * page_size)

        fromSql = ''' from organization_info o left join organization_info p on p.id = o.parent_id left join oauth_client_info oci on oci.id = o.oauth_client_id 
                 left join user_info ui on ui.user_label = p.owner'''
        # get total 
        sql = "select count(1) {} {}".format(fromSql,condSql)
        dbResult = self.dbutils.executeQuery(sql,condParams)
        for row in dbResult:
            res["total"] = row[0]
            break

        sql = "select {} {} {} {} {}".format(fields,fromSql,condSql,orderSql,limitSql)
        dbResult = self.dbutils.executeQuery(sql,condParams)

        for row in dbResult:
            i = 1
            item = dict()
            item["id"] = row[i];i+=1
            item["name"] = row[i];i+=1
            if row[i] is not None:
                item["address"] = row[i]
            i+=1
            item["country"] = row[i];i+=1
            item["zone_id"] = row[i];i+=1
            item["parent_id"] = row[i];i+=1
            item["parent_name"] = row[i];i+=1
            item["customer_type"] = row[i];i+=1
            item["client_online"] = row[i];i+=1
            item["device_total"] = row[i];i+=1
            item["device_online"] = row[i];i+=1
            item["device_offline"] = row[i];i+=1
            item["device_unused"] = row[i];i+=1
            item["total_bytes"] = row[i];i+=1
            item["status"] = row[i];i+=1
            item["nms"] = row[i];i+=1
            item["owner"] = row[i];i+=1
            item["sponsor"] = row[i];i+=1
            orgs.append(item)
            
        res["list"] = orgs    
        
        return res
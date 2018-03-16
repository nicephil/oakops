#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import json

config = {
    'host': '127.0.0.1',
    'user': 'oakridge',
    'password': 'oakridge',
    'port': 3306,
    'database': 'authc',
    'charset': 'utf8',
    'use_unicode' : True
}

class DBUtils:
    def executeUpdate(self, sql, params):
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()
        except Exception as e:
            print('connect fails!{}'.format(e))
            return
        try:
            result = cursor.execute(sql, params)
        except Exception as e:
            print('connect fails!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
        return result

    def executeQuery(self, sql, params):
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()
        except Exception as e:
            print('connect fails!{}'.format(e))
            return
        try:
            cursor.execute(sql, params)
            res = cursor.fetchall()
        except Exception as e:
            print('execute query fails!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
        return res
    
    def executeQueryAndReturnDictList(self, sql, params):
        result = []
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()
        except Exception as e:
            print('connect fails!{}'.format(e))
            return
        try:
            cursor.execute(sql, params)
            res = cursor.fetchall()
            index = cursor.description
            
            for row in res:
                item = dict()
                for i in range(len(index)) :
                    item[index[i][0]] = row[i]
                result.append(item)
            
        except Exception as e:
            print('execute query fails!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
        return result
   
'''
util = DBUtils()
res = util.executeQueryAndReturnDict("select id,name,address from organization_info;",None)
print(json.dumps(res,ensure_ascii=False))
'''
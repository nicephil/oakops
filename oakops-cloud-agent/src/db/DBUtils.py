import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'oakridge',
    'password': 'oakridge',
    'port': 3306,
    'database': 'authc',
    'charset': 'utf8'
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
            print('connect fails!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
        return res

'''        
util = DBUtils()
res = util.executeQuery("select id,name from organization_info;",None)
print(res)
'''
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'oakridge',
    'password': 'oakridge',
    'port': 3306,
    'database': 'authc',
    'charset': 'utf8'
}

try:
    cnn = pymysql.connect(**config)
except Exception as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
try:
    sql_query = 'select id,name from organization_info;'
    cursor.execute(sql_query)
    for id, name in cursor:
        print (id, name)
except Exception as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()

class DBUtils:
    def executeUpdate(self, sql, params):
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()
        except Exception as e:
            print('connect fails!{}'.format(e))
            return
        try:
            cursor.execute(sql, params)
        except Exception as e:
            print('connect fails!{}'.format(e))
        finally:
            cursor.close()
            conn.close()
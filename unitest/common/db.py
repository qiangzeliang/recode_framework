import pymysql

from unitest.readConfig import ReadConfig
# 获取连接方法
import pymysql
import json
db = ReadConfig()
# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=db.get_db("host"),
                           port=int(db.get_db("port")),
                           user=db.get_db("username"),
                           passwd=db.get_db("password"),
                           db=db.get_db("database"),
                           charset=db.get_db("charset"))  # 如果查询有中文，需要指定测试集编码
    return conn


# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    cur.execute(sql)  # 执行sql
    result = cur.fetchall()  # 获取所有查询结果
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果


# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接


# 封装常用数据库操作
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from city where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False


def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    change_db(sql)


def del_user(name):
    sql = "delete from user where name='{}'".format(name)
    change_db(sql)


print(get_db_conn())

yu = query_db("select * from city")
print(yu)

for i in yu:
    print(i)
    li = list(i)
    print(li[3])


tuplex = ((2, "w"),(3, "r"),(6, "x"))
print(dict((y, x) for x, y in tuplex))


print(check_user("Eindhoven"))
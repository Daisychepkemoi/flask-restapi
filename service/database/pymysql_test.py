import pymysql
from service.database.db_connect import db_connect 
conn = db_connect.connect()
# conn = pymysql.Connect(host='sql9.freesqldatabase.com', user='sql9636212', passwd='rHGDvEsIUR', database="sql9636212")

cursor = conn.cursor()
sql_query = """CREATE TABLE  IF NOT EXISTS Book (
    id integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
    
    )"""
cursor.execute(sql_query)
conn.close()

import pymysql
class db_connect():
    def connect():
        conn = pymysql.connect(
                host = "sql9.freesqldatabase.com",
                database = "sql9636212",
                user = "sql9636212",
                password = "rHGDvEsIUR",
                charset = "utf8mb4",
                cursorclass = pymysql.cursors.DictCursor
            )
        return conn 


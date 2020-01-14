import sqlite3


class DBConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


# db = "L7_DB.db"
# with DBConn(db) as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM employee")
#     for i in cursor:
#         print(i)
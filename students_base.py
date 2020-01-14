from db_cm import DBConn


class User:

    def get_best_students(self):
        sql = """SELECT students.id, first_name, second_name, department, class, num_of_stud, month1, 
            month2, month3, month4, month5 FROM students 
            INNER JOIN rates ON students.rating_id = rates.id 
            WHERE month1=5 and month2=5 and month3=5 and month4=5 and month5=5"""
        self.get_from_base(sql)

    def get_students(self):
        sql = """SELECT students.id, first_name, second_name, department, class, num_of_stud, month1, 
            month2, month3, month4, month5 FROM students 
            INNER JOIN rates ON students.rating_id = rates.id """
        self.get_from_base(sql)

    def get_by_snumber(self, snumber):
        sql = """SELECT students.id, first_name, second_name, department, class, num_of_stud, month1, 
                month2, month3, month4, month5 FROM students 
                INNER JOIN rates ON students.rating_id = rates.id 
                WHERE num_of_stud=?"""
        with DBConn("students.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql, [snumber])
            rows = 0
            for i in cursor:
                print(i)
                rows += 1
            if rows == 0:
                print(f"No results for {snumber}")

    @staticmethod
    def get_from_base(sql):
        with DBConn("students.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            for i in cursor:
                print(i)


class Admin(User):

    def add_student(self):
        pass

    def change_student(self, num_of_stud):
        pass


user = User()
user.get_by_snumber(1643)
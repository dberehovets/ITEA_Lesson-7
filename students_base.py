from db_cm import DBConn


class User:

    def get_best_students(self):
        sql = """SELECT students.id, first_name, second_name, department, class, num_of_stud, month1, 
            month2, month3, month4, month5 FROM students 
            INNER JOIN rates ON students.id = rates.id 
            WHERE month1=5 and month2=5 and month3=5 and month4=5 and month5=5"""
        self._get_from_base(sql)

    def get_students(self):
        sql = """SELECT students.id, first_name, second_name, department, class, num_of_stud, month1, 
            month2, month3, month4, month5 FROM students 
            INNER JOIN rates ON students.id = rates.id """
        self._get_from_base(sql)

    def get_by_snumber(self, snumber):
        sql = """SELECT students.id, first_name, second_name, department, class, num_of_stud, month1, 
                month2, month3, month4, month5 FROM students 
                INNER JOIN rates ON students.id = rates.id 
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
    def _get_from_base(sql):
        with DBConn("students.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            for i in cursor:
                print(i)


class Admin(User):

    def add_student(self):
        student_info = self._get_info()
        rates_list = list(map(int, input("List of rates (5):\n").split()))
        sql = "INSERT INTO students (first_name, second_name, department, class, num_of_stud) VALUES (?, ?, ?, ?, ?)"
        sql2 = "INSERT INTO rates (month1, month2, month3, month4, month5) VALUES (?, ?, ?, ?, ?)"
        with DBConn("students.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql2, rates_list)
            cursor.execute(sql, student_info)
            conn.commit()

    def update_student(self, num_of_stud):
        self.get_by_snumber(num_of_stud)
        student_info = self._get_info()
        rates_changing = input("Type Y if you would like to update rates or N to skip:\n")

        rates_list = []
        sql_rates = ""
        if rates_changing in "Yy":
            rates_list = list(map(int, input("List of rates (5):\n").split()))
            sql_rates = """UPDATE rates SET month1=?, month2=?, month3=?, month4=?, month5=? 
            WHERE id = (SELECT id FROM students WHERE num_of_stud=?)"""

        sql = "UPDATE students SET first_name=?, second_name=?, department=?, class=?, num_of_stud=? WHERE num_of_stud=?"

        with DBConn("students.db") as conn:
            cursor = conn.cursor()
            if sql_rates != "":
                cursor.execute(sql_rates, [*rates_list, num_of_stud])
            cursor.execute(sql, [*student_info, num_of_stud])
            conn.commit()

    @staticmethod
    def _get_info():
        name = input("Type name:\n")
        second_name = input("Type second name:\n")
        department = input("Department:\n")
        group = input("Group:\n")
        num_of_stud = input("Number of student ticket:\n")
        return [name, second_name, department, group, num_of_stud]


user = Admin()
user.update_student(1515)
user.get_students()
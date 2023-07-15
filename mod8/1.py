import sqlite3

conn = sqlite3.connect('db2.sqlite')
cur = conn.cursor()
cur.execute("CREATE TABLE Students (id int, name VARCHAR(32), surname VARCHAR(32), age int, city VARCHAR(32))")
cur.execute("CREATE TABLE Courses (id int, name VARCHAR(32), time_start DATE, time_end DATE)")
cur.execute("CREATE TABLE Student_Courses (id int, student_id int, course_id int,"
            "FOREIGN KEY(course_id) REFERENCES Courses(id), FOREIGN KEY(student_id) REFERENCES Students(id))")
cur.executemany("INSERT INTO Courses VALUES (?,?,?,?)", [(1, 'python', "2021-07-21", "2021-08-21"),
                                                         (2, 'java', "2021-07-13", "2021-08-16")])
cur.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", [(1, 'Max', 'Brooks', 24, 'Spb'),
                                                           (2, 'John', 'Stones', 15, 'Spb'),
                                                           (3, 'Andy', 'Wings', 45, 'Manhester'),
                                                            (4, 'Kate', 'Brooks', 34, 'Spb')])
cur.executemany("INSERT INTO Student_Courses VALUES(?,?,?)", [(1, 1, 1), (2, 2, 1), (3, 3, 1), (4, 4, 2)])
conn.commit()
cur.execute("SELECT * FROM Student_Courses JOIN Students ON Student_Courses.student_id = Students.id")
cur.execute("SELECT * FROM Student_Courses JOIN Courses ON Student_Courses.course_id = Courses.id")
conn.commit()
cur.execute("SELECT Students.name FROM Students INNER JOIN Student_Courses ON"
            " Student_Courses.student_id = Students.id  where course_id  == 1 AND city =='Spb' ")
print(cur.fetchall())
cur.execute("SELECT name FROM Students where age > 30")
print(cur.fetchall())
cur.execute("SELECT Students.name FROM Students INNER JOIN Student_Courses ON"
            " Student_Courses.student_id = Students.id  where course_id  == 1")
print(cur.fetchall())
conn.close()

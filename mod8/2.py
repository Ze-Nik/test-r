from peewee import *

conn = SqliteDatabase('db2.sqlite')


class Students(Model):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn


class Courses(Model):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')

    class Meta:
        database = conn


class Student_Courses(Model):
    id = IntegerField(column_name='id')
    student_id = IntegerField(column_name='student_id')
    course_id = IntegerField(column_name='course_id')

    class Meta:
        database = conn


for student in Students.select():
    if student.age > 30:
        print(student.name)

print()
k = []
for student in Student_Courses.select():
    if student.course_id == 1:
        k.append(student.student_id)
for student in Students.select():
    if student.id in k:
        print(student.name)
print()
for student in Students.select():
    if student.id in k and student.city =='Spb':
        print(student.name)




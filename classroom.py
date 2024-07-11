from relation import Relator 
import sqlite3

con=sqlite3.connect("studentdb.db")
cur=con.cursor()
cur.execute('''create table if not exists students(
studentID integer primary key,
name varchar(100), 
age integer,
gender varchar(100),
classroom varchar(20),
cca varchar(100))''')
insertSQL = "INSERT INTO students values(%s,%s,%s,%s,%s,%s)"
con.commit()
class Student(Relator):
  def __init__(self, name, age, gender):
    super().__init__(name)
    self.age = age
    self.gender = gender
class Classroom(Relator):
  def __init__(self, name, level):
    super().__init__(name)
    self.level = level
class School(Relator):
  def __init__(self, name, level):
    super().__init__(name)
    self.level = level
class CCA(Relator):
  def __init__(self, name, genre):
    super().__init__(name)
    self.genre = genre

ABCHS=School("ABC High School", "High School")
ABCHS+[Classroom("1.01",1),Classroom("1.02",1),Classroom("1.03",1),Classroom("2.01",2),Classroom("2.02",2),Classroom("2.03",2)]
print("Classes:", ABCHS.children_names())

for d in cur:
  print(d)
con.close()
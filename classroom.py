from relation import Relator 
import sqlite3

con=sqlite3.connect("studentdb.db")
cur=con.cursor()

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
ABCHS+[
  Classroom("1.01",1),
  Classroom("1.02",1),
  Classroom("1.03",1),
  Classroom("2.01",2),
  Classroom("2.02",2),
  Classroom("2.03",2)
]
ABCHS+[
  CCA("Band", "Performing Arts"),
  CCA("Chess Club", "Clubs"),
  CCA("Football", "Sports"),
  CCA("Basketball", "Sports"),
  CCA("Robotics Club", "Clubs"),
  CCA("Girl Scouts","Uniform Groups")
]
print("Classes:", ABCHS.children_is_type_names(Classroom))
print("CCAs:", ABCHS.children_is_type_names(CCA))

cur.execute('SELECT * FROM studenttable')
data=cur.fetchall()
for row in data:
  ABCHS+Student(row[1],row[2],row[3])
  for i in ABCHS.children_is_type(Classroom):
    if row[4]==i.name:
      i+Student(row[1],row[2],row[3])
  #tbc
con.close()
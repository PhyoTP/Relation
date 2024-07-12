import sqlite3

con = sqlite3.connect("studentdb.db")
cur = con.cursor()
cur.execute('''create table if not exists studenttable(
studentID integer primary key,
name varchar(100), 
age integer,
gender varchar(1),
classroom varchar(20),
cca varchar(100))''')
con.commit()

# Correct SQL insertion string with ? placeholders
insertSQL = '''INSERT INTO studenttable (studentID, name, age, gender, classroom, cca) VALUES (?, ?, ?, ?, ?, ?)'''

data = [
    (1, "John", 15, "M", "1.01", "Chess Club"),
    (2, "Jane", 16, "F", "1.02", "Basketball"),
    (3, "Jim", 15, "M", "1.03", "Robotics"),
    (4, "Jill", 16, "F", "2.01", "Band"),
    (5, "Jack", 15, "M", "2.02", "Football"),
    (6, "Jess", 16, "F", "2.03", "Girl Scouts")
]

cur.executemany(insertSQL, data)
con.commit()

cur.execute('SELECT * FROM studenttable')
for row in cur.fetchall():
    print(row)

con.close()
import sqlite3

conn = sqlite3.connect('acer.db')
print("Openned database successfully")

conn.execute("DELETE from EMPLOYEE1 where id = 2")
conn.commit()

cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM EMPLOYEE1")
for row in cursor:
    print("ID = " ,row[0])
    print("NAME = " ,row[1])
    print("AGE = " ,row[2])
    print("ADDRESS = " ,row[3])
    print("SALARY = " ,row[4])

print("Operation done successfully")
conn.close()

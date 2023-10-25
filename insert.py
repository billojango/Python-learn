import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1, 'Jeff',33,'Carlifonia',45000.00)");

conn.execute("INSERT INTO EMPLOYEE1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2, 'Allen',25,'Texas',15000.00)");

conn.execute("INSERT INTO EMPLOYEE1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3, 'Mark',23,'Norway',145000.00)");

conn.execute("INSERT INTO EMPLOYEE1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(4, 'Brenda',30,'kenya',200000.00)");

conn.commit()
print("Records created successfully")
conn.close()
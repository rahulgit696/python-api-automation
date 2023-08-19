import mysql.connector
from utilities.configurations import *
# host, database, user, password

# connection_check = mysql.connector.connect(host='localhost', database='APIDevelop',
#                         user='root', password='Rahul@12345')

connection_check = get_connection()

print(connection_check.is_connected())

cursor_check = connection_check.cursor()
cursor_check.execute('select * from CustomerInfo')
# row = cursor_check.fetchone()
# print(row)
#
# print(row[3])
#
# rowAll = cursor_check.fetchall()
# print(rowAll[1])

row = cursor_check.fetchall()

print(row)
sum = 0
for rows in row:
    sum = sum + rows[2]
print(sum)

query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("Australia", "Jmeter")

cursor_check.execute(query,data)

connection_check.commit()

connection_check.close()
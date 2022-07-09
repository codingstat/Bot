import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="Rijo",password="2244",database="Name database")
mycursor=mydb.cursor()
mycursor.execute("Select * from Table name")
for i in mycursor:
	print(i)
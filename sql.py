import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="")

command = db.cursor()

command.execute("show databases")
for i in command:
  print(i)
import mysql.connector

mydb = mysql.connector.connect(
  host="singh",
  user="root",
  passwd="",
    db="Empdatabase"
)

print(mydb)
import mysql.connector

#create connection to the db
mydb = mysql.connector.connect(user='root', password='root', 
host='127.0.0.1', database='mydb')

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydb")  

# create table
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, food VARCHAR(255) NOT NULL, PRIMARY KEY (id))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
    



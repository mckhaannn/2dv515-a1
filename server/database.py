import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="2dv515"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE movies (id INT PRIMARY KEY, title VARCHAR(255), "
#                 "year VARCHAR(255))")
# mycursor.execute("CREATE TABLE users (userId INT PRIMARY KEY, name VARCHAR(255))")
# mycursor.execute("CREATE TABLE ratings (id INT AUTO_INCREMENT PRIMARY KEY, userId VARCHAR(255), "
#                  "movieId VARCHAR(255), rating VARCHAR(255))")
print(mydb)

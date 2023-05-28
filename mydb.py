

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

# prepare a cursir object
cursorObject = dataBase.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")
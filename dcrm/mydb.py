import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Jupiter.1979#'
)

# Prepare a cursor object

cursorObject = dataBase.cursor()

# Create Data Base

cursorObject.execute("CREATE DATABASE crmDataBase")

print("All Done!")
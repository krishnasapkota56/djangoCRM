import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='krishna.nepal1',
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE crm")


print("All done")

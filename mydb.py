

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '0173286913'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")
print('All Done!')
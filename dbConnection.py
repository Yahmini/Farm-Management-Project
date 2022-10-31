import mysql.connector as mycon
def getConnection():
    con=mycon.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    return con

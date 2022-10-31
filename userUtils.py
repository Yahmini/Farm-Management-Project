import mysql.connector as mycon

def getConnection():
    con=mycon.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    return con
def get(tableName):
    con=mycon.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    cur.execute("SELECT * FROM "+ tableName)
    results = cur.fetchall()
    con.close()
    return results
a = get("inventory")

def verifyLogin(userName,userPwd):
    print('userName',userName)
    qry = "select * from users where userName='"+userName+"' and userPassword='"+userPwd+"'"
    print("Query:"+ qry)
    conn=getConnection()
    cur =conn.cursor()
    cur.execute(qry)
    results = cur.fetchall()
    print(results)
    if len(results) >= 1:
        msg = "success"
    else:
        msg = "failed"
    conn.close()
    return msg
    

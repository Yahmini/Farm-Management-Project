import mysql.connector as mycon
import dbConnection as con
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

def addInventory(name1,type1,count1):
    cnt = int(count1)
    qry = "INSERT INTO inventory VALUES(name1,type1,cnt)"
    print("Query:"+ qry)
    conn=con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.close()

def getRecord(keyValue,columnName,columnType,tableName):
    if columnType == 'int':
        qry = "SELECT * FROM "+tableName+ " where "+columnName+"="+keyValue+""
    else:
        qry = "SELECT * FROM "+tableName+ " where "+columnName+"='"+keyValue+"'"
    print("Query:"+ qry)
    conn=con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    results = cur.fetchone()
    conn.close()
    return results

def getTransactionRecord(tableName):
    con=mycon.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    cur.execute("SELECT * FROM "+ tableName+" ORDER BY date DESC")
    results = cur.fetchall()
    con.close()
    return results

def getEventRecord(tableName):
    con=mycon.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    cur.execute("SELECT * FROM "+ tableName+" ORDER BY date DESC")
    results = cur.fetchall()
    con.close()
    return results

def getUnitPrice(name,type,item,measuring_unit):
    con=mycon.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    qry="SELECT unitPrice FROM price_details where name='"+name+"' AND type='"+type+"' AND item='"+item+"' AND measuring_unit='"+measuring_unit+"'"
    print(qry)
    cur.execute(qry)
    results = cur.fetchone()
    print(results)
    unitPrice = results[0]
    con.close()
    return unitPrice
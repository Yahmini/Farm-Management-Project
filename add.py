import dbConnection as con
def addInventory(name1,type1,count1):
    cnt = int(count1)
    qry = "INSERT INTO inventory VALUES('"+name1+"','"+type1+"',"+count1+")"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()


def updateInventory(name1,type1,count1):    
    qry = "UPDATE inventory SET name='"+name1+"',type='"+type1+"',count="+count1+" where name='"+name1+"'"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def deleteInventory(name1):    
    qry = "delete from inventory where name='"+name1+"'"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def addTransaction(date,type,name,income,expense,item,measuring_unit,units_sold,transtype):
    qry = "INSERT INTO transaction(date,type,name,item,measuring_unit,units_sold,income,expense,transaction_type) VALUES('"+date+"','"+type+"','"+name+"','"+item+"','"+measuring_unit+"',"+units_sold+","+income+","+expense+",'"+transtype+"')"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def updateTransaction(date,type,name,income,expense,sno,item,measuring_unit,units_sold,transtype):    
    qry = "UPDATE transaction SET date='"+date+"',type='"+type+"',name='"+name+"',income='"+income+"',expense='"+expense+"', item='"+item+"',measuring_unit='"+measuring_unit+"',units_sold="+units_sold+",transaction_type='"+transtype+"' where sno="+sno
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def deleteTransaction(sno):    
    qry = "delete from transaction where sno="+sno+""
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def profitcalculate(invName):
    qry = "select sum(income)-sum(expense) as profit from transaction where name='"+invName+"';"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    try:
        results=cur.fetchone()
    except:
        results=None
    conn.close()
    return results

def addEvent(date,name,event,category):
    qry = "INSERT INTO Event(date,name,event,category) VALUES('"+date+"','"+name+"','"+event+"',"+category+"')"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def updateEvent(date,name,event,category,sno):    
    qry = "UPDATE event SET date='"+date+"',name='"+name+"',event='"+event+"',category='"+category+"' where sno="+sno+""
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def deleteEvent(sno):    
    qry = "delete from event where sno="+sno+""
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def addUser(userName,userPassword,userPhone):    
    qry = "INSERT INTO Users(userName,userPassword,userPhone) VALUES('"+userName+"','"+userPassword+"','"+userPhone+"');"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def addUnitDetails(name,type,unitDetails,item,measuringUnit,unitPrice):
    qry = "INSERT INTO price_details(name,type,unitDetails,item,measuring_unit,unitPrice) VALUES('"+name+"','"+type+"','"+unitDetails+"','"+item+"','"+measuringUnit+"',"+unitPrice+")"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def updateUnitDetails(name,type,unitDetails,item,measuring_unit,unitPrice,sno):
    qry = "UPDATE price_details SET name='"+name+"',type='"+type+"',unitDetails='"+unitDetails+"',unitPrice="+unitPrice+",item='"+item+"',measuring_unit='"+measuring_unit+"' where sno="+sno+""
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

def deleteRecord(tableName, fieldName, fieldType,fieldValue):    
    if fieldType == 'int':
        qry = "delete from "+tableName+" where "+fieldName+"="+fieldValue
    else:
        qry = "delete from "+tableName+" where "+fieldName+"='"+fieldValue+"'"
    print("Query:"+ qry)
    conn= con.getConnection()
    cur = conn.cursor()
    cur.execute(qry)
    conn.commit()
    conn.close()

    
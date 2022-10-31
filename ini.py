import mysql.connector as myconn
def creating_users():
    con=myconn.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    cur.execute("DROP TABLE users")
    cur.execute("CREATE TABLE users ( userId INTEGER(100)  NOT NULL AUTO_INCREMENT,userName VARCHAR(255), userPassword VARCHAR(255), userPhone VARCHAR(100), userRole VARCHAR(255), PRIMARY KEY(userId))") 
    cur.execute("INSERT INTO users(userName,userPassword,userPhone,userRole) VALUES('yahmini', 'snow_yam','9739841352','admin')")
    con.commit()
    con.close()

def creating_table():
    con=myconn.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    cur.execute("DROP TABLE inventory")
    cur.execute("CREATE TABLE inventory ( name VARCHAR(255), type VARCHAR(255), count INTEGER(10))") 
    cur.execute("INSERT INTO inventory VALUES('Mango', 'Tree', 200)")
    cur.execute("INSERT INTO inventory VALUES('Coconut', 'Tree', 250)")
    cur.execute("INSERT INTO inventory VALUES('Chicken', 'Animal', 25)")
    con.commit()
    con.close()
#creating_table()
def transaction_table():
    con=myconn.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    #cur.execute("DROP TABLE transaction")
    cur.execute("CREATE TABLE transaction (sno INTEGER(100) NOT NULL AUTO_INCREMENT,date DATE, type VARCHAR(255), name VARCHAR(255),item VARCHAR(100),measuring_unit VARCHAR(100),units_sold INTEGER(20),income INTEGER(20), expense INTEGER(20),transaction_type VARCHAR(100), PRIMARY KEY (sno))" )
    #cur.execute("INSERT INTO transaction(date,type,name,income,expense) VALUES(20221025, 'Tree','Mango', 2000, 1000)")
    #cur.execute("INSERT INTO transaction(date,type,name,income,expense) VALUES(20221130, 'Tree', 'Amla',2500, 1200)")
    #cur.execute("INSERT INTO transaction(date,type,name,income,expense) VALUES(20221230, 'Animal', 'Cow', 25000, 5000)")
    con.commit()
    con.close()
#transaction_table()
    
def event_table():
    con=myconn.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    #cur.execute("DROP TABLE event")
    cur.execute("CREATE TABLE event (sno INTEGER(100) NOT NULL AUTO_INCREMENT,date DATE, name VARCHAR(255), event VARCHAR(255),category VARCHAR(255) , PRIMARY KEY (sno))" )
    cur.execute("INSERT INTO event(date,name,event,category) VALUES(20221025,'Mango','harvest', 'tree')")
    cur.execute("INSERT INTO event(date,name,event,category) VALUES(20221130, 'Amla','harvest', 'tree')")
    cur.execute("INSERT INTO event(date,name,event,category) VALUES(20221230, 'Cow','food suply', 'animal')")
    con.commit()
    con.close()

def price_details():
    con=myconn.connect(host="localhost",
    user="root",
    password="admin",
    database="farmmanagement")
    cur =con.cursor()
    cur.execute("DROP TABLE price_details")
    cur.execute("CREATE TABLE price_details (sno INTEGER(100) NOT NULL AUTO_INCREMENT,name VARCHAR(255), type VARCHAR(255),unitDetails VARCHAR(255) ,item VARCHAR(100),measuring_unit VARCHAR(100),unitPrice FLOAT(100,2), PRIMARY KEY (sno))" )
    con.commit()
    con.close()
#transaction_table()
price_details()





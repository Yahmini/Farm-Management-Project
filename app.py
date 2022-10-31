from flask import Flask,render_template,request,redirect,url_for
import userUtils,dbutils,add
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from datetime import date
app = Flask(__name__)
Bootstrap(app)
datepicker(app)

@app.route('/')
def index():
   return render_template("login.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['userName']
      pwd = request.form["userPwd"]
      msg = userUtils.verifyLogin(user,pwd)
      print(msg)
      if msg == 'success':
         return redirect(url_for('success'))
      else:
         return redirect(url_for('failed'))
   else:
      user = request.args.get('userName')
      return redirect(url_for('success',name = user))

@app.route('/success',methods = ['POST', 'GET'])
def success():
   results = dbutils.get("inventory")
   print(results)
   return render_template("inventory.html",result = results)
   

@app.route('/failed',methods = ['POST', 'GET'])
def failed():   
   return 'Please enter correct credentials'

@app.route('/logout',methods = ['POST', 'GET'])
def logout():   
   return render_template("login.html")

@app.route('/next',methods = ['POST', 'GET'])
def addpage():
   return render_template("add.html")

@app.route('/add',methods = ['POST', 'GET'])
def newinventory():
    name1 = request.form['invName']
    print(name1)
    type1 = request.form["invType"]
    count1= request.form['invCount']
    msg = add.addInventory(name1,type1,count1)
    user = 'admin'
    return redirect(url_for('success'))

@app.route('/edit',methods = ['POST', 'GET'])
def editinventory():
    name1 = request.args.get("invName")
    print(name1)
    columnName ="name"
    tableName ="inventory"
    results = dbutils.getRecord(name1,columnName,'string',tableName)
    user = 'admin'
    return render_template("editInventory.html",result = results)

@app.route('/update',methods = ['POST', 'GET'])
def updateinventory():
    name1 = request.form['invName']
    print(name1)
    type1 = request.form["invType"]
    count1= request.form['invCount']
    msg = add.updateInventory(name1,type1,count1)
    user = 'admin'
    return redirect(url_for('success',name = user))

@app.route('/delete',methods = ['POST', 'GET'])
def deleteinventory():
    name1 = request.args.get("invName")
    print(name1)
    add.deleteInventory(name1)
    user = 'admin'
    return redirect(url_for('success',name = user))

@app.route('/transaction',methods = ['POST', 'GET'])
def transaction():
   results = dbutils.getTransactionRecord("transaction")
   return render_template("transaction.html", result = results)

@app.route('/viewTransaction',methods = ['POST', 'GET'])
def viewtransaction():
   today = date.today()
   return render_template("addtransaction.html",today = today)

@app.route('/addTransaction',methods = ['POST', 'GET'])
def newtrans():
    date1 = request.form['trandate']
    print(date1)
    name1 = request.form["tranName"]
    type1 = request.form["tranType"]
    item1= request.form["item"]
    munit1= request.form["measuring_unit"]
    unitssold1= request.form["unitssold"]
    transtype1= request.form["transtype"]
    unitprice = dbutils.getUnitPrice(name1,type1,item1,munit1)
    print(unitprice)
    income1= int(unitssold1)*unitprice
    print(income1)
    income = str(income1)
    expense1= request.form['tranexpense']
    msg = add.addTransaction(date1,type1,name1,income,expense1,item1,munit1,unitssold1,transtype1)
    user = 'admin'
    return redirect(url_for('transaction',name = user))

@app.route('/edittransaction',methods = ['POST', 'GET'])
def editTransaction():
    name1 = request.args.get("sno")
    print(name1)
    columnName ="sno"
    tableName ="transaction"
    results = dbutils.getRecord(name1,columnName,'int',tableName)
    print(results)
    user = 'admin'
    return render_template("edittransaction.html",result = results)

@app.route('/updatetransaction',methods = ['POST', 'GET'])
def updatetransaction():
    date1 = request.form['trandate']
    print(date1)
    name1 = request.form["tranName"]
    type1 = request.form["tranType"]
    item1= request.form["item"]
    munit1= request.form["measuring_unit"]
    unitssold1= request.form["unitssold"]
    transtype1= request.form["transtype"]
    unitprice = dbutils.getUnitPrice(name1,type1,item1,munit1)
    income1= int(int(unitssold1)*unitprice)
    print(income1)
    income = str(income1)
    expense1= request.form['tranexpense']
    sno= request.form['sno']
    msg = add.updateTransaction(date1,type1,name1,income,expense1,sno,item1,munit1,unitssold1,transtype1)
    user = 'admin'
    return redirect(url_for('transaction',name = user))


@app.route('/deletetransaction',methods = ['POST', 'GET'])
def deletetransaction():
    name1 = request.args.get("sno")
    print(name1)
    add.deleteTransaction(name1)
    user = 'admin'
    return redirect(url_for('transaction',name = user))
   
@app.route('/profit',methods = ['POST', 'GET'])
def profitloss():
    name1 = request.args.get("invName")
    print(name1)  
    intprofit=0  
    result= add.profitcalculate(name1)
    print(result)
    finalresult=result[0]
    if finalresult == None:
      profit ="Transaction Not Found"
      profitstatus="no transaction found"
    else:
         print(result)
         intprofit = result[0]
         if intprofit >= 0:
            profit= True
            profitstatus="Profit"
         else:
            profit= False
            profitstatus = "Loss"    

    profittuple = (name1,profitstatus, intprofit)
    print(profittuple)
    return render_template('profit.html',result = profittuple)

@app.route('/event',methods = ['POST', 'GET'])
def getevents():
   results = dbutils.getEventRecord("event")
   return render_template("event.html", result = results)

@app.route('/getevents',methods = ['POST', 'GET'])
def getallevents(name):
   results = dbutils.getEventRecord("event")
   return render_template("event.html", result = results)

@app.route('/viewEvent',methods = ['POST', 'GET'])
def viewevent():
   return render_template("addevent.html")

@app.route('/addEvent',methods = ['POST', 'GET'])
def newevent():
    date1 = request.form['event_date']
    print(date1)
    name1 = request.form["event_name"]
    event1 = request.form["event_event"]
    category1= request.form['event_category']
    add.addEvent(date1,event1,name1,category1)
    #print(msg)
    user = 'admin'
    return redirect(url_for('getevents',name = user))

@app.route('/editevent',methods = ['POST', 'GET'])
def editEvent():
    name1 = request.args.get("sno")
    print(name1)
    columnName ="sno"
    tableName ="event"
    results = dbutils.getRecord(name1,columnName,'int',tableName)
    print(results)
    user = 'admin'
    return render_template("editevent.html",result = results)

@app.route('/updateevent',methods = ['POST', 'GET'])
def updateevent():
    date1 = request.form['event_date']
    print(date1)
    name1 = request.form["event_name"]
    type1 = request.form["event_event"]
    category1= request.form['event_category']
    sno= request.form['sno']
    msg = add.updateEvent(date1,type1,name1,category1,sno)
    user = 'admin'
    return redirect(url_for('getevents',name = user))

@app.route('/deleteevent',methods = ['POST', 'GET'])
def deleteevent():
    no= request.args.get("sno")
    print(no)
    add.deleteEvent(no)
    user = 'admin'
    return redirect(url_for('getevents',name = user))

@app.route("/register",methods = ['POST', 'GET'])
def register():
   return render_template("register.html")

@app.route("/addUser",methods = ['POST', 'GET'])
def addUser():
   userName = request.form["userName"]
   userPassword = request.form["userPassword"]
   userPhone = request.form["userPhone"]
   add.addUser(userName,userPassword,userPhone)
   return render_template("login.html")

@app.route('/viewPrice',methods = ['POST', 'GET'])
def viewPrice():
   results = dbutils.get("price_details")
   return render_template("viewPrice.html", result = results)

@app.route('/addUnitDetails',methods = ['POST', 'GET'])
def addUnitDetails():
   return render_template("addUnitDetails.html")

@app.route('/addPrice',methods = ['POST', 'GET'])
def addPrice():
   name1 = request.form["unitName"]
   type1 = request.form["unitType"]
   item1 = request.form["item"]
   munit1 = request.form["measuring_unit"]
   unitdetails1 = request.form["unitDetails"]
   unitprice = request.form["unitPrice"]
   add.addUnitDetails(name1,type1,unitdetails1,item1,munit1,unitprice)
   return redirect(url_for('viewPrice'))

@app.route('/editPrice',methods = ['POST', 'GET'])
def editPrice():
   name1 = request.args.get("sno")
   columnName ="sno"
   tableName ="price_details"
   results = dbutils.getRecord(name1,columnName,'int',tableName)
   print(results)
   user = 'admin'
   return render_template("editUnitDetails.html",result = results)

@app.route('/updatePrice',methods = ['POST', 'GET'])
def updatePrice():
   sno= request.form["sno"]
   name1 = request.form["unitName"]
   type1 = request.form["unitType"]
   item1 = request.form["item"]
   munit1= request.form["measuring_unit"]
   unitdetails1 = request.form["unitDetails"]
   unitprice = request.form["unitPrice"]
   add.updateUnitDetails(name1,type1,unitdetails1,item1,munit1,unitprice,sno)
   return redirect(url_for('viewPrice'))


@app.route('/deletePrice',methods = ['POST', 'GET'])
def deletePrice():
   name1 = request.args.get("sno")
   add.deleteRecord("price_details","sno","int",name1)
   return redirect(url_for('viewPrice'))

if __name__ == '__main__':
   app.run(debug = True)
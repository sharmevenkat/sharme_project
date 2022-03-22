from flask import Flask,request
import sqlite3
app =Flask(__name__)
@app.get('/')
def func():
   con=sqlite3.Connection("C:/Users/trc/Desktop/nightskill/sharme/sample.db")
   curs=con.cursor()
   curs.execute("select * from studentdet")
   data=curs.fetchall()
   con.commit()
   con.close()
   return f'{data}'
@app.post('/h')
def world():
   con=sqlite3.Connection("C:/Users/trc/Desktop/nightskill/sharme/sample.db")
   curs=con.cursor()
   data= request.get_json()
   Name=data["Name"]
   Rollno=data["Rollno"]
   Mark=data["Mark"]
   detail=(Name,Rollno,Mark)
   curs.execute("create table if not exists studentdet (Name varchar(50),Rollno int,Mark int)")
   curs.execute("insert into studentdet values(?,?,?)",detail)
   con.commit()
   con.close()
   print(data)
   return f'{data}'
'''@app.patch("/upd")
def up():
   data =request.get_json()
   update(data)
   return("Updated")
def update(data):
   con=sqlite3.Connection("C:/Users/trc/Desktop/nightskill/sharme/sample.db")
   query =f'update studentdet set Rollno ="{data["Rollno"]}" where Name ="{data["Name"]}"'
   cur=con.cursor()
   cur.execute(query)
   con.commit()
@app.delete("/delete")
def deletes():
   data=request.get_json()
   delete(data["Name"])
   return "Deleted"
def delete(Name):
  con=sqlite3.Connection("C:/Users/trc/Desktop/nightskill/sharme/sample.db")
  query = f'delete from studentdet where Name ="{Name}"'
  cur=con.cursor()
  cur.execute(query)
  con.commit()'''




app.run(debug=True)

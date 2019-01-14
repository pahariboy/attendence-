import database
import datetime
import time
import sqlite3
stud1=335
stud2=389
stud3=324
stud4=344
count1=0
count2=0
count3=0
count4=0

conn=sqlite3.connect('project.db')
c=conn.cursor()
                     #main program

print("--------------Welcome to biometric attendence system--------------")
print("please start entering your college id to update your attendence")
id=input()
while(id!=0):
 
 if id==stud1:
  count1=count1+1
 elif id==stud2:
  count2=count2+1
 elif id==stud3:
    count3=count3+1
 else :
     count4=count4+1

 print("Enter 0 to exit")
 id=input()


print("--------Attendence is updated--------")
print("-------Details are-------")
database.Database("335","sarbeshwar singh","22","2016","cse",count1)
print("**************************")
database.Database("389","sumit sharma","22","2016","cse",count2)
print("**************************")
database.Database("324","sahil dhiman","11","2016","cse",count3)
print("**************************")
database.Database("344","savar kaul","22","2016","cse",count4)


                      #database linking
def create_table():
  c.execute(" CREATE TABLE IF NOT EXISTS attendence(Time time,id int ,name varchar(20),section int,batch int,course char(30),attendence int)")
def data_entry():
    Time=time.asctime()
    id=1611981335
    name="sarbeshwar singh"
    section=22
    batch= 2016
    course="cse"
    attendence=count1
    c.execute(" INSERT INTO attendence (Time,id,name,section,batch,course,attendence) values(?,?,?,?,?,?,?)",(Time,id,name,section,batch,course,attendence))
    conn.commit()
    Time=time.asctime()
    id=1611981389
    name="sumit sharma"
    section=22
    batch= 2016
    course="cse"
    attendence=count2
    c.execute(" INSERT INTO attendence (Time,id,name,section,batch,course,attendence) values(?,?,?,?,?,?,?)",(Time,id,name,section,batch,course,attendence))
    conn.commit()
    Time=time.asctime() 
    id=1611981324
    name="sahil dhiman"
    section=11
    batch= 2016
    course="cse"
    attendence=count3
    c.execute(" INSERT INTO attendence (Time,id,name,section,batch,course,attendence) values(?,?,?,?,?,?,?)",(Time,id,name,section,batch,course,attendence))
    conn.commit()
    Time=time.asctime()
    id=1611981344
    name="savar kaul"
    section=22
    batch= 2016
    course="cse"
    attendence=count4
    c.execute(" INSERT INTO attendence (Time,id,name,section,batch,course,attendence) values(?,?,?,?,?,?,?)",(Time,id,name,section,batch,course,attendence))
    conn.commit()



    c.close()
    conn.close()
create_table()
data_entry()









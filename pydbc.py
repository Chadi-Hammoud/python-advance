import mysql.connector  
#######First Method################## 
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "UBILITY_DB")  
  
#printing the connection object   
print(myconn)  
  
#creating the cursor object  
cur = myconn.cursor()  
  
print(cur) 


############Getting the list of existing databases#################### 
 
try:  
    dbs = cur.execute("show databases")  
except:  
    myconn.rollback()  
for x in cur:  
    print(x)  
# myconn.close()  

#############Creating the new database#################################
# cur = myconn.cursor()  
try:  
    #creating a new database  
    cur.execute("create database PythonDB2")  
  
    #getting the list of all the databases which will now include the new database PythonDB  
    dbs = cur.execute("show databases")  
      
except:  
    myconn.rollback()  
  
for x in cur:  
        print(x)  
          
# myconn.close()  

##############Creating the table####################
#creating the cursor object  
# cur = myconn.cursor()  
  
try:  
    #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
    dbs = cur.execute("""create table Employee(
                            id int(20) not null primary key,
                            name varchar(20) not null,
                            salary float not null,
                            Dept_id int not null)""")  
except:  
    myconn.rollback()  
  
# myconn.close()  
###############Alter Table##################
# cur = myconn.cursor()  

try:  
    #adding a column branch name to the table Employee  
    cur.execute("alter table Employee add last_name varchar(20) not null")  
except:  
    myconn.rollback()  
  
myconn.close()  
###################################################
###############Insert Operation###########################











###############Adding a record to the table#####################

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database = "Employee_DB")  

cur = myconn.cursor()  
try:  
    #creating a new database  
    cur.execute("create database Employee_DB")  
  
    #getting the list of all the databases which will now include the new database PythonDB  
    dbs = cur.execute("show databases")  
      
except:  
    myconn.rollback()  
        
try:  
    #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
    dbs = cur.execute("""create table Employee(
                            id int(20) not null primary key,
                            name varchar(20) not null,
                            salary float not null,
                            Dept_id int not null)""")  
except:  
    myconn.rollback()  
        
#creating the cursor object  
# cur = myconn.cursor()  
print(cur)

# sql = 'insert into Employee(id, name, salary, Dept_id) values (2,"John", 110, 25000) '#(%s, %s, %s, %s)"  
  
#The row values are provided in the form of tuple   
val = ("John", "110", "25000", "Dohe")  
  
try:  
    #inserting the values into the table  
    cur.execute(sql)#,val)  
  
    #commit the transaction   
    myconn.commit()  
    # print(cur.execute(sql,val))
    # print("Your Record has been added")
      
except:  
    myconn.rollback()  
  
print(cur.rowcount,"record inserted!")  
myconn.close()  


myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database = "ubility_db")  

# cur = myconn.cursor()  
cur = myconn.cursor()  
sql = 'insert into Employee(name,salary, dept_id, last_name) values(%s, %s, %s, %s)'#("chadi", 25000.00, 201, "Newyork"); ' #(%s, %s, %s, %s)"  
  
#The row values are provided in the form of tuple   
val = ("Hammoud", 2500, 201, "lastname")  
  
try:  
    #inserting the values into the table  
    cur.execute(sql,val)  
    # cur.execute(sql)  
  
    #commit the transaction   
    myconn.commit()  
      
except:  
    myconn.rollback()  
  
print(cur.rowcount,"\trecord inserted!")  
# myconn.close()  
# cur.close()
##############Insert multiple rows######################

val = [("John", 25000.00, 201, "Newyork"),("David",25000.00,202,"Port of spain"),("Nick",90000.00,201,"Newyork")]  
      
try:  
    #inserting the values into the table  
    cur.executemany(sql,val)  
  
    #commit the transaction   
    myconn.commit()  
    print(cur.rowcount,"records inserted!")  
      
except:  
    myconn.rollback()  
  
# myconn.close()  


#############Read Operators######################
  
try:  
    #Reading the Employee data      
    cur.execute("select * from Employee")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
    #printing the result  
      
    for x in result:  
        print(x);  
except:  
    myconn.rollback()  
  
# myconn.close()  

###############Read specific row################################
try:  
    #Reading the Employee data      
    cur.execute("select name, id, salary from Employee")  
  
    #fetching the rows from the cursor object  
    result = cur.fetchall()  
    #printing the result  
    # for x in result:  
    #     print(x);  
    print("Name    id    Salary");  
    for row in result:  
        print("%s    %d    %d"%(row[0],row[1],row[2]))  
except:  
    myconn.rollback()  
# myconn.close()  

################Update Record########################
try:  
    #updating the name of the employee whose id is 110  
    cur.execute("update Employee set last_name = 'alex' where name = 'chadi'")  
    myconn.commit()  
except:  
      
    myconn.rollback()  
myconn.close()  


############Delete Operation####################
  
try:  
    #Deleting the employee details whose id is 110  
    cur.execute("delete from Employee where id = 110")  
    myconn.commit()  
except:  
      
    myconn.rollback()  
  
myconn.close()







































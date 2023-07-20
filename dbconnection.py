import mysql.connector

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root", database = "UBILITY_DB")

cur = myconn.cursor()  



def getDatabaseList(myconn, cur):
    try:  
     dbs = cur.execute("show databases")  
    except:  
        myconn.rollback()  
    for x in cur:  
        print(x)  
    # myconn.close()  


def createDatabase(myconn, cur,dbname):
    try:  
        cur.execute("create database "+dbname)  
        dbs = cur.execute("show databases")  
  
    except:  
        myconn.rollback()  
        
    getDatabaseList(myconn, cur) 
    myconn.close() 
    
    
def createTable(myconn, cur, tableName):
    #It need too many time and logic 
    pass


def insertRecord(myconn, cur):
    pass

def insertMultipleRecord(myconn, cur):
    pass


def displayRecords(myconn, cur):
    pass




# getDatabaseList(myconn, cur)
# createDatabase(myconn, cur,"TestDB")
import mysql.connector

host = 'localhost'
username = 'root'
password = 'admin'

class Connection:
    def __init__(self, host, username,password):
        self.host = host
        self.username = username
        self.password = password
    
    def connectToSql(self,table):
        mydb = mysql.connector.connect(
        host = self.host,
        user = self.username,
        password = self.password,
        database = 'crsdb'
        )
        myCursor = mydb.cursor()
        myCursor.execute("SELECT * FROM " + table)
        myresult = myCursor.fetchall()
        return myresult


# TODO
conn = Connection(host,username,password).connectToSql('dataservey')
print(type(conn))

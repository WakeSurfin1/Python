# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:29:02 2018

@author: WakeSurfin1
@date 11-22-2018

Interface with Teradata database
Create a connection string
Run query and return results

@usage:
    
from TeradataDbi_class import TeradataDbi
db_object = TeradataDbi()

strQuery = "SELECT column1, column2, column3, colum4 FROM databaseName.tableName where column4 = 'VA';"
queryResults = db_object.execSqlQueryOdbc("ServerName", "DbUserName", "DBPassword", strQuery, "C:/temp/tdDbiLog.txt")

for record in queryResults:
    print(record.column1)
    print(record.column2)
    print(record.column3)
    print(record.column4)  

"""

import pyodbc, datetime
from sys import exit

class TeradataDbi:

    def execSqlQueryOdbc(self, serverName, userName, password, querySql, logFile):

        db_connect_string = "DRIVER={Teradata};DBCNAME=" + str(serverName) + ";UID=" + str(userName) + ";PWD=" + str(password) 
        
        # Set time out configuration values
        SQL_ATTR_CONNECTION_TIMEOUT = 113	
        login_timeout = 60
        connection_timeout = 120
    
        try:
            cnxn = pyodbc.connect(db_connect_string, timeout=login_timeout, attrs_before={SQL_ATTR_CONNECTION_TIMEOUT: connection_timeout})
      
        except Exception as e:
            sqlLogFile = open(logFile,"a")
            sqlLogFile.write(str(datetime.datetime.now()) + "\n ERROR: connection failed " + db_connect_string + " :" + str(e))
            sqlLogFile.close()
            exit(1)
        try:            
            crsr = cnxn.cursor()
            crsr.execute(querySql)
        except Exception as e:
            sqlLogFile = open(logFile,"a")
            sqlLogFile.write(str(datetime.datetime.now()) + "\n ERROR: query failed " + querySql + " :" + str(e))
            sqlLogFile.close()
            exit(1)
            
        queryResults = crsr.fetchall()
        crsr.close()
        return queryResults
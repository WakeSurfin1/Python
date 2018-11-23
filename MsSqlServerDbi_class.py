# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:22:22 2018

@author: WakeSurfin1

@2018-11-18

Interface with Microsoft Sql Server database
Create a connection string
Run query and return results

@usage 

from MsSqlServerDbi_class import MsSqlServerDbi

db_object = MsSqlServerDbi()

strQuery = "SELECT column1, column2, column3 FROM databaseName.dbo.tableName WHERE column1 = 'value';"

queryResults = db_object.execSqlQuery("serverName", "databaseName", strQuery, "C:/temp/dbiLog.txt")

for record in queryResults:
	print(record.column1)
	print(record.column2)
	print(record.column3)

"""

import pyodbc, datetime

class MsSqlServerDbi:

    def execSqlQuery(self, serverName, databaseName, querySql, logFile):
        
        db_connect_string = "DRIVER={SQL Server};SERVER=" + str(serverName) + ";DATABASE=" + str(databaseName) + ";TRUSTED_CONNECTION=yes"

        sqlLogFile = open(logFile,"a")

        # Set time out configuration values
        SQL_ATTR_CONNECTION_TIMEOUT = 113	
        login_timeout = 30
        connection_timeout = 60
        
        try:
            cnxn = pyodbc.connect(db_connect_string, timeout=login_timeout, attrs_before={SQL_ATTR_CONNECTION_TIMEOUT: connection_timeout})
    
        except Exception as e:
            sqlLogFile.write(str(datetime.datetime.now()) + "\n ERROR: connection failed " + db_connect_string + " :" + str(e))
            exit(1);

        try:
            crsr = cnxn.cursor()
            crsr.execute(querySql)
    
        except Exception as e:
            sqlLogFile.write(str(datetime.datetime.now()) + "\n ERROR: query failed " + querySql + " :" + str(e))
            exit(1);
       
        queryResults = crsr.fetchall()
        return queryResults
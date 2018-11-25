# -*- coding: utf-8 -*-
"""
@author: WakeSurfin1

@date: 2018-11-25

API Get GitHub Jobs data  

OutPut to HTML table

Base end point = https://jobs.github.com/positions.json?

Parameters:

description — A search term, such as "ruby" or "java". This parameter is aliased to search.
location — A city name, zip code, or other location search term.
lat — A specific latitude. If used, you must also send long and must not send location.
long — A specific longitude. If used, you must also send lat and must not send location.
full_time — If you want to limit results to full time positions set this parameter to 'true'.

Examples:

https://jobs.github.com/positions.json?description=python&full_time=true&location=sf
https://jobs.github.com/positions.json?search=node
https://jobs.github.com/positions.json?lat=37.3229978&long=-122.0321823
    
    
Data Fields:

id
type
url
created_at
company
company_url
location
title
description
how_to_apply
company_logo

"""
import requests, json
from datetime import datetime
from logger_class import Logger
from configparser import ConfigParser
import os
from sys import exit

# 0 ---------------------------------------------------------------------

# dynamically build the log path and file name
# log pathFile = current path + /Logs/ + base script name + _log.txt
strCurDir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
strBaseName = os.path.basename(__file__).split(".")[0]
strLogFile = strCurDir + "/logs/" + strBaseName + "_log.txt"

# create the log object and pass the log path file
logObj = Logger(strLogFile)

# 1 ---------------------------------------------------------------------

logObj.info("1: Begin " + strBaseName + ".py - open End Point URL")

# get input file from config.ini
config = ConfigParser()
config.read(strBaseName + '.ini')
strEndPointUrl = config.get('config_a', 'strEndPointUrl')
strOutPutFile = config.get('config_a', 'strOutPutFile')

logObj.info("Request get end point = " + strEndPointUrl)

response = requests.get(strEndPointUrl)

if(response.ok):
    logObj.info("API get response OK " + str(response.status_code))
    logObj.info("API get time elapsed " + str(response.elapsed))
else:
    logObj.error("API get response <> OK " + response.raise_for_status()) 
    exit(1)
    

# 2 --------------------------------------------------------------------

logObj.info("2: Ouput data to " + strOutPutFile)

# If the output file exists, delete it
try:
    os.remove(strOutPutFile)
except OSError:
    pass

## convert json to string and then string to Python list
strOutput = json.dumps(response.json())
ListOut = json.loads(strOutput)

if len(ListOut) < 1:
    logObj.warn("API Get Request did not return any records. Exit")
    exit(1)

try:
    outFile = open(strOutPutFile, "a")                 
except Exception as e:
    logObj.error("Could not open " + strOutPutFile + " " + str(e))
    exit(1)  
    
strCurDateTime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

### build HTML Table output file

outFile.write("<html>" + "\n")
outFile.write("<head><title>GitHub Analytics Jobs</head></title>" + "\n")
outFile.write("<body>" + "\n")
outFile.write("<table border = " + '"' + str(3) + '"' + " bgcolor=" + '"' + "gray" + '"' + ">" + "\n")
outFile.write("<caption bgcolor=" + '"' + "gray" + '"' + "> GitHub Analytics Jobs</caption>" + "\n")
outFile.write("<tr> <th>Create Date</th> <th>Company</th> <th>Location</th> <th>Title</th> <th>Current Date</th> </tr> " + "\n")

i=0
for dictOut in ListOut:
    strRecord = ""
    for key, value in dictOut.items():
        if key == 'created_at':
            strRecord = "<tr> <td> " + str(value) + " </td>"     
        elif key == 'company':
            strRecord = strRecord + " <td> " + value + " </td>"
        elif key == 'location':
            strRecord = strRecord + " <td> " + value + " </td>"
        elif key == 'title':
            strRecord = strRecord + " <td> " + value + " </td> <td> " + strCurDateTime + " </td> </tr> \n"  
    
    outFile.write(strRecord)
    i += 1 
    
outFile.write("</table>" + "\n") 
outFile.write("</body>" + "\n")
outFile.write("</html>" + "\n")   

intOutFileSize = os.stat(strOutPutFile).st_size

if intOutFileSize < 1: 
    logObj.warn(strOutPutFile + " byte size = " + str(intOutFileSize))
else:
    logObj.info(strOutPutFile + " byte size = " + str(intOutFileSize))


''' pipe delimited flat file output
i=0
for dictOut in ListOut:
    strRecord = ""
    for key, value in dictOut.items():
        if key == 'created_at':
            strRecord = str(value) + "|"     
        elif key == 'company':
            strRecord = strRecord + value + "|"
        elif key == 'location':
            strRecord = strRecord + value + "|"
        elif key == 'title':
            strRecord = strRecord + value + "|" + strCurDateTime + "\n"  
    
    outFile.write(strRecord)
    i += 1  
print(str(i))   

''' 

outFile.close()

# 3 --------------------------------------------------------------------

logObj.info("3: exit \n")   
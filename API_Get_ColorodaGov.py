# -*- coding: utf-8 -*-
"""
@author: WakeSurfin1

@date: 2018-11-24

API Get Colorado state goverment list of business entities  

Write specific columns to the output file

End Point = http://data.colorado.gov/resource/4ykn-tg5h.json

Data description: below is a list of data feilds.
not all fields are a populated and 
the fields are not consistently ordered
    
Data Fields:

entityid, 
entityname, 
principaladdress1, 
principaladdress2, 
principalcity, 
principalstate, 
principalzipcode, 
principalcountry, 
mailingaddress1, 
mailingaddress2, 
mailingcity, 
mailingstate, 
mailingzipcode, 
mailingcountry, 
entitystatus, 
jurisdictonofformation, 
entitytypeverbatim, 
entitytype, 
agentfirstname, 
agentmiddlename, 
agentlastname, 
agentsuffix, 
agentorganizationname, 
agentprincipaladdress1, 
agentprincipaladdress2, 
agentprincipalcity, 
agentprincipalstate, 
agentprincipalzipcode, 
agentprincipalcountry, 
agentmailingaddress1, 
agentmailingaddress2, 
agentmailingcity, 
agentmailingstate, 
agentmailingzipcode, 
agentmailingcountry, 
entityformdate, 
location 


"""
import requests, json
from datetime import datetime
from logger_class import Logger
from configparser import ConfigParser
import os

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
config.read('config.ini')
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
ListOutPut = json.loads(strOutput)

strCurDateTime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# open the output file
try:
    outFile = open(strOutPutFile, "a")                 
except Exception as e:
    logObj.error("Could not open " + strOutPutFile + " " + str(e))
    exit(1);

# create the header record
outFile.write("entity id|entity name|entity type|datetime" + "\n")    

i=0
for dictOutPut in ListOutPut: 
    outFile.write(dictOutPut['entityid'] + "|" + dictOutPut['entityname'] + "|" + dictOutPut['entitytype'] + "|" + strCurDateTime + "\n") 
    i += 1

# verify output record count and size
if i < 1:
    logObj.warn("API Get request output records = " + str(i))
else:    
    logObj.info("API Get request output records = " + str(i))

intOutFileSize = os.stat(strOutPutFile).st_size

if intOutFileSize < 1: 
    logObj.warn(strOutPutFile + " byte size = " + str(intOutFileSize))
else:
    logObj.info(strOutPutFile + " byte size = " + str(intOutFileSize))
    
outFile.close()

# 3 --------------------------------------------------------------------

logObj.info("3: exit \n")   
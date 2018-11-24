# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:00:10 2018

@author: WakeSurfin1

@ created 2018-11-18

parse a .csv file, skip the header row
calculate age based on dob 
out put year of service and age to scatter chart

"""
from datetime import datetime
from logger_class import Logger
from configparser import ConfigParser
import matplotlib.pyplot as plt
import os

# 0 ---------------------------------------------------------------------

# dynamically build the log path and file name
# log pathFile = current path + /Logs/ + base script name + _log.txt
strCurDir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
strBaseName = os.path.basename(__file__).split(".")[0]
strLogFile = strCurDir + "/logs/" + strBaseName + "_log.txt"

# create the log object and pass the log path file
logger_object = Logger(strLogFile)

# 1 --------------------------------------------------------------------
logger_object.info("1: Begin Parse_CSV_File.py - open input file")

# get input file from config.ini
config = ConfigParser()
config.read('config.ini')
strDataFile = config.get('config_a', 'strDataFile')

try:
	infile = open(strDataFile,"r");
    
except Exception as e:
	logger_object.error("Can not open " + strDataFile + " : " + str(e))
	exit(1);

# 2 --------------------------------------------------------------------  
logger_object.info("2: loop through the input file " + strDataFile)  

# calculate current date in format YYYY-MM-DD 
strToday = datetime.today().strftime('%Y-%m-%d')
dateToday = datetime.strptime(strToday, '%Y-%m-%d')

#skip the header row and calculate age in years
#create a new lists years of service and age
X=[]
Y=[]
i=0
for line in infile:
    if i > 0:
        field = line.split(',')
        dateDob = datetime.strptime(field[3], '%Y-%m-%d')
        # Calculate age as the difference between DOB and Today
        ageYears = abs((dateDob - dateToday).days)//365
        X.append(field[4])
        Y.append(ageYears)
        
    i += 1

logger_object.info(strDataFile + " record count = " + str(i))     
 
# 3 -------------------------------------------------------------------  
logger_object.info("3: Build Scatter Chart ") 

# contruct scatter chart
plt.scatter(X,Y)

#customize point size, point color, and point character
plt.scatter(X, Y, s=60, c='red', marker='^')

# Add title and labels to the graph
plt.title('Relationship Between Years of Service and Age')
plt.xlabel('Years of Service')
plt.ylabel('Age')    
    
# 4 -------------------------------------------------------------------  
logger_object.info("4: exit \n")   
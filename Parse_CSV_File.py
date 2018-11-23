# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:00:10 2018

@author: WakeSurfin1

@2018-11-18

parse a .csv file, skip the header row
calculate age based on dob 
out put name and age to log file

"""
from datetime import datetime
from logger_class import Logger

logger_object = Logger("C:/scripts/logs/Parse_CSV_Log.txt")

# 1 --------------------------------------------------------------------
logger_object.info("1: Begin Parse_CSV_File.py - open input file")

input = "C:/scripts/logs/InputData.csv"

try:
	infile = open(input,"r");
    
except Exception as e:
	logger_object.error("Can not open " + input + " : " + str(e))
	exit(1);

# 2 --------------------------------------------------------------------  
logger_object.info("2: loop through the input file " + input)  

# calculate current date in format YYYY-MM-DD 
strToday = datetime.today().strftime('%Y-%m-%d')
dateToday = datetime.strptime(strToday, '%Y-%m-%d')

#skip the header row and calculate age in years
#create a new list of first name and age
a=[]
i=0
for line in infile:
    if i > 0:
        field = line.split(',')
        dateDob = datetime.strptime(field[3], '%Y-%m-%d')
        ageYears = abs((dateDob - dateToday).days)//365
        field.append(ageYears)
        a.append(field[1] + ' ' + str(field[5])) 
        
    i += 1

logger_object.info(input + " record count = " + str(i))     
 
# 3 -------------------------------------------------------------------  
logger_object.info("3: output name and age to log file ") 

for NameAge in a:
    logger_object.info(NameAge)
    
# 4 -------------------------------------------------------------------  
logger_object.info("4: exit \n")   

    
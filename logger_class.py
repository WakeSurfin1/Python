# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 21:12:24 2018

@author: WakeSurfin1

@date:  2018-11-11

@Usage:  
    
from logger_class import Logger

logger_object = Logger("C:/scripts/logs/pylogOOP.txt")

logger_object.critical("This is a critical message")
logger_object.error("This is an error message")
logger_object.warn("This is an warn message")
logger_object.info("This is an info message")
logger_object.debug("This is an debug message")    

"""
import datetime
from sys import exit

class Logger(object):
    
    def __init__(self, file_name):
        self.file_name = file_name
        
    def _write_log(self, level, strIn):
        try:
            log_file = open(self.file_name, "a")
            strOut = str(datetime.datetime.now()) + ": " + strIn
            log_file.write("[" + level + "] " + strOut + "\n")
                 
        except Exception as e:
            print("ERROR: can not open file " + str(self.file_name) + " " + str(e))
            exit(1);
                
    def critical(self, strMsg):
      self._write_log("CRITICAL", strMsg)
      
    def error(self, strMsg):
      self._write_log("ERROR", strMsg)  

    def warn(self, strMsg):
      self._write_log("WARN", strMsg)
      
    def info(self, strMsg):
      self._write_log("INFO", strMsg)
      
    def debug(self, strMsg):
      self._write_log("DEBUG", strMsg)
      
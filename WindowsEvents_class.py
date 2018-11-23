# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:22:22 2018

@author: WakeSurfin1

@2018-11-23

Log events to the Windows Event Viewer -> Windows Logs -> Application

@usage 

from WindowsEvents_class import WindowsEvents
import os

strScriptName = os.path.basename(__file__)
intEventId = 2
intEventCat = 5

strEventType = "INFORMATION"
strEventDescr = "This is information"

WinEventObj = WindowsEvents()

WinEventObj.WriteWinAppLog(strScriptName, intEventId, intEventCat, strEventType, strEventDescr)

strEventType = "WARN"
strEventDescr = "This is a warning"

WinEventObj.WriteWinAppLog(strScriptName, intEventId, intEventCat, strEventType, strEventDescr)

strEventType = "ERROR"
strEventDescr = "This is an ERROR!"

WinEventObj.WriteWinAppLog(strScriptName, intEventId, intEventCat, strEventType, strEventDescr)

"""

import win32api, win32con, win32evtlog, win32security, win32evtlogutil 

class WindowsEvents:

    def WriteWinAppLog(self, strProcName, intEventID, intCategory, strEventType, strdesc):
        
        # get Windows OS details
        ph = win32api.GetCurrentProcess()
        th = win32security.OpenProcessToken(ph, win32con.TOKEN_READ)
        my_sid = win32security.GetTokenInformation(th, win32security.TokenUser)[0]
        
        #set Windows event type parm
        if strEventType.upper() == 'INFORMATION':
            myType = win32evtlog.EVENTLOG_INFORMATION_TYPE
            
        elif strEventType.upper() == 'WARN':
            myType = win32evtlog.EVENTLOG_WARNING_TYPE

        elif strEventType.upper() == 'ERROR':
            myType = win32evtlog.EVENTLOG_ERROR_TYPE

        else:                 
            myType = win32evtlog.EVENTLOG_INFORMATION_TYPE
            
        # assign function parms to ReportEvent() call     
        descr = [strdesc]
        data = "Application\0Data".encode("ascii")
 
        win32evtlogutil.ReportEvent(strProcName, intEventID, eventCategory=intCategory, eventType=myType, strings=descr, data=data, sid=my_sid)
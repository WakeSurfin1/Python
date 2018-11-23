# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:13:07 2018

@author: WakeSurfin1

Simple API get request to the Internation space 

Json dumps and dump out puts Json data to a string or a file
Json loads and load converts Json data to Python objects

"""

import requests, json

response = requests.get("http://api.open-notify.org/iss-now.json")

print(response.status_code)

print(type(response.json()))

print(response.json())

print(response.headers)

str_convertTo_string = json.dumps(response.json())

print(type(str_convertTo_string))

print(str_convertTo_string)

print(type(json.loads(str_convertTo_string)))

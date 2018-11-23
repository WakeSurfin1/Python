# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:46:28 2018

@author: WakeSurfin1

@date: 2018-11-17 

"""

import matplotlib.pyplot as plt

# lists of X and Y coordinates
X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]

# contruct the graph
plt.scatter(X,Y)

#customize point size, point color, and point character
plt.scatter(X, Y, s=60, c='red', marker='^')

# Add title and labels to the graph
plt.title('Relationship Between Temperature and Iced Coffee Sales')
plt.xlabel('Cups of Iced Coffee Sold')
plt.ylabel('Temperature in Fahrenheit')

plt.show()
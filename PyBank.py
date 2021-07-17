#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Python 3 PyBank Challenge Script 
# Joseph Chancey
# Created 7/17/2021

# Dependencies
import os
import csv

# Load File, assign it to variable
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# Variables
months_total = 0
month_change = []
net_change_li = []
net_total = 0
highest_increase = ["", 0]
highest_decrease = ["", 9999999999999]

# Loop through dataset to read it
with open(budget_csv) as bank_data:
    interpreter = csv.reader(bank_data)
    
    # Identify header through 'next()' function
    headings = next(interpreter)
    
    # Make sure correct data is assigned to correct variables
    first_row = next(interpreter)
    months_total = months_total + 1 
    net_total = net_total + int(first_row[1])
    last_net = int(first_row[1])
    
    # Loop through all data to assign to variables
    for i in interpreter:
        
        # Totals
        months_total = months_total + 1
        net_total = net_total + int(i[1])
        
        # Changes 
        net_change = int(i[1]) - last_net
        last_net = int(i[1])
        net_change_li.append(net_change)
        print(net_change_li)
        
        


# In[ ]:





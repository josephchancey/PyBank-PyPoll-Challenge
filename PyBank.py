#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
net_change = []
net_total = 0
highest_increase = ["", 0]
highest_decrease = ["", 9999999999999]

# Loop through dataset to store data into variable
with open(budget_csv) as bank_data:
    interpreter = csv.reader(bank_data)
    
    #Identify header through 'next()' function
    headings = next(interpreter)
    


# In[ ]:





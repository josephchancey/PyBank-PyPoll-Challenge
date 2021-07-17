#!/usr/bin/env python
# coding: utf-8

# In[16]:


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
# Set Value Minimums
highest_increase = ["", 0]
#Set Value Ceiling ~ Not Ideal If Values Cross Beyond This Ceiling
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
        month_change.append(i[0])
        
        # Greatest Incerase
        if net_change > highest_increase[1]:
            highest_increase[0] = i[0]
            highest_increase[1] = net_change
            
        # Greatest Decrease
        if net_change < highest_decrease[1]:
            highest_decrease[0] = i[0]
            highest_decrease[1] = net_change
            
    # Average Out
    net_mo_avg = sum(net_change_li) / len(net_change_li)
    
    #print
    summary_out = (
        f"\nPyBank Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {months_total}\n"
        f"Total $: {net_total}\n"
        f"Avg. Change: ${net_mo_avg:.2f}\n"
        #################################### Date                 # Total
        f"Greatest Profit Increase: {highest_increase[0]}, (${highest_increase[1]})\n"
        f"Greatest Profit Decrease: {highest_decrease[0]}, (${highest_decrease[1]})"
                  )

output_file = os.path.join(".", "Resources", "PyBank_Budget_Analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(summary_out)
    print("File Saved. Tasks Completed.")


# In[ ]:





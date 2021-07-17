#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Python 3 PyPoll Challenge Script 
# Joseph Chancey
# Created 7/17/2021

# Dependencies

import os
import csv

# Load File + Define Output path, assign to variables
poll_csv = os.path.join(".", "Resources", "election_data.csv")
output_file = os.path.join(".", "Resources", "PyPoll_Election_Analysis.txt")

# Totaling
total_votes = 0

# Candidates
candidate_options = []
candidate_votes = { }

# Winning Count Container
winning_candidate = ""
winning_total = 0

# Loop Through and Read Dataset
with open(poll_csv) as election_data:
    reader = csv.reader(election_data)
    
    # Identify header through 'next()' function
    header = next(reader)
    print(header)


# In[ ]:





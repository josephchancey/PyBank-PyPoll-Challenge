#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    
    # Loader animation
    for i in reader:
        # Loading Dots
        print(". ", end="")
        
        # Total Vote Count Adder
        total_votes = total_votes + 1
        
        # Candidate Name From Row
        candidate_name = i[2]
        
        # Condition for Candidate Name Not Being In Options of Existing Candidates
        # .append every name + total their votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            # Count Candidate Votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
            


# In[ ]:





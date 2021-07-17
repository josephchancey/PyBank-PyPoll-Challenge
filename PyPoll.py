#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
        # Loading Dots - Commented Out Due To Performence Issues
        #print(". ", end="")
        
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
        
# Output/Print results
with open(output_file, "w") as txt_file:
    election_results = (f"\nElection Results\n"
                       f"-------------------------\n"
                       f"Total Votes: {total_votes}\n"
                       f"-------------------------\n")
    
    #Print results
    print(election_results, end="")
    
    # Write Summary .txt File
    txt_file.write(election_results)
    
    # Vote Count For Each Candidate And Percentage of Total Votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(total_votes) * 100
        
        # Pick Winning Vote Count
        if(votes > winning_total):
            winning_total = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"

        print(voter_output, end="")

        txt_file.write(voter_output)
        
    # Statement For Winning Candidate
    winning_candidate_summary = (f"-------------------------\n"
                                f"Winner: {winning_candidate}\n"
                                f"-------------------------\n")
    
    # Update and Add Winning Candidate
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


# In[ ]:





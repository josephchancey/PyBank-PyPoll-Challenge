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


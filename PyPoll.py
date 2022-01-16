# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

# Import the datetime class from the datetime module.
import datetime
import random
import numpy
import os
import csv
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Assign a variable for the file to load and the path.
#file_to_load = "Module3\course\Resources\election_results.csv"
file_to_load = os.path.join("Module3", "course", "Resources", "election_results.csv")

# Open the election results and read the file.
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
     
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Module3", "course", "analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Arapahoe, Denver, Jefferson")   
    # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")
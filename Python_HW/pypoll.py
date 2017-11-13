import os


path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(path,"election_data_2.csv")

import csv

print(" ")
print(" ")
print("Election Results")
print("-------------------------")
with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile)
    rows_vote = list(csvreader)
    voters = (len(rows_vote)-1)
    print("Total Votes: " + str(voters))

print("-------------------------")
print(" ")
print("Results:")
print(" ")

import pandas as pd
import os

def round2(number):
    rounded_number = round(number, 2)
    string = str(rounded_number)
    return string


print("Vote Percentages (%):")
poll = pd.read_csv("election_data_2.csv")
poll.head()

decimal = poll["Candidate"].value_counts(normalize=True)
percent = ((decimal)*100)
percent
print(round2(percent))

candidates = poll["Candidate"].value_counts()
candidates
print(" ")
print("Vote Tallies:")
print(candidates)
print(" ")

winner_name = poll["Candidate"].value_counts().idxmax()
winner_name
print("-------------------------")
print("Winner: "+(str(winner_name)))
print("-------------------------")
print(" ")

with open('Election Results.txt', 'a') as f:
    print(" ",file=f)
    print(" ",file=f)
    print("Election Results",file=f)
    print("-------------------------",file=f)
    print("Total Votes: " + str(voters),file=f)
    print("-------------------------",file=f)
    print(" ",file=f)
    print("Results:",file=f)
    print(" ",file=f)
    print("Vote Percentages (%):",file=f)
    print(round2(percent),file=f)
    print(" ",file=f)
    print("Vote Tallies:",file=f)
    print(candidates,file=f)
    print(" ",file=f)
    print("-------------------------",file=f)
    print("Winner: "+(str(winner_name)),file=f)
    print("-------------------------",file=f)
    print(" ",file=f)
import os


path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(path,"budget_data_1.csv")

import csv
def round2(number):
    rounded_number = round(number, 2)
    string = str(rounded_number)
    return string

print(" ")
print("Financial Analysis")
print("-------------------------")
print(" ")

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile)
    rows = list(csvreader)
    month_count = (len(rows)-1)
    print("Total Months: " + str(month_count))

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile)
    rev = 0
    for row in csvreader:
        _rev = row[1]
        try:
            _rev = float(_rev)
        except ValueError:
            _rev = 0
        
        rev += _rev
        rev2 = round2(rev)
    print("Total Revenue: $" + (rev2))

import pandas as pd
import os
budget = pd.read_csv("budget_data_1.csv")
budget2= budget["Revenue"].diff()
changes_sum=budget2.sum()
avg_mean = round2(changes_sum/month_count)
print("Average Revenue Change: $" +str(avg_mean))

highest_increase = round2(budget2.max())
print("Greatest Increase in Revenue: $" + str(highest_increase))
lowest_increase = round2(budget2.min())
print("Greatest Decrease in Revenue: $" +str(lowest_increase))

print(" ")
print("-------------------------")
print(" ")

with open('Financial Analysis.txt', 'a') as f:
    print(" ",file=f)
    print(" ",file=f)
    print("Financial Analysis",file=f)
    print("-------------------------",file=f)
    print(" ",file=f)
    print("Total Months: " + str(month_count),file=f)
    print("Total Revenue: $" + (rev2),file=f)
    print("Average Revenue Change: $" +str(avg_mean),file=f)
    print("Greatest Increase in Revenue: $" + str(highest_increase),file=f)
    print("Greatest Decrease in Revenue: $" +str(lowest_increase),file=f)
    print(" ",file=f)
    print("-------------------------",file=f)
    print(" ",file=f)

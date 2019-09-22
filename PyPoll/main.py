#This is my main.py file for PyPoll

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

#Define Variables
total_votes = 0
election_dict = {}
vote_count=0

# Open the csv file
with open(csvpath, newline='') as csvfile:

    #read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    #print(csv_header) #debug

    row_count = sum(1 for row in csvfile)
    #print(row_count) # debug

# new loop
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)   

    for row in csvreader:
        # define variable for candidate
        candidate = row[2]

        # count total of all votes cast
        total_votes = total_votes+1

        # increment candidate's vote count if already in dictionary
        if candidate in election_dict.keys():
            election_dict[candidate] += 1

        # give candidate first vote and add to dictionary
        else:
            election_dict[candidate] = 1

    # print vote total before doing results loop
    print("                           ")
    print(" Election Results")
    print("---------------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------------")

    # print out results for all candidate key:value pairs
    for key,value in election_dict.items():
        print(f'{key}: {round(value*100/total_votes,3)}%  ({value})')

        # determine winner
        if vote_count < value:
            vote_count = value
            winner = key
    
    # print out results for the winner
    print("--------------------------")
    print(f'Winner: {winner}')
    print("--------------------------")


with open("PyPoll_output", 'w') as f:

    f.write("   Election Results\n")
    f.write("-----------------------\n")
    f.write(f'Total Votes: {total_votes}\n')
    f.write("-----------------------\n")
    for key,value in election_dict.items():
        f.write(f'{key}: {round(value*100/total_votes,3)}%  ({value})\n')

    f.write("-----------------------\n")
    f.write(f'Winner: {winner}\n')
    f.write("-----------------------\n")


    #f.write(f'Average Profit: {formatted_average}\n')
    #f.write(f'Greatest Profit: {greatest_profit_month}  {formatted_profit}\n')
    #f.write(f'Greatest Loss: {greatest_loss_month}  {formatted_loss}')
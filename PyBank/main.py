# This is my replacement main.py in PyBank.
# I completed my original PyBank at the end of class Saturday Sept 21.
# Unfortunately when I got home and ran it, it was a complete whacked out mess.
# I closed, opened, etc.  No dice.
# I spent a rather hefty amount of time debugging the ever-increasing errors.
# It only kept getting worse.
# I completely rewrote this Saturday night.  NOT FUN.
# Would love to know why this happened.
# So now it is with great relief that I present my PyyBank solution to you ... 


# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Define Variables
total_months = 0
net_total_profits = 0
greatest_profit = 1
greatest_loss = -1

# Open the csv file
with open(csvpath, newline='') as csvfile:

    #read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    #print(f"CSV Header: {csv_header}")   #debug

    #Count rows
    row_count = sum(1 for row in csvfile)
    #print(row_count)   # debug

#Open the csv file again.  not sure why this is necessary, but it won't run without this.
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

# loop through the rows
    for row in csvreader:
        #print (row) #debug

        #increment row counter to count months
        total_months = total_months + 1
        #print("total months = " + str(total_months)) #debug

        #Defining variables for each column
        month = (row[0])
        row_profit = int(row[1])

        #calculate total profit
        net_total_profits = net_total_profits + int(row[1])
        formatted_total = ('$' + format(net_total_profits, ',.0f'))

        #calculate average monthly profit & loss
        average = float(net_total_profits / total_months)
        formatted_average = ('$' + format(average, ',.0f'))

        # loop to identify profits by row
        if row_profit > greatest_profit:
            greatest_profit = row_profit
            greatest_profit_month = month
            formatted_profit = ('$' + format(greatest_profit, ',.0f'))
        
        # Loop to identify losses
        if row_profit < greatest_loss:
            greatest_loss = row_profit
            greatest_loss_month = month
            formatted_loss = ('$' + format(greatest_loss, '.0f'))

    # Print out results
    print("--------------------------")
    print("    Financial Analysis")     
    print("--------------------------")
    print(f"Total Months: {row_count}") 
    print(f"Net Profit: {formatted_total}")
    print(f"Average Profit: {formatted_average}")
    print(f"Greatest Profit: {greatest_profit_month}  {formatted_profit}")
    print(f"Greatest Loss: {greatest_loss_month}  {formatted_loss}")

# write output file
with open("PyBank_output", 'w') as f:
    f.write("     Financial Analysis\n")
    f.write("-----------------------\n")
    f.write(f'Total Months: {row_count}\n')
    f.write(f'Net Profit: {formatted_total}\n')
    f.write(f'Average Profit: {formatted_average}\n')
    f.write(f'Greatest Profit: {greatest_profit_month}  {formatted_profit}\n')
    f.write(f'Greatest Loss: {greatest_loss_month}  {formatted_loss}')
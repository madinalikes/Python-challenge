import os
import csv

#set variables
total_row_count = 0
dates = []
total = 0
profit = []
profit_change = []

greatest_increase = 0
greatest_decrease = 0

budget_csv = os.path.join("/Users/madin/Desktop", "PyBank","Resources","budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
 
    # calculate the total number of months included in the dataset
        total_row_count += 1
    # add the current rows date to the dates array
        dates.append(row[0])

    # Calculate the net total amount of "Profit/Losses"
        total += int(row[1])
    # add the current profit/loss amount to profit array
        profit.append(int(row[1]))

#loop through each month of value of "Profit/Losses" and caculate the change between each two monthes
for i in range(len(profit)-1):
        change = profit[i+1] - profit[i]
        profit_change.append(change)
        
        #cacualte average change in "Profit/Losses"
        average_change = round(sum(profit_change)/len(profit_change),2)
        
        # if the change is the greatest increase in profit
        if (change > greatest_increase):
            # set greatest increase month to the change month
            greatest_increase_month = dates[i+1]
            # set greatest increase to the change amount
            greatest_increase = change
        # if the change is the greatest decrease in profit
        if (change < greatest_decrease):
            # set greatest decrease month to the change month
            greatest_decrease_month = dates[i+1]
            # set greatest decrease to the change amount
            greatest_decrease = change

# print Analysis                  
print(" Financial Analysis")
print("-" * 25)
print(f"Total Months: {total_row_count}") 
print("Total: $" + str(total))
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    
    
#open the output file to export a text file with the results
output_file = os.path.join("/Users/madin/Desktop", "PyBank","Resources", "Financial_Analysis.txt")

with open(output_file, 'w', newline='') as text:
     text.write(" Financial Analysis\n")
     text.write("-----------------------\n")
     text.write(f"Total Months: {total_row_count}\n") 
     text.write(f"Total: $ {total}\n")
     text.write(f"Average Change: ${average_change}\n")
     text.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
     text.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

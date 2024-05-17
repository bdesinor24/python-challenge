# Import the CSV file into PyBank
import os
import csv
filepath= os.path.join("Resources","budget_data.csv")
# Created variables for the months, income, and percent changes
month = []
profit_loss = []
total_month=0
total_income=0
percentage_change=[]
# Opened the CSV file data
with open(filepath) as file_handler:
    lines = csv.reader(file_handler, delimiter=",")
    header_lines= next(lines)
# Using created variables in the for loop to calculate the total months and income
    for row in lines:
        total_month=total_month+1 
        total_income= total_income+ int(row[1])
# Using months and profit loss to calculate the percentage changes         
        month.append(row[0])
        profit_loss.append(int(row[1]))
        percentage_change.append(profit_loss[total_month-1]-profit_loss[total_month-2])
        total_percent_change=sum(percentage_change)
# Using max funtions to the greatest profit increase
    greatest_profit=max(percentage_change)
    greatest_profit_index=percentage_change.index(greatest_profit)
# Using percent change and the len funtion to divide percent change for the average
    average_percent_change=total_percent_change/(len(percentage_change)-1)
# Using min funtions to the greatest profit increase
    greatest_decrease_profit=min(percentage_change)
    greatest_decrease_index=percentage_change.index(greatest_decrease_profit)
    profit_loss=total_income/total_month
# Using print funtions to the display the outputs
    print("Financial Analysis") 
    print("------------------------------") 
    print("Total Months:",total_month)
    print("Total: $",total_income)
    print("Average Change:", average_percent_change)
    print(f"Greatest Increase in Profit:{month[greatest_profit_index]} ({greatest_profit})")
    print(f"Greatest Decrease in Profit: {month[greatest_decrease_index]} ({greatest_decrease_profit})")
# Using with open funtions to write to text file    
with open("Analysis/PyBank Output.txt","w") as file:
    file.write("Financial Analysis\n")
    file.write("------------------------------\n")
    file.write(f"Total Months: {total_month}\n")
    file.write(f"Total: ${total_income}\n")
    file.write(f"Average Change: {average_percent_change}\n")
    file.write(f"Greatest Increase in Profit:{month[greatest_decrease_index]} ({greatest_decrease_profit})\n")
    file.write(f"Greatest Decrease in Profit: {month[greatest_decrease_index]} ({greatest_decrease_profit})\n")

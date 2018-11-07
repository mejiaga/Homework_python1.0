import csv
import os
file = os.path.join('PyBank_Resources_budget_data.csv')
with open("PyBank_Resources_budget_data.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)

# The total number of months included in the dataset
# The total amount of "profit/Losses" over the period
# Average change in monthly profit "profit Losses"
total_months = []
total_profit = []
monthly_change = []

#new variable
with open("PyBank_Resources_budget_data.csv", encoding="utf-8") as budget_data:
# I had to look this up...I am not sure when to use this encoding?
    csvreader = csv.reader(budget_data) 
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

    
        # Append the total months and total profit to a list above(row[0]}) creates a list of months and profit
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_change)
max_decrease_value = min(monthly_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = os.path.join ("Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

          
    

   
    

    
   


        







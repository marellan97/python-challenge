#importing modules
import os, csv

#setting the path for the file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#output for the text file
text_file = "pybank_financial_analysis.txt"

#defining my lists
total_months = []
total_rev = []
monthly_change_rev = []

#open csv 
with open(budget_data_csv,newline="", encoding="utf-8") as budget:

     #defining my csvreader variable
    csvreader = csv.reader(budget,delimiter=",") 

    #so it does't count the header
    header = next(csvreader)  

    #loop
    for row in csvreader:

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_rev.append(int(row[1]))

    #loop through to get the change in monthly profits
    for i in range(len(total_rev)-1):
        
        #Taking the difference between both months and append to change in monthly profits
        monthly_change_rev.append(total_rev[i+1]-total_rev[i])

#Obtaining the max and min
max_increase = max(monthly_change_rev)
max_decrease = min(monthly_change_rev)

#Obtaining the max and min of each month
max_increase_month = monthly_change_rev.index(max(monthly_change_rev)) + 1
max_decrease_month = monthly_change_rev.index(min(monthly_change_rev)) + 1 

#Print statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_rev)}")
print(f"Average Change: {round(sum(monthly_change_rev)/len(monthly_change_rev),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")

#to print to my text file
with open(text_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_rev)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change_rev)/len(monthly_change_rev),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})")
    file.write("\n")



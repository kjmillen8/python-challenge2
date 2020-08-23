#Modules
import os
import csv

#Variable to hold Path to collect data from CSV
budget_data = os.path.join('Resources', 'budget_data.csv')

#Create the lists to store data
months = []
profits_losses = []
profits_losses_change = []

#Create variables
total_profit = 0
total_months = 0
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]

#Read csv and analyze
with open(budget_data) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    print(budget_data)

    #Skip header, skip first month to complete calculation for differences
    csv_header=next(budget_data)
    first_month=next(budget_data) 

    #Still include first month in total profit variable, total month variable 
    total_months = total_months + 1
    total_profit = total_profit + int(first_month[1])
    previous_profit = int(first_month[1])   

    #Loop through all the other rows in the dataset
    for row in budget_data:
    
        #Count the total months (rows) in the dataset
        total_months = total_months + 1

        #Count the net total of profits/losses
        total_profit = total_profit +int(row[1])

        #Hold the monthly difference in a list and calculate the monthly change
        profits_losses_change = int(row[1]-previous_profit)

        #Update previous_profit variable for next monthly change calculation
        previous_profit = int(row[1])

        #And create a list with the difference each month
        profits_losses = profits_losses + [profits_losses_change]

        #And keep a list of the whole date that shows the change each month
        months = months + [row[0]]

        #Greatest Profit Increase (date and amount)
        if profits_losses_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profits_losses_change 
        #& Greatest Profit Decrease (date and amount)
        if profits_losses_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profits_losses_change

    #Average monthly change in Profit/Losses
    monthly_change = sum(profits_losses/len(profits_losses))

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${round(monthly_change,2)}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})')

#Export text file with results of financial analysis
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total: ${total_profit}'])    
    csvwriter.writerow([f'Average Change: ${round(monthly_change,2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})'])
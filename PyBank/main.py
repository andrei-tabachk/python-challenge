import csv
import os

budget_path = os.path.join("Resources", "budget_data.csv")
with open(budget_path, "r") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")
    next(csvreader)

    #variables 
    total_months = 0
    total_profit_loss = 0
    previous_month_profit_loss = 0
    monthly_changes = []
    greatest_increase = ['',0]
    greatest_decrease = ['',0]

    #loop through rows
    for row in csvreader:
        #add up for total months
        total_months += 1

        #calculate total profit/loss
        profit_loss = int(row[1])
        total_profit_loss += profit_loss

        #monthly change
        if total_months > 1:
            monthly_change = profit_loss - previous_month_profit_loss
            monthly_changes.append(monthly_change)

            #greatest increase
            if monthly_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = monthly_change

            #greatest_decrease
            if monthly_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = monthly_change
        
        previous_month_profit_loss = profit_loss    

    # Calculate the average
    average_change = sum(monthly_changes) / len(monthly_changes)

    #Print title
    print("Financial Analysis")
    print("-----------------------")
    print('Total Months:', total_months)
    print("Total:", '${:,.2f}'.format(total_profit_loss))
    print('Average Change:', '${:.2f}'.format(average_change))
    print('Greatest Increase in Profits:', '{} (${:.2f})'.format(greatest_increase[0], greatest_increase[1]))
    print('Greatest Decrease in Profits:', '{} (${:.2f})'.format(greatest_decrease[0], greatest_decrease[1]))

    



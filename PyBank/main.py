import csv
data = csv.DictReader(open('Resources/budget_data.csv'))


months = 0
total = 0
previous_rev = 0
changes = []
max_increase_month = ""
min_decrease_month = ""

for row in data:
    months += 1
    rev = int(row["Profit/Losses"])
    total += rev
    
    if months > 1:
        change = rev - previous_rev
        changes.append(change)
    
    previous_rev = rev
    
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

data = csv.DictReader(open('Resources/budget_data.csv'))

for row in data:
    if int(row["Profit/Losses"]) - previous_rev == greatest_increase:
        max_increase_month = row["Date"]
    if int(row["Profit/Losses"]) - previous_rev == greatest_decrease:
        min_decrease_month = row["Date"]
    previous_rev = int(row["Profit/Losses"])
    
output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${total:,}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {max_increase_month} (${greatest_increase})
    Greatest Decrease in Profits: {min_decrease_month} (${greatest_decrease})
'''



print(output)






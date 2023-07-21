# Import the csv module to read data from a CSV file
import csv
# Open the 'budget_data.csv' file and use DictReader to read its contents as a dictionary
with open('Resources/budget_data.csv') as csv_file:
    data = list(csv.DictReader(csv_file))

# Store the header row
header = data[0].keys()

# Initialize variables to store data and perform calculations
months = 0
total = 0
previous_rev = 0
changes = []
max_increase_month = ""
min_decrease_month = ""

# Loop through each row in the CSV data
for row in data:
    # Count the number of months by incrementing the months variable
    months += 1
    # Get the revenue (Profit/Losses) for the current row and convert it to an integer
    rev = int(row["Profit/Losses"])
     # Add the revenue to the total
    total += rev
    
    # Calculate the change in revenue from the previous month and store it in the changes list
    if months > 1:
        change = rev - previous_rev
        changes.append(change)
        
     # Update previous_rev for the next iteration
    previous_rev = rev
    
# Calculate the average change in revenue  
average_change = sum(changes) / len(changes)
# Find the greatest increase and decrease in revenue
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Reopen the 'budget_data.csv' file to read the data again
data = csv.DictReader(open('Resources/budget_data.csv'))

# Loop through the data again to find the months with the greatest increase and decrease in revenue
for row in data:
    # Check if the change in revenue for the current row matches the greatest increase
    if int(row["Profit/Losses"]) - previous_rev == greatest_increase:
        max_increase_month = row["Date"]
    # Check if the change in revenue for the current row matches the greatest decrease
    if int(row["Profit/Losses"]) - previous_rev == greatest_decrease:
        min_decrease_month = row["Date"]
        # Update previous_rev for the next iteration
    previous_rev = int(row["Profit/Losses"])
   
# Create a formatted string to store the analysis output 
output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${total:}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {max_increase_month} (${greatest_increase})
    Greatest Decrease in Profits: {min_decrease_month} (${greatest_decrease})
'''


# Print the analysis output to the terminal
print(output)

# Specify the filename for the output text file
output_file = 'financial_analysis_output.txt'

# Open the file in write mode and write the output to it
with open(output_file, 'w') as file:
    file.write(output)

# Print a message indicating that the file has been successfully exported
print(f"Financial analysis output has been exported to '{output_file}'.")





















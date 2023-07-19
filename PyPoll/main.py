import csv

# Read the CSV file
with open('Resources/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    
     # Skip the header row
    next(reader) 
    
    #initialize variables
    total_votes = 0
    candidate_votes = {}

    # Iterate over each row in the CSV file
    for row in reader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate name
        candidate = row[2]

        # Increase the vote count for the candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
percentage_votes = {candidate: (votes / total_votes) * 100
    for candidate, votes in candidate_votes.items()}

# Find the winner based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Generate the election results
output = f'''
Election Results\n
-------------------------\n
Total Votes: {total_votes}\n
-------------------------\n
'''

for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    output += f'{candidate}: {percentage:.3f}% ({votes})\n'

output += f'-------------------------\n\nWinner: {winner}\n\n-------------------------\n'

print(output)









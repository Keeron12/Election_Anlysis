import csv

import os

# Assign a variable for the file to load and the path.
file_to_load = 'c:/Users/Keeron/Documents/Rice University Data Anlyst Bootcamp/Challenges/Challenge 3/Election_Anlysis/Resources/election_results.csv'

# Assign a variable to save the file to a path
file_to_save = 'c:/Users/Keeron/Documents/Rice University Data Anlyst Bootcamp/Challenges/Challenge 3/Election_Anlysis/analysis/election_analysis.txt'

# Set vote counter to zero
total_votes = 0

# Start a new candidates list
candidate_options = []

# Create a dictionary to hold the votes for each candidate
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Skip the header row
    headers = next(file_reader)

    # Print each row in the csv file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add candidates name to candidate option list
            candidate_options.append(candidate_name)

            # Track each candidates vote
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"

        f"---------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"----------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)


    
    # Determine the percentage of votes for each candidate by looping through the counts

    # Iterate thriugh the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
  
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # vote_percentage
            winning_count = votes

            winning_percentage = vote_percentage

            # Set the winning candidate equal to the candidate's name

            winning_candidate = candidate_name

        
    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (

        f"-------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count:,}\n"

        f"Winning Percentage: {winning_percentage:.1f}%\n"

        f"--------------------\n")

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

    print(winning_candidate_summary)

# Print the total votes
print(total_votes)



import os
import csv

# Set variables
total_votes = 0
candidate_list = []
unique_candidate = []
candidate_votes = []
percentage = []
final_data = []
winner = ""

# Open and read csv
csvpath = os.path.join("/Users/madin/Desktop", "PyPoll", 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    
    # Read through each row of data after the header
    for row in csvreader:
        total_votes += 1
        # Row two of the csv file is the candidate list
        candidate_list.append(row[2]) 
                
# Sort entire candidates list 
sorted_candidates = sorted(candidate_list, reverse=True)

# Compare each candidates name in sorted_candidates list to find unqiue candidates
for candidate in range(total_votes):
    # If the candidates are not equal to each other, put the candidate name in unique candidate list
    if sorted_candidates[candidate-1] != sorted_candidates[candidate]:
        unique_candidate.append(sorted_candidates[candidate-1]) 

# Loop through with nest loop sorted_candidates to cacualte how many total votes each unqiue candiate received and cacualte percentages
for i in range(len(unique_candidate)):
    candidate_count = 0

    for j in range(len(sorted_candidates)):
        if unique_candidate[i] == sorted_candidates[j]:
            candidate_count += 1
    candidate_votes.append(candidate_count)
    
    # Round numbers to three numbers after decimal point
    percentage.append(format((candidate_count/total_votes * 100), '.3f')+'%')

# Loop through the length of unique candidates    
# Compare each unqiue candiates's total votes to find the winner    
for v in range(len(unique_candidate)):
    if candidate_votes[v] > candidate_votes [v - 1]:
        winner = unique_candidate[v]

# Sort the candidate list before printing
unique_candidate = sorted(unique_candidate)

print("Election Results")  
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25) 

# Zip three lists of unique_candidate, percentage and candidate_votes
for (x,y,z) in zip (unique_candidate, percentage, candidate_votes):
# Print each unique candidate's percentage and candidate vote in individual line    
    print(str(x) + ": " + str(y) +" (" + str(z) + ")")
    final_data.append(str(x) + ": " + str(y) +" (" + str(z) + ")")
    
print("-"*25) 
print(f"Winner:  {winner}")
print("-"*25) 

# Open the output file to  export a text file with the final result
output_file = os.path.join(".", "Election_Results.txt")
with open(output_file, 'w', newline='') as text:
    text.write(" Election Results\n")
    text.write("-----------------------\n")
    text.write(f"Total Votes: {total_votes}\n") 
    text.write("-----------------------\n")
    for index in range(len(final_data)):
        text.write(f"{final_data[index]}\n")
    text.write(f"-----------------------\n")
    text.write(f"Winner:  {winner}\n")
    text.write(f"-----------------------\n")
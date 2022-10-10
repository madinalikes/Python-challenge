import os
import csv

#set variables
total_votes = 0
candidate_list = []
unique_candidate = []
candidate_votes = []
percentage = []
final_data = []
winner = ""

#set path for the file and read using CSV module
csvpath = os.path.join('.','Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #read the header row first
    csv_header = next(csvreader)
    
     #read each row of csvreader after the header
    for row in csvreader:
        total_votes += 1
        
        candidate_list.append(row[2]) 
                
#sort entire candidates list 
sorted_candidates = sorted(candidate_list)

#compare each candidates name in sorted_candidates list to find unqiue candidates
for h in range(total_votes):
    if sorted_candidates[h-1] != sorted_candidates[h]:
        unique_candidate.append(sorted_candidates[h-1]) 

#use nest loop to loop through sorted_candidates to cacualte how many total votes each unqiue candiate received         
#cacualte percentages
for i in range(len(unique_candidate)):
    candidate_count = 0

    for j in range(len(sorted_candidates)):
        if unique_candidate[i] == sorted_candidates[j]:
            candidate_count += 1
    candidate_votes.append(candidate_count)
    
    #round up and keep three zeros after decimal 
    percentage.append(format((candidate_count/total_votes * 100), '.3f')+'%')

#loop through the length of unique candidates    
#compare each unqiue candiates's total votes to find the winner    
for k in range(len(unique_candidate)):
    if candidate_votes[k] > candidate_votes [k - 1]:
        winner = unique_candidate[k]
        
print("Election Results")  
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25) 

#zip three lists of unique_candidate, percentage and candidate_votes
#print each unique candidate's percentage and candidate vote in individual line
for (x,y,z) in zip (unique_candidate, percentage, candidate_votes):
    print(str(x) + ": " + str(y) +" (" + str(z) + ")")
    final_data.append(str(x) + ": " + str(y) +" (" + str(z) + ")")
    
print("-"*25) 
print(f"Winner:  {winner}")
print("-"*25)      

#open the output file to  export a text file with the final result
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
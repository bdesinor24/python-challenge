# Import the CSV file into PyBank
import os
import csv
filepath= os.path.join("Resources","election_data.csv")
# Created variables for the votes and candidates
votes=[]
candidate_votes=dict
Raymon=0
Charles=0
Diane=0
# Opened the CSV file data
with open(filepath) as file_handler:
    lines = csv.reader(file_handler, delimiter=",")
    header_lines= next(lines)
    print("Election Results")
    print("-----------------------------")
# Using created variables in the for loop to calculate the total votes  
    for row in lines:
        votes.append(row[1])
        total_votes=len(votes)
# Using created variables in the for loop to calculate the total votes by candidate        
        if row[2] == "Raymon Anthony Doane":
            Raymon +=1
        elif row[2] == "Diana DeGette":
            Diane+=1
        elif row[2] == "Charles Casper Stockham":
            Charles+=1       
# Using print funtions to the display the outputs
    if Raymon> Diane:
        print("Total Votes:",total_votes)
        print("-----------------------------")
        print(f"Charles Casper Stockham: {Charles/total_votes:0%} ({Charles})")
        print(f"Diana DeGette: {Diane/total_votes:0%} ({Diane})")
        print(f"Raymon Anthony Doane: {Raymon/total_votes:0%} ({Raymon})")
        print("-----------------------------")
        print("Winner: Raymon Anthony Doane")
    elif Diane> Charles:
        print("Total Votes:",total_votes)
        print("-----------------------------")
        print(f"Charles Casper Stockham: {Charles/total_votes:0%} ({Charles})")
        print(f"Diana DeGette: {Diane/total_votes:0%} ({Diane})")
        print(f"Raymon Anthony Doane: {Raymon/total_votes:0%} ({Raymon})")
        print("-----------------------------")
        print("Winner: Diana DeGette")
    elif Charles>Raymon:
        print("Total Votes:",total_votes)
        print("-----------------------------")
        print("Winner: Charles Casper Stockham:")
# Using with open funtions to write to text file 
with open("Analysis/PyPoll Output.txt","w") as file:
    file.write("Election Results\n")
    file.write("------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------------\n")
    file.write(f"Charles Casper Stockham: {Charles/total_votes:0%} ({Charles})\n")
    file.write(f"Diana DeGette: {Diane/total_votes:0%} ({Diane})\n")
    file.write(f"Raymon Anthony Doane: {Raymon/total_votes:0%} ({Raymon})\n")
    file.write("------------------------------\n")
    file.write(f"Winner: Diana DeGette\n")

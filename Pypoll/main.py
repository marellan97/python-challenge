#importing modules
import os, csv

#setting the path for the file
election_data_csv = os.path.join("Resources", "election_data.csv")

#setting my variables
total_votes = 0 
charles_casper_stockham_votes = 0
diana_degette_votes = 0
raymon_anthony_doann_votes = 0

#opening csv file
with open(election_data_csv,newline="", encoding="utf-8") as csvfile:

    #delaring my csvreader variable
    csvreader = csv.reader(csvfile,delimiter=",") 

    #skipping the header
    header = next(csvreader) 

    #loop
    for row in csvreader:

        #getting total number of votes
        total_votes += 1

#print(total_votes)

        #total of 3 candidates, if found we need to know how many times the name comes up and how many votes each of them got
        if row[2]== "charles_casper_stockman":
            charles_casper_stockham_votes +=1
        elif row[2] == "diana_degette":
            diana_degette_votes +=1
        elif row[2] == "raymon_anthony_doann":
            raymon_anthony_doann_votes +=1


#creating dictionary with the lists created
candidates = ["charles_casper_stockham", "diana_degette", "raymon_anthony_doann"]
votes = [charles_casper_stockham_votes, diana_degette_votes, raymon_anthony_doann_votes]

#zip the list and find the winner using the max function
candidates_and_votes = dict(zip(candidates,votes))
key = max(candidates_and_votes, key=candidates_and_votes.get)

#turning values into percentage
charles_per = (charles_casper_stockham_votes/total_votes) *100
diana_per = (diana_degette_votes/total_votes) * 100
raymon_per = (raymon_anthony_doann_votes/total_votes)* 100

#print statements
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_per:.3f}% ({charles_casper_stockham_votes})")
print(f"Diana Degette: {diana_per:.3f}% ({diana_degette_votes})")
print(f"Raymon Anthony Doann: {raymon_per:.3f}% ({raymon_anthony_doann_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#setting path for txt. file
text_file ="Election_Analysis_Results.txt"

#to print to my txt. file
with open(text_file,"w") as file:
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Charles: {charles_per:.3f}% ({charles_casper_stockham_votes})\n")
    file.write(f"Diana: {diana_per:.3f}% ({diana_degette_votes})\n")
    file.write(f"Raymon: {raymon_per:.3f}% ({raymon_anthony_doann_votes})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"----------------------------\n")

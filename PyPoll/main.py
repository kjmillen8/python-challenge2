#Modules
import os
import csv

#Create the lists to store data
votes = []
vote_count = []
vote_percent = []
candidates = []
votes = 0

csv_reader = ['1','2']

election_data = os.path.join('Resources', 'election_data.csv')

#Read csv and analyze
with open(vote_counting) as csvfile:
    vote_counting = csv.reader(csvfile, delimiter=',')
    print(vote_counting)

    #Skip header, skip first month to complete calculation for differences
    csv_header=next(election_data)

    #Analyze votes
    for row in election_data:
        
        #Total # votes cast
        total_votes = total_votes + 1

        #Percentage of votes each candidate won
        a = append.(row:[2])

    for a in candidates:

        #List of candidates who received votes
        candidates.append(a)
        
        #Total votes for each candidate
        b = candidates.count(b)
        vote_count.append(b)

        #% of votes for each candidate
        c = (b/count)*100
        vote_percent.append(c)
    
    popular_vote_count = max(vote_count)
    winner = candidates[vote_count.index(popular_vote_count)]

print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")
print(f'popular_vote_count)
print(f'winner')
print("----------------------------")

#Export text file with results of election results
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}')
    csvwriter.writerow([f'Total: ${total_profit}'])    
    csvwriter.writerow([f'Average Change: ${round(monthly_change,2)}'])
    csvwriter.writerow([f'winner')
    csvwriter.writerow(["----------------------------"])
    
        
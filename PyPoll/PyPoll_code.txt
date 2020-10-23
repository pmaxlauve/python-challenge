filepath = "C:\\Users\\pmaxl\\OneDrive\\Desktop\\BootCamp\\Homework\\wk3_HW\\python-challenge\\PyPoll\\Resources\\PyPoll_data.csv"




import pandas as pd




    #import the data from csv
poll_data = pd.read_csv(filepath)




    #count the total number of votes
total_votes = len(poll_data["Voter ID"])


Candidate = []
    
    #loop over poll_data to find all unique entries to poll_data["Candidate"]
for x in poll_data["Candidate"]:
    if x not in Candidate:

        Candidate.append(x)

    
vote_count = []


    #loop over poll_data to find the total votes for each candidate and assign it to 'vote_count'
for x in Candidate:
    
    votes = (poll_data["Candidate"] == x).sum()
    vote_count.append(votes)
    

    #zip vote_count and Candidate together to form 1 df 'candidate_summary
candidate_summary = pd.DataFrame(zip(Candidate, vote_count), columns = ["Candidate", "Total Votes"])



    #create new column in candidate summary 'Vote Percent'
candidate_summary["Vote Percent"] = round(candidate_summary["Total Votes"]/total_votes*100, 3)

    #create varialbe 'most_votes
most_votes = max(vote_count)


    #find index value of max(vote_count)
w_index = [x for x, y in enumerate(vote_count) if y == most_votes]


    #convert w_index to an integer
w_ind = int(w_index[0])

    #create variable 'winner'
winner = Candidate[w_ind]



print("Election Results")
print("-----------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------")
for x in range(len(Candidate)):
    print(f'{candidate_summary["Candidate"][x]}: {candidate_summary["Vote Percent"][x]}%  ({candidate_summary["Total Votes"][x]})')


print("-----------------------")
print(f'Winner: {winner.upper()}!')
print("-----------------------")














    






    
    
    
    

    







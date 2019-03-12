import os
import csv

file = os.path.join('PyPoll', 'election_data.csv')

with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    count = 0
    names = []
    candidates = []
    votes = []
    vote_count = 1

    for row in csvreader:
        if row[0] != "":
            count += 1
            names.append(row[2])
    names.sort()
    candidates.append(names[0])

    for n in range(len(names)-1):
        if names[n+1] == names[n]:
            vote_count += 1
        else:
            candidates.append(names[n + 1])
            votes.append(vote_count)
            vote_count = 1
    votes.append(vote_count)

print("Election Results")
print("____________________________")
print("Total Votes: " + str(count))
print("____________________________")


for _ in range(len(candidates)):
    percent = round(votes[_]/count*100, 3)
    print(candidates[_] + ": " + str(percent) + "00% (" + str(votes[_]) + ")")
print("____________________________")


report = os.path.join('/Users/duynguyen/python-challenge',
                      'PyPoll', 'Election_Report.txt')

with open(report, 'w', newline="") as rep:
    rep.write("Election Results\n")
    rep.write("____________________________\n")
    rep.write("Total Votes: " + str(count))
    rep.write("\n____________________________\n")
    for _ in range(len(candidates)):
        percent = round(votes[_] / count * 100, 3)
        rep.write(candidates[_] + ": " + str(percent) +
                  "00% (" + str(votes[_]) + ")\n")
    rep.write("____________________________")
    max = 0
    maxpos = 0
    for _ in range(len(votes)):
        if votes[_] > max:
            max = votes[_]
            maxpos = _
    rep.write("\nWinner: " + candidates[maxpos])
    rep.write("\n____________________________")

print("Winner: " + candidates[maxpos])
print("____________________________")

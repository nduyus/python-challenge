import os
import csv

file = os.path.join('PyBank', 'budget_data.csv')

with open(file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    count = 0
    total = 0
    sum = 0
    diff = []
    dif = 0
    max, min = 0, 0
    maxpos, minpos = 0, 0
    datemax, datemin = "", ""
    date = []
    for row in csvreader:
        if row[0] != "":
            count += 1
        total = total + int(row[1])
        diff.append(float(row[1]) - dif)
        dif = float(row[1])
        date.append(row[0])

    for a in diff:
        sum = sum + int(a)
    print(sum)
    print(len(diff))
    average = round(sum/len(diff), 2)

    for n in range(len(diff)):
        if diff[n] > max:
            max = diff[n]
            maxpos = n
    for m in range(len(diff)):
        if diff[m] < min:
            min = diff[m]
            minpos = m
    for d in range(len(date)):
        if d == maxpos:
            datemax = date[d]
        elif d == minpos:
            datemin = date[d]

    print("Financial Analysis")
    print("_________________________")
    print("Total months: " + str(count))
    print("Total: $" + str(total))
    print("Average Change: $" + str(average))
    print("Greatest Increase in Profits: " + datemax + " ($" + str(max) + ")")
    print("Greatest Decrease in Profits: " + datemin + " ($" + str(min) + ")")

report = os.path.join('/Users/duynguyen/python-challenge',
                      'PyBank', 'Financial_Report.txt')
with open(report, 'w', newline='') as rep:
    rep.write("Financial Analysis")
    rep.write("\n_________________________")
    rep.write("\nTotal months: " + str(count))
    rep.write("\nTotal: $" + str(total))
    rep.write("\nAverage Change: $" + str(average))
    rep.write("\nGreatest Increase in Profits: " +
              datemax + " ($" + str(max) + ")")
    rep.write("\nGreatest Decrease in Profits: " +
              datemin + " ($" + str(min) + ")")

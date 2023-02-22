import sys
import csv

pointToSpent = int(sys.argv[1])
filename = sys.argv[2]

# Reading the csv data
data = []
with open(filename, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        row['points'] = int(row['points'])
        data.append(row)
  
# Sorting the data based on the timestamp
sorted_data = sorted(data, key=lambda x: x['timestamp'])

ret = {}
for i in sorted_data:
    # initialize to 0
    if i["payer"] not in ret:
        ret[i["payer"]] = 0
        
    # Case for negative points
    if i["points"] < 0:
        pointToSpent += abs(i["points"])
        continue
    else:
        if pointToSpent == 0:
            ret[i["payer"]] = ret.get(i["payer"]) + i["points"]
            continue
        # Case if the points is greater than the points
        if (pointToSpent - i["points"]) <= 0:
            remainder = i["points"] - pointToSpent
            ret[i["payer"]] += remainder
            pointToSpent = 0
        else:
            pointToSpent -= i["points"]
print(ret)    

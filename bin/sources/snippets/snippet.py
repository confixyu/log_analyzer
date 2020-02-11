import csv
from collections import defaultdict

# This func for now only read the txt file and store in a global variable
def inputFile(filePath):
    try:
        file = open(filePath, "r+")
        userFile = file.readlines()
        return userFile
    except Exception as e:
        print("Something is wrong reading user file:(")
        print(e)

# This func for now only read the csv file then filter and map into a dictionary 
# for the return
def readLogList():
    try:
        filename = 'sources/constants/logIDS.csv'
        fieldnames = ['ID', 'log']
        d = defaultdict(list)
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            next(reader)
            for row in reader:
                d[row['ID']].append(row['log'])
        print(dict(d))
        return dict(d)
    except Exception as e:
        print("Show error from readLogList")
        print(e)
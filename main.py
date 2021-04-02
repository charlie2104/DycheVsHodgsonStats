import os
import glob
import re
import csv

a = glob.glob("season*.csv")

fileName = a[0]

fields = []
rows = []
burnleyGames = []
palaceGames = []

burnleySeasonGoals = 0
palaceSeasonGoals = 0
burnleyGoalsConceded = 0
palaceGoalsConceded = 0

with open(fileName, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
        
#  printing first 5 rows
for row in rows:
    if(row[fields.index("HomeTeam")] == "Burnley" or row[fields.index("AwayTeam")] == "Burnley"):
        burnleyGames.append(row)
    if(row[fields.index("HomeTeam")] == "Crystal Palace" or row[fields.index("AwayTeam")] == "Crystal Palace"):
        palaceGames.append(row)

#print("Burnley results 17/18")
for match in burnleyGames:
    #print(match[fields.index("HomeTeam")] + " vs " + match[fields.index("AwayTeam")] + " (" + match[fields.index("FTHG")] + ", " + match[fields.index("FTAG")] + ")")
    if(match[fields.index("HomeTeam")] == "Burnley"):
        burnleySeasonGoals += int(match[fields.index("FTHG")])
        burnleyGoalsConceded += int(match[fields.index("FTAG")])
    else:
        burnleySeasonGoals += int(match[fields.index("FTAG")])
        burnleyGoalsConceded += int(match[fields.index("FTHG")])

        
#print("\nPalace results 17/18")
for match in palaceGames:
    #print(match[fields.index("HomeTeam")] + " vs " + match[fields.index("AwayTeam")] + " (" + match[fields.index("FTHG")] + ", " + match[fields.index("FTAG")] + ")")
    if(match[fields.index("HomeTeam")] == "Crystal Palace"):
        palaceSeasonGoals += int(match[fields.index("FTHG")])
        palaceGoalsConceded += int(match[fields.index("FTAG")])
    else:
        palaceSeasonGoals += int(match[fields.index("FTAG")])
        palaceGoalsConceded += int(match[fields.index("FTHG")])

print("Burnley stats")
print("burnley total goals scored: " + str(burnleySeasonGoals))
print("burnley goals conceeded: " + str(burnleyGoalsConceded))

print("\nPalace stats")
print("palace total goals scored: " + str(palaceSeasonGoals))
print("palace goals conceeded: " + str(palaceGoalsConceded))


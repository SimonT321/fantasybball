import csv
import glob

listPlayers = []

files = glob.glob("./allBoxScores/*.csv")
for f in files:
    with open(f) as boxScore:
        next(boxScore)
        reader = csv.reader(boxScore, delimiter=',')
        for r in reader:
            if(r[1] not in listPlayers):
                listPlayers.append(r[1])

with open('players.csv', 'w') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(listPlayers)

import csv

with open('players.csv', newline='') as allPlayerFile:
    reader = csv.reader(allPlayerFile)
    allPlayers = list(reader)

with open('rosteredPlayers.csv', newline='') as rosteredPlayerFile:
    reader = csv.reader(rosteredPlayerFile)
    rosteredPlayers = list(reader)

freeAgents = allPlayers
for player in allPlayers:
    if player in rosteredPlayers:
        freeAgents.remove(player)

with open('freeAgents.csv', 'w') as freeAgentFile:
    wr = csv.writer(freeAgentFile, quoting=csv.QUOTE_ALL)
    wr.writerow(freeAgents)
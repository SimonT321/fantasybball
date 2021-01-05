import pandas as pd
import csv

rosteredPlayersDF = pd.read_csv(r"rosteredPlayers.csv")
allPlayersDF = pd.read_csv(r"players.csv")

freeAgents = []
for player in allPlayersDF:
    if player not in rosteredPlayersDF:
        freeAgents.append(player)

freeAgentsDF = DataFrame(freeAgents)
freeAgentsDF.to_csv(r'freeAgents.csv')
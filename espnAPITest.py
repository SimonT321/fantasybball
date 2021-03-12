# This file finds all of the current rostered players in my fantasy league in writes them to the file 'rosteredPlayers.csv9'

from espn_api.basketball import League
import csv
# Init
league = League(league_id=26491754, year=2021, espn_s2='', swid='')

allTeams = []
rosteredPlayers = []
counter = 0
for team in league.teams:
    allTeams.append(team)
    for i in range(len(team.roster) - 1):
        rosteredPlayers.append(team.roster[i].name.split()[:2])

rosteredPlayers = list(map(lambda x: ' '.join(x), rosteredPlayers))

with open('rosteredPlayers.csv','w', newline='') as rosterFile:
    rosterWriter = csv.writer(rosterFile, quoting=csv.QUOTE_ALL)
    rosterWriter.writerow(rosteredPlayers)

freeAgents = []
pObject = []
pObject = league.free_agents(size=600)
for o in pObject:
    freeAgents.append(o.name)

freeAgents = list(map(lambda x: ' '.join(x), freeAgents))

with open('ESPNFreeAgents.csv','w', newline='') as freeAgentFile:
    freeWriter = csv.writer(freeAgentFile, quoting=csv.QUOTE_ALL)
    freeWriter.writerow(freeAgents)



print(freeAgents[5].name)
print(freeAgents[5].eligibleSlots)
    

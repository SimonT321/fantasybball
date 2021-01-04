# This file finds all of the current rostered players in my fantasy league in writes them to the file 'rosteredPlayers.csv9'

from espn_api.basketball import League
import csv
# Init
league = League(league_id=26491754, year=2021, espn_s2='AECbvyw1Y02wEo0LlQcX5lgTJU%2FAlxocr%2FXy84GxtgdZEP7efKX%2FlxDWyYgILTlm03oCh215z%2B2shXCfJh3TBJh1Cm6UzegJE%2FyMrJpPToTYh8kyD%2BSMgJpdkthHI8qDO5LRI2wd1fB32TazHtfCx2Di4qwpLc3q2kIG5uhzXP4gXg6DduKzwDyYrFT3THeIHn3l9bHWSygdV9rAJ81P%2BCCu5Z7exkqRPXdhEk%2FhjV1k6pm3AROA0HipTrcMKJVcOvBbgR6ttE7St5U5bNkyBDdQ', swid='{A412EB56-A5A1-46C9-A811-9A0B750D4CA9}')

allTeams = []
rosteredPlayers = []
counter = 0
for team in league.teams:
    allTeams.append(team)
    for i in range(len(team.roster) - 1):
        rosteredPlayers.append(team.roster[i].name)


with open('rosteredPlayers.csv','w', newline='') as rosterFile:
    rosterWriter = csv.writer(rosterFile, quoting=csv.QUOTE_ALL)
    rosterWriter.writerow(rosteredPlayers)

  

    

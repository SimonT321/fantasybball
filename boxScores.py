from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import csv

# Output all team box scores for January 1st, 2018 in JSON format to 1_1_2018_box_scores.csv
client.team_box_scores(day=1, month=1, year=2018, output_type=OutputType.CSV, output_file_path="./1_1_2018_box_scores.csv")


with open("schedule.csv") as schedule:
    next(schedule)
    reader = csv.reader(schedule, delimiter=',')
    for r in reader:
        date = r[0]
        date = date.split(' ')
        date = date[0].split('-')
        year = date[0]
        month = date[1]
        day = date[2]
        if(int(day) > 4 and int(month) == 1):
            break
        print(date)
        client.player_box_scores(day=day, month=month, year=year, output_type=OutputType.CSV, output_file_path="./allBoxScores/{}_{}_{}_box_scores.csv".format(month, day, year))
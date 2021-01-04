from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import csv
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
date = date.split('-')
print(date)
day = date[2]
month = date[1]
year = date[0]
client.player_box_scores(day=day, month=month, year=year, output_type=OutputType.CSV, output_file_path="./allBoxScores/{}_{}_{}_box_scores.csv".format(month, day, year))
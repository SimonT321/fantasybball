from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import csv

# Output all games for the 2020-2021 season in CSV format to 2020_2021_season.csv
print("Writing games for 2020-2021 season to CSV file")
client.season_schedule(season_end_year=2021, output_type=OutputType.CSV, output_file_path="./2020_2021_season.csv")

with open("2020_2021_season.csv") as csv_file:
    rdr = csv.reader(csv_file)
    with open("schedule.csv", mode = 'w') as schedule:
        wtr = csv.writer(schedule)
        for r in rdr:
            wtr.writerow((r[0], r[1], r[3]))
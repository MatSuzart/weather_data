from pathlib import Path
import csv

path = Path('data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

#Extrai as temperaturas máximas
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
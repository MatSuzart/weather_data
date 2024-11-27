from pathlib import Path
import csv
import matplotlib.pyplot as plt
import seaborn as sns  # Adicionei seaborn
from datetime import datetime

path = Path('data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

#Extrai datas, temperaturas máximas e mínims
#Extrai datas e temperaturas máximas
dates,highs,lows = [], [], []

'''for index, column_header in enumerate(header_row):
    print(index, column_header)'''
#Extrai as temperaturas máximas
highs = []
for row in reader:
    current_date = datetime.strtime(row[2],'%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)

#Plota as temperaturas máximas
plt.style.use('seaborn')
sns.set()  # Adicionei seaborn
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red',alpha=0.5)
ax.plot(dates, lows, color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#Formata o gráfico
ax.set_title("Daily High Temperatures July 2021", fontsize=24)
ax.set_xlabel("Date", fontsize=16)  
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)  
fig.autofmt_xdate()
plt.show()

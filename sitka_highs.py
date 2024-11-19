from pathlib import Path
import csv
import matplotlib.pyplot as plt
import seaborn as sns  # Adicionei seaborn

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

#Plota as temperaturas máximas
sns.set()  # Adicionei seaborn
fig, ax = plt.subplots()
ax.plot(highs, color='red')

#Formata o gráfico
ax.set_title("Daily High Temperatures July 2021", fontsize=24)
ax.set_xlabel("Date", fontsize=16)  # Corrigi o valor do rótulo
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)  # Corrigi o parâmetro

plt.show()

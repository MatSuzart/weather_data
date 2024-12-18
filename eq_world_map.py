from pathlib import Path
import json

import plotly.express as px
# Lê os dados como uma string e os converte em um objeto Python
path = Path('eq_data/eq_data_30_day_m1.json')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examina todos os terremotos no conjunto de dados
all_eq_dicts = all_eq_data['features']
mags = []
lons = []  # Adicionando a lista de longitudes
lats = []  # Adicionando a lista de latitudes

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats,lon=lons,title=title,color=mags,color_continupus_scale='Viridis',labels={'color':'Magnitude'},projection='natural earth')
fig.show()
print(mags[:10])  # Exibe as 10 primeiras magnitudes
print(len(all_eq_dicts))  # Exibe o número total de terremotos
print(lons[:5])  # Exibe as 5 primeiras longitudes
print(lats[:5])  # Exibe as 5 primeiras latitudes

# Cria uma versão mais legível do arquivo de dados
path = Path('eq_data/readable_eq_data.json')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

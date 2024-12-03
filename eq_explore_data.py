from pathlib import Path
import json

#Lê os dados como uma string e os converte em um objeto python
path = Path('eq_data/eq_data_1_day_m1.json')
contents = path.read_text()
all_eq_data = json.loads(contents)
#Examina todos os terremotos no conjunto de dados
all_eq_dicts = all_eq_data['features']
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'['mag']]
    mags.append(mag)
print(mags[:10])
print(len(all_eq_dicts))
#Cria uma versão mais legível do arquivo de dados
path = Path('eq_data/readable_eq_data.json')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
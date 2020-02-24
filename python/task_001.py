from collections import OrderedDict
from operator import getitem

# -----------------------------------------------------
# Read pokemon csv file into a dictionary,
# -----------------------------------------------------
with open("../data/pokemon.csv", mode='r') as csv_file:
    csv_reader = [[val.strip() for val in r.split(",")] for r in csv_file.readlines()]

(_, *header), *data = csv_reader
pokemon_dict = {}
for row in data:
    key, *values = row
    pokemon_dict[int(key)] = {key: value for key, value in zip(header, values)}

pokemon_count = len(pokemon_dict)
print(pokemon_count)
print(pokemon_dict[1]['Speed'])

# -----------------------------------------------------
# Cleaning data
# converting to appropriate data types
# -----------------------------------------------------
for i in range(1, pokemon_count):
    pokemon_dict[i]['Total'] = float(pokemon_dict[i]['Total'])
    pokemon_dict[i]['HP'] = float(pokemon_dict[i]['HP'])
    pokemon_dict[i]['Attack'] = float(pokemon_dict[i]['Attack'])
    pokemon_dict[i]['Defense'] = float(pokemon_dict[i]['Defense'])
    pokemon_dict[i]['Sp. Atk'] = float(pokemon_dict[i]['Sp. Atk'])
    pokemon_dict[i]['Sp. Def'] = float(pokemon_dict[i]['Sp. Def'])
    pokemon_dict[i]['Speed'] = float(pokemon_dict[i]['Speed'])
    pokemon_dict[i]['Legendary'] = pokemon_dict[i]['Legendary'] == 'TRUE'

# -----------------------------------------------------
# Exercises
# -----------------------------------------------------

# Print the `unique pokemon types`
unique_pokemon_types = []
for pokemon in range(1, pokemon_count):
    if pokemon_dict[pokemon]['Type 1'] not in unique_pokemon_types:
        unique_pokemon_types.append(pokemon_dict[pokemon]['Type 1'])
print(unique_pokemon_types)

# Print the names of the pokemon that have two types
two_type_pokemon = []
for pokemon in range(1, pokemon_count):
    if pokemon_dict[pokemon]['Type 1'] != '' and pokemon_dict[pokemon]['Type 2'] != '':
        two_type_pokemon.append(pokemon_dict[pokemon]['Name'])
print(two_type_pokemon)

# Print the names of the pokemon that are Legendary
legendary_pokemon = []
for pokemon in range(1, pokemon_count):
    if pokemon_dict[pokemon]['Legendary']:
        legendary_pokemon.append(pokemon_dict[pokemon]['Name'])
print(legendary_pokemon)

# 5 fastest pokemon
# PSA tuple of pokemon sorted in ascending order by speed
sorted_pokemon_speed_list = sorted(pokemon_dict.items(), key=lambda x: float(x[1]['Speed']))
# reverse for descending order
sorted_pokemon_speed_list.reverse()
top_five_list = sorted_pokemon_speed_list[1:5]

for pokemon in range(0, 4):
    print("Pokemon: " + top_five_list[pokemon][1]['Name'] + "\tSpeed " + str(top_five_list[pokemon][1]['Speed']))

# What is the type and defense of `Flareon`
flareon_dict = dict(filter(lambda x: x[1]['Name'] == 'Flareon', pokemon_dict.items()))
print(flareon_dict) #by printing the entire flareon dictionary, we can find out the id
print('Flareon type: ' + flareon_dict[148]['Type 1'])
print('Flareon defense: ' + str(flareon_dict[148]['Defense']))

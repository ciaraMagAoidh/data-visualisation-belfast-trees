from csv import DictReader

# -----------------------------------------------------
# Read pokemon csv file into a dictionary,
# -------------------------------------------------------
with open("../datasets/pokemon.csv", mode='r') as csv_file:
    csv_reader = [[val.strip() for val in r.split(",")] for r in csv_file.readlines()]

(_, *header), *data = csv_reader
pokemon_dict = {}
for row in data:
    key, *values = row
    pokemon_dict[int(key)] = {key: value for key, value in zip(header, values)}

pokemon_count = len(pokemon_dict)
print(pokemon_count)




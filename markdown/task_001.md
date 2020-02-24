****# Exploring data with python
## The Pokemon Dataset
In this activity, we will be exploring the pokemon data set with python. More information on this data set can be found on [Kaggle](https://www.kaggle.com/abcsds/pokemon).
* [Understanding the concept of Python Libraries](https://data-flair.training/blogs/python-libraries/)
* [Open and reading a CSV file with Python](https://realpython.com/python-csv/)
* [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

### What does the pokemon data look like?
```text
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
```

Now we know the structure of our data (a csv file), we can read it into a python dictionary using the [csv library](https://docs.python.org/3/library/csv.html).

```python
with open("../datasets/pokemon.csv", mode='r') as csv_file:
    csv_reader = [[val.strip() for val in r.split(",")] for r in csv_file.readlines()]

(_, *header), *data = csv_reader
pokemon_dict = {}
for row in data:
    key, *values = row
    pokemon_dict[int(key)] = {key: value for key, value in zip(header, values)}

pokemon_count = len(pokemon_dict)
print(pokemon_count)
```

We now have a python dictionary called `pokemon_dict` that we can use to explore the data from the pokemon data set.

### Try some of these exercises to learn more about the pokemon dataset.

* #### Print the `unique pokemon types` from type 1
* #### Print the names of the pokemon that have `two types`
* #### Print the names of the pokemon that are `Legendary`
* #### What pokemon have the `5 fastest speeds`?
* #### What is the type and defense of `Flareon`

 


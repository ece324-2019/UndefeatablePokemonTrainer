import pandas as pd
pokedex = pd.read_csv("pokedex.csv", header=None, names=['hp', 'atk', 'def', 'spa', 'spd', 'spe', 'type1', 'type2'])
print(pokedex)
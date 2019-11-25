import pandas as pd
import numpy as np
import random
from read_pokedex import *
from write_pokedex_csv import get_species

random.seed(0)

# rewarding parameters
alpha = 1.1
beta = 1.01

# punishment parameters
gamma = 0.95
delta = 1.05

epsilon = 100
start_val = 0.09

# move parameters
outrage = np.array([0., 1., 0., 0.])
outrage_comp = np.array([start_val, 0., start_val, start_val])

superpower = np.array([0., 0., 0., 1.])
superpower_comp = np.array([start_val,0.,start_val,start_val])

rockslide = np.array([0., 0., 1., 0.])
rockslide_comp = np.array([start_val,start_val,0., start_val])

irontail = np.array([1., 0., 0., 0.])
irontail_comp = np.array([0., start_val, start_val,start_val])


def reward(move, move_comp):
	global alpha, beta, epsilon
	move *= alpha
	move_comp *= beta
	move_epsilon = [i * random.random() / epsilon for i in move_comp]
	return move + move_comp + move_epsilon
def punish(move, move_comp):
	global gamma, delta, epsilon
	move *= gamma
	move_comp *= delta
	move_epsilon = [i * random.random() / epsilon for i in move_comp]
	return move + move_comp + move_epsilon

all_stats, all_move = get_data()

battle_df = pd.read_csv("battle_data.csv", names=['species', 'move', 'result'])
move = list(battle_df["move"])
result = list(battle_df["result"])
#print(battle_df.to_string())
species = get_species()
#species_index = [i for i in range(len(species))]
battle_species = list(battle_df["species"])
battle_species_index = [species.index(i) for i in battle_species]
battle_stats = np.empty([len(battle_species_index), 43])
for i in range(len(battle_stats)):
	battle_stats[i] = all_stats[battle_species_index[i]]

unique_pokemon = battle_df.species.unique()
unique_pokemon_index = [species.index(i) for i in unique_pokemon]
unique_pokemon_move = [np.copy(all_move[i]) for i in unique_pokemon_index]
unique_pokemon_move_comp = [np.copy(all_move[i]) for i in unique_pokemon_index]

for i in range(len(unique_pokemon_move_comp)):
	for j in range(4):
		if (unique_pokemon_move_comp[i][j] == 0):
			unique_pokemon_move_comp[i][j] = start_val
		else:
			unique_pokemon_move_comp[i][j] = 0

unique_pokemon_move_dict = dict(zip(unique_pokemon, unique_pokemon_move))
unique_pokemon_move_comp_dict = dict(zip(unique_pokemon, unique_pokemon_move_comp))
battle_move = np.empty([len(battle_species_index), 4])

for i in range(len(result)):
	if result[i] == "win":
		battle_move[i] = reward(unique_pokemon_move_dict[battle_species[i]], unique_pokemon_move_comp_dict[battle_species[i]])
	elif result[i] == "loss":
		battle_move[i] = punish(unique_pokemon_move_dict[battle_species[i]], unique_pokemon_move_comp_dict[battle_species[i]])

#normalization of data do not know if neccessary yet soft maxed it
for i in battle_move:
	total_sum = sum(np.exp(i))
	for j in range(len(i)):
		i[j] = np.exp(i[j]) / total_sum
print(battle_move)


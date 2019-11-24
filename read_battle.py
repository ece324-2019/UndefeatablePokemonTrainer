import pandas as pd
import numpy as np
from read_pokedex import *
from write_pokedex_csv import get_species

# rewarding parameters
alpha = 1.1
beta = 1.01

# punishment parameters
gamma = 0.95
delta = 1.1

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


def reward(move):
	global alpha, beta, outrage, outrage_comp, superpower, superpower_comp, rockslide, rockslide_comp, irontail, irontail_comp
	if (move == "Outrage"):
		outrage *= alpha
		outrage_comp *= beta
		return outrage + outrage_comp
	elif (move == "Superpower"):
		superpower *= alpha
		superpower_comp *= beta
		return superpower + superpower_comp
	elif (move == "Rock Slide"):
		rockslide *= alpha
		rockslide_comp *= beta
		return rockslide + rockslide_comp
	elif (move == "Iron Tail"):
		irontail *= alpha
		irontail_comp *= beta
		return irontail + irontail_comp

def punish(move):
	global gamma, delta, outrage, outrage_comp, superpower, superpower_comp, rockslide, rockslide_comp, irontail, irontail_comp
	if (move == "Outrage"):
		outrage *= gamma
		outrage_comp *= delta
		return outrage + outrage_comp
	elif (move == "Superpower"):
		superpower *= gamma
		superpower_comp *= delta
		return superpower + superpower_comp
	elif (move == "Rock Slide"):
		rockslide *= gamma
		rockslide_comp *= delta
		return rockslide + rockslide_comp
	elif (move == "Iron Tail"):
		irontail *= gamma
		irontail_comp *= delta
		return irontail + irontail_comp

battle_df = pd.read_csv("battle_data.csv", names=['species', 'move', 'result'])
all_stats, all_move = get_data()
species = get_species()
#species_index = [i for i in range(len(species))]
battle_species = list(battle_df["species"])
battle_species_index = [species.index(i) for i in battle_species]

battle_stats = np.empty([len(battle_species_index), 43])

for i in range(len(battle_stats)):
	battle_stats[i] = all_stats[battle_species_index[i]]

move = list(battle_df["move"])
result = list(battle_df["result"])
battle_move = np.empty([len(battle_species_index), 4])
for i in range(len(result)):
	if result[i] == "win":
		battle_move[i] = reward(move[i])
	elif result[i] == "loss":
		battle_move[i] = punish(move[i])

#normalization of data do not know if neccessary yet
for i in battle_move:
	for j in range(len(i)):
		i[j] /= sum(i)
print(battle_move)

import pandas as pd
import numpy as np

class haxorus:
	num = 731
	moves = ['Outrage', 'Iron Tail', 'Rock Slide', 'Superpower']
	moves_type = ['Dragon', 'Steel', 'Rock', 'Fighting']
	moves_damage = [120, 100, 75, 120]
	atk = 147
	type1 = 'Dragon'
	type2 = None
def calc_damage(power, my_atk, opp_def, move_type, my_type1, my_type2, opp_type1, opp_type2):
	modifier = calc_type_eff(my_type1, my_type2, move_type, opp_type1, opp_type2)
	base = (((2 * 100 / 5 + 2) * power * my_atk / opp_def) / 50) + 2
	damage = base * modifier
	return damage
def calc_type_eff(my_type1, my_type2, move_type, opp_type1, opp_type2):
	type_eff = type_chart.at[move_type, opp_type1]
	if (opp_type2) != None:
		type_eff *= type_chart.at[move_type, opp_type2]
	if (move_type == my_type1):
		type_eff *= 1.5
	elif ((my_type2 == None) and (move_type == my_type2)):
		type_eff *= 1.5
	return type_eff

pokedex = pd.read_csv("pokedex.csv", header=None, names=['hp', 'atk', 'def', 'spa', 'spd', 'spe', 'type1', 'type2'])
pokedex = pokedex.where((pd.notnull(pokedex)), None)

#pokedex['type2'] = pokedex['type2'].apply(lambda x: None if np.isnan(x) else x)

#print(pokedex)
type_chart = pd.read_csv("data/chart.csv", index_col=0)
move = [None for i in range(len(pokedex.index))]

for i in range(len(pokedex.index)):
	move[i] = haxorus.moves[np.argmax([
	calc_damage(haxorus.moves_damage[0], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[0], haxorus.type1,
				haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2']),
	calc_damage(haxorus.moves_damage[1], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[1], haxorus.type1,
				haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2']),
	calc_damage(haxorus.moves_damage[2], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[2], haxorus.type1,
				haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2']),
	calc_damage(haxorus.moves_damage[3], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[3], haxorus.type1,
				haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2'])
		])]

pokedex["Move"] = move
print(pokedex.to_string())

#print(pokedex.loc[[haxorus.num]])



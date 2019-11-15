import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class haxorus:
	moves = ['Outrage', 'Iron Tail', 'Rock Slide', 'Superpower']
	moves_type = ['Dragon', 'Steel', 'Rock', 'Fighting']
	moves_damage = [120, 100, 75, 120]
	atk = 147
	type1 = 'Dragon'
	type2 = None
def calc_damage(type_chart, power, my_atk, opp_def, move_type, my_type1, my_type2, opp_type1, opp_type2):
	modifier = calc_type_eff(type_chart, my_type1, my_type2, move_type, opp_type1, opp_type2)
	base = (((2 * 100 / 5 + 2) * power * my_atk / opp_def) / 50) + 2
	damage = base * modifier
	return damage
def calc_type_eff(type_chart, my_type1, my_type2, move_type, opp_type1, opp_type2):
	type_eff = type_chart.at[move_type, opp_type1]
	if (opp_type2) != 'None':
		type_eff *= type_chart.at[move_type, opp_type2]
	if (move_type == my_type1):
		type_eff *= 1.5
	elif ((my_type2 != 'None') and (move_type == my_type2)):
		type_eff *= 1.5
	return type_eff

def get_dataframe():
	return pd.read_csv("pokedex.csv", header=None, names=['species', 'hp', 'atk', 'def', 'spa', 'spd', 'spe', 'type1', 'type2'])

def get_labelled_dataframe():
	pokedex = get_dataframe()
	pokedex = pokedex.where((pd.notnull(pokedex)), 'None')
	type_chart = pd.read_csv("data/chart.csv", index_col=0)
	move = [None for i in range(len(pokedex.index))]

	for i in range(len(pokedex.index)):
		move[i] = haxorus.moves[np.argmax([
		calc_damage(type_chart, haxorus.moves_damage[0], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[0], haxorus.type1,
					haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2']),
		calc_damage(type_chart, haxorus.moves_damage[1], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[1], haxorus.type1,
					haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2']),
		calc_damage(type_chart, haxorus.moves_damage[2], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[2], haxorus.type1,
					haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2']),
		calc_damage(type_chart, haxorus.moves_damage[3], haxorus.atk, pokedex.loc[i,'def'], haxorus.moves_type[3], haxorus.type1,
					haxorus.type2, pokedex.loc[i,'type1'], pokedex.loc[i,'type2'])
			])]
	pokedex = pokedex.set_index('species')
	pokedex["move"] = move
	return pokedex

stats_data_mean = 0
stats_data_std = 0
data = []
def get_data():
	global stats_data_mean
	global stats_data_std
	pokedex = get_labelled_dataframe()
	list_of_stats = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
	stats_data = pokedex[list_of_stats] # extract continuous features into a separate variable
	stats_data_mean = stats_data.mean()
	stats_data_std = stats_data.std()
	stats_data = (stats_data - stats_data_mean) / stats_data_std # normalize the features
	#print(stats_data.head())
	stats = stats_data.to_numpy() # convert to numpy array
	#print(continuous_arr.shape)


	label_encoder = LabelEncoder()
	list_of_categories = ['type1', 'type2', 'move']
	categorical_data = pokedex[list_of_categories] # extract categorical features into a separate variable

	categorical_data = categorical_data.apply(label_encoder.fit_transform) # transform features into integers
	oneh_encoder = OneHotEncoder(categories='auto', sparse=False)
	moves = oneh_encoder.fit_transform(categorical_data[['move']])
	# print(moves)
	types = categorical_data[['type1', 'type2']]
	# print(types)
	one_hot_types = oneh_encoder.fit_transform(types)
	global data
	data = np.concatenate([one_hot_types, stats], axis=1)
	return data, moves

def inputize_data(position):
	global data
	return (data[position])

get_data()
# print(data[0])
pokedex = get_dataframe()
# pokedex = pokedex.set_index('species')
# print (pokedex.loc[pokedex['species']=='Haxorus'].index.values[0])
# print (stats_data_std)


import csv
file = open('data/pokedex.txt', 'r')

#file = open('bulbasaur.txt', 'r')
allLines = []
for line in file:
	allLines.append(line.lstrip().rstrip())
types = [i for i in allLines if i.startswith('types')]
types = [i.split(',') for i in types]

baseStats = [i for i in allLines if i.startswith('baseStats')]
baseStats = [i.split(',') for i in baseStats]

hp = []
atk = []
defe = []
spa = []
spd = []
spe = []
type1 = []
type2 = [None for i in range(1068)]

k = 0
for i in types:
	i.remove('')
for i in types:
	for j in range(len(i)):
		i[j] = i[j].replace("[","").replace("]","").replace("types:","").replace('"',"").replace(" ","")
		if j == 0:
			type1.append(i[j])
		else:
			type2[k] = i[j]
	k += 1

for i in baseStats:
	i.remove('')
	for j in range(len(i)):
		if i[j].startswith("baseStats"):
			hp.append(int(i[j].replace("baseStats: {hp: ", "")))
		elif i[j].startswith(" atk"):
			atk.append(int(i[j].replace(" atk: ", "")))
		elif i[j].startswith(" def"):
			defe.append(int(i[j].replace(" def: ", "")))
		elif i[j].startswith(" spa"):
			spa.append(int(i[j].replace(" spa: ", "")))
		elif i[j].startswith(" spd"):
			spd.append(int(i[j].replace(" spd: ", "")))
		elif i[j].startswith(" spe"):
			spe.append(int(i[j].replace(" spe: ", "").replace("}", "")))
csvData = [[hp[i], atk[i], defe[i], spa[i], spd[i], spe[i], type1[i], type2[i]]for i in range(1068)]
with open('pokedex.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(csvData)
csvFile.close()
print(csvData)
print(type1)
print(type2)
print(hp)
print(atk)
print(defe)
print(spa)
print(spd)
'''
print(len(types))
print(len(hp))
print(len(atk))
print(len(defe))
print(len(spa))
print(len(spd))
print(len(type1))
print(len(type2))
#print(baseStats)'''
file.close()




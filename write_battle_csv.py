import csv

with open('UndefeatableNN.csv', 'r') as f:
  reader = csv.reader(f)
  lines = list(reader)

battleData = []

for line in lines:
  line.pop(0) # Remove the battle number
  pokemon = line.pop(0)
  move = line.pop(0)
  result = line.pop(-1)
  battleData.append([pokemon, move, result])

with open('battle_data.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(battleData)
csvFile.close()



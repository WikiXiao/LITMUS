import csv
import random

csvFile = open('negative_all.csv','r',encoding='latin-1')
reader = csv.reader(csvFile)

numOfData = 1600000
negative_data_size = 10000
random_index = []
data = []

for i in range(numOfData):
	idx = random.randint(0,numOfData)
	if idx not in random_index:
		random_index.append(idx)
	if(len(random_index)==negative_data_size):
		break

for item in reader:
	data.append(item[5])

output = open('negative.txt','w',encoding='utf-8')
for i in range(len(random_index)):
	idx = random_index[i]
	ret = data[idx]
	output.write(ret+"\n")
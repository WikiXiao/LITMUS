import random
import re
#num of data 5314980
numOfData = 5314980
positive_data_size = 10000
random_index = []

for i in range(numOfData):
	idx = random.randint(0,numOfData)
	if idx not in random_index:
		random_index.append(idx)
	if(len(random_index)==positive_data_size):
		break

data = open('positive_all.json','r').readlines()
output = open('positive.txt','w')
for i in range(len(random_index)):
	idx = random_index[i]
	msg = data[5*idx+2]
	pattern = re.compile(r'..\"message\": \"([\s\S]*)\",')
	ret = pattern.findall(msg)[0]
	output.write(ret+"\n")

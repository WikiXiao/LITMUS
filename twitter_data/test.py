def getTweetFromTrainingData(filename):
	data = open(filename,'r').readlines()
	numOfData = len(data)//5
	for i in range(numOfData):
		date_idx = 5*i+1
		msg_idx = 5*i+2
		loc_idx = 5*i+3
		date = data[date_idx]
		msg = data[msg_idx]
		loc = data[loc_idx]

getTweetFromTrainingData('tweetData.json')



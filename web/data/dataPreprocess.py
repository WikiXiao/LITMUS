import json
with open("./states.json",'r') as load_f:
	load_dict = json.load(load_f)


stateList = []
for record in load_dict:
	stateList.append(record)

newDict = {}
for state in stateList:
	newDict[state] = {}
	for record in  load_dict[state]:
		date =  record['date']
		newDict[state][date]={}
		newDict[state][date]['confirmed']=record['confirmed']
		newDict[state][date]['deaths']=record['deaths']

	
	

json_str = json.dumps(newDict)
with open('preprocessed.json', 'w') as json_file:
	json_file.write(json_str)

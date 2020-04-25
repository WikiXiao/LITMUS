import os
import json
import csv

path ={2:[27,28,29],3:[i for i in range (1,24)]}
jsonFile = open("tweetData.json","w")
#writer = csv.writer(csvfile)

#writer.writerow(["tweetdate","location","message"])
for month in path:
	for date in path[month]:
		dirpath = os.path.join('./',str(month).zfill(2),str(date).zfill(2))
		subdirs = os.listdir(dirpath)
		if ".DS_Store" in subdirs :
			subdirs.remove(".DS_Store")
		for subdir in subdirs:
			newdirpath = os.path.join(dirpath, subdir)
			filelists =  os.listdir(newdirpath)
			if ".DS_Store" in filelists:
				filelists.remove(".DS_Store")
			for filelist in filelists:
				finalDirPath = os.path.join(newdirpath,filelist)
				with open(finalDirPath, "r") as f:
					for line in f:
						content = json.loads(line)
						#print(content)
						#print(content.keys())
						message = content["text"]
						message.replace("\n", " ")
						tweetdate = "2020-"+str(month).zfill(2)+"-"+str(date).zfill(2)
						location = content["user"]["location"]
						if  location  is None:
							location = ""
						data_Dict = {"tweetdate":tweetdate, "message": message, "location":location}
						json_str = json.dumps(data_Dict, indent=2)
						jsonFile.write(json_str+"\n")
						#print(tweetdate, location, message )
						#writer.writerows([tweetdate, location, message ])
#csvfile.close()
jsonFile.close()
print(dirpath)
print(os.listdir(dirpath))
import matplotlib.pyplot as plt
import re
import csv

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_abbr = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
twitter_states = [0]*len(states)
twitter_date = [0]*23

twitter_data = open('twitter.json','r').readlines()
numOftweets = len(twitter_data)//3

collaborative_file = open('collaborative.csv','r')
collaborative_data = csv.reader(collaborative_file)
collaborative_states = [0]*len(states)
collaborative_date = [0]*23

date_p = re.compile(r'..\"tweetdate\": \"([\s\S]*)\",')
msg_p = re.compile(r'..\"message\": \"([\s\S]*)\",')
loc_p = re.compile(r'..\"location\": \"([\s\S]*)\",')

for i in range(numOftweets):
	date_str = twitter_data[3*i]
	msg_str = twitter_data[3*i+1]
	loc_str = twitter_data[3*i+2]
	date = date_p.findall(date_str)[0]
	y_str,m_str,d_str = date.split('-')
	y = int(y_str)
	m = int(m_str)
	d = int(d_str)
	msg = msg_p.findall(msg_str)[0]
	loc = loc_p.findall(loc_str)[0]
	if m<2 or (m==2 and d<=28) or (m==3 and d>=23) or m>=4:continue
	state_idx = states.index(loc)
	twitter_states[state_idx]+=1
	if m==2:
		date_idx = d-29
	else:
		date_idx = d
	twitter_date[date_idx]+=1

for item in collaborative_data:
	if collaborative_data.line_num == 1:
		continue
	date = item[1]
	y_str,m_str,d_str = date.split('-')
	y = int(y_str)
	m = int(m_str)
	d = int(d_str)
	num = int(item[2])
	loc = item[5]
	if m<2 or (m==2 and d<=28) or (m==3 and d>=23) or m>=4:continue
	if loc in states:
		state_idx = states.index(loc)
		collaborative_states[state_idx]+=num
		if m==2:
			date_idx = d-29
		else:
			date_idx = d
		collaborative_date[date_idx]+=num


# plt.bar(range(len(twitter_states)),twitter_states,color='rgb')
# plt.title('Num of Probalistic Source for each State')
# plt.xlabel('State')

plt.bar(range(len(collaborative_states)),collaborative_states,color='rgb')
plt.title('Num of Collaborative Source for each State')
plt.xlabel('State')

# l1=plt.plot(range(23),twitter_date,'r--',label='probalistic')
# l2=plt.plot(range(23),collaborative_date,'g--',label='collaborative')
# plt.title('Num of Instances by Date')
# plt.xlabel('Date')

plt.legend()
plt.show()



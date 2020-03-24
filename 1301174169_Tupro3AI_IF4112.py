# this Code Made by Putri Apriyanti Windya (1301174169) IF-41-12 Informatics Engineering, Telkom University
# In this case i use three category they are high, low and mid. so that, i have eight point in each case. eight point for Follower and eight for engagement 

import csv
import matplotlib.pyplot as plt

# read data from given csv in this task
def readDataTest():
	dataTest = []
	with open('influencers.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader: 
			dataTest.append(row)

	return dataTest

# sava data to new excel
def saveData(data):
	with open('chosen.csv','w',newline ='\n') as hasil:
		write = csv.writer(hasil,dialect='excel')
		for row in data : 
			write.writerow([row[0]])
			print([row[0]])
	hasil.close()

# count value to make a linguistic function or membership function
def get(a,b,c,d):
	return (a-b)/(c-d)

# count low value of membership function	
def low(x,a,b):
	if(x<=a): return 1
	elif(x<=b): return get(b,x,b,a)
	else: return 0

# count mid value of membership function	
def mid(x,a,b,c,d):
	if(x<=a): return 0;
	elif(x<=b): return get(x,a,b,a)
	elif(x<=c): return 1
	elif(x<=d): return get(c,x,c,d)
	else: return 0

# count high value of membership function	
def high(x,a,b):
	if(x<=a): return 0
	elif(x<=b): return get(x,a,b,a)
	else: return 1;

# fuzzification process
def fuzzificationProcess(data):
	data.append(high(float(data[1]),followerA,followerH)) #3
	data.append(mid(float(data[1]),followerC,followerD,followerE,followerF)) #4
	data.append(low(float(data[1]),followerA,followerB)) #5
	data.append(high(float(data[2]),engaG,engaH))#6
	data.append(mid(float(data[2]),engaC,engaD,engaE,engaF)) #7
	data.append(low(float(data[2]),engaA,engaB)) #8
	return data

# inference process
def inferenceProcess(data):
	data.append(max(min(data[6],data[3]),min(data[6],data[4]),min(data[3],data[7])))
	data.append(max(min(data[6],data[5]),min(data[8],data[3]),min(data[4],data[7])))
	data.append(max(min(data[4],data[8]),min(data[7],data[5]),min(data[8],data[5])))
	return data

# defuzzification process
def defuzzificationProcess(y):
	acc = 95 # accepted value
	cons = 65 # considered value
	rejc = 45 # rejected value 
	y.append((acc*y[9]+(cons*y[10])+(rejc*y[11]))/(y[9]+y[10]+y[11]));
	return y;

# take element of array index 12
def take(elem):
	return elem[12]

# Initiate Follower's point
followerA=20000;
followerB=30000;
followerC=20000;
followerD=30000;
followerE=45000;
followerF=50000;
followerG=45000;
followerH=60000;

# Initiate Engagement's point
engaA=2;
engaB=2.5;
engaC=2;
engaD=3;
engaE=4;
engaF=4.5;
engaG=3;
engaH=6;

data = readDataTest() # read data from csv

dataplt = readDataTest() 

for i in range(1,101): # process data using 3 step of fuzzy logic
	data[i]=fuzzificationProcess(data[i])
	data[i]=inferenceProcess(data[i])
	data[i]=defuzzificationProcess(data[i])

data.pop(0)
data.sort(key=take,reverse=True) 
for i in range(80):
	data.pop(20)

# save best 20 of data test (influencers.csv)
saveData(data)

# print(data[3][9])


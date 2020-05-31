
import json
from pprint import pprint
import random
import time
star_time=time.time()
r=[]
rooms={}
Students=[]
shufle={}
with open("studentsdata.json","r+") as data:

	
	# # this loop is to enter in the list containing all the data
	data=json.load(data)

	# 	# this loop is to enter in the dictionary and to get keys
	for i in data:

		# 		# i am appending the rooms name in one list named r
		for j in i:
			r.append(j)
			# print(r)
			for l in i[j]:
				Students.append(l)
				if j not in rooms:
					rooms[j]=[i[j][l]]
				else:
					rooms[j].append(i[j][l])
	print(Students)
# print(rooms)

# r=["R1","R2"]
# rooms={"R1":[1,2,3,4],"R2":[5,6,7,8]}
# Students=["Tarik anwar","Sonu","Somesh shakya","Amarpal shakya","Bijender","Shubham","Kaushal","Akash"]
# shufle={}

while True:
	k={}

	# i am usng tis condition to insure that every one has alloted his room or not
	if len(Students)==0:
		break
	else:

		# i am using random here to take rooms name and for taking bed no. by using that random room name from thier lists
		i=random.choice(Students)
		for name in data:
			for j in name:
				# print(name[j])
				while True:
					a=random.choice(r)
					if i in name[a]: 
						continue
					else:
						break



		# this condition will check whether the particular room has empty bed to allote or not
		# if it doesn't have bed to allote and all bed are full then it will delete that room my room names list
		if len(rooms[a])==0:
			del rooms[a]
			r.remove(a)
		else:
			b=random.choice(rooms[a])
			k[i]=b
			if a not in shufle:
				shufle[a]={}
				shufle[a].update(k)
			else:
				shufle[a].update(k)
			rooms[a].remove(b)
			# print(rooms[a])
			Students.remove(i)
pprint(shufle)
# i am storing shufled data in a json file so that i can use that in future or for some other purposes
with open("studentsdata.json","w") as file:
	json.dump([shufle],file,indent=4)

print(time.time())
print(star_time)
print(time.time()-star_time)

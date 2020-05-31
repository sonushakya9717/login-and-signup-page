# marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]
# total_marks = 0
# counter = 0
# while counter <= len(marks):
# 	total_marks = total_marks + marks[counter]
# 	counter = counter + 1
# print(total_marks)

# name = ["Savitri", "Phule", "26"]
# # Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
# print (name[0]+name[1])
# # Code mei dekhiye naam theek se print kyu nahi ho raha
# def definition_say_hello():
# 	print("navgurukul")
# 	print ("NavGurukul mei humein apni learning ki responsibility leni padti hai.")

# definition_say_hello()

# print ("NavGurukul mei hum sab logo ko ek tarah se treat karte hai.")

# definition_say_hello()

# def ask_question():
# 	print("Who is the founder of Facebook?")
# 	print("- Mark Zuckerberg")
# 	print("- Bill Gates")
# 	print("- Steve Jobs")
# 	print("- Larry Page")

# a=1
# while a<=100:
# 	ask_question()
# 	a+=1
# a="a"
# if len(a)==0


# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif")
# say_hello("kartik")

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# num_y = 22
# add_numbers(num_x, num_y)

# def say_hello_language(name, language):
#     if language == "hindi":
#         print ("Namaste ", name)
#         print ("Aap kaise ho?")
#     elif language == "punjabi":
#         print ("Sat sri akaal ", name)
#         print ("Tuhada ki haal hai?")
#     else:
#         print ("Hello ", name)
#         print ("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# # say_hello_language("Kavay", "hindi")

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")



# def add_numbers_list(list1 ,list2):
# 	for i in range(len(list1)):
# 		print( list1[i]+list2[i])
# add_numbers_list([50,10,13],[10,20,60])

# def check_numbers(list1,list2):
# 	for i in range(len(list1)):
# 		if list1[i]%2==0 and list2[i]%2==0:
# 			print("dono even hai")
# 		else:
# 			print("dono even nhi hai")
# check_numbers([2,6,18,10,3,75],[6,19,24,12,3,87])
# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print (sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print (sum2)
# print (sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print (number_a)

# def calculator():
# 	a=[1,2,3,4]
# 	b=[2,3,4,5]
# 	c=[]
# 	for i in range(len(a)):
# 		if i==0:
# 			d=(a[i]+b[i])
# 		elif i==1:
# 			d=(a[i]-b[i])
# 		elif i==2:
# 			d=(a[i]*b[i])
# 		elif i==3:
# 			d=(a[i]/b[i])
# 		else:
# 			print("system crashed")
# 		c.append(d)
# 	print(c)

# calculator()

# def max_marks():
# 	marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# 	for i in marks:
# 		print(max(i))
# max_marks()

# sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# print("initial list",num_list)
# num_list_sub_20 = numbers_less_than_twenty(num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)



# import random 

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

# while True:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     moves=['rock','scissors','paper']
#     random_move = random.choice(moves)
#     computer_choice = random_move

#     if player_choice == computer_choice:
#         print ('Draw!')
#     elif  player_choice== 'rock' and computer_choice == 'scissors':
#         win()
#     elif  player_choice== 'paper' and computer_choice== 'scissors':
#         lose()
#     elif player_choice== 'scissors' and computer_choice == 'paper':
#         win()
#     elif player_choice == 'scissors' and computer_choice== 'rock':
#         lose()
#     elif player_choice == 'paper' and computer_choice == 'rock':
#         win()
#     elif player_choice =='rock'  and computer_choice =='paper' :
#         lose()
#     again = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break

# from random import randint # allows you to generate a random number

# # variables for the alien
# alive = True
# stamina = 10

# # this function runs each time you attack the alien
# def report(stamina):
# # syntactic error in if else statements
#     if stamina > 8:
#         print ("The alien is strong! It resists your pathetic attack!")
#     elif stamina > 5:
#         print ("With a loud grunt, the alien stands firm.")
#     elif stamina > 3:
#         print ("Your attack seems to be having an effect! The alien stumbles!")
#     elif stamina > 0:
#         print ("The alien is certain to fall soon! It staggers and reels!")
#     else:
#         print ("That's it! The alien is finished!")

# # main function - accepts your input for fight with the alien
# def fight(stamina): # stamina
#     while stamina > 0:
#       # won't enter this loop ever. The function will always return False.
#         response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run:-")
#         # chose a response from ( hit, attack, fight and run)
#         # fight scene
#         if "hit" ==response or "attack" ==response:
#             less = randint(0, stamina)
#             stamina -= less # subtract random int from stamina
#             report(stamina) # see function above
#         elif response=="fight":
#             print ("Fight how? You have no weapons, silly space traveler!")
#         elif "run" in response:
#             print ("Sadly, there is nowhere to run.")
#             print ("The spaceship is not very big.")
#         else:
#             print ("The alien zaps you with its powerful ray gun!")
#             return True
#     return False

# print ("A threatening alien wants to fight you!\n")
# # quotes at the end.

# # call the function - what it returns will be the value of alive
# alive = fight(stamina)

# if alive==True: # means if alive == True
#     print ("\nThe alien lives on, and you, sadly, do not.\n")
# else:
#     print ("\nThe alien has been vanquished. Good work!\n")

# file = open("k.txt")
# data = file.read()
# print (data)
# file.close()

# count=0
# file= open("k.txt")
# for i in file:
# 	count+=1
# print(count)


# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# file=open("file-question3.txt","a")
# for i in banks_list:
	# b=fi/le.write(i+"\n")rishabh - meerut



# file=open("saral.txt","r")
# for i in file:
# 	print(i)
# 	if 'delhi' in i:
# 		delhi=open("delhi.txt","a")
# 		delhi.write(i+"\n")
# 	elif 'shimla' in i:
# 		shimla=open("shimla.txt","a")
# 		shimla.write(i+"\n")
# 	else:
# 		other=open("other.txt","a")
# 		other.write(i+"\n")

# def kartik(**name):
# 	print("hello "+ name["man"])

# kartik(women="shubham",man="kartik",chakka="sonu")






#########################################RECURSION###########################################
# def pattern(number):
#     if number == 1:
#         return 1
#     else:
#         return pattern(number-1) +2

# print(pattern(10))

#############################################################################################

# def pattern(number):
# 	if number==1:
# 		return 1
# 	else:
# 		return pattern(number-1) +3
# c=[]
# for i in range(1,10):
# 	c.append(pattern(i))
# print(c)

#############################################################################################

# def factorial(num):
# 	if num==0:
# 		return 1
# 	else :
# 		return (num)*factorial(num-1)
# print(factorial(4))

#############################################################################################

# def sum_list(list):
# 	if len(list)==1:
# 		return list[0]
# 	else:
# 		return list[0]+sum_list(list[1:])
# print(sum_list([1,2,3,4,5]))

#############################################################################################

# def palindrome(string):
# 	if string==" ":
# 		return True
# 	elif len(string)==1:
# 		return True
# 	elif string[0] == string[len(string)-1]:
# 		return palindrome(string[1:][:-1])
# 	else:
# 		return False

# print(palindrome("pop"))

##############################################################################################

# def getFibNumber(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return getFibNumber(number-1) + getFibNumber(number-2)
# f=[]
# for i in range (1,21):
# 	f.append(getFibNumber(i))
# print(f)
	
##############################################################################################


# def getFibList(number):
#     if number == 1:
#         return [1]

#     elif number == 2:
#         return [0, 1]

#     else:
#         get_previous_fib_list = getFibList(number-1)
#         new_last_element = get_previous_fib_list[-1] + get_previous_fib_list[-2]

#         get_previous_fib_list.append(new_last_element)

#         current_fib_list = get_previous_fib_list

#         return current_fib_list

# print(getFibList(10))

##############################################################################################
# def getFibNumber(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return getFibNumber(number-1) + getFibNumber(number-2)

##############################################################################################



# def is_present_in_list(number_to_search, list_to_search):
#     counter = 0
#     while (counter < len(list_to_search)):
#         if number_to_search == list_to_search[counter]:
#             return True
#         counter += 1

#     return False

# print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))

###############################################################################################

# hangman_image=(open("hangmanimage.py","r")).read()
# # for i in hangman_image:
# # print(hangman_image(IMAGES[0]))
# print(hangman_image(IMAGES[0]))


################ FOR PRINTING LINE BY INDEX ##################

# if a%2==0print(a)# line=file.read()
# line=line.split('\n')
# print(line[1])


################################################### -:REQUESTS:- ############################################################
###################################################-:SLUG  AAYA:-############################################################

# import requests
# import json
# def courses_available():
# 	data=requests.get("http://saral.navgurukul.org/api/courses")

# 	with open("coursesAvailable.json","w+") as sonu:
# 		json.dump((data.text),sonu)
# 	with open("coursesAvailable.json","r")  as text:
# 		a=json.loads(json.load(text))
# 		count = 1
# 		global kali
# 		kali = []
# 		for i in a["availableCourses"]:
# 			print(count,i["name"])
# 			kali.append(i["id"])
# 			count += 1
# 	global user
# 	user = int(input("select course :: "))
# 	# print(kali)


# def exercises():
# 	print()
# 	print()
# 	slugs=requests.get("http://saral.navgurukul.org/api/courses/"+str(kali[user-1])+"/exercises")
# 	# print(slugs)
# 	hey = slugs.json()
# 	# print(hey)
# 	count1 = 1
# 	global khali_list
# 	global khali_list3
# 	khali_list = []
# 	khali_list3=[]
# 	for q in hey["data"]:
# 		print(count1 ,q["name"])
# 		if q["childExercises"]!=[]:
# 			count2=1
# 			for k in q["childExercises"]:
# 				print("                                     ",count2,k["name"])
# 				count2+=1
# 		else:
# 			pass
# 		count1 +=1
# 		khali_list3.append(q["slug"])
# 		khali_list.append(q["id"])
# 	# print(khali_list3)


# def exercise_content():
# 	global content
# 	content=int(input("enter which part:-"))
# 	print()
# 	print()
# 	about=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(khali_list3[content-1]))
# 	hi=about.json()
# 	print(hi["content"])



# k=0
# courses_available()

# while k<4:
# 	exercises()
# 	navigation=input("navigate the page by using up ::").upper()
# 	if navigation=="UP":
# 		courses_available()

# 	else:
# 		exercise_content()
# 		navigation=input("navigate the page by using up:-").upper()

# 		if navigation=="UP":
# 			continue

# 		else:
# 			if content>1:
# 				exer_navigation=input("write 'p' for privious exercise and 'N' for next")

# 				if exer_navigation=="p":
# 					content=content-1
# 					about=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(khali_list3[content-1]))
# 					hi=about.json()
# 					print(hi["content"])

# 				elif exer_navigation=="n":
# 					content=content+1
# 					about=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(khali_list3[content-1]))
# 					hi=about.json()
# 					print(hi["content"])

# 			else:
# 				exer_navigation=input("write 'p' for privious exercise and 'N' for next")

# 				if exer_navigation=="p":
# 					print("There is no privious exercise of this")
					
# 				elif exer_navigation=="n":
# 					content=content+1
# 					about=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(khali_list3[content-1]))
# 					hi=about.json()
# 					print(hi["content"])
# 	k+=1


# i=1
# count=0
# while i>0:
# 	if i%2==0:
# 		count+=1
# 		print(i)
# 		if count==10:
# 			break
# 	i+=1





#################################################highest palindrome#########################################
# d=0
# c=0
# for i in range (100,999):
# 	for j in range (100,999):
# 		c=i*j
# 		if str(c)[::-1]==str(c):
# 			if c>d:
# 				d=c
# 			else:
# 				pass
# 		else:
# 			pass
# print(d)

############################################################################################################

d=0
c=0
for i in range (100,10000):
	for j in range (100,10000):
		c=i*j
		if str(c)[::-1]==str(c):
			if c>d:
				d=c
			else:
				pass
		else:
			pass
print(d)






























































########################################################################################################################################















	













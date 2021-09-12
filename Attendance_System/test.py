'''
with open("alloted.txt", "wt") as file:
	l = ""
	for i in range (1, 101):
		l = l + str(i) + ","
	file.writelines(l)
'''




with open("alloted.txt", "rt") as file:
	l = file.readlines()
available = l[0].split(",")
print (available)



'''
import random
print (random.randint(0, 10))
'''

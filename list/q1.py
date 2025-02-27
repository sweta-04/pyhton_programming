## WAP that generates a list of 20 random numbers between 1 to 100
#Remove the first and last elemnts
#Sort the list
#print the result

import random
li = []

for i in range(0,20):
	li.append(random.randint(1,100))
print("Original list is : ", li)

rm = li
rm.pop(0)
rm.pop(18	)

newlist = rm.sort()
print("Popped and sorted list is ",rm)

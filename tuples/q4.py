# program to find  all lower case tuples 

x = map(tuple,input("Enter the list of tuples ").split(' '))
lowtuple = []

for a in x:
	for b in a:
		if(b.islower()):
			lowtuple.append(b)
print(lowtuple)
			

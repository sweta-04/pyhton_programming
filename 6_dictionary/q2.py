#update all the even values by multiplying by n in dictionqary where n will be the user input

dict = {'A' : 4, 'B' : 7, 'C' : 8, 'D' : 0}
print(dict)

n = int(input("Enter value of n "))
for i in dict:
	if(dict[i] % 2 == 0):
		dict[i] = dict[i] * n

print("After multiplying even vlaues of dictionary ", dict)

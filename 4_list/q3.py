# WAP to find the sum of character ASCII value in string list

list = []
res = []

size = int(input("Enter the size of the list "))

for i in range(size):
	list.append(input("Enter elemnts"))
	
# now claculate the sum
for i in list:
	ascii_sum = 0
	for j in i:
		ascii_sum += ord(j)
	res.append(ascii_sum)
print("sum of ascii charcater of string in list is :",res)
		

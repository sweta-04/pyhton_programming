#WAP to increment number string ny n

list = []
size = int(input("Enter the size of the list"))
n = int(input("Enter the value to increment"))

for i in range(size):
	list.append(input("Append eleemnts into list"))
	
for i in range(size):
	if(list[i].isdigit()):
		list[i] = str(int(list[i])+n)
print(list)

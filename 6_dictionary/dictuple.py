# update all the  dictionary tuple value ny adding n where n is given by the user in python
dict = {'A' :(7,8), 'B' : 8, 'C' : (1,5), 'D' : 87}
print("Original dictionary" , dict)

n = int(input("Enter the value of n which you want to add in tuple of dict "))

for key,value in dict.items():
	if (type(value) == tuple):
		dict.update({key :tuple( i + n for i in value)})
	else:
		dict.update({key:value})
print("updated dictionary :", dict)

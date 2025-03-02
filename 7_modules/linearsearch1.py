from linearsearch import ls

list = [3,9,2,-5,34]
target = int(input("Enter the target element"))


index = ls(list,target)

if(index == -1):
	print("Not found ")
	
else:
	print(target , "Found at index ",index)


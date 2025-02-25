word = input("Enter your word : ")


initial = 0
size = len(word) #5

print("Range of input : [ %d : %d ]" %(initial, size) )



print("printing via loop : ")

for i in range(initial, size): #0 1 2 3 4
	print(word[i])
	
	
print("by colons : ")
print(word[ : :-1])
	
	
print("printing via loop in reverse: ")

for i in range(size-1, -1, -1): # 4 
	print(word[i])	
	
	

	


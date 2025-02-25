word = input("ENTER ANY STRING TO CHECK: ")

l=len(word)
flag=1


for i in range(l):
	if(word[i]!=word[l-i-1]):
		flag=0
		break
	
if(flag):
	print("Yes")
else:
	print("Not palindrome")


def reverse(num):
	'''sum=0
	l=len(num)
	x=int(num)
	for i in range(l):
		dig = x % 10
		sum=sum*10+dig
		x = x // 10
	
	
	while(num != 0):
		dig = num % 10
		sum=sum*10+dig
		num = num // 10
		
		
	return sum'''
	
	result = num[ : :-1]
	
	return result
	
		
	

num = input("Enter an integer ")
print("The reverse of ",num, "is =",reverse(num))

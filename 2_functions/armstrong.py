def armstrong(num):

	x = int(num)
	l = len(num)
	sum = 0
	
	while(x!=0):
		rem = x%10
		sum += (rem ** l)
		x = x // 10
		
	if( sum == int(num)):
		return 1
	else:
		return 0
		
		
	

num = input("Enter the number : ")
result = armstrong(num)

if(result):
	print("Armstrong")
else:
	print("Not armstrong")

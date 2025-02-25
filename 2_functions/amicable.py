def amicable(x):
	sum=0
	for i in range(1,x):
		if(x%i==0):
			sum = sum+i
	
	return sum
	
a,b=map(int,input("Enter two numbers to check :").split(' '))

if(amicable(a)==b and amicable(b)==a):
	print("amicable pair ")
else:
	print("not amicable pair")
		
		

def factorial(num):
	fact=1
	while(num!=0):
		fact=fact*num
		num -= 1
	return fact


def strong(num):
	sum=0
	n=num
	while(num != 0):
		dig =num % 10
		f=factorial(dig) 
		sum = sum + f
		num=num // 10
		
	if(n==sum):
		return 1
	else:
		return 0
		
num = int(input("Enter the number to check : "))

res = strong(num)
if(res):
	print("YES STRONG ")
else:
	print("NOT STRONG ")
		
		




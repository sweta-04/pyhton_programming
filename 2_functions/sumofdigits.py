def sumofdigits(num):
	sum=0
	
	while(num!=0):
		dig=num%10
		sum += dig
		num=num // 10
	return sum



num = int(input("Enter the  number to find digits sum : "))
result= sumofdigits(num)

print("sum of digits is ",result)


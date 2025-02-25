
num=int(input("Enter the number to check:"))

l=len(str(num))
n=num
sum=0
while(num!=0):
	dig=num%10
	sum += dig ** l
	num=num//10
if(sum==n):
	print("yes it is an armstrong number :")
else:
	print("Not ana armstrong number ")

	

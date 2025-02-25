char=input("Enter any chatacter: ")
a=ord(char)
if((a>=65 and a<=90) or (a>=97 and a<=122)):
	print("it is an alphabet ")
elif(a>=48 and a<=57):
	print("it is digit ")
else:
	print("special character")
	

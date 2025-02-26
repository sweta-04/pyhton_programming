# write a user defined function to remove ith element from tghe string

def removeelement(str,n):
	res = str[:n] + str[n+1:]
	return res
str = input("Enter the string :")
n = int(input("Enter the index to remove element :"))

print(removeelement(str,n))

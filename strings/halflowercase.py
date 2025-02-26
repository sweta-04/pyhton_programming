#WAp to input string in upper case and convert half of the string to lower case using string slicing

str = input("Enter the string in upper case ")

res = str[:len(str)//2].lower()+str[len(str)//2:]
print(res)

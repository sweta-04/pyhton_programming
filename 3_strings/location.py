# find the location of any given word in a string

str = input("Enter the string :")
x = str.split(' ')

word = input("Enter the word to check their location ")

pos = (x.index(word)+1)

print("Found at position ", pos)

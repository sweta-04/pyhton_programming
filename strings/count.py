str = input("Enter the string")

vow = 0
cons = 0
digit = 0

for i in range(0, len(str)):
	ch = str[i]
	if((ch >= 'a' and ch <= 'z' ) or (ch >= 'A' and ch <= 'Z')):
		#covert carcter in lower case
		ch = ch.lower()
		if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
			vow +=1
		else:
			cons +=1
	else:
		digit +=1
		
print("vowels :" , vow)
print("consonants:", cons)
print("digits:", digit)

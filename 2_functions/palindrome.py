def palindrome(word):
	res=word[ : : -1]
	if(res==word):
		print("Yes palindrome")
	else:
		print("Not palindrome")
		
word=input("Enter the word : ")

palindrome(word)

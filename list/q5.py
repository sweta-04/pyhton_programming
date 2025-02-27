# Taking input as a list of strings
words = input("Enter words separated by space: ").split()

# Separate lists for lowercase and uppercase words
lowercase_words = []
uppercase_words = []

# Filtering words based on case
for word in words:
    if word.islower():
        lowercase_words.append(word)
    elif word.isupper():
        uppercase_words.append(word)

# Printing the lists
print("Lowercase words:", lowercase_words)
print("Uppercase words:", uppercase_words)


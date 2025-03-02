words = ['name', 'sweta', 'kumari']
vowels = "aeiouAEIOU"

max_vowels = 0
result = []

# Find the maximum number of vowels in any word
for word in words:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    if count > max_vowels:
        max_vowels = count

# Find words with the maximum number of vowels
for word in words:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    if count == max_vowels:
        result.append(word)

print("Worsd with maximum vowels is ",result)

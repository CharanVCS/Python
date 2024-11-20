# Define the input string
word = "worldOfOnlyVictors_WorldOfOnlyLove"

# Print the substring from index 0 to index 4 (5 characters)
print(word[0:5])

# Print the substring from index 5 to index 6 (2 characters)
print(word[5:7])

# Print the substring from the start to index 4 (5 characters)
print(word[:5])

# Find the index of the first occurrence of the substring 'Of'
print(word.index('Of'))

# Print the substring from the start to index 17 (18 characters)
print(word[:18])

# Print the substring from index 18 to the end of the string
print(word[18:])

# Print the substring from the start to the index of the first occurrence of the substring 'Of'
print(word[:word.index('Of')])

# Print every second character starting from index 18 to the end of the string
print(word[18::2])

# Reverse the string and print it
print(word[::-1])

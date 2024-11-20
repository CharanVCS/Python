original = input("Please enter a sentence:").strip().lower()

words = original.split()
print(words)

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowelpos=0
        for letter in word:
            if letter not in "aeiou":
                vowelpos=vowelpos+1
            else:
                break
        cons = word[:vowelpos]
        the_rest= word[vowelpos:]
        new_word = the_rest + "yay"
        new_words.append(new_word)

output = " ".join(new_words)            
print(output)
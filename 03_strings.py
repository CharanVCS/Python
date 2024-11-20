s = input("Enter your name:")
print("Hey", s+"..!\nhave a nice day!")

print(len(s))
print(s.endswith('e'))
print(s.startswith('c'))

print(s.count('string'))
print(s.capitalize())

print(s.find('string')) # it returns index of first occurence of string
print(s.replace('string','String'))

# always use find() instand of index()
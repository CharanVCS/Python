name = input("what is your name? -> ").capitalize()
age = input("what is your age? -> ")
city = input("what is your city? -> ").capitalize()
joy = input("what do you love doing? -> ").capitalize()
outp = "Your name is {}, your age is {}, your live in {} and your love doing {}".format(name, age, city, joy)
print(outp)
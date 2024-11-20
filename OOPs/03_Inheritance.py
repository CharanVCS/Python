#multilevel inheritance
class sig: 
    a=1

class sig1(sig): # Here sig is base_class of sig1
    b=2

class sig2(sig1): # Here sig1 is base_class of sig2
    c=3

sg=sig1()
sg1=sig2()

print(sg.a)
print(sg1.a)

print(sg1.c)
# print(sg.c) #it gives error

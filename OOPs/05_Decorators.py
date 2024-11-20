class signal:
    name='sine'             
    amp= 2       
    wlen='X'

    @property #we can use fun() f1 as variable to attribute by property decorator called getter method also
    def f1(self):
        return self.name
    
    @f1.setter #fun() s1 act as attribute of class 
    def f1(self, arg):
         self.name=arg

sg=signal()
print(sg.name)
print(sg.f1)
# print(sg.f1()) #it gives error,it is not act like function

sg.f1='cos'
print(sg.f1)
print(sg.name)

# we can change class attribute by object with @setter function
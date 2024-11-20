# basic class syntax
class signal:
    name='sine' # class attribute             
    amp= 2      # class attribute  
    wlen='X'    # class attribute        

    def fun(self): # here 'self' refers to this func only works as class itself not as separate func
        print(f'Name of signal is {self.name}')

sg1 =signal() # basic object syntax, here object is sg1

print(sg1.name)
print(sg1.amp)
sg1.name='cos' #instant attribute
print(sg1.name)

# signal.fun() # this line gives error,if we call fun() by class it gives error
sg1.fun()
signal.fun(sg1)

# we cant change class attribute by object but we can change it instantly that is instant attribute
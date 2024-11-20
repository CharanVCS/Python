class sig:
    a=1
    def __init__(self) :
        print('signal1')
        
class sig1(sig):
    b=2
    def __init__(self):
        print('signal2')
        super().__init__() # this line calls base_class (which is class sig) of this class sig1

class sig2(sig1):
    c=3
    def __init__(self):
        super().__init__() # same here also so,this is calls constuctor
        print('signal3')

sg1=sig1()
sg2=sig2()

print(sg1.a)
print(sg2.a)

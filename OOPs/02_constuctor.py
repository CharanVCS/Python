
class signal:
    def __init__(self,name,amp,wlen): # constuctor 
    # def __init__(self) -> None: # this line is syntax of func automatically excute along with object 
        self.name=name
        self.amp=amp
        self.wlen=wlen

sg1=signal('sine signal',2,'x') 
sg2=signal('cos signal',3,'y')

print(sg1.name)                      
print(sg2.name)

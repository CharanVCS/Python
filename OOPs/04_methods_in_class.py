class Signal():
    name='sine'             
    amp= 2       
    wlen='S' 

    @staticmethod # it allows to excute fun() by class without any object
    def fun():
        print('Signal is generated')

    @classmethod # it allows to change class attribute by class 
    def change(cls, a, b, c):
        cls.name=a
        cls.amp=b
        cls.wlen=c

sg1 =Signal()
sg1.fun()
Signal.fun()

Signal.change('form',69,'X')
print("signal name:",sg1.name)
print("signal amp:",sg1.amp)
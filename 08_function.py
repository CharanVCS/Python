'''basic syntax of functions in python
    def func_name(argument):{
        code statements
    }'''

def greet(name='dude'): #Here dude is the define parameter value
    print('Hey',name.capitalize()+'..!,practics your code also..!')

greet(input('Enter your name:'))
greet()

a=int(input('\nEnter first number:'))
b=int(input('Enter second number:'))

def sum(a=None,b=None): 
    return a+b

print(f'sum is {sum( a,b)}') # Here we used f-string to use varible or functions in string as {brackets}

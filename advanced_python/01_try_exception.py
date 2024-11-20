try:
    a =int(input('Enter only Number below 100:'))
    if a>100:
        raise Exception('it is above 100')
    b =int(input('Enter another Number but not zero:'))
    print('sum=',a+b)
    print('division=',a/b)

except ValueError:
    print('this is value error')
except ZeroDivisionError:
    print('error is ZeroDivisionError')
except Exception as e:
    print(f'This is error by intepreter:{e}')
else:
    print('try was successfull')
    
print('Excution of code is completed')

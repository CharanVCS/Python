def func():
    try:
        a =int(input('Enter Number A below 100:'))
        b =int(input('Enter another Number:'))
        if a>100:
            raise Exception('number A is above 100')
        print('sum=',a+b)
        return a+b

    except Exception as e:
        print(f'This is error by intepreter:{e}')
        return 0
    finally:
        print('Always be printed')

    print('this will not be printed')
        
func()
 
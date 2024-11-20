exp = input('Expression: ').strip()
exp = exp.split()
x = int(exp[0])
y = int(exp[2])
match exp[1]:
    case '+':
        r = x+y
        print(f'{r:.1f}')
    case '-':
        r = x-y
        print(f'{r:.1f}')
    case '*':
        print(f'{x*y:.1f}')
    case '/':
        print(f'{x/y:.1f}')

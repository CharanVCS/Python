users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fray", "Georgie", "Harry"]

while True :
    print('Hi! My name is Travis')
    name = input('What is your name:').strip().capitalize()

    if name in users :
        print('Hello {}!', format(name))
        remove = input('would you like to be remove from the system (y/n)? ').strip().lower()
        if remove=='y' :
            users.remove(name)
        else:
            print('No problem')
    else :
        print('aha..i dont regonized you')
        add = input('Would you like to be added to the system (y/n)? ').strip().lower()
        if add=='y':
            users.append(add)
        else:
            print('No Worries, see you around!')

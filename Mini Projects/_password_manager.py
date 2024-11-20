import cryptography.fernet 
mpwd=input('Enter master password:')

def view():
    with open ('password.txt', 'r') as f:
        for data in f.readlines():
            # data=(f.read()).rstrip()
            name , upwd = (data.rstrip()).split('|')
            print('name:',name,'| password',upwd.decode())

def add():
    name=input('Account name: ')
    pwd= input('password: ')
    with open ('password.txt', 'a') as f:
        f.write(name+'|'+ pwd.encode() + '\n')
         
while True:

    mode=input('would you like to add new password or view existing one (view,add):')
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')
        continue

a=input("press any key to exit")
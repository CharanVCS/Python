import random
import string

def generate (minlen, number= True,special=True ):
    letters=string.ascii_letters
    num = string.digits
    special_char = string.punctuation

    characters= letters
    if number:
        characters +=num
    if special:
        characters += special_char

    pwd =""
    checkpwd=False
    num_check=False
    specialchar_check=False

    while not checkpwd or len(pwd)<minlen:
        char =random.choice(characters)
        pwd += char

        if char in num:
            num_check= True
        elif char in special_char:
            special_charcheck= True
        
        checkpwd= True
        if number:
            checkpwd=num_check
        if special:
            checkpwd =checkpwd and special_charcheck
    return pwd  

minlen=int(input('Enter the minimum length:')) 
num_check=input('Do you want to have numbers (y/n)? ').lower() == 'y'
special_check= input('Do you want to have special characters (y/n)? ').lower() =='y'  
print('The generated password is',generate(minlen, num_check, special_check))
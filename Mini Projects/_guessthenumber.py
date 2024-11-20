import random
print('computer generated a number between 1 to 100\n')
number = random.randint(1,101)
guesses = 0
def gu(guesses):
    gs=input('Guess the number:')
    if gs.isdigit():
        gs=int(gs)
        if gs<=0:
            print("please enter number greater then 0")
            gu(guesses)
    else:
        print("please enter number next time")
        gu(guesses)
    guesses+=1
    return [gs, guesses]

while True:
    gss= gu(guesses)
    if gss[0] ==number:
        print(f'Yeah..! Your guess is correct\nyou guessed in {gss[1]} attempts')
        break

    elif gss[0]<number:
        print('your guess is too less!')
        # gu()
    else:
        print('your guess is too big!')
        # gu()
END=input('Press Enter to exit')
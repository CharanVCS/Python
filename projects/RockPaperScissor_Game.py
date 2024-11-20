import random
import time
import pyttsx3

def say(text):
    """Function to announce text using pyttsx3"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def rps(comp, user):
    """Function to determine the result of Rock, Paper, Scissors"""
    if user == comp:
        return None
    elif (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):
        return True
    else:
        return False

def get_user_choice():
    """Function to get the user's choice"""
    while True:
        user = input('Enter your choice: ').lower()
        if user in ('r', 'p', 's', 'q', 'score'):
            return user
        else:
            print('Please enter a correct choice')
            say("Your choice is wrong, please enter a correct choice")

def display_instructions():
    """Function to display game instructions"""
    instructions = '''Choose either Rock, Paper, or Scissor:
    To choose, enter:
    r for Rock
    p for Paper
    s for Scissor
    q for Quit
    If you want to know your score, enter 'score'
    '''
    print(instructions)

def main():
    """Main function to run the Rock, Paper, Scissors game"""
    greet = "Welcome to Rock, Paper, Scissors game"
    print(greet)
    say(greet)

    choices = ('r', 'p', 's')
    items = {
        'r': 'Rock',
        'p': 'Paper',
        's': 'Scissor'
    }
    score = [0, 0]

    while True:
        display_instructions()
        user = get_user_choice()

        if user == 'q':
            quit_message = "Thank you for playing! Goodbye!"
            print(quit_message)
            say(quit_message)
            break

        if user == 'score':
            score_message = f"Your score is: Wins - {score[0]}, Losses - {score[1]}"
            print(score_message)
            say(score_message)
            continue

        # Making computer choice
        comp = random.choice(choices)
        
        print(f'You chose {items[user]} <-> Computer chose {items[comp]}')

        # Determine match result
        win = rps(comp, user)
        if win is None:
            result_message = 'Match is a Draw'
        elif win:
            result_message = 'You WIN..! :)'
            score[0] += 1
        else:
            result_message = 'You lose..! :('
            score[1] += 1

        print(result_message)
        say(result_message)
        time.sleep(0.7)

if __name__ == "__main__":
    main()

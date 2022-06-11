#!/usr/bin/env python
import random
"""Play Rock Paper Scissor with computer
Usage:
    ./rps.py

Author:
    Noble Mutoko - 11.06.2022
"""
choices = ['R','P','S']
def check_winner(user,comp):
    """Check user input is equal to Compute Input
    Args:
        user_choice: Input from the user
        comp: Random choice from the computer
    Returns:
        Winner as computer or user
        If a draw returns a draw
    """
    if(user=='R' and comp =='S'):
        return user
    elif(user=='P' and comp=='R'):
        return user
    elif(user=='S' and comp=='P'):
        return user
    elif(user=='S' and comp=='S' or user=='P' and comp=='P' or user=='R' and comp=='R'):
        return 'Its a draw'
    else:
        return comp
game = True
def play_game():
    while game:
        """Allow play until there is a winner
        Args
            check_winner: Gets user input and computer input

        Returns
            Winner after comparison of choice
        """
        try:
            print('To play:')
            print('Enter R for rock')
            print('Enter P for paper')
            print('Enter S for scissors')
            user_choice = input('Choose an option to play: ')
            comp = random.choice(choices)
            if user_choice.upper() in choices:
                result =check_winner(user_choice,comp)
                if(result==user_choice and result!= comp):
                    print('User choice: {} & Computer choice: {}'.format(user_choice,comp))
                    print('User won')
                    print('exiting ...')
                    break
                elif(result==comp and result!=user_choice):
                    print('User choice: {} \n Computer choice: {}'.format(user_choice,comp))
                    print('Computer has won')
                    print('exiting ...')
                    break
                elif(result=='none'):
                    print('its a draw ^^')
                    continue     
            else:
                print('Invalid choice:\n')
                continue 
        except KeyboardInterrupt or KeyError :
                print("\nexiting ....")
                break

if __name__ =='main':
    play_game()
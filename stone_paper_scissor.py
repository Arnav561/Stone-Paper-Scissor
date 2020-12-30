import random
import pygame
from playsound import playsound
from pygame import mixer

pygame.mixer.init()

# Stone paper or scissors
def gamewinner(computer, you):
    if computer == you:
        return None
    elif computer == 's':
        if you == 'p':
            return True
        elif you == "sc":
            return False
    elif computer == 'p':
        if you == 's':
            return False
        elif you == "sc":
            return True
    elif computer == "sc":
        if you == 'p':
            return False
        elif you == 's':
            return True


#Background Music
mixer.music.load('bgmusic.wav')
mixer.music.play(-1)

choice = 'y'

print('''\n\nFirst turn will be Of computer. Following is the menu of the game:


                                's' for stone
                                'p' for paper
                                'sc' for scissor
                        
    
NOTE:- If you enter anything other than 's', 'sc' or 'p', then it's an ERROR & you gotta, try again!''')

playsound("my recordings\\start.mpeg")

while choice == 'y' or choice == 'Y':

    random_no = random.randint(1, 3)

    if random_no == 1:
        comp = 's'
    elif random_no == 2:
        comp = "sc"
    elif random_no == 3:
        comp = 'p'
    
    print("\n\nComputer's turn is done! It's your turn now.\n\n")

    user_Turn = input("\n\t\tEnter your choice: ")

    if user_Turn != 's' and user_Turn != "sc" and user_Turn != 'p':
        print("\nYou entered a wrong value. Please try again!\n")
        continue

    function_returning = gamewinner(comp, user_Turn)

    print("Computer chose ", comp)
    print("You choose ", user_Turn)

    if function_returning == None:
        print("\n\t\tThe game is a Tie.(Draw)\n")
        playsound("my recordings\\The game is tie.mpeg")
    elif function_returning == True:
        print("\n\t\tYay!! You won the game.\n")
        playsound("my recordings\\User won the  game .mpeg")
    elif function_returning == False:
        print("\n\t\tSorry, you lost the game. Better Luck next time.\n")
        playsound("my recordings\\computer wins.mpeg")
    
    choice = input("\nDo you want to play the game again (y/n): ")

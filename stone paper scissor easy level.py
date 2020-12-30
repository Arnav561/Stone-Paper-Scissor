import random
from playsound import playsound

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


playsound("my recordings\\start.mpeg")
choice = 'y'
while choice == 'y' or choice == 'Y':

    print("\n\nFirst turn will be Of computer you have to enter 's'for stone, 'p'for paper and 'sc' for scissor.\n NOTE:-if you will enter a number other than 's', 'sc' or 'p' the match will be tie")

    random_no = random.randint(1, 3)

    if random_no == 1:
        comp = 's'
    elif random_no == 2:
        comp = "sc"
    elif random_no == 3:
        comp = 'p'
    
    print("\n\nComputer's turn is done!")

    user_Turn = input("HI, user it's your turn now.\nEnter your choice: ")

    function_returning = gamewinner(comp, user_Turn)

    print("Computer chose ", comp)
    print("You choose ", user_Turn)

    if function_returning == None:
        playsound("my recordings\\The game is tie.mpeg")
    elif function_returning == True:
        playsound("my recordings\\User won the  game .mpeg")
    elif function_returning == False:
        playsound("my recordings\\computer wins.mpeg")
    
    choice = input("Do you want to play the game again (y/n): ")

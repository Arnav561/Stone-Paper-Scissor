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

print("\n\nFirst turn will be Of computer. You have to enter:\n's'for stone\n'p'for paper\n'sc' for scissor\n\nNOTE:- If you enter anything other than 's', 'sc' or 'p', then it's an ERROR & you gotta, try again!!")

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

    function_returning = gamewinner(comp, user_Turn)

    print("Computer chose ", comp)
    print("You choose ", user_Turn)

    if function_returning == None:
        playsound("my recordings\\The game is tie.mpeg")
        print("\n\t\tThe game is a Tie.(Draw)\n")
    elif function_returning == True:
        playsound("my recordings\\User won the  game .mpeg")
        print("\n\t\tYay!! You won the game.\n")
    elif function_returning == False:
        playsound("my recordings\\computer wins.mpeg")
        print("\n\t\tSorry, you lost the game. Better Luck next time.\n")
    
    choice = input("\nDo you want to play the game again (y/n): ")

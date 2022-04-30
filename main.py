# snake water gun game
from random import randint
from os import system

def gameWin(comp, you):
    if comp == you:
        return None

    if comp == "s":
        if(you == "w"):
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if(you == "s"):
            return True
        elif you == "g":
            return False
    if comp == "g":
        if(you == "s"):
            return False
        elif you == "w":
            return True


a = randint(1, 3)
if a == 1:
    comp = 's'
elif a == 2:
    comp = 'w'
elif a == 3:
    comp = 'g'

print("computer's turn : snake(s) , water(w) , gun(g)? ")
you = input("your's turn : snake(s) , water(w) , gun(g)? ")

system('cls') #for clearing previous output

print("computer chose :",comp)
print("you chose :",you)

st = gameWin(comp, you) # st for status that player wins or not

# showing  result that who wins
if st == None:
    print("the game is a tie!")
elif st == True:
    print("you win!")
else:
    print("computer wins!")



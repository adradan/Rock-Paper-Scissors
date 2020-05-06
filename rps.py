import re

userCont = True
againLoop = 1


def badInput():
    print("Please only type in the given choices.\n")


#Using arrays are easier/more compact than using 3 if/else statements
def whichChoice(x):
    reChoices = [
        'r',
        'p',
        's',
    ]

    returnChoice = {
        'r': reChoices[0],
        'p': reChoices[1],
        's': reChoices[2]
    }

    check = x.startswith(tuple(reChoices))

    if check:
        return returnChoice[x[0]]
    else:
        badInput()


#Gives computer's response
def compAns(x):
    if x == 'r':
        print("Computer chose Paper")
    elif x == 'p':
        print("Computer chose Scissors")
    elif x == 's':
        print("Computer chose Rock")


def askAgain():
    global againLoop

    while againLoop == 1:
        again = input("Try again? y/n or spell it out\n")
        if again.strip().lower().startswith('y'):
            againLoop = 0
            return True
        elif again.strip().lower().startswith('n'):
            againLoop = 0
            return False
        else:
            badInput()
    else:
        print("Goodbye.")


#Creates a loop so user can replay as much times as they want
#Serves as the main function
while userCont == True:
#Initializing variables used in order of appearance
    choice = ""
    whatChoice = 0
    answ = 0
    againLoop = 1
    again = ""

#Asks for user's choice
    print( "Choose Rock, Paper, or Scissors (R, P, S, or spell it out)" )
    choice = input()

#whatChoice is set by whichChoice function
    whatChoice = whichChoice(choice.strip().lower())

#Gives computer's answer
    compAns(whatChoice)

    replay = askAgain()
    if replay:
        userCont = True
        print()
    else:
        userCont = False
else:
    print("Goodbye.")


import re

userCont = True

#Searches string for the available choices and returns numbers based on choice
def whichChoice(x):
#Searchs for responses
    answPaperI = re.compile(r'{}'.format('p'), flags=re.IGNORECASE).search(x)
    answPaper = re.compile(r'{}'.format('paper'), flags=re.IGNORECASE).search(x)

    answRockI = re.compile(r'{}'.format('r'), flags=re.IGNORECASE).search(x)
    answRock = re.compile(r'{}'.format('rock'), flags=re.IGNORECASE).search(x)

    answScissorsI = re.compile(r'{}'.format('s'), flags=re.IGNORECASE).search(x)
    answScissors = re.compile(r'{}'.format('scissors'), flags=re.IGNORECASE).search(x)

#Returns number based on choice
    if answPaper or answPaperI:
        return 2
    elif answScissors or answScissorsI:
        return 3
    elif answRock or answRockI:
        return 1
    else:
        print("You did not choose a letter or spell out the word, please try again.\n")


#Gives computer's response
def compAns(x):
    if x == 1:
        print("Computer chose Paper")
    elif x == 2:
        print("Computer chose Scissors")
    elif x == 3:
        print("Computer chose Rock")


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
    whatChoice = whichChoice(choice.strip())

#Gives computer's answer
    compAns(whatChoice)

#Allows user to try again or quit
    while againLoop == 1:
        print("Again? Yes/No")
        again = input()
        if "yes" in again:
            print()
            userCont = True
            againLoop = 0
        elif "no" in again:
            print()
            userCont = False
            againLoop = 0
        else:
            print()
            print("I don't understand, please say yes or no")    
else:
#Tells user goodbye then quits program
    print("Goodbye.")


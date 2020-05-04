import re

userCont = True

#Using arrays are easier/more compact than using 3 if/else statements
def whichChoice(x):
    rePaper = re.compile(r'p|paper', flags=re.IGNORECASE)
    reScissors = re.compile(r's|scissors', flags=re.IGNORECASE)
    reRock = re.compile(r'r|scissors', flags=re.IGNORECASE)

    reChoices = [rePaper, reScissors, reRock]

    for search in reChoices:
        searchChoice = search.search(x)
        if searchChoice:
            return(searchChoice.group(0))
            break

#Gives computer's response
def compAns(x):
    if x == 'r':
        print("Computer chose Paper")
    elif x == 'p':
        print("Computer chose Scissors")
    elif x == 's':
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
    whatChoice = whichChoice(choice.strip().lower())

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


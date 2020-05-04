import re

userCont = True

#Searches string for the available choices and returns numbers based on choice
#This way of searching for the proper response made the if/else statement have to go in certain orders
#If the user gave paper and rock was at the top of the if/else chain, the program would first recognize it as a Rock answer and improperly give Paper
#Rock had to go last since all the other choices also had an "r" in them
def whichChoice(x):
#The choice will be recognized as paper if the letter "p" is found or the string "paper"
    answPaperI = re.compile(r'{}'.format('p'), flags=re.IGNORECASE).search(x)
    answPaper = re.compile(r'{}'.format('paper'), flags=re.IGNORECASE).search(x)

#The choice is recognized as rock if the letter "r" or string "rock" is found
    answRockI = re.compile(r'{}'.format('r'), flags=re.IGNORECASE).search(x)
    answRock = re.compile(r'{}'.format('rock'), flags=re.IGNORECASE).search(x)

#The choice is recognized as scissors if the letter "s" or string "scissors" is found
    answScissorsI = re.compile(r'{}'.format('s'), flags=re.IGNORECASE).search(x)
    answScissors = re.compile(r'{}'.format('scissors'), flags=re.IGNORECASE).search(x)

#If choice recognized as paper, sets differentiate = 2
    if answPaper or answPaperI:
        return 2
#If recognized as Scissors, differentiate = 3
    elif answScissors or answScissorsI:
        return 3
#If recognized as Rock, differentiate = 1
    elif answRock or answRockI:
        return 1
#If the program did not find any of the strings or letters, will tell them to try again
    else:
        print("You did not choose a letter or spell out the word, please try again.\n")


#Gives computer response based on previously given number by whichChoice()
def compAns(x):
#If user gave rock, gives paper
    if x == 1:
        print("Computer chose Paper")
#User paper, prints cpu scissors
    elif x == 2:
        print("Computer chose Scissors")
#User scissor, prints cpu rock
    elif x == 3:
        print("Computer chose Rock")


#Creates a loop so user can replay as much times as they want
#Serves as the main function
while userCont == True:
#Initializing variables used in order of appearance
    choice = ""
    differentiate = 0
    answ = 0
    againLoop = 1
    again = ""

#Asks user to choose option
    print( "Choose Rock, Paper, or Scissors (R, P, S, or spell it out)" )
#Sets string "choice" to whatever user gave
    choice = input()

#Sets differentiate integer variable by calling on whichChoice()function
    differentiate = whichChoice(choice.strip())

#Calls on compAns function and sets it's variable to the value of differentiate
    compAns(differentiate)

#Allows user to try again or quit
#againLoop is already set to 1 so at first open the loop will start
    while againLoop == 1:
        print("Again? Yes/No")
#Sets user's response into again variable
        again = input()
#If the word yes is found in the again variable/user input, will restart entire loop from beginning allowing for a retry
        if "yes" in again:
            print()
            userCont = True
            againLoop = 0
#If the word no is found, the entire loop will end, skipping to line 77
        elif "no" in again:
            print()
            userCont = False
            againLoop = 0
#If neither yes or no is found, tells user to input either yes or no
        else:
            print()
            print("I don't understand, please say yes or no")    
else:
#Tells user goodbye then quits program
    print("Goodbye.")


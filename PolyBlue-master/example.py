from polyBlueClient import PolyBlueClient
# Be sure to import the Python module from the polyBlueClient.py file in your code

# Call the PolyBlueClient class and pass it the name of your BlueMix application
# In this example, the BlueMix application is running under 'tornado-polyblue',
# and can be accessed from http://tornado-polyblue.mybluemix.net
p = PolyBlueClient('flpoly-brandonhigbee')


#Hangman game
#Brandon Higbee
#functions:
#getName -> getCategory -> getWord -> play the game

import random
from string import Template
clear = "\n" * 40

usedLetters = []

def getName() :
    name = p.getInput("What is your name? : (no spaces) ")
    p.sendOutput("\n\n\n")
    return name


#reads through a file of categories and picks a random one.
#adds each category in file to a list and randomly selects an index
def getCategory() :
    openFile = open("categories.txt", "r")

    categories = []
    
    read = openFile.readline()

    while read != "" :
        categories.append(read)
        read = openFile.readline()

    openFile.close()

    category = categories[random.randint(0, len(categories) - 1)]
    #take off \n at the end of categories' string, small bug fix
    if category.endswith("\n") :
        category = category[:-1]
    
    return category



#get category, put words in list and choose a random index for the word
def getWord(category) :
    openFile = open((category + ".txt"), "r")

    words = []
    
    read = openFile.readline()

    while read != "" :
        words.append(read)
        read = openFile.readline()
    openFile.close()
    
    word = words[random.randint(0, len(words) - 1)]
    if word.endswith("\n") :
        word = word[:-1]

    return word



#makes array of underscores with the chosen word
def makeUnderscoreArray(word, category) :
    #call to a function to create a playing board with ascii art
    underScores = []
    for letter in word :
        if letter.isalpha() :
            underScores.append("_")
        else :
            underScores.append(" ")
    return underScores



#prints the list of underscores
def printUnderscoreArray(underScores) :
    underString = ""
    for letters in underScores :
        underString = underString + letters + " "

    p.sendOutput(underString)
    return 



def printHangguy(turn) :
    index = 0
    output = ""

    gallows = ["       _______", "   |/      |", "   |      (_)", "   |      \|/", "   |       |","   |      / \ ","___|___"]

    p.sendOutput(name)
    while index != turn :
        output += gallows[index] + "\n"
        index += 1
    p.sendOutput(output)
    
    output = "Already attempted: "
    for letters in usedLetters :
        output = output + letters + "   "
    p.sendOutput(output + "\n")



def printHighscores(playerScore) :          #open file, grab highscores from file, print line by line from list
    readFile = open("highscores.txt", "r")   
    read = readFile.readline()      

    i = 1       #highscore number    
    p.sendOutput(' {:=^29}'.format("Highscores")) 
    while read != "" :  #will display highscore table
        stringParts = read.split(" ")
        playerName = stringParts[0]
        highscore = int(stringParts[1])

        str1 = '|| {:2s} {:16s} {:5d} ||'.format(str(i),playerName,highscore)

        
        p.sendOutput(str1)

        read = readFile.readline()
        i += 1
    readFile.close()
    p.sendOutput(" " + ("=" *29))
    p.sendOutput("Your score: " + str(playerScore))


    
def writeHighscores(playerName, playerScore) :  #open file, grab highscores, see if player beat score, rewrite highscores to file
    readFile = open("highscores.txt", "r")
    read = readFile.readline()      

    highscores = []
    
    i = 0       #highscore number    
    
    while read != "" :
        stringParts = read.split(" ")
        highscores.append(stringParts)
        read = readFile.readline()
    readFile.close()
    
    writeFile = open("highscores.txt", "w")

    playerEntry = [playerName, str(playerScore) + "\n"]
    
    for scores in highscores :
        if int(scores[1]) < playerScore :
            highscores.insert(i, playerEntry)
            highscores.pop()
            break
        i += 1

    for scores in highscores :
        writeFile.write(scores[0] + " " + scores[1])
    writeFile.close()



        
    
 

name = getName()            #get the name of the player
category = getCategory()    #get the category of the word
word = getWord(category)    #get the word from the chosen category

underScores = makeUnderscoreArray(word, category)   #make the underscore array matching the word chosen

turnFail = True
playerWin = False
turn = 0
while "_" in underScores and turn != 7 :  #actual game part
    turnFail = True
    printHangguy(turn)
    p.sendOutput("The category is: " + category)
    printUnderscoreArray(underScores)
    letter = p.getInput("Enter a letter: ")
    p.sendOutput(clear)
    
    if letter not in usedLetters :
        usedLetters.append(letter)
    
    if letter == word :     #if the player enters the word correctly, end game
        break
    
    i = 0
    for letters in word :
        if letter == letters :
            underScores[i] = letter
            turnFail = False
        i += 1

    if "_" in underScores :
        p.sendOutput(clear)
    else :
        p.sendOutput(clear)
        printUnderscoreArray(underScores)

    if turnFail == True :   #if incorrect letter is entered, increase counter
        turn += 1
        
    
won = False
score = 700 - (turn * 100) #maximum of 7 turns allowed
                            #points are remaining turns * 100 
#check if they won or lost.
if turn == 7 :  #7 is maximum turn count
    printHangguy(turn)
    p.sendOutput("You have lost!")
    p.sendOutput("The word was : " + word)  #let them know the word
else :
    printHangguy(turn)
    p.sendOutput("You have won! Congratulations!")
    won = True

writeHighscores(name, score)

if won == True :
    answer = p.getInput("Do you want to see the highscores? (yes or no) : ")
    if answer.lower().strip() == "yes" :
        p.sendOutput(clear)
        printHighscores(score)



p.close()   #close the connection

import os
'''
    TODO:
        Decide on standardized test suite to run through this program (to implement for easy testing later) to check with all major tests and before pushes
        Setup a standardized system for the languageToUse so that it can be any of em implemented
        Setup input UI & whatnot to manually make it run whatever input text ya like
        Change setup env stuff to be determined at runtime
        |_>Include changing the language version for languages like GreenRune with both letter-by-letter and word-by-word versions
        |_>Include changing speed of run
        Change how the letters are displayed to make lines of text (at first in only english's way, designed to be changable for languages with other directions of reading)
        Figure out how to make the flags in each letter file to check for and how to pick up on em to in order to pull in letters
        Implement reading in all the non-letter bits of each language as appropriate -> ( and ), etc. + error throwing 4 illegal characters
        Find a more effective way to center all letters both in height and width
'''
#   METHOD(S) TO BE USED IN THE FILE LATER
def goToStartingPoint(language, letter, letterHeight, windowWidth, letterIndex, fullWritingLength):
    #   This method assumes equal back-to-back spaces for each letter in letter-by-letter languages
    #       Need to later determine spacing for the word-by-word languages
    results = ['turtle.penup()', 'turtle.goto()', 'turtle.pendown()', 'turtle.setheading(90)']

    if language == 'GreenRune':
        # letterWidth =/= letterHeight for GreenRune, need to calculate this out better so that letters don't overlap each other after all letters are written to stay in their vertical bounds first
        yCoordiante = 0
        if ['b','c','k','r','(',')'].count(letter) == 1:
            yCoordiante -= letterHeight / 2
        else:
            yCoordiante += letterHeight / 2

        xCoordinate = -1 * (windowWidth / 2) + (letterHeight / 2) + (letterHeight * letterIndex) # should be to the left edge of the letter
        if ['h','i','j','o','q','s','w','?','u'].count(letter) == 1:
            xCoordinate += letterHeight / 2
        elif ['g','y','('].count(letter) == 1:
            xCoordinate += letterHeight

        stringToAdd = str(xCoordinate) + ',' + str(yCoordiante)
        results[1] = results[1][:-1] + stringToAdd + results[1][-1]

        return results

    return

def getCodeForLetter(language, letter, writingType):
    codeToWriteLetter = []

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__) ), 'CypherLibrary/' + language + '/' + letter + '.py'), 'r' ) as x:
        codeToWriteLetter = x.read()
    
    if codeToWriteLetter.count('#SINGULAR START') == 1 and writingType == 'individual' and language == 'GreenRune':
        startingIndex = codeToWriteLetter.index('#SINGULAR START') + len('#SINGULAR START\n')
        endingIndex = codeToWriteLetter.index('#SINGULAR END')
    else:
        startingIndex = codeToWriteLetter.index('#START') + len('#START\n')
        endingIndex = codeToWriteLetter.index('#END')
    
    codeToWriteLetter = codeToWriteLetter[startingIndex:endingIndex]

    return codeToWriteLetter 

#   READ IN THE STUFF TO TRANSLATE
inputString = 'I Love You Zee'
languageToUse = 'GreenRune'
writingType = 'individual'      #should be either 'individual' or 'compound' and used only for languages like GreenRune that can be written in either format
numeralSystemToUse = ''
output = open('encodedText.py', 'w')
windowHeight, windowWidth = 600, 1000
writingSpeed = 0

#   ONLY POTENTIALLY USED VARIABLES
greenRuneWritingType = ''
letterHeight = int(windowWidth / (len(inputString) + 1) )

#   ALTER THE TEXT INPUT / DETERMINE SETUP ENV AS NECESSARY 4 LANGUAGE SELECTED
#       MINOR CHANGES COULD BE FOUND AND MADE BEFORE CONINUING, BUT FOR LARGER ISSUES SHOULD ERROR OUT AND ASK FOR CORRECTION


#   SETUP THE STARTING ENV 
output.write('import turtle\nwindow = turtle.Screen()\nwindow.setup(width=' + str(windowWidth) + ', height=' + str(windowHeight) + ')\nturtle.mode("logo")\nturtle.speed(' + str(writingSpeed) + ')\n')

if languageToUse == 'GreenRune':
    if greenRuneWritingType == '':
        greenRuneWritingType = 'sequential'
    inputString = inputString.lower()

    output.write('letterHeight = ' + str(letterHeight) + '\n\n')


#   WRITE OUT THE TEXT AS A WHOLE - TWO SECTIONS, 1 FOR WRITING EACH LETTER, 1 FOR WRITING EACH WORD (BASED ON LANG & WRITING STYLE IN IT)
#       LETTER BY LETTER LANGUAGES

codeToWriteFullSentence = []
for letterIndex in range(len(inputString) ):
    nextLetterToWrite = inputString[letterIndex]
    if nextLetterToWrite == ' ':
        continue
    resetCode = goToStartingPoint(language=languageToUse, letter=nextLetterToWrite, letterHeight=letterHeight, windowWidth=windowWidth, letterIndex=letterIndex, fullWritingLength=len(inputString) )

    # PULL UP THE CODE FOR THIS LETTER & RESETTING AFTERWARDS
    nextLettersCode = getCodeForLetter(language=languageToUse, letter=nextLetterToWrite, writingType=writingType)

    # ADD ALL THIS CODE TO THE BIG LIST
    for line in resetCode:
        codeToWriteFullSentence.append(line)
    # for line in nextLettersCode:
    #     codeToWriteFullSentence.append(line)
    codeToWriteFullSentence.append(nextLettersCode)

for line in codeToWriteFullSentence:
    output.write(line + '\n')
output.write('turtle.done()\n')








#       WORD BY WORD LANGUAGES



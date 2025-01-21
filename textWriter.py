import os
import sys
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
        Related but make numbers go to number system selected if not covered by language
        Find a more effective way to center all letters both in height and width
        |_>Update the starting code that gets ignored in all files (of each language as read in) to include lower borders
        |_>Then, update those same letter files to center the drawn text within the box, and to stay in the damn box to begin with!
        |_>Could then or in a later update all about efficiency trim down on the number of commands by using more efficient ones to trim down on runtime by decresasing read in and write out amounts
        Make it so you can put in the language w/out precisely matching capitalization of the file structure for that language (changes to getCodeForLetter() )
'''
#   METHOD(S) TO BE USED IN THE FILE LATER
def goToStartingPoint(language, letter, letterHeight, windowWidth, letterIndex, fullWritingLength):
    #   This method assumes equal back-to-back spaces for each letter in letter-by-letter languages
    #       Need to later determine spacing for the word-by-word languages
    results = ['turtle.penup()', 'turtle.goto()', 'turtle.pendown()', 'turtle.setheading(90)']

    if language == 'GreenRune':
        # letterWidth == letterHeight for GreenRune.
        yCoordiante = 0
        if ['b','c','k','r','(',')','\''].count(letter) == 1:
            yCoordiante -= letterHeight / 2
        else:
            yCoordiante += letterHeight / 2

        xCoordinate = -1 * (windowWidth / 2) + (letterHeight / 2) + (letterHeight * letterIndex) # should be to the left edge of the letter
        if ['h','i','j','o','q','s','w','?','u'].count(letter) == 1:
            xCoordinate += letterHeight / 2
        elif ['g','y',')'].count(letter) == 1:
            xCoordinate += letterHeight

        stringToAdd = str(xCoordinate) + ',' + str(yCoordiante)
        results[1] = results[1][:-1] + stringToAdd + results[1][-1]

        return results

    return

def translateNextLetterToFilename(language, letter):
    if language == 'GreenRune':
        GreenRuneLetterFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'y':'y', 'z':'z', ')':'closeParen', '\'':'openQuotation', '(':'openParen', '?':'questionMark', ',':'comma'}
        result = GreenRuneLetterFileNames.get(letter)
        if result is None:
            raise ImportError('The letter you are seaching for: ' + letter + ' is not in the language that you provided (' + language + ')\n')
        return result
        

def getCodeForLetter(language, letter, writingType):
    codeToWriteLetter = []
    try:
        letter = translateNextLetterToFilename(language=language, letter=letter)
    except:
        raise ImportError('The letter you are seaching for: ' + letter + ' is not in the language that you provided (' + language + ') and this was cuaght by getCodeForLetter\n')
    
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
if len(sys.argv) <= 4:
    raise RuntimeError('This command should be run with multiple arguments. The first for a text file of input text, the second with the name of the output python file. The third is language for text, and fourth is language for numbers if not included in third. There may be more optional arguments after this based on the languages used.')

inputFileName = str(sys.argv[1] )
input = open(inputFileName, 'r')
inputString = []
for x in range(300):
    nextLine = input.read()
    if nextLine == "": 
        break
    inputString.append(nextLine.split('\n\n') )
inputString = inputString[0][0]

outputFileName = str(sys.argv[2] )
languageToUse = str(sys.argv[3] )
writingType = 'individual'      #should be either 'individual' or 'compound' and used only for languages like GreenRune that can be written in either format
numeralSystemToUse = str(sys.argv[4] )
output = open(outputFileName, 'w')
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
    if nextLetterToWrite.isspace():
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



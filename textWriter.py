import sys
import textWriterHelper
'''
    TODO:
        Decide on standardized test suite to run through this program (to implement for easy testing later) to check with all major tests and before pushes
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
        Pull out the language check everywhere to use function 2 return an enum @ startup
        Allow Flux Judonese to write in its other directions using the direction optional argument and variable - letters will handle directional change on their end 4 writing specifics
        Make the 'hidden' letters of languages accessible: letters with dots and whitespace of Artemis Fowl, end quotes of GreenRune
'''
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
languageToUse = textWriterHelper.makeLanguageUniform(str(sys.argv[3] ) )
writingType = 'individual'      #should be either 'individual' or 'compound' and used only for languages like GreenRune that can be written in either format
numeralSystemToUse = str(sys.argv[4] )
output = open(outputFileName, 'w')
windowHeight, windowWidth = 600, 1000
writingSpeed = 0

#   ONLY POTENTIALLY USED VARIABLES - 1 line / language instituting them
greenRuneWritingType, letterHeight = '', int(windowWidth / (len(inputString) + 1) )                         # from GreenRune
bottomLeft, bottomRight, topLeft, topRight, length = (0,0), (0,0), (0,0), (0,0), letterHeight / 5           # from Minecraft Enchant Table
direction = 0                                                                                               # from Flux Judonese
lineWidth = letterHeight / 10                                                                               # from HowToTrainYourDragon

#   SETUP THE STARTING ENV 
output.write('import turtle\nwindow = turtle.Screen()\nwindow.setup(width=' + str(windowWidth) + ', height=' + str(windowHeight) + ')\nturtle.mode("logo")\nturtle.speed(' + str(writingSpeed) + ')\n')

if languageToUse == 'GreenRune':
    if greenRuneWritingType == '':
        greenRuneWritingType = 'sequential'
    inputString = inputString.lower()
    output.write('letterHeight = ' + str(letterHeight) + '\n\n')

if languageToUse == 'MinecraftEnchantTable':
    output.write('length = ' + str(length) + '\n\n')

if languageToUse == 'FluxJudonese':
    output.write('direction = ' + str(direction) + '\n\n')
    output.write(textWriterHelper.printExtraFilePrimerMaterial(language=languageToUse) )

if languageToUse == 'Covenant':
    output.write('letterHeight = ' + str(letterHeight) + '\n')
    output.write('largeSide = ' + str(letterHeight / 2) + '\n')
    output.write('smallerSide = ' + str(letterHeight / 5) + '\n')

if languageToUse == 'HowToTrainYourDragon':
    output.write('letterHeight = ' + str(letterHeight) + '\n')
    output.write('lineWidth = ' + str(lineWidth) + '\n')
    output.write('diagonal = ' + str(lineWidth * 3) + '\n')

#   WRITE OUT THE TEXT AS A WHOLE - TWO SECTIONS, 1 FOR WRITING EACH LETTER
#  1 FOR WRITING EACH WORD (BASED ON LANG & WRITING STYLE IN IT) LETTER BY LETTER LANGUAGES

codeToWriteFullSentence = []
for letterIndex in range(len(inputString) ):
    nextLetterToWrite = inputString[letterIndex]
    if nextLetterToWrite.isspace():
        continue
    
    if ['Covenant', 'FluxJudonese', 'GreenRune', 'HowToTrainYourDragon', 'MinecraftEnchantTable'].count(languageToUse) == 1:
        identifyingLetterHeight = letterHeight

    resetCode = textWriterHelper.goToStartingPoint(language=languageToUse, letter=nextLetterToWrite, identifyingLetterHeight=identifyingLetterHeight, windowWidth=windowWidth, letterIndex=letterIndex, fullWritingLength=len(inputString) )

    # PULL UP THE CODE FOR THIS LETTER & RESETTING AFTERWARDS
    nextLettersCode = textWriterHelper.getCodeForLetter(language=languageToUse, letter=nextLetterToWrite, writingType=writingType)

    # ADD ALL THIS CODE TO THE BIG LIST
    for line in resetCode:
        codeToWriteFullSentence.append(line)
    codeToWriteFullSentence.append(nextLettersCode)

for line in codeToWriteFullSentence:
    output.write(line + '\n')
output.write('turtle.done()\n')








#       WORD BY WORD LANGUAGES



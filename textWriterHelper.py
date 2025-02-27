import os
#   METHOD(S) TO BE USED IN THE FILE LATER
def goToStartingPoint(language, letter, identifyingLetterHeight, windowWidth, letterIndex, fullWritingLength):
    #   This method assumes equal back-to-back spaces for each letter in letter-by-letter languages - implement differences in this by language
    #       Need to later determine spacing for the word-by-word languages
    results = ['turtle.penup()', 'turtle.goto()', 'turtle.pendown()']

    if language == 'GreenRune':
        # letterWidth == letterHeight for GreenRune.
        letterHeight = identifyingLetterHeight
        letter = letter.lower()
        yCoordiante = 0
        if ['b','c','k','r','(',')','\''].count(letter) == 1:
            yCoordiante -= letterHeight / 2
        else:
            yCoordiante += letterHeight / 2

        xCoordinate = -1 * (windowWidth / 2) + (letterHeight / 2) + (letterHeight * letterIndex)
        if ['h','i','j','o','q','s','w','?','u'].count(letter) == 1:
            xCoordinate += letterHeight / 2
        elif ['g','y',')'].count(letter) == 1:
            xCoordinate += letterHeight
    
    elif language == 'MinecraftEnchantTable':
        length, letterLength = identifyingLetterHeight / 5, identifyingLetterHeight
        yCoordiante = -1 * (identifyingLetterHeight / 2)
        xCoordinate = -1 * (windowWidth / 2) + (letterLength / 2) + (letterLength * letterIndex)
        bottomLeft, bottomRight, topLeft, topRight = (xCoordinate, yCoordiante), (xCoordinate + letterLength, yCoordiante), (xCoordinate, yCoordiante * -1), (xCoordinate + letterLength, yCoordiante * -1)

        results.append('length = ' + str(length) )
        results.append('bottomLeft = ' + str(bottomLeft) )
        results.append('bottomRight = ' + str(bottomRight) )
        results.append('topLeft = ' + str(topLeft) )
        results.append('topRight = ' + str(topRight) )

    elif language == 'FluxJudonese':
        length, letterLength = identifyingLetterHeight / 7, identifyingLetterHeight
        xCoordinate, yCoordiante = -1 * (windowWidth / 2) + (letterLength / 2) + (letterLength * letterIndex), -1 * (identifyingLetterHeight / 2)
        bottomLeft, bottomRight, topLeft, topRight =  (xCoordinate, yCoordiante), (xCoordinate + letterLength, yCoordiante), (xCoordinate, yCoordiante * -1), (xCoordinate + letterLength, yCoordiante * -1)

        results.append('length = ' + str(length) )
        results.append('bottomLeft = ' + str(bottomLeft) )
        results.append('bottomRight = ' + str(bottomRight) )
        results.append('topLeft = ' + str(topLeft) )
        results.append('topRight = ' + str(topRight) )

    elif language == 'Covenant':
        letterHeight = identifyingLetterHeight
        xCoordinate, yCoordiante = -1 * (windowWidth / 2) + (letterHeight / 2) + (letterHeight * letterIndex), -1 * (letterHeight / 2)
        
        results.insert(2, 'turtle.setheading(45)')
        results.insert(3, 'turtle.forward( ( ( (2 * (letterHeight ** 2) ) ** (0.5) ) / 2) - ( (2 * ( (letterHeight / 4) ** 2) ) ** (0.5) ) )')

    elif language == 'HowToTrainYourDragon':
        letterHeight = identifyingLetterHeight
        xCoordinate, yCoordiante = -1 * (windowWidth / 2) + (letterHeight / 2) + (letterHeight * letterIndex), -1 * (letterHeight / 2)

    elif language == 'Alienese':
        letterHeight = identifyingLetterHeight
        xCoordinate = -1 * (windowWidth / 2) + letterHeight + (letterHeight * letterIndex)
        if letter.islower():
            yCoordiante = -1 * letterHeight / 2
        else:
            yCoordiante = 0

    results[1] = results[1][:-1] + str(xCoordinate) + ',' + str(yCoordiante) + results[1][-1]
    return results

def translateNextLetterToFilename(language, letter):
    if language == 'Alienese':
        AlieneseFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z', 'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', ':':'colon', '"':'doubleQuoteOpen', '!':'exclamationPoint', '-':'hyphen', '.':'period', ';':'semiColon', "'":'singleQuote'}
        result = AlieneseFileNames.get(letter)

    letter = letter.lower()

    if language == 'GreenRune':
        GreenRuneLetterFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z', ')':'closeParen', '\'':'openQuotation', '(':'openParen', '?':'questionMark', ',':'comma'}
        result = GreenRuneLetterFileNames.get(letter)

    if language == 'MinecraftEnchantTable':
        MinecraftEnchantTableFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}
        result = MinecraftEnchantTableFileNames.get(letter)
    
    if language == 'FluxJudonese':
        FluxJudoneseFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}
        result = FluxJudoneseFileNames.get(letter)

    if language == 'Covenant':
        CovenantFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}
        result = CovenantFileNames.get(letter)

    if language == 'HowToTrainYourDragon':
        HowToTrainYourDragonFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'ij', 'j':'ij', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'uvw', 'v':'uvw', 'w':'uvw', 'x':'x', 'y':'y', 'z':'z'}
        result = HowToTrainYourDragonFileNames.get(letter)
    
    if result is None:
        raise ImportError('The letter you are seaching for: ' + letter + ' is not in the language that you provided (' + language + '\'n')
    return result
        

def getCodeForLetter(language, letter, writingType):
    codeToWriteLetter = []
    try:
        letter = translateNextLetterToFilename(language=language, letter=letter)
    except:
        raise ImportError('The letter you are seaching for: ' + letter + ' is not in the language that you provided (' + language + '\'n')
    
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

def makeLanguageUniform(input):
    input = input.lower()
    AlienesePseudonyms = ['al', 'fa', 'alienese', 'futurama']
    ArtemisFowlPseudonyms = ['af']
    CCGallifreyanPseudonyms = ['cc']
    CircularGallifreyanPseudonyms = ['cg']
    CisterianNumbersPseudonyms = ['cn', 'cisterian', 'cisteriannumbers', 'cisteriannumber']
    CovenantPseudonyms = ['co', 'covenant', 'haloaliens', 'halo']
    FluxJudonesePseudonyms = ['fj', 'flux', 'fluxjudonese', 'judonese']
    ForerunnerPrometheanPseudonyms = ['fp']
    GreenRunePseudonyms = ['gr', 'greenrune']
    HowToTrainYourDragonPseudonyms = ['ht', 'httyd', 'howtotrainyourdragon', 'vikingalphabet']
    MinecraftEnchantTablePseudonyms = ['mc', 'minecraft', 'met', 'minecraftenchanttable', 'standardgalacticalphabet']
    allLanguages = [AlienesePseudonyms, ArtemisFowlPseudonyms, CCGallifreyanPseudonyms, CircularGallifreyanPseudonyms, CisterianNumbersPseudonyms, CovenantPseudonyms, FluxJudonesePseudonyms, ForerunnerPrometheanPseudonyms, GreenRunePseudonyms, HowToTrainYourDragonPseudonyms, MinecraftEnchantTablePseudonyms ]
    allLanguageFileNames = ['Alienese', 'ArtemisFowl', 'CCGallifreyan', 'CircularGallifreyan', 'CisterianNumbers', 'Covenant', 'FluxJudonese', 'ForerunnerPromethean', 'GreenRune', 'HowToTrainYourDragon', 'MinecraftEnchantTable']
    for index in range(len(allLanguages) ):
        if allLanguages[index].count(input) == 1:
            return allLanguageFileNames[index]
    raise RuntimeError('This command should be run with multiple arguments. The first for a text file of input text, the second with the name of the output python file. The third is language for text, and fourth is language for numbers if not included in third. There may be more optional arguments after this based on the languages used.')

def makeOptionUniform(option):
    option = option.lower()
    recognizedOptions = {'windowwidth':'windowWidth', 'windowheight':'windowHeight', 'writingspeed':'writingSpeed', 'letterheight':'letterHeight', 'writingtype':'writingType'}
    if recognizedOptions.get(option[:option.find('=') ], -1) != -1:
        optionName = recognizedOptions.get(option[:option.find('=') ] )
        option = optionName + option[option.find('='): ]
    else:
        raise RuntimeError('The option ' + input + ' was not recognized. If this is a valid option that you should be able to change please let me know and I will update the program. Otherwise, you have mispelled that option. Check it out and fix that.\n')
    return option

def printExtraFilePrimerMaterial(language):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__) ), 'CypherLibrary/' + language + '/encodedTextPrimerFile.txt'), 'r' ) as x:
        return x.read()
    
def languageIncludesNumbers(language):
    languagesThatSupportNumbers = ['Alienese', 'CisterianNumbers', 'ForerunnerPromethean']
    # for index in range(len(languagesThatSupportNumbers) ):
    #     if languagesThatSupportNumbers.count(input) == 1:
    #         return True
    if language in languagesThatSupportNumbers:
        return True
    return False

def setupStartingEnvironment(outputStream, language, inputTextLength, options={} ):
    defaultOptions = {'windowWidth':1000, 'windowHeight':600, 'writingSpeed':0, 'letterHeight':1, 'writingType':'individual'}
    if len(options) == 0:           
        options = defaultOptions
    else:
        for essentialOption in defaultOptions:
            if essentialOption not in options.keys():
                options.update( {essentialOption:defaultOptions.get(essentialOption) } )
    if defaultOptions.get('writingSpeed') > 10:
        defaultOptions.update( {'writingSpeed':10} )
    

    outputStream.write('import turtle\nwindow = turtle.Screen()\nwindow.setup(width=' + str(options.get('windowWidth') ) + ', height=' + str(options.get('windowHeight') ) + ')\nturtle.mode("logo")\nturtle.speed(' + str(options.get('writingSpeed') ) + ')\n')

    letterHeight = int(options.get('windowWidth') / (inputTextLength + 1) )
    specificVariables = {'letterHeight':letterHeight, 'windowHeight':options.get('windowHeight'), 'windowWidth':options.get('windowWidth') }
    specificVariables.update( {} )

    if language == 'GreenRune':
        outputStream.write('letterHeight = ' + str(letterHeight) + '\n\n')

    if language == 'MinecraftEnchantTable':
        length = letterHeight / 5
        outputStream.write('length = ' + str(length) + '\n\n')

    if language == 'FluxJudonese':
        direction = 0
        outputStream.write('direction = ' + str(direction) + '\n\n')
        outputStream.write(printExtraFilePrimerMaterial(language=language) )

    if language == 'Covenant':
        outputStream.write('letterHeight = ' + str(letterHeight) + '\n')
        outputStream.write('largeSide = ' + str(letterHeight / 2) + '\n')
        outputStream.write('smallerSide = ' + str(letterHeight / 5) + '\n')

    if language == 'HowToTrainYourDragon':
        lineWidth = letterHeight / 10  
        outputStream.write('letterHeight = ' + str(letterHeight) + '\n')
        outputStream.write('lineWidth = ' + str(lineWidth) + '\n')
        outputStream.write('diagonal = ' + str(lineWidth * 3) + '\n')

    if language == 'Alienese':
        dotWidth, lowerLetterHeight = letterHeight / 20, letterHeight * (2 / 3)  
        outputStream.write('letterHeight = ' + str(letterHeight) + '\n')
        outputStream.write('dotWidth = ' + str(dotWidth) + '\n')
        outputStream.write('lowerLetterHeight = ' + str(lowerLetterHeight) + '\n')

    return specificVariables


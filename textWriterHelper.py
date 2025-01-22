import os
#   METHOD(S) TO BE USED IN THE FILE LATER
def goToStartingPoint(language, letter, identifyingLetterHeight, windowWidth, letterIndex, fullWritingLength):
    #   This method assumes equal back-to-back spaces for each letter in letter-by-letter languages - implement differences in this by language
    #       Need to later determine spacing for the word-by-word languages
    results = ['turtle.penup()', 'turtle.goto()', 'turtle.pendown()']

    if language == 'GreenRune':
        # letterWidth == letterHeight for GreenRune.
        letterHeight = identifyingLetterHeight
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

    results[1] = results[1][:-1] + str(xCoordinate) + ',' + str(yCoordiante) + results[1][-1]
    return results

def translateNextLetterToFilename(language, letter):
    letter = letter.lower()
    if language == 'GreenRune':
        GreenRuneLetterFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z', ')':'closeParen', '\'':'openQuotation', '(':'openParen', '?':'questionMark', ',':'comma'}
        result = GreenRuneLetterFileNames.get(letter)

    if language == 'MinecraftEnchantTable':
        MinecraftEnchantTableFileNames = {'a': 'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z'}
        result = MinecraftEnchantTableFileNames.get(letter)
    
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
    AlienesePseudonyms = ['al']
    ArtemisFowlPseudonyms = ['af']
    CCGallifreyanPseudonyms = ['cc']
    CircularGallifreyanPseudonyms = ['cg']
    CisterianNumbersPseudonyms = ['cn', 'cisterian', 'cisteriannumbers', 'cisteriannumber']
    CovenantPseudonyms = ['co']
    FluxJudonesePseudonyms = ['fj']
    ForerunnerPrometheanPseudonyms = ['fp']
    GreenRunePseudonyms = ['gr', 'greenrune']
    HowToTrainYourDragonPseudonyms = ['ht']
    MinecraftEnchantTablePseudonyms = ['mc', 'minecraft', 'met', 'minecraftenchanttable', 'standardgalacticalphabet']
    allLanguages = [AlienesePseudonyms, ArtemisFowlPseudonyms, CCGallifreyanPseudonyms, CircularGallifreyanPseudonyms, CisterianNumbersPseudonyms, CovenantPseudonyms, FluxJudonesePseudonyms, ForerunnerPrometheanPseudonyms, GreenRunePseudonyms, HowToTrainYourDragonPseudonyms, MinecraftEnchantTablePseudonyms ]
    allLanguageFileNames = ['Alienese', 'ArtemisFowl', 'CCGallifreyan', 'CircularGallifreyan', 'CisterianNumbers', 'Covenant', 'FluxJudonese', 'ForerunnerPromethean', 'GreenRune', 'HowToTrainYourDragon', 'MinecraftEnchantTable']
    for index in range(len(allLanguages) ):
        if allLanguages[index].count(input) == 1:
            return allLanguageFileNames[index]
    raise RuntimeError('This command should be run with multiple arguments. The first for a text file of input text, the second with the name of the output python file. The third is language for text, and fourth is language for numbers if not included in third. There may be more optional arguments after this based on the languages used.')

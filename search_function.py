from english_words import english_words_set

def wordSnippets(wordLength):
    snippetCountx1 = 0
    snippetCountx2 = 0
    snippetCountx3 = 0

    snippetCountx3 = wordLength // 3
    wordLength -= snippetCountx3*3

    snippetCountx2 = wordLength // 2
    wordLength -= snippetCountx2*2

    snippetCountx1 = wordLength // 1

    return [snippetCountx3, snippetCountx2, snippetCountx1]

def wordSimilarityFunc(snippets, searchWord, comparisonWord, searchSensitivity):
    wordSimilarity = 0
    for i in range(3):
        for x in range(snippets[i]):
            snippetSimilarity = 0
            for letterNumber in range(len(searchWord[0:3-i])):
                try:
                    if searchWord[letterNumber] == comparisonWord[letterNumber]:
                        snippetSimilarity += 1
                except:
                    continue
            if snippetSimilarity >= (3-i)/searchSensitivity:
                wordSimilarity += 1
            else:
                wordSimilarity -= 1
            searchWord = searchWord[3-i:len(searchWord)]
            comparisonWord = comparisonWord[3-i:len(comparisonWord)]
    return wordSimilarity

def main(listOfWords, searchWord, searchSensitivity):
    foundWordList = []

    #Fast search for word
    if searchWord in listOfWords:
        foundWordList.append([searchWord, 100])
        del(listOfWords[listOfWords.index(searchWord)])

    searchWordLength = len(searchWord)
    numberOfSearchWordSnippets = wordSnippets(searchWordLength)

    #Searching for any words similar
    for word in listOfWords:
        wordSimilarity = wordSimilarityFunc(numberOfSearchWordSnippets, searchWord, word, searchSensitivity)

        percentage = 100/sum(numberOfSearchWordSnippets)
        wordSimilarityPercentage = percentage*wordSimilarity

        if wordSimilarityPercentage >= 45:
            foundWordList.append([word,wordSimilarityPercentage])

    return foundWordList





if __name__ == '__main__':
    listOfWords = [i.lower() for i in english_words_set]

    print(max(listOfWords, key=len))

    word = input("Enter search term - ")
    #searchSensitivity controls how close each snippet has to be to the searched word. 3 is low, 1 is high
    searchSensitivity = 1
    foundWordList = main(listOfWords, word.lower(), searchSensitivity)
    try:
        for word in foundWordList:
            print(word)
    except:
        print("No Instances")


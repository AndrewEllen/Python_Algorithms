
def wordSnippets(searchWordLength):
    snippetCountx3 = 0
    snippetCountx2 = 0
    snippetCountx1 = 0

    snippetCountx3 = searchWordLength // 3
    searchWordLength -= snippetCountx3*3

    snippetCountx2 = searchWordLength // 2
    searchWordLength -= snippetCountx2*2

    snippetCountx1 = searchWordLength // 1

    print(snippetCountx3, snippetCountx2, snippetCountx1)
    return snippetCountx3, snippetCountx2, snippetCountx1

def main(list, word):
    searchWordLength = len(word)
    snippetCountx3, snippetCountx2, snippetCountx1 = wordSnippets(searchWordLength)
    for listWord in list:
        listWordLength = len(listWord)
        listWordSimilarityScore = 0

        for i in range(searchWordLength):
            try:
                try:
                    listOfLetters = word[i:i+3]
                except:
                    try:
                        listOfLetters = word[i:i+2]
                    except:
                        listOfLetters = word[i]

                listOfLettersLength = len(listOfLetters)
                if listOfLettersLength == 0:
                    continue
                listOfLettersSimilarityScore = 0

                for letter in listOfLetters:
                    wordComparisonSnippet = listWord[i:i+listOfLettersLength]
                    if letter in wordComparisonSnippet:
                        listOfLettersSimilarityScore += 1
                        continue
                    else:
                        continue

                if listOfLettersSimilarityScore >= listOfLettersLength/2:
                    listWordSimilarityScore += 1
                else:
                    listWordSimilarityScore -= 1
            except:
                pass
        if listWordSimilarityScore >= listWordLength/2:
            print(listWord)


if __name__ == '__main__':
    listOfWords = [
        "hello",
        "word",
        "hi",
        "goodbye",
        "atypical",
        "typical"
    ]
    word = input("Enter search term - ")
    main(listOfWords, word.lower())


def main(list, word):
    searchWordLength = len(word)
    for listWord in list:
        listWordLength = len(listWord)
        listWordSimilarityScore = 0
        for i in range(searchWordLength):
            try:
                try:
                    listOfLetters = listWord[i:i+3]
                except:
                    try:
                        listOfLetters = listWord[i:i+2]
                    except:
                        listOfLetters = listWord[i]

                listOfLettersLength = len(listOfLetters)
                if listOfLettersLength == 0:
                    continue
                listOfLettersSimilarityScore = 0

                for letter in listOfLetters:
                    if letter in word[i:i+listOfLettersLength]:
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
        "atypical"
    ]
    word = input("Enter search term - ")
    main(listOfWords, word.lower())

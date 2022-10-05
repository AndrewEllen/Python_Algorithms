
def main(list, word):
    searchWordLength = len(word)
    for listWord in list:
        listWordLength = len(listWord)
        listWordSimilarityScore = 0
        for i in range(searchWordLength):
            try:
                if listWord[i] == word[i]:
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
        "goodbye"
    ]
    word = input("Enter search term - ")
    main(listOfWords, word)

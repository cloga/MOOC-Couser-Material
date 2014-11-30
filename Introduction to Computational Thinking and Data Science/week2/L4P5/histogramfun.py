import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    per_list = []
    for word in wordList:
        fre = 0
        for vo in vowels:
            fre = fre + word.upper().count(vo)
        per_list.append(fre / float(len(word)))
    print per_list
    pylab.hist(per_list, bins=numBins)
    pylab.title('vowel proportion')
    pylab.xlabel('Fraction of vowel')
    pylab.ylabel('word count')
    pylab.show()
    

    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)

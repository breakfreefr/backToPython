#!python3 -tt
# # read in the dictionary and make a list of random 2 3 4 5 letter words.
## first refactor code to have a proper main

'''
saved on github.com with user breakfreefr !

this is a refactored version ....
'''

import random
import re

def getWords():

    dictionaryFilename='/usr/share/dict/words'

    file = open(dictionaryFilename, 'r')
    allWords = file.read()
    file.close()

    oneLetter = re.findall(r'\n(\w)\n', allWords)
    twoLetter = re.findall(r'\n(\w\w)\n', allWords)
    threeLetter = re.findall(r'\n(\w\w\w)\n', allWords)
    fourLetter = re.findall(r'\n(\w\w\w\w)\n', allWords)
    fiveLetter = re.findall(r'\n(\w\w\w\w\w)\n', allWords)
    
    print ('Total words in dict:', len(allWords))

    shortList = (oneLetter, twoLetter, threeLetter, fourLetter, fiveLetter)
    return shortList

def getCombinedList(shortList):
    # takes the tuple list and turns into a single list

    (oneLetter, twoLetter, threeLetter, fourLetter, fiveLetter) = shortList
    combinedList = oneLetter + twoLetter + threeLetter + fourLetter + fiveLetter

    return combinedList

def printSummary(shortList, combinedList):

    (oneLetter, twoLetter, threeLetter, fourLetter, fiveLetter) = shortList

    print ('1 letter:', len(oneLetter))
    print ('2 letters:', len(twoLetter))
    print ('3 letters:', len(threeLetter))
    print ('4 letters:', len(fourLetter))
    print ('5 letters:', len(fiveLetter))

    print ('\nGives a combined list of:', len(combinedList))

    print ('ie: total number of combinations:', len(combinedList)**5 )
    print ()
    return

def getRandomWord(wordList):

    nthWord = random.randint(1,len(wordList))
    aWord =  wordList[nthWord]   

    return aWord

def main():

    theWords = getWords()
    combinedList=getCombinedList(theWords)
    printSummary(theWords, combinedList)
    print()

    for noOfPhrases in range(1,10):
        w1 = getRandomWord(combinedList)
        w2 = getRandomWord(combinedList)
        w3 = getRandomWord(combinedList)
        w4 = getRandomWord(combinedList)

        print(w1 + '-' + w2 + '-' + w3 + '-' + w4 )
        print()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
#!python3 -tt
# # read in the dictionary and make a list of random 2 3 4 5 letter words.
## first refactor code to have a proper main

'''
saved on github.com with user breakfreefr !

this is a refactored version ....
'''

import random
import re

def openDict():

    dictionaryFilename='/usr/share/dict/words'

    file = open(dictionaryFilename, 'r')
    fourWordList = []
    for word in file:
        if len(word) == 5: # file has cr at each line end.
            fourWordList.append(word[0:])
    file.close()

    countFourLetters = len(fourWordList)
    print ('four lettered words in dictionary are :', countFourLetters)
    return fourWordList

def randomFourWord(fourWordList):
    wordN = random.randint(1,len(fourWordList))
    return fourWordList[wordN]


def main():

    fourwordlist = openDict()
    for noOfWords in range(1,5):
        print (randomFourWord(fourwordlist) + "-" + randomFourWord(fourwordlist) + "-" + randomFourWord(fourwordlist))


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
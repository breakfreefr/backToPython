# read in the dictionary and make a list of four letter words.

'''
Paul Smith returning to python after a couple of years
This is a very simple exercise to get my feet wet and 
do something relatively simple yet fun.

saved on github.com with user breakfreefr !
'''

import random

dictionaryFilename='/usr/share/dict/words'

file = open(dictionaryFilename, 'rU')
fourWordList = []
for word in file:
    if len(word) == 6: # file has cr at each line end.
        fourWordList.append(word[0:5])
file.close()

countFourLetters = len(fourWordList)
print 'four lettered words in dictionary is :', countFourLetters

def randomFourWord():
    wordN=random.randint(1,countFourLetters)
    return fourWordList[wordN]

for noOfWords in range(1,5):
    print randomFourWord() + "-" + randomFourWord() + "-" + randomFourWord()
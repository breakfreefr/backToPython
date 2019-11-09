#!python3
#
# Simple use of  module which produces random word strings
# and then displauys on the lcd of pione
#
# Paul Smith - November 2019
#
# show the time every second
#
import I2C_LCD_driver
from time import *
import minijib
import time

def main():

    mylcd = I2C_LCD_driver.lcd()

    mylcd.lcd_display_string("hello",1)
    mylcd.lcd_display_string("hello freddy",2)


    theWords = minijib.getWords()
    combinedList=minijib.getCombinedList(theWords)
    minijib.printSummary(theWords, combinedList)

    newPhrase = 'mini jibberish !!!'
    while True:
        oldPhrase = newPhrase
        newPhrase = minijib.getPhrase(combinedList)
        mylcd.lcd_display_string(newPhrase),1)
        mylcd.lcd_display_string(oldPhrase),2)
        
        sleep(5)

if __name__ == '__main__':
  main()
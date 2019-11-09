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

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("hello",1)
mylcd.lcd_display_string("hello freddy",2)

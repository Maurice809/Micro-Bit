# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
for u in range(9):
    for i in range(5):
        display.set_pixel(i,4,u)
    sleep(100) 
for i in range(4, 0, -1):
    display.set_pixel(i,4,0)
    sleep(150)
for x in range(2):
    for u in range(9, -1, -1):
        for i in range(4):
            display.set_pixel(i,4,u)
            sleep(15)
        display.set_pixel(4,4,9)
    sleep(1200)
    for u in range(9, -1, -1):
        for i in range(4, 0, -1):
            display.set_pixel(i,4,u)
            sleep(15)
        display.set_pixel(0,4,9)
    sleep(1200)
for u in range(9, -1, -1):
    display.set_pixel(0,4,9)
    sleep(15) 
display.clear()
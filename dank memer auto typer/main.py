import pynput
import random
import time
from pynput.keyboard import Key, Controller
memetypes = ["n" , "e" , "r" , "d"]
keyboard = Controller()
i = 0

while i < 1:
    
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    time.sleep(random.randint(2, 7))
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    time.sleep(random.randint(2, 7))
    keyboard.type('pls pm')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type(random.choice(memetypes))
    keyboard.press(Key.enter)
    time.sleep(random.randint(2, 7))
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    time.sleep(random.randint(2, 7))
    keyboard.type('pls use pink')  
    time.sleep(2)
    keyboard.type('270904126974590976') #dankmemer's id
    time.sleep(2)
    keyboard.type('1')
    time.sleep(49)


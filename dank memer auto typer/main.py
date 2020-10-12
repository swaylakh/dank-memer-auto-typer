import pynput
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
i = 0

while i < 1:
    
    keyboard.type('pls hunt')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('pls fish')
    keyboard.press(Key.enter)
    time.sleep(3)
    keyboard.type('pls pm')
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type('d')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('pls beg')
    keyboard.press(Key.enter)
    time.sleep(2)
    time.sleep(49)


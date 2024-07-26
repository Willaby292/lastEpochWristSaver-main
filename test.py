
import pyautogui, sys
import time
from tkinter import *

screenWidth, screenHeight = pyautogui.size()

# start_time = time.time()
# print(start_time)

# while time.time() - start_time < 10:
#     print(time.time() - start_time)
#     time.sleep(1)

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
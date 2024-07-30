import keyboard
from threading import Thread
from Skill import *
from Inventory import *
import math

# 0(800, 350) 1(950, 350) 2(1100, 350)
# 3(800, 500) 4(950, 500) 5(1100, 500)
# 6(800, 650) 7(950, 650) 8(1100, 650)

# x range 800-1100 = 300 intervals of 150
# y range 350-650 = 300  intervals of 150
def moveMouse(screenWidth, screenHeight):
    lastEpochConstant = 100 #px this will mess with this on other monitors...
    while True:
        keyPress = keyboard.read_key()
        if keyPress == ('up'):
            pyautogui.moveTo(screenWidth/2, screenHeight/4 - lastEpochConstant)
        elif keyPress == ('down'):
            pyautogui.moveTo(screenWidth/2, screenHeight*(3/4) - lastEpochConstant)
        elif keyPress == ('left'):
            pyautogui.moveTo(screenWidth/4, screenHeight/2 - lastEpochConstant)
        elif keyPress == ('right'):
            pyautogui.moveTo(screenWidth*(3/4), screenHeight/2 - lastEpochConstant)

def spinMouse(radius=500, speed=0.5):
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    angle = 0

    while True:
        if keyboard.is_pressed('0'):
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            pyautogui.moveTo(x, y)
            angle += speed
            if angle >= 2 * math.pi:
                angle -= 2 * math.pi  # Ensure angle stays within 0 to 2π range
        elif keyboard.is_pressed('9'):
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            pyautogui.moveTo(x, y)
            angle -= speed
            if angle < 0:
                angle += 2 * math.pi  # Ensure angle stays within 0 to 2π range
        else:
            time.sleep(0.01)  # Small sleep to prevent high CPU usage


# def moveLeague(screenWidth, screenHeight):
#     while True:
#         x, y = pyautogui.position()
#         #up
#         if screenWidth/3 < x <screenWidth*2/3:
#             if screenHeight/3 > y:
#             #up
#             elif y > screenHeight*2/3:
#             #down
#         if screenHeight/3 < y <screenHeight*2/3:
#             if screenWidth/3 > x:
#             #left
#             elif x > screenWidth*2/3:
#             #right
#         #down
#         #left
#         #right

if __name__ == '__main__':
    screenWidth, screenHeight = pyautogui.size()

    sigil = Skill('q', '*', '-')
    potion = Skill('1', '*', '-')
    whirlwind = Skill('w', '*', '-')

    sortInv = Inventory('/')
    emptyInv = Inventory('page up')
    teleToTeam = Inventory('7')

    sigilInterval = 4.5
    potionInterval = 8

    sigilThread = Thread(target = sigil.press, args=(sigilInterval,)) #interval here is ~5/16ths of what it should be but multithreading with whirlwind slows it down for some reason so i had to lower interval
    sigilThread.daemon = True
    sigilThread.start()

    whirlwindThread = Thread(target = whirlwind.hold)
    whirlwindThread.daemon = True
    whirlwindThread.start()

    potionThread = Thread(target = potion.press, args=(potionInterval,))
    potionThread.daemon = True
    potionThread.start()

    sortThread = Thread(target = sortInv.sort)
    sortThread.daemon = True
    sortThread.start()

    emptyThread = Thread(target = emptyInv.holdEmpty)
    emptyThread.daemon = True
    emptyThread.start()

    moveThread = Thread(target = moveMouse, args=(screenWidth, screenHeight))
    moveThread.daemon = True
    moveThread.start()

    mouseSpinThread = Thread(target = spinMouse)
    mouseSpinThread.daemon = True
    mouseSpinThread.start()

    teleThread = Thread(target = teleToTeam.teleToFriend)
    teleThread.daemon = True
    teleThread.start()

    print('end script with page down')

    keyboard.wait('page down')
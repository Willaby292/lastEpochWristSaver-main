import pyautogui
import keyboard
import time


def convertScreenRatioWidth(num, screenWidth):
    return num/1920 * screenWidth

def convertScreenRatioHeight(num, screenHeight):
    return num/1080 * screenHeight


class Inventory:
    def __init__(self, keyRun):
        self.keyRun = keyRun

# inefficient way to clear inv
    # def emptyFull(self):
    #     screenWidth, screenHeight = pyautogui.size()
    #     while True:
    #         try:
    #             keyboard.wait(self.keyRun) #key error is raised here when keyboard is waiting for the same input in two places. Idk why but I jsut force it through
    #         except KeyError:
    #             print('empty inventory forced through')
    #         pyautogui.keyDown('shift')
    #         x = 1230/1920 * screenWidth
    #         y = 685/1080 * screenHeight
    #         pyautogui.moveTo(x, y)
    #         pyautogui.rightClick()
    #         for i in range(0, 14):
    #             for j in range(0, 8):
    #                 pyautogui.move(0, 50/1080 * screenHeight)
    #                 pyautogui.rightClick()
    #             x += 47/1920 * screenWidth
    #             pyautogui.moveTo(x, y)
    #             pyautogui.rightClick()
    #         pyautogui.keyUp('shift')

    def holdEmpty(self):
        screenWidth, screenHeight = pyautogui.size()
        while True:
            try:
                keyboard.wait(self.keyRun) #key error is raised here when keyboard is waiting for the same input in two places. Idk why but I jsut force it through
            except KeyError:
                print('hold empty inventory forced through')
            pyautogui.keyDown('shift')
            x = convertScreenRatioWidth(1230, screenWidth)
            y = convertScreenRatioHeight(685, screenHeight)
            buttony = convertScreenRatioHeight(635, screenHeight)
            dist = convertScreenRatioHeight(140, screenHeight)
            while keyboard.is_pressed(self.keyRun):
                pyautogui.moveTo(x, y)
                pyautogui.rightClick()
                pyautogui.move(0, dist)
                pyautogui.rightClick()
                pyautogui.moveTo(x, buttony)
                pyautogui.click()
            pyautogui.keyUp('shift')


    def sort(self):
        screenWidth, screenHeight = pyautogui.size()
        while True:
            try:
                keyboard.wait(self.keyRun) #key error is raised here when keyboard is waiting for the same input in two places. Idk why but I jsut force it through
            except KeyError:
                print('sort inventory forced through')
            transferx = convertScreenRatioWidth(1669, screenWidth)
            sortx = convertScreenRatioWidth(1266, screenWidth)
            buttony = convertScreenRatioHeight(635, screenHeight)
            pyautogui.press('i')
            pyautogui.moveTo(transferx, buttony)
            pyautogui.click()
            pyautogui.moveTo(sortx, buttony)
            pyautogui.click()
            pyautogui.press('i')

    def teleToFriend(self):
        screenWidth, screenHeight = pyautogui.size()
        lastEpochConstant = 100
        while True:
            try:
                keyboard.wait(self.keyRun) #key error is raised here when keyboard is waiting for the same input in two places. Idk why but I jsut force it through
            except KeyError:
                print('sort inventory forced through')
            pyautogui.moveTo(75, 266)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1263, 483)
            pyautogui.click()
import pyautogui
import keyboard
import time

pyautogui.FAILSAFE = False

class Skill:
    def __init__(self, gameKey, keyStart, keyStop):
        self.gameKey = gameKey
        self.keyStart = keyStart
        self.keyStop = keyStop

    def hold(self):
        while True:
            try:
                keyboard.wait(self.keyStart) #key error is raised here when keyboard is waiting for the same input in two places. Idk why but I jsut force it through
            except KeyError as e:
                print('hold forced through')
            time.sleep(0.25)
            pyautogui.keyDown(self.gameKey)
            while True:
                if keyboard.is_pressed(self.keyStop):
                    break
            pyautogui.keyUp(self.gameKey)


    def pressHelper(self, interval):
        while True:
            start_time = time.time()
            pyautogui.press(self.gameKey)
            while time.time() - start_time < interval:
                if keyboard.is_pressed(self.keyStop):
                    return
                time.sleep(0.01)

    def press(self, interval):
        while True:
            try:
                keyboard.wait(self.keyStart) #same as above
            except KeyError as e:
                print('press forced through')
            time.sleep(0.5)
            self.pressHelper(interval)
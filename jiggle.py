import pyautogui
import time
import tkinter


# Checks if the mouse has moved after a period of time.  If it has not moved,
def run(window):
    print("running")
    alt = 0
    window.after(2000)
    x, y = pyautogui.position()
    window.after(10000)
    print("Stage 1")
    x_now, y_now = pyautogui.position()
    if x == x_now and y == y_now:
        print("Stage 2")
        while x == x_now and y == y_now:
            print("Stage 3")
            if alt == 0:
                print("Alt 0")
                pyautogui.moveRel(0, 2, duration=0)
                alt = 1
                x, y = pyautogui.position()
                window.after(10000)
                x_now, y_now = pyautogui.position()
            elif alt == 1:
                print("Alt 1")
                pyautogui.moveRel(0, -2, duration=0)
                alt = 0
                x, y = pyautogui.position()
                window.after(10000)
                x_now, y_now = pyautogui.position()
        print("Finished")

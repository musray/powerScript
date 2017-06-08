#!/usr/bin/env python3

import time
import datetime
import pyautogui


def move():
    for i in range(10):
        where = pyautogui.position()
        new_position = (where[0] + 200, where[1])  # move the mouse to right by 1px
        pyautogui.moveTo(new_position)

        time.sleep(1)

        where = pyautogui.position()
        new_position = (where[0] - 200, where[1])  # move the mouse to right by 1px
        pyautogui.moveTo(new_position)


def main():
    duration = 10 # move the mouse every 10 minutes 
    while True:
        now = datetime.datetime.now()
        print('%s , wait %d seconds.' % (now, duration))
        time.sleep(duration) # 15 seconds
        move()


if __name__ == '__main__':
    main()


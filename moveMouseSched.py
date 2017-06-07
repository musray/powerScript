#!/usr/bin/env python3

import time
import pyautogui


def move():
    where = pyautogui.position()
    new_position = (where[0] + 1, where[1])  # move the mouse to right by 1px
    pyautogui.moveTo(new_position)


def main():
    duration = 900 # move the mouse every 15 minutes 
    while True:
        print('wait %d seconds.' % duration)
        time.sleep(duration) # 15 seconds
        move()


if __name__ == '__main__':
    main()



import pyautogui as py
from pyclick import HumanClicker, HumanCurve
import math
import random
import time

"""
This module provides functions to perform various human-like actions using the mouse and keyboard.
It utilizes the pyautogui and pyclick libraries to create human-like movement curves and delays.
"""


def MoveF(x, y, t):

    fromPoint = py.position()
    options = {
        "knotsCount": 2,
    }
    human_curve = HumanCurve(fromPoint=fromPoint, toPoint=(x, y), **options)
    hc = HumanClicker()
    # move the mouse to position (100,100) on the screen in approximately 2 seconds
    hc.move((x, y), t, humanCurve=human_curve)


def HumanLikeMove(movex, movey):
    x, y = py.position()
    distance = math.sqrt(pow((x-movex), 2) + pow((y-movey), 2))
# 2140 total
    if distance <= 150:
        MoveF(movex, movey, random.uniform(0.7, 1.1))
    elif 150 < distance <= 300:
        MoveF(movex, movey, random.uniform(1.3, 1.6))
    elif 300 < distance <= 700:
        MoveF(movex, movey, random.uniform(1.6, 2.1))
    else:
        MoveF(movex, movey, random.uniform(2.5, 3))


def HumanLikeClick():
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)
    py.click()
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)


def Humanlikescroll(x):
    RN = random.randint(1, 3)
    x1 = round(x/RN)
    x2 = x % RN
    py.scroll(x2)
    for _ in range(RN):
        time.sleep(random.uniform(0.7, 1.2))
        py.scroll(x1)


def HumanLikeKeyboard(word):
    time.sleep(1)
    i = 0
    for _ in range(len(word)):
        b = random.uniform(0.09, 0.3)
        time.sleep(b)
        py.write(word[i])
        i += 1


def scrollpage():
    c = random.randint(400, 1000)
    Humanlikescroll(-c)
    Wait = random.randint(0, 2)
    time.sleep(Wait)


def HumanLikeWait(t, Bx, By):
    start = time.time()
    first = py.position()
    X_RelPose = Y_RelPose = 0
    fromPoint = py.position()

    while time.time() - start < t:

        if first[0] - Bx/2 < 50:
            x = random.randint(-fromPoint[0] +
                               50, -fromPoint[0]+Bx/2+first[0]+50)
        elif first[0] + Bx/2 > 1880:
            x = random.randint(-fromPoint[0]-Bx /
                               2+first[0], 1880-fromPoint[0] - 50)
        else:
            x = random.randint(-fromPoint[0]-Bx/2 +
                               first[0], -fromPoint[0]+Bx/2+first[0])

        if first[1] - By/2 < 50:
            y = random.randint(-fromPoint[1] +
                               50, -fromPoint[1]+By/2+first[1]+50)
        elif first[1] + By/2 > 1880:
            y = random.randint(-fromPoint[1]-By /
                               2+first[1], 1880-fromPoint[1] - 50)

        else:
            y = random.randint(-fromPoint[1]-By/2 +
                               first[1], -fromPoint[1]+By/2+first[1])

        X_RelPose = X_RelPose + x
        Y_RelPose = Y_RelPose + y

        fromPoint = py.position()

        options = {
            "knotsCount": 2,
        }

        human_curve = HumanCurve(fromPoint=fromPoint, toPoint=(
            fromPoint[0] + x, fromPoint[1] + y), **options)

        hc = HumanClicker()

        Chance = random.randint(1, 3)
        if Chance != 3:
            # move the mouse to position (100,100) on the screen in approximately 2 seconds
            hc.move((fromPoint[0] + x, fromPoint[1] + y),
                    random.uniform(1, 2), humanCurve=human_curve)
        else:
            time.sleep(random.uniform(1, 2))

        # py.moveTo(fromPoint[0] + x, fromPoint[1] + y,0.1)
        time.sleep(random.uniform(0.1, 0.3))
        fromPoint = py.position()

    HumanLikeMove(first[0]+random.randint(-5, 5),
                  first[1]+random.randint(-5, 5))

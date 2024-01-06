from PIL import ImageGrab
import string
import json
import datetime
from pyclick import HumanClicker, HumanCurve
import math
from timeit import default_timer as timer
from random import random
import pyautogui as py
import time
import random
from random import randrange
import subprocess
from PIL import Image, ImageGrab
from datetime import date
import tkinter as t
from tkinter import ttk
import pyperclip
import sys
import pygetwindow as gw
import winsound
import os


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


def MoveF(x, y, t):

    fromPoint = py.position()
    options = {
        "knotsCount": 2,
    }
    human_curve = HumanCurve(fromPoint=fromPoint, toPoint=(x, y), **options)
    hc = HumanClicker()
    # move the mouse to position (100,100) on the screen in approximately 2 seconds
    hc.move((x, y), t, humanCurve=human_curve)


def HumanLikeClick():
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)
    py.click()
    py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
    time.sleep(0.1)


def HumanLikeKeyboard(word):
    time.sleep(1)
    i = 0
    for _ in range(len(word)):
        b = random.uniform(0.09, 0.3)
        time.sleep(b)
        py.write(word[i])
        i += 1


def EnterUrl(Nameurl):
    HumanLikeMove(593+random.randint(-10, 10), 54)
    time.sleep(random.uniform(0.5, 0.8))
    HumanLikeClick()
    with py.hold('ctrl'):
        py.press(['a'])
    time.sleep(random.uniform(0.5, 0.8))
    py.press('Backspace')
    HumanLikeKeyboard(Nameurl)
    time.sleep(random.uniform(0.5, 0.8))
    py.press('Enter')
    time.sleep(8)

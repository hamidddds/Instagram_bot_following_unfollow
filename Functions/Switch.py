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
import ComputerFunctions as ai

time.sleep(2)
# ai.EnterUrl("www.instagram.com/")
switch = py.locateCenterOnScreen('C:\\Users\\hamid\\Dropbox\\My Codes instagram\\Instagram Bot\\Functions\\a.png', region=(
    1050, 124, 800, 200), confidence=0.7)

if switch:
    ai.HumanLikeMove(switch[0], switch[1])
    time.sleep(random.uniform(0.4, 0.8))
    py.click()
    time.sleep(1)
    for _ in range(4):
        time.sleep(random.uniform(0.4, 0.8))
        py.press('tab')
    time.sleep(random.uniform(0.4, 0.8))
    py.press('enter')
    time.sleep(random.uniform(1))

import pygetwindow as gw
from Logger import app_logger
import Logger
import lib_HumanMove as hu
import time
import pyautogui as py
import random
import tkinter as t
from tkinter import ttk
import os
import platform
import lib_OpenFollowinPage as openpage
import lib_Follwoing as Following
import lib_HumanMove as hu


def EnterUrl(Nameurl):
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    chrome_window.activate()
    time.sleep(0.5)
    # Send Alt+D to focus the address bar
    py.hotkey('alt', 'd')

    # Wait for a short time to ensure the address bar is focused
    time.sleep(0.5)
    hu.HumanLikeKeyboard(Nameurl)
    time.sleep(random.uniform(0.5, 0.8))
    py.press('enter')
    time.sleep(3)


def main(tagname):
    FirstPostPosition = (800+random.randint(-50, 50),
                         520+random.randint(-50, 50))
    EnterUrl(r"www.instagram.com/"+r"tag/{tagname}")
    hu.HumanLikeMove(FirstPostPosition)
    hu.HumanLikeClick()

import HumanMove as hu
import pyautogui as py
from pyclick import HumanClicker, HumanCurve
import math
import random
import time
import json
from PIL import ImageGrab  # Required for screen capture
import pyperclip  # Required for clipboard operations
import os
import platform


def locate_center_on_screen(image_path, region=None, confidence=0.7):
    try:
        return py.locateCenterOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


def FollowingPost(RemainedFollowed):  # return0 means it fails #end

    image_filenames = ['images/Following_like_button.png',
                       'images/Following_red_like_button.png',
                       'images/Following_red_like_comment_forward_button.png',
                       'images/Following_Like_Foward_button.png',
                       'images/Following_like_comment_forward_button.png',
                       'images/Following_Like_Comment_button.png',
                       'images/Following_red_like_comment.png',
                       ]

    Others = locate_center_on_screen('Images\others.png',
                                     region=(1000, 800, 600, 200), confidence=0.7)
    if (Others != None):
        hu.HumanLikeMove(Others[0], Others[1])
        py.click()
        time.sleep(1)
    else:
        for filename in image_filenames:
            time.sleep(0.6)
            V = locate_center_on_screen(filename, region=(
                700, 800, 600, 400), confidence=0.8)
            time.sleep(1)
            hu.HumanLikeMove(V[0], V[1])
            time.sleep(0.4)
            py.moveRel(0, 40, 0.5)
            time.sleep(0.35)
            py.click()
            time.sleep(2)


def clear_terminal():
    """
    Clears the terminal screen.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


clear_terminal()
time.sleep(3)
FollowingPost(4)

import HumanMove as hu
import time
import pyautogui as py
import random
import sys
import MoveToPosition as mp
import tkinter as t
from tkinter import ttk
import os
import platform


def clear_terminal():
    """
    Clears the terminal screen.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def ChangeTheProcessBar(Text):
    global NewProcess
    global root
    NewProcess.pack_forget()
    NewProcess = t.Label(root, text=Text)
    NewProcess.pack()
    root.update()
    time.sleep(1)


def get_screen_resolution():
    """
    Gets the current screen resolution.

    Returns:
    tuple: The width and height of the screen.
    """
    screen_width, screen_height = py.size()
    return screen_width, screen_height


def EnterUrl(Nameurl):
    hu.HumanLikeMove(593 + random.randint(-10, 10), 54)
    time.sleep(random.uniform(0.5, 0.8))
    hu.HumanLikeClick()
    with py.hold('ctrl'):
        py.press(['a'])
    time.sleep(random.uniform(0.5, 0.8))
    py.press('backspace')
    hu.HumanLikeKeyboard(Nameurl)
    time.sleep(random.uniform(0.5, 0.8))
    py.press('enter')
    time.sleep(8)


def ProcessBar():
    global root
    global NewProcess
    root = t.Tk()
    root.wm_attributes("-topmost", 1)
    root.geometry('300x100+0+900')
    Title = t.Label(root, text='Processing...')
    Title.pack()
    pb = ttk.Progressbar(root, length=200, mode='indeterminate')
    pb.pack()
    pb.start()
    NewProcess = t.Label(root, text='')
    NewProcess.pack_forget()
    root.update()
    # bb = t.Label(root, text='salam %d' % a)
    return


if __name__ == "__main__":

    width, height = get_screen_resolution()
    print(f"Current screen resolution: {width}x{height}")

    # Check if the resolution is 1920x1080
    if width != 1920 or height != 1080:
        print("Screen resolution is not 1920x1080. Terminating the script.")
        sys.exit(1)

    # If the resolution is 1920x1080, proceed with the rest of the script
    print("Screen resolution is 1920x1080. Continuing with the script.")

    clear_terminal()
    ProcessBar()
    TargetName = "mizmamoshavere"
    # Move to homepage
    # mp.Move("home")
    EnterUrl("www.instagram.com/"+TargetName)
    ChangeTheProcessBar('Starting Following ...')

import pygetwindow as gw
from Logger import app_logger
import Logger
import lib_HumanMove as hu
import time
import pyautogui as py
import random
import sys
import lib_MoveToPosition as mp
import tkinter as t
from tkinter import ttk
import os
import platform
import lib_OpenFollowinPage as openpage
import lib_Follwoing as Following


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
    clear_terminal()
    ProcessBar()
    TargetName = "partoo333"
    Number_of_following = 5
    following_flag = 1
    postnum = 1
    page_opener = openpage.OpeningFollowingPage()
    Follow_p = Following.Following(Number_of_following)

    ChangeTheProcessBar('Openning the webpage ...')

    width, height = get_screen_resolution()
    print(f"Current screen resolution: {width}x{height}")

    # Check if the resolution is 1920x1080
    if width != 1920 or height != 1080:
        print("Screen resolution is not 1920x1080. Terminating the script.")
        app_logger.error(
            'Screen resolution is not 1920x1080. Terminating the script.')
        sys.exit(1)

    ChangeTheProcessBar('Starting Following ...')
    # openpage()

    start_time = time.time()

    while True:
        start_time = time.time()

        if following_flag == 1:
            ChangeTheProcessBar('Openning the webpage ...')
            EnterUrl("www.instagram.com/"+TargetName)
            ChangeTheProcessBar('Following ...')
            page_opener.chose_post(postnum)
            page_opener.openfollowingpage()
            result = Follow_p.Finding_follow_buttom()
            if isinstance(result, tuple):
                _, postnum = result
            if Number_of_following >= Follow_p.Followed:
                following_flag = 0
        else:
            while 1500-(time.time()-start_time) > 0:
                hu.HumanLikeWait(20, 500, 500)
                time.sleep(60)
                following_flag = 1

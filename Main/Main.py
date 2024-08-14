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
import lib_ResultManager as result


class Results:
    def __init__(self) -> None:
        self.TotalNumberOfFollowed == 0
        self.DailyNumberOffollowed == 0
        self.LastStartTimeFollowing = 0
        self.targetname = ""
        self.typename = ""


def changewindowssize():
    # Find all Chrome windows
    chrome_windows = gw.getWindowsWithTitle('Chrome')

    if chrome_windows:
        # Select the first Chrome window found
        chrome_window = chrome_windows[0]

        # If the window is maximized, restore it first
        if chrome_window.isMaximized:
            chrome_window.restore()

        # Set the desired width and height
        new_width = 1400
        new_height = 1038

        # Resize the window
        chrome_window.resizeTo(new_width, new_height)

        # Move the window to the top-left corner
        chrome_window.moveTo(-8, 1)
    else:
        print("Chrome window not found.")


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

# write a class for all essential variables


def EnterUrl(TargetName, type):
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    chrome_window.activate()
    time.sleep(0.5)
    # Send Alt+D to focus the address bar
    py.hotkey('alt', 'd')

    # Wait for a short time to ensure the address bar is focused
    time.sleep(0.5)
    if type == "Hashtag":
        situation = "explore/tags/"
    elif type == "Page":
        situation = ""
    link = f"www.instagram.com/" + situation + TargetName

    hu.HumanLikeKeyboard(link)
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


def initiate():
    clear_terminal()
    # ProcessBar()


if __name__ == "__main__":
    initiate()
    # TargetName = "academy.movafaghyat"
    TargetType = "Hashtag"
    TargetName = "tech"
    Number_of_following = 15
    following_flag = 1
    postnum = 1
    total_follow = 0
    page_opener = openpage.OpeningFollowingPage()
    Following_func = Following.Following(Number_of_following)
    Result = result.ResultsManager()

    width, height = get_screen_resolution()
    print(f"Current screen resolution: {width}x{height}")

    # Check if the resolution is 1920x1080
    changewindowssize()

    start_time = time.time()

    while True:
        start_time = time.time()

        if following_flag == 1:
            # ChangeTheProcessBar('Openning the webpage ...')
            EnterUrl(TargetName=TargetName, type=TargetType)
            # ChangeTheProcessBar('Following ...')
            page_opener.chose_post(postnum, Target=TargetType)
            Following_box_validity = page_opener.openfollowingBox()

            if Following_box_validity == 1:
                temp = Number_of_following - Following_func.Followed

                if temp > 0:
                    Following_func.Following_Number = temp
                    Situation = Following_func.Finding_follow_buttom()

                else:

                    Result.update(target_name=TargetName, type_name=TargetType,
                                  number_of_followed_today=Following_func.Followed, success_rate=80.0)
                    following_flag = 0
                    Following_func.Following_Number = Number_of_following

        else:
            while 1800-(time.time()-start_time) > 0:
                hu.HumanLikeWait(20, 500, 500)
                time.sleep(60)

            following_flag = 1

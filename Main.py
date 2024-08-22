import pandas as pd
import pygetwindow as gw
from module.Logger import app_logger
import module.Logger
import module.lib_HumanMove as hu
import time
import pyautogui as py
import random
import tkinter as t
from tkinter import ttk
import os
import platform
import module.lib_OpenFollowinPage as openpage
import module.lib_Follwoing as Following
import module.lib_ResultManager as result
import module.Lib_liking as liking


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

        # Wait a moment to ensure the window is fully restored before resizing
        import time
        time.sleep(0.5)  # Adjust the sleep time if needed

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
    py.hotkey('Space')
    time.sleep(0.5)
    py.hotkey('Backspace')
    time.sleep(0.5)
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
    return


def initiate():
    clear_terminal()
    ProcessBar()


def read_inputs():
    file_path = os.path.join('data', 'Inputs.xlsx')

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    # Read the Excel file
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except Exception as e:
        raise RuntimeError(
            f"An error occurred while reading the Excel file: {e}")

    # Check if required columns exist
    required_columns = ['Target Name', 'Type Name', 'Number Of follow']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(
                f"The column '{col}' is missing from the Excel file.")

    # Read values
    TargetName = df.loc[0, 'Target Name']
    TargetType = df.loc[0, 'Type Name']
    Number_of_following = df.loc[0, 'Number Of follow']

    return TargetName, TargetType, Number_of_following


if __name__ == "__main__":

    initiate()
    changewindowssize()
    TargetName, TargetType, Number_of_following = read_inputs()
    # TargetName = "academy.movafaghyat"
    # TargetType = "Hashtag"
    # TargetName = "tech"
    # Number_of_following = 5
    following_flag = 1
    Liking_flag = 1
    flag_finished_following = 0
    postnum = 1
    Time_liking = 900
    page_opener = openpage.OpeningFollowingPage()
    Following_func = Following.Following(Number_of_following)
    Result = result.ResultsManager()
    like_func = liking.Liking_posts(Time_liking)

    width, height = get_screen_resolution()
    print(f"Current screen resolution: {width}x{height}")

    # Check if the resolution is 1920x1080
    ChangeTheProcessBar('Following ...')
    while True:
        wait_time = random.randint(3600, 3900)
        start_time = time.time()

        if following_flag == 1:
            ChangeTheProcessBar('Openning the webpage ...')
            EnterUrl(TargetName=TargetName, type=TargetType)

            page_opener.chose_post(postnum, Target=TargetType)
            Following_box_validity = page_opener.openfollowingBox()

            if Following_box_validity == 1:
                flag_finished_following = Following_func.Following_main(
                    TargetName)

            if flag_finished_following == 1:
                Result.update(target_name=TargetName, type_name=TargetType,
                              number_of_followed=Number_of_following)
                following_flag = 0
                flag_finished_following = 0

        if Liking_flag == 1:
            EnterUrl(TargetName=" ", type="Page")
            # ?? check validity
            like_func.liking()
            Liking_flag = 0

        if Liking_flag == 0 and following_flag == 0:
            while wait_time-(time.time()-start_time) > 0:

                HumanWait = random.randint(60, 120)
                hu.HumanLikeWait(HumanWait, 500, 500)
                time.sleep(random.randint(600, 700))

            following_flag = 1
            Liking_flag == 1

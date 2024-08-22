import pandas as pd
from PIL import ImageGrab, ImageChops
from datetime import datetime
from . import lib_HumanMove as hu
import pyautogui as py
import random
import time
import json
import pyperclip  # Required for clipboard operations
import os
import platform
import pygetwindow as gw
import winsound
from . import lib_OpenFollowinPage as openpage
from .Lib_Finding_image_on_screen import find_images


def clear_terminal():
    """
    Clears the terminal screen.
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def copyurlUrl():  # new
    # Find the active Chrome window
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]

    # Bring Chrome window to the front
    chrome_window.activate()
    time.sleep(0.5)
    # Send Alt+D to focus the address bar
    py.hotkey('alt', 'd')

    # Wait for a short time to ensure the address bar is focused
    time.sleep(0.5)

    # Send Ctrl+C to copy the URL to clipboard
    py.hotkey('ctrl', 'c')

    # Get the URL from the clipboard
    url = pyperclip.paste()
    return url


class UsersDetailManager:
    def __init__(self):
        current_directory = os.path.dirname(__file__)
        self.user_details = os.path.join(
            current_directory, '..', 'data', 'Users_detail.xlsx')
        self.check_and_create_file()

    def check_and_create_file(self):
        if not os.path.exists(self.user_details):
            # Create a new DataFrame with the required columns
            df = pd.DataFrame(columns=['User name', 'page', 'date'])
            df.to_excel(self.user_details, index=False)
            print(f"File created: {self.user_details}")
        else:
            print(f"File already exists: {self.user_details}")

    def add_new_entry(self, user_name, page, date):
        # Ensure the date is a datetime object
        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')

        # Load the existing Excel file
        df = pd.read_excel(self.user_details)

        # Ensure the page column is treated as a string
        df['page'] = df['page'].astype(str)

        # Create the new row as a DataFrame
        new_row = pd.DataFrame(
            {'User name': [user_name], 'page': [str(page)], 'date': [date]})

        # Check if the existing DataFrame is empty
        if df.empty:
            df = new_row
        else:
            # Concatenate the new row to the existing DataFrame
            df = pd.concat([df, new_row], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df.to_excel(self.user_details, index=False)
        print(f"New entry added: {new_row}")


class Following:
    def __init__(self, NumberOfFullowing) -> None:
        self.userdetail = UsersDetailManager()
        self.scrollCount = 0
        self.Followed = 0
        self.situation = 0
        self.Following_box = (330, 330, 600, 600)

        self.inside_box_pos = (790+random.randint(-10, 10),
                               601+random.randint(-30, -30))

        self.outside_box_pos = (350+random.randint(-10, 10),
                                450+random.randint(-30, -30))
        current_directory = os.path.dirname(__file__)

        self.finished_pages_path = os.path.join(
            current_directory, '..', 'data', 'Finished_pages.json')

        self.json_path = os.path.join(
            current_directory, '..', 'data', 'my_list.json')

        # 0 means it is under process
        self.im = None
        self.PostNum = 1  # 0 means it doesnt need to change the post
        self.Total_number_of_following = NumberOfFullowing

        self.initialize()

    def initialize(self):

        if os.path.exists(self.json_path):
            with open(self.json_path, 'r') as file:
                self.saved_following = json.load(file)
        else:
            self.saved_following = []

        if os.path.exists(self.finished_pages_path):
            # Check if the file is empty
            if os.path.getsize(self.finished_pages_path) == 0:
                # If the file is empty, write an empty list to it
                self.Finished_pages = []
                with open(self.finished_pages_path, 'w') as file:
                    json.dump(self.Finished_pages, file)
            else:
                # Otherwise, load the content of the file
                with open(self.finished_pages_path, 'r') as file:
                    self.Finished_pages = json.load(file)
        else:
            # If the file doesn't exist, create it with an empty list
            self.Finished_pages = []
            with open(self.finished_pages_path, 'w') as file:
                json.dump(self.Finished_pages, file)

        print('Starting Following ...')

    def Following_main(self, TargetName):
        # add a controll function wich open limited page instead of many pages

        self.Following_Number = self.Total_number_of_following-self.Followed

        check = self.CheckValidity()

        if check == 0:
            print("cannot see the following box")
            return 0

        while True:
            a = self.scoroll()
            # move out of box
            hu.HumanLikeMove(self.outside_box_pos)

            if a == 0:  # end of the scroll
                self.EndOfScroll_validity()
                return 0

            time.sleep(random.uniform(0.8, 1))
            FollowButtom = find_images(
                r'Images\followbutton2.png')
            time.sleep(random.uniform(0.5, 0.6))
            # start following

            if FollowButtom != None:
                for pos in FollowButtom:

                    check = self.CheckValidity()

                    if check == 2:
                        print("cannot see the following box but fixed")
                        break
                    elif check == 0:
                        print("cannot see the following box")
                        return 0

                    hu.HumanLikeMove(
                        [pos[0] - 240 + random.randint(-10, 10), pos[1]-7])
                    # Then, move to the y-axis position
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.3, 0.5))
                    py.moveRel(random.randint(1, 3), 3, 0.3)
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.3, 0.5))
                    hu.HumanLikeMove([pos[0]-240-random.randint(200, 300),
                                     pos[1] + random.randint(40, 60)])
                    time.sleep(random.uniform(0.4, 0.6))

                # ceheck the following is over or not
                openeningPages = self.Open_pages(TargetName)
                if openeningPages == 1:
                    print("Done with following")
                    return 1

                self.im = ImageGrab.grab(self.Following_box)
                # ????

                hu.HumanLikeMove(self.inside_box_pos)
                NowScroll = random.randint(-500, -400)
                hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
                time.sleep(0.5)
                FollowButtom = []

    def scoroll(self):
        # returning 0 means that we need to go to the next post
        self.scrollCount = 0

        hu.HumanLikeMove(self.inside_box_pos)
        x, y = py.position()

        for _ in range(300):
            self.scrollCount = self.scrollCount+1

            # if the cursor move a long disntace bring it back

            x1, y1 = py.position()
            if abs(x1-x) > 21 or abs(y1-y) > 21:
                hu.HumanLikeMove([x, y])

            Following_image = []

            Following_image = find_images(
                r'Images\Validity_following\Follow_buttom.png')

            if Following_image == None or len(Following_image) < 3:
                self.im = ImageGrab.grab(self.Following_box)
                NowScroll = random.randint(-500, -400)
                hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
                time.sleep(random.uniform(0.5, 0.8))
                end_scroll = self.EndOfScroll()

                if end_scroll == 1:
                    self.EndOfScroll_validity()
                    return 0  # end of scroll
            else:

                return 1

    def EndOfScroll(self):
        a2 = ImageGrab.grab(self.Following_box)
        diff = ImageChops.difference(self.im, a2)
        if diff.getbbox() is None:
            print('End of scroll,lets go to the next post!')
            self.PostNum = self.PostNum+1
            return 1

    def Open_pages(self, TargetName):
        time.sleep(0.5)
        # Send Alt+D to focus the address bar
        py.hotkey('alt', 'd')

        # Wait for a short time to ensure the address bar is focused
        time.sleep(0.5)

        # Send Ctrl+C to copy the URL to clipboard
        py.hotkey('ctrl', 'c')
        Homepage = copyurlUrl()

        py.hotkey('ctrl', 'Tab')

        print(Homepage)

        Name_Of_page = ''
        username = []

        while 1:
            Name_Of_page = copyurlUrl()
            print(Name_Of_page)
            #
            username = Name_Of_page.split("www.instagram.com/")[-1].rstrip('/')
            if Homepage == Name_Of_page:
                with open(self.json_path, 'w') as file:
                    json.dump(self.saved_following, file)
                return 0
            else:
                if username in self.saved_following:
                    time.sleep(random.uniform(0.4, 0.8))
                    py.hotkey('ctrl', 'w')
                else:
                    self.saved_following.append(username)
                    time.sleep(random.uniform(0.5, 0.7))
                    FollowButtom = find_images(
                        r'Images\followbutton2.png')
                    time.sleep(random.uniform(0.5, 0.9))
                    # start following

                    if FollowButtom:
                        print('Following...')
                        hu.HumanLikeMove([FollowButtom[0][0]+random.randint(-25, 25),
                                         FollowButtom[0][1]+random.randint(-10, 10)])
                        time.sleep(random.uniform(0.8, 1))
                        py.click()
                        time.sleep(0.5)
                        # winsound.Beep(1000, 200)
                        time.sleep(random.uniform(2, 3))
                        current_date = datetime.now()
                        self.userdetail.add_new_entry(
                            user_name=username, page=TargetName, date=current_date)

                        self.Followed += 1
                        print("followed")

                        if self.Followed >= self.Following_Number:
                            while True:
                                time.sleep(random.uniform(0.5, 0.7))
                                Name_Of_page = copyurlUrl()
                                time.sleep(random.uniform(0.5, 0.7))
                                if Homepage == Name_Of_page:
                                    with open(self.json_path, 'w') as file:
                                        json.dump(self.saved_following, file)
                                        self.Followed = 0
                                        return 1
                                else:
                                    py.hotkey('ctrl', 'w')
                        time.sleep(random.uniform(0.4, 0.8))
                        py.hotkey('ctrl', 'w')
                        time.sleep(random.uniform(0.4, 0.8))

    def CheckValidity(self):
        ii = 0
        for i in range(3):

            time.sleep(random.uniform(0.7, 1))
            Like_image = find_images(
                r'Images\Validity_following\FollowingPage_LIkeButtom.png')
            # start following
            if Like_image:

                Following_image = find_images(
                    r'Images\Validity_following\Following_buttom.png')
                Follow_Butt = find_images(
                    r'Images\Validity_following\Follow_buttom.png')
                Request_Butt = find_images(
                    r'Images\Validity_following\requested_Buttom.png')

                if Following_image is None and Follow_Butt is None and Request_Butt is None:
                    print("Cannot see the page")
                else:
                    print('can see following box')
                    return 1
            else:

                postpage = copyurlUrl()
                if 'instagram.com/p/' in postpage:
                    time.sleep(2)
                    ii = ii+1
                else:
                    return 0

                if ii == 1:
                    py.press('f5')
                    time.sleep(2)
                    a = openpage.OpeningFollowingPage()
                    a.openfollowingBox()
                    return 2

        if i == 3:

            screenshot = py.screenshot()
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"CannotOpenFollowingBox_{timestamp}.png"
            screenshot.save(filename)
            print("NotDone")
            return 0

    def EndOfScroll_validity(self):
        self.Finished_pages.append(copyurlUrl())
        with open(self.finished_pages_path, 'w') as file:
            json.dump(self.Finished_pages, file)

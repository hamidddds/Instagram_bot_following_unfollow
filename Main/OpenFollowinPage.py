import os
import platform
import HumanMove as hu
import pyautogui as py
import time
from PIL import ImageGrab  # Required for screen capture
import datetime


def locate_center_on_screen(image_path, region=None, confidence=0.7):
    try:
        return py.locateCenterOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


def locateOnScreen(image_path, region=None, confidence=0.7):
    try:
        return py.locateOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


def generate_filename_with_timestamp():
    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date and time
    timestamp = now.strftime("%Y%m%d_%H%M")
    # Construct the filename
    return "screenshot_" + timestamp + ".png"


class OpeningFollowingPage:
    def __init__(self) -> None:
        self.Followed_temp = 0
        self.Followed = 0
        self.situation = 0
        # 0 means unsucess
        # 1 means it is sucess
        self.PostNum = 1  # 0 means it doesnt need to change the post
        self.EndOfScroll = None
        # self.saved_following = []

        # self.initialize()

    # def initialize(self):
    #     with open('my_list.json', 'r') as file:
    #         self.saved_following = json.load(file)
    #     # self.chose_post()
    #     self.Getting_Ready_FOr_Follow()

    def chose_post(self):
        pass

    def openfollowingpage(self):
        Locations = []

        image_filenames = ['images/like_button.png',
                           'images/red_like_button.png',
                           'images/forward.png',
                           'images/Comment_button.png',
                           ]

        Others = locate_center_on_screen('images/others.png',
                                         region=(1000, 800, 600, 200), confidence=0.7)

        if (Others != None):
            hu.HumanLikeMove(Others[0], Others[1])
            py.click()
            time.sleep(1)
            if self.validity() == 0:
                pass
            else:
                return 1

        else:
            like_bottom_location = locate_center_on_screen('Main\Images\like_button.png', region=(
                700, 800, 600, 400), confidence=0.8)
            if like_bottom_location == None:
                like_bottom_location = locate_center_on_screen('Main\images/red_like_button.png', region=(
                    700, 800, 600, 400), confidence=0.8)
                if like_bottom_location != None:
                    Locations.append((like_bottom_location[0],
                                      like_bottom_location[1]))
            else:
                Locations.append((like_bottom_location[0],
                                  like_bottom_location[1]))
            comment_bottom_location = locate_center_on_screen('Main\images/Comment_button.png', region=(
                700, 800, 600, 400), confidence=0.8)

            if comment_bottom_location != None:
                Locations.append((comment_bottom_location[0],
                                  comment_bottom_location[1]))

            forward_bottom_location = locate_center_on_screen('Main\images/forward.png', region=(
                700, 800, 600, 400), confidence=0.8)

            if forward_bottom_location != None:
                Locations.append((forward_bottom_location[0],
                                  forward_bottom_location[1]))

            if len(Locations) == 0:
                print("wrong Page")
                return 0

            for i in range(len(Locations)):
                for j in range(i, len(Locations)):
                    location_coordinate = [(
                        Locations[i][0] + Locations[j][0]) / 2, (Locations[i][1] + Locations[j][1]) / 2]
                    time.sleep(1)
                    hu.HumanLikeMove(
                        int(location_coordinate[0]), int(
                            location_coordinate[1]))
                    time.sleep(0.4)
                    py.moveRel(0, 40, 0.5)
                    time.sleep(0.35)
                    py.click()
                    time.sleep(2)
                    if self.validity() == 0:
                        pass
                    else:
                        return 1

            print('Cannot Recognize The following page???')
            screenshot = ImageGrab.grab()  # Capture the specified region
            random_filename = generate_filename_with_timestamp()
            screenshot.save("canotseethepost_"+random_filename)
            return 0

    def validity(self):
        V = locateOnScreen('images/followingValidity.png', region=(
            500, 300, 800, 300), confidence=0.8)
        if V != None:
            pass
        else:
            return 0


def clear_terminal():
    # Detect the operating system
    current_os = platform.system()

    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# # Example usage
# clear_terminal()
# page_opener = OpeningFollowingPage()
# page_opener.openfollowingpage()

import pyautogui
from PIL import Image
from Logger import app_logger
from random import random
import lib_HumanMove as hu
import pyautogui as py
import time
from PIL import ImageGrab  # Required for screen capture
import datetime
import Logger
from datetime import datetime


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

        self.initialize()

    def initialize(self):
        pass
        # self.chose_post()

    def chose_post(self):
        hu.HumanLikeMove(800, 782)
        hu.HumanLikeClick()
        time.sleep(1)
        if self.PostNum != 1:
            time.sleep(random.uniform(0.5, 0.8))
            for i in range(1, self.PostNum-1):
                py.press('Right')
                self.PostNum = 0

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
                app_logger.error('cannot see the following page page')
                # Take a screenshot
                screenshot = pyautogui.screenshot()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"FollowingPage_is_not_detected{timestamp}.png"
                screenshot.save(filename)
                return

        else:
            like_bottom_location = locate_center_on_screen('Main\Images\like_button.png', region=(
                700, 800, 600, 400), confidence=0.8)
            if like_bottom_location == None:
                like_bottom_location = locate_center_on_screen('Main\images/red_like_button.png', region=(
                    700, 800, 600, 400), confidence=0.9)

            if like_bottom_location != None:
                Locations.append((like_bottom_location[0],
                                  like_bottom_location[1]))
            else:
                app_logger.info('Like buttom cannot be detected')
                screenshot = pyautogui.screenshot()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"Like_buttom_is_not_detected_{timestamp}.png"
                screenshot.save(filename)

            comment_bottom_location = locate_center_on_screen('Main\images/Comment_button.png', region=(
                700, 800, 600, 400), confidence=0.8)

            if comment_bottom_location != None:
                Locations.append((comment_bottom_location[0],
                                  comment_bottom_location[1]))
                app_logger.info('comment buttom cannot be detected')
                screenshot = pyautogui.screenshot()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"comment_buttom_is_not_detected_{timestamp}.png"
                screenshot.save(filename)

            forward_bottom_location = locate_center_on_screen('Main\images/forward.png', region=(
                700, 800, 600, 400), confidence=0.8)

            if forward_bottom_location != None:
                Locations.append((forward_bottom_location[0],
                                  forward_bottom_location[1]))
                app_logger.info('Forward buttom cannot be detected')
                screenshot = pyautogui.screenshot()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"Forward_buttom_is_not_detected_{timestamp}.png"
                screenshot.save(filename)

            if len(Locations) == 0:
                app_logger.error('Following page is not detected')
                print("wrong Page")
                return

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
                        return
            app_logger.info('Cannot Recognize The following page.')
            print('Cannot Recognize The following page???')
            screenshot = ImageGrab.grab()  # Capture the specified region
            random_filename = generate_filename_with_timestamp()
            screenshot.save("canotseethepost_"+random_filename)
            return

    def validity(self):
        V = locateOnScreen('images/followingValidity.png', region=(
            500, 300, 800, 300), confidence=0.8)
        if V != None:
            pass
        else:
            return 0

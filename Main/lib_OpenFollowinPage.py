from Lib_Finding_image_on_screen import find_images
import random
import os
import pyautogui
from PIL import Image
from Logger import app_logger
import lib_HumanMove as hu
import pyautogui as py
import time
from PIL import ImageGrab  # Required for screen capture
import Logger
from datetime import datetime
import json
import pyperclip


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

    url = pyperclip.paste()

    return url


def generate_filename_with_timestamp():
    # Get the current date and time
    now = datetime.now()
    # Format the date and time
    timestamp = now.strftime("%Y%m%d_%H%M")
    # Construct the filename
    return "screenshot_" + timestamp + ".png"


class OpeningFollowingPage:
    def __init__(self) -> None:
        self.Followed_temp = 0
        self.Followed = 0
        self.situation = 0
        self.likecommentfowrward = (1150, 580, 400, 200)
        # 0 means unsucess
        # 1 means it is sucess
        self.PostNum = 1  # 0 means it doesnt need to change the post
        self.EndOfScroll = None
        # self.saved_following = []

        self.initialize()

    def initialize(self):
        if not os.path.exists("/screenshots/Error_screenshots"):
            os.makedirs("/screenshots/Error_screenshots")

        # self.chose_post()
    def chose_post(self, post_num=None):
        if os.path.exists('Finish_following_posts.json'):
            with open('Finish_following_posts.json', 'r') as file:
                finished_following_post = json.load(file)

        if post_num is None:
            post_num = self.PostNum

        hu.HumanLikeMove(800, 782)
        hu.HumanLikeClick()
        time.sleep(1)

        if self.PostNum != 1:
            for _ in range(1, self.PostNum-1):
                while True:
                    url = copyurlUrl()
                    if url is not finished_following_post:
                        py.press('Right')
                        time.sleep(random.uniform(0.5, 0.8))

        time.sleep(random.uniform(0.5, 0.8))
        py.press('f5')
        time.sleep(2)

    def openfollowingpage(self):
        Locations = []

        Others = find_images(r'Images\others.png',
                             region_coefficients=[1, 1/2, "right", ""])
        likes_buttom = find_images(r'Images\likes.png',
                                   region_coefficients=[1, 1/2, "right", ""])

        if Others is not None:
            hu.HumanLikeMove(Others[0][0], Others[0][1])
            py.click()
            time.sleep(1)
        elif likes_buttom is not None:
            hu.HumanLikeMove(likes_buttom[0][0], likes_buttom[0][1])
            py.click()
            time.sleep(1)

        # Retry validity check up to 3 times
        for _ in range(3):
            if self.validity() == 0:
                break  # Page is detected, no need to retry
            time.sleep(3)  # Wait for the page to possibly load

        # Final check after all attempts
        if self.validity() == 0:
            app_logger.error(
                'Cannot detect the following page after multiple attempts.')
            # Take a screenshot for debugging

            self.screenshoterror("LikesAndOthers_error")
        else:

            like_bottom_location = find_images(
                r'Images\like_button.png',
                region_coefficients=[1, 1/2, "right", ""])

            if like_bottom_location != None:
                Locations.append((like_bottom_location[0][0],
                                  like_bottom_location[0][1]))
            else:
                app_logger.info('Like buttom cannot be detected')
                self.screenshoterror("like_button_error")

            comment_bottom_location = find_images(
                r'Images\Comment_button.png',
                region_coefficients=[1, 1/2, "right", ""])
            print(comment_bottom_location)

            if comment_bottom_location != None:
                Locations.append((comment_bottom_location[0][0],
                                  comment_bottom_location[0][1]))
                app_logger.info('comment buttom cannot be detected')
                self.screenshoterror("CommentButtomError")

            forward_bottom_location = find_images(
                r'Images\forward.png',
                region_coefficients=[1, 1/2, "right", ""])

            if forward_bottom_location != None:
                print(forward_bottom_location)
                Locations.append((forward_bottom_location[0][0],
                                  forward_bottom_location[0][1]))

                # app_logger.info('Forward buttom cannot be detected')
                self.screenshoterror("ForwardButtomError")

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
                    py.moveRel(0, 15, 0.3)
                    time.sleep(0.3)
                    py.click()
                    time.sleep(2)
                    if self.validity() == 1:
                        pass
                    else:
                        self.PostNum = self.PostNum+1
                        return
            app_logger.info('Cannot Recognize The following page.')
            print('Cannot Recognize The following page???')
            screenshot = ImageGrab.grab()  # Capture the specified region
            random_filename = generate_filename_with_timestamp()
            screenshot.save("canotseethepost_"+random_filename)
            return

    def validity(self):
        V = find_images('images/followingValidity.png')
        if V != None:
            return 1
        else:
            return 0

    def screenshoterror(self, name=''):
        screenshot = pyautogui.screenshot()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{name}{timestamp}.png"
        filepath = os.path.join(
            r'/screenshots/Error_screenshots', filename)


# page_opener = OpeningFollowingPage()
# page_opener.openfollowingpage()

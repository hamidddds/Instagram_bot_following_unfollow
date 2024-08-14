from Lib_Finding_image_on_screen import find_images
import random
import os
from Logger import app_logger
import lib_HumanMove as hu
import pyautogui as py
import time
import Logger
import datetime
import pyperclip
import pygetwindow as gw


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
        self.First_post_location = []
        self.Followed_temp = 0
        self.Followed = 0
        self.situation = 0
        self.finished_following_post = []
        self.likecommentfowrward_position = (650, 500, 600, 400)
        # 0 means unsucess
        # 1 means it is sucess
        self.PostNum = 1  # 0 means it doesnt need to change the post
        self.EndOfScroll = None
        # self.saved_following = []

        self.initialize()

    def initialize(self):
        pass

       # self.chose_post()

    def chose_post(self, post_num=None, Target="Page"):

        if Target == "Page":
            self.First_post_location = [
                432+random.randint(-20, 20), 840+random.randint(-20, 20)]
        elif Target == "Hashtag":
            self.First_post_location = (500+random.randint(-50, 50),
                                        520+random.randint(-50, 50))

        if post_num is None:
            post_num = self.PostNum

        hu.HumanLikeMove(self.First_post_location)
        hu.HumanLikeClick()
        # ??????????? validity?
        time.sleep(random.uniform(1, 2))

        if self.PostNum != 1:
            py.press('Right')
            for _ in range(1, self.PostNum-1):
                while True:
                    url = copyurlUrl()
                    if url is not self.finished_following_post:
                        return
                    else:
                        py.press('Right')

        time.sleep(random.uniform(0.6, 1))

    def openfollowingBox(self):

        self.validity()
        py.press('f5')
        time.sleep(random.uniform(2, 3))
        Locations = []

        Others = find_images(r'Images\others.png',
                             chrome_region=self.likecommentfowrward_position)
        likes_buttom = find_images(r'Images\likes.png',
                                   chrome_region=self.likecommentfowrward_position)

        if Others is not None:
            Locations = [Others[0][0], Others[0][1]]

        elif likes_buttom is not None:
            Locations = [likes_buttom[0][0], likes_buttom[0][1]]
        else:
            print("Likes and otehrs buttom are not found")

        if len(Locations) != 0:
            hu.HumanLikeMove(Locations)
            py.click()
            time.sleep(random.uniform(1, 2))
        else:
            Locations = None

        # Retry validity check up to 3 times
        for _ in range(3):
            if self.FollowingBox_validity() == 1:
                return 1  # Page is detected, no need to retry
            time.sleep(2)  # Wait for the page to possibly load

        # Final check after all attempts
        if self.FollowingBox_validity() == 0:
            app_logger.error(
                'Cannot detect the following page after multiple attempts.')

            print("Cannot detect the following page using others and likes")
            # Take a screenshot for debugging

            self.screenshoterror("LikesAndOthers_error",
                                 region=self.likecommentfowrward_position)

            self.PostNum = self.PostNum + 1

            app_logger.info('Cannot Recognize The following page.')
            print('Cannot Recognize The following page???')
            self.screenshoterror("canotseethepost_")
            return 0
        else:
            return 1

    def FollowingBox_validity(self):
        V = find_images('images/followingValidity.png')
        if V != None:
            return 1
        else:
            return 0

    def screenshoterror(self, name='', region=None):
        try:
            # Capture the screenshot
            if region:
                screenshot = py.screenshot(region=region)
            else:
                screenshot = py.screenshot()

            # Create a timestamp
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

            # Construct the filename
            filename = f"{name}{timestamp}.png"

            # Define the relative directory to save the screenshot
            directory = r'screenshots\Error_screenshots'

            # Ensure the directory exists
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Construct the full file path
            filepath = os.path.join(directory, filename)

            # Save the screenshot
            screenshot.save(filepath)

            print(f"Screenshot saved as: {filepath}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def validity(self):
        postpage = copyurlUrl()
        if 'instagram.com/p/' in postpage:
            time.sleep(2)
            print("following box is not oppened")
        else:
            return 0

# page_opener = OpeningFollowingPage()
# page_opener.openfollowingBox()


# like_bottom_location = find_images(
#     r'Images\like_button.png',
#     chrome_region=self.likecommentfowrward_position)

# if like_bottom_location != None:
#     Locations.append((like_bottom_location[0][0],
#                       like_bottom_location[0][1]))
# else:
#     app_logger.info('Like buttom cannot be detected')
#     print("Cannot detect the following page using Like buttom")
#     self.screenshoterror("like_button_error",
#                          region=self.likecommentfowrward_position)

# comment_bottom_location = find_images(
#     r'Images\Comment_button.png',
#     chrome_region=self.likecommentfowrward_position)
# print(comment_bottom_location)

# if comment_bottom_location != None:
#     Locations.append((comment_bottom_location[0][0],
#                       comment_bottom_location[0][1]))
# else:
#     app_logger.info('comment buttom cannot be detected')
#     print("Cannot detect the following page comment buttom")
#     self.screenshoterror("CommentButtomError",
#                          region=self.likecommentfowrward_position)

# forward_bottom_location = find_images(
#     r'Images\forward.png',
#     chrome_region=self.likecommentfowrward_position)

# if forward_bottom_location != None:
#     Locations.append((forward_bottom_location[0][0],
#                       forward_bottom_location[0][1]))
# else:

#     # app_logger.info('Forward buttom cannot be detected')
#     print("Cannot detect the following page forward buttom")
#     self.screenshoterror("ForwardButtomError",
#                          region=self.likecommentfowrward_position)

# if len(Locations) == 0:
#     app_logger.error('Following page is not detected')
#     self.screenshoterror("wrong page")
#     print("wrong Page")
#     return 0
# else:
#     for i in range(len(Locations)):
#         for j in range(i, len(Locations)):
#             location_coordinate = [(
#                 Locations[i][0] + Locations[j][0]) / 2, (Locations[i][1] + Locations[j][1]) / 2]
#             time.sleep(random.uniform(1, 1.5))
#             if isinstance(location_coordinate, list):
#                 location_coordinate = [
#                     int(x) for x in location_coordinate]
#             else:
#                 location_coordinate = int(location_coordinate)
#             hu.HumanLikeMove(
#                 location_coordinate)
#             time.sleep(0.4)
#             py.moveRel(0, 30, 0.3)
#             time.sleep(0.3)
#             py.click()
#             time.sleep(random.uniform(0.5, 1))
#             if self.FollowingBox_validity() == 1:
#                 return 1


import numpy as np
import cv2
import pyautogui as py
import time
import random
import pygetwindow as gw
from . import lib_HumanMove as hu
import random
import time
from .Lib_Finding_image_on_screen import find_images


class Liking_posts():
    def __init__(self, TimeIn) -> None:
        self.OutSide = (1100, 800)
        self.HomePagePos = (290, 300, 550, 620)
        self.Loading_page_logo_pos = (589, 510, 150, 150)
        self.NumberOfLikes = 0
        self.TimeIn = TimeIn

    def liking(self):

        hu.HumanLikeMove(self.OutSide)
        time1 = time.time()
        while time.time()-time1 < self.TimeIn:

            NowScroll = random.randint(-2000, -1000)
            self.scroll(NowScroll)  # 430 scroll kamele

            chance = random.randint(1, 3)
            if chance != 1:
                time.sleep(4)
                self.clickmore()
                WaitTime = random.randint(4, 5)
                hu.HumanLikeWait(WaitTime, 20, 20)

            WaitTime = random.randint(1, 2)
            time.sleep(WaitTime)
            likes_buttom = find_images(r'Images\like_button.png',
                                       chrome_region=self.HomePagePos)
            time.sleep(random.uniform(0.5, 0.6))
            # start following
            if likes_buttom != None:
                for pos in likes_buttom:
                    chance = random.randint(1, 3)
                    if chance != 3:
                        print(1)
                        hu.HumanLikeMove(
                            [pos[0] + random.randint(-2, 2), pos[1] + random.randint(-2, 2)])
                        time.sleep(random.uniform(0.5, 1))
                        hu.HumanLikeClick()
                        time.sleep(2)
                        hu.HumanLikeMove(self.OutSide)
                        time.sleep(1)

    def clickmore(self):
        More_link = find_images(r'Images\More.png',
                                chrome_region=self.HomePagePos)
        if More_link is not None:
            hu.HumanLikeMove([More_link[0][0] + random.randint(-2, 2),
                              More_link[0][1] + random.randint(-2, 2)])
            time.sleep(random.uniform(0.5, 1))
            hu.HumanLikeClick()
            time.sleep(1)
            hu.HumanLikeMove([1100+random.randint(-100, 100),
                             800+random.randint(-150, 150)])

    def scroll(self, x):
        RN = random.randint(3, 5)
        x1 = round(x/RN)
        x2 = x % RN

        py.scroll(x2)

        for _ in range(RN):

            Chance = random.randint(1, 4)
            if Chance == 1:
                scroll_fake = random.randint(200, 300)
                py.scroll(scroll_fake)
                time.sleep(random.uniform(4, 7))
                py.scroll(-scroll_fake+random.randint(0, 40))
                time.sleep(random.uniform(4, 7))

            py.scroll(x1 + random.randint(0, 15))
            time.sleep(random.uniform(0.2, 0.4))
            py.moveRel(random.randint(-3, 3), random.randint(-3, 3))
            time.sleep(random.uniform(0.7, 1.2))

    # def validity(self):
    #     hu.HumanLikeMove((1055, 31))
    #     More_link = find_images(r'Images\Loading_page_logo.png',
    #                             chrome_region=self.Loading_page_logo_pos)
    #     for i in range(1, 6):
    #         if More_link is not None:
    #             time.sleep(2)
    #         else:

    #             if self.IsPageEmpty() == "PageIsNotEmpty":
    #                 print("CanSeeTheHomePage")
    #                 return "CanSeeTheHomePage"
    #         if i == 6:
    #             print("CanNotSeeTheHomePage")
    #             return "CannotSeeHomePage"

    # def IsPageEmpty(self):
    #     region1 = (289, 151, 900, 50)
    #     region2 = (1149, 143, 50, 600)
    #     region3 = (1000, 333, 300, 300)
    #     is_empty1 = self.is_plain_color(region1)
    #     is_empty2 = self.is_plain_color(region2)
    #     is_empty3 = self.is_plain_color(region3)
    #     if is_empty1 == False or is_empty2 == False or is_empty3 == False:
    #         return "PageIsNotEmpty"
    #     else:
    #         return "PageIsEmpty"

    # def is_plain_color(self, region):
    #     # Take a screenshot of the specified region
    #     screenshot = py.screenshot(region=region)

    #     # Convert the screenshot to a NumPy array
    #     screenshot_np = np.array(screenshot)

    #     # Convert the image from RGB to BGR (as OpenCV uses BGR format)
    #     screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    #     # # Save the screenshot using OpenCV
    #     # cv2.imwrite("screenshot_region.png", screenshot_bgr)

    #     # Get the unique colors in the image
    #     unique_colors = np.unique(
    #         screenshot_bgr.reshape(-1, screenshot_bgr.shape[2]), axis=0)

    #     # Check if there's only one unique color in the image
    #     if len(unique_colors) == 1:
    #         return True  # The region is plain color
    #     else:
    #         return False  # The region has something inside


# time.sleep(1)


# if __name__ == "__main__":
#     a = Liking_posts()
#     a.HomePage()
#     while (True):
#         a.liking(50)

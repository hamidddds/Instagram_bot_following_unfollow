import os
import tkinter as tk
import win32con
import ctypes
import threading
import time
import pygetwindow as gw
import pyautogui
import pyperclip
import time
import pyautogui
import pygetwindow as gw
import datetime
from pyclick import HumanClicker, HumanCurve
import math
from timeit import default_timer as timer
from random import random
import pyautogui as py
import time
import random
from random import randrange
import subprocess
from PIL import Image, ImageGrab
import chime
from datetime import date
import tkinter as t
from tkinter import ttk
import pyperclip
import sys
chime.theme('zelda')


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Rest of your code


def ChangeTheProcessBar(Text):
    global NewProcess
    global root
    NewProcess.pack_forget()
    NewProcess = t.Label(root, text=Text)
    NewProcess.pack()
    root.update()
    time.sleep(1)


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


class PageInformation:
    def __init__(self, nameofpage):
        self.name = nameofpage
        # self.pageinf = {"Hfolloing": Hfolloing}
        time.sleep(2)

    def get_page_info(self):
        return self.pageinf


def HumanLikeKeyboard(word):
    time.sleep(1)
    i = 0
    for _ in range(len(word)):
        b = random.uniform(0.09, 0.3)
        time.sleep(b)
        py.write(word[i])
        i += 1


# class ErrorManager:
#     def __init__(self) -> None:
#         self.slide = 0
#         self.emore = 0
#         self.Csmilyface = 0
#         self.ereply = 0
#         self.my_dict = {}
#         self.efollowin = 0

#     def Slide(self):
#         self.slide += 1
#         nowtime = datetime.datetime.now()
#         self.my_dict['Sliding'] = nowtime

#     def EMore(self):  # cannot find more buttom
#         self.emore += 1
#         nowtime = datetime.datetime.now()
#         self.my_dict['More'] = nowtime

#     def Smilyface(self):
#         nowtime = datetime.datetime.now()
#         self.my_dict['smilyface'] = nowtime
#         self.Csmilyface += 1

#     def Ereply(self):
#         nowtime = datetime.datetime.now()
#         self.my_dict['reply'] = nowtime
#         self.ereply += 1

#     def EFollowin(self):
#         nowtime = datetime.datetime.now()
#         self.my_dict['EFollowin'] = nowtime
#         self.efollowin += 1


# class Counter:
#     def __init__(self) -> None:
#         self.coments, self.replay = 0
#         self.targetpage, self.likestory, self.likepost, self.likecoments = 0

#     def likesCounts(self, like):
#         if like == "story":
#             self.likestory += 1
#         elif like == "post":
#             self.likepost += 1
#         elif like == "coments":
#             self.likecoments += 1

#     def ComentCount(self, coment):
#         if coment == "post":
#             self.coments += 1
#         elif coment == "replay":
#             self.replay = +1

#     def Targetpage(self, targetpage):
#         if targetpage == "targetpage":
#             self.targetpage += 1
#         elif targetpage == "targetpage":
#             self.targetpage = +1


class validity():
    def __init__(self) -> None:
        pass

    def copyurlUrl(self):
        # Find the active Chrome window
        chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]

        # Bring Chrome window to the front
        chrome_window.activate()

        # Send Alt+D to focus the address bar
        pyautogui.hotkey('alt', 'd')

        # Wait for a short time to ensure the address bar is focused
        time.sleep(0.5)

        # Send Ctrl+C to copy the URL to clipboard
        pyautogui.hotkey('ctrl', 'c')

        # Get the URL from the clipboard
        url = pyperclip.paste()
        start_pos = url.find("https://") + len("https://")
        end_pos = url.find(".com")

        # Extract the substring between "https://" and ".com"
        extracted_part = url[start_pos:end_pos]

        url = extracted_part
        return url

    def Checkpage(self, nameofwebsite):
        url = self.copyurlUrl()
        if url == nameofwebsite:
            print('The pages seems to eb okay')
            return True
        else:
            return False
        # ChangeTheProcessBar('Checking validity of Target page')


def EnterUrl(Nameurl):
    ChangeTheProcessBar('salam')
    s = MouseMovements()
    s.HMove(593+random.randint(-10, 10), 54)
    time.sleep(random.uniform(0.5, 0.8))
    s.HClick()
    with py.hold('ctrl'):
        py.press(['a'])
    time.sleep(random.uniform(0.5, 0.8))
    py.press('Backspace')
    HumanLikeKeyboard(Nameurl)
    time.sleep(random.uniform(0.5, 0.8))
    py.press('Enter')
    time.sleep(8)


class MouseMovements:
    def __init__(self) -> None:
        self.x, self.y = py.position()

    def update(self) -> None:
        self.x, self.y = py.position()

    def MoveF(self, Move_x, Move_y, t):

        fromPoint = py.position()
        options = {
            "knotsCount": 2,
        }
        human_curve = HumanCurve(
            fromPoint=fromPoint, toPoint=(Move_x, Move_y), **options)

        hc = HumanClicker()
        # move the mouse to position (100,100) on the screen in approximately 2 seconds
        hc.move((Move_x, Move_y), t, humanCurve=human_curve)
        self.update()

    def HMove(self, Move_x, Move_y) -> None:

        distance = math.sqrt(pow((self.x-Move_x), 2) + pow((self.y-Move_y), 2))
    # 2140 total
        if distance <= 150:
            self.MoveF(Move_x, Move_y, random.uniform(0.7, 1.1))
        elif 150 < distance <= 300:
            self.MoveF(Move_x, Move_y, random.uniform(1.3, 1.6))
        elif 300 < distance <= 700:
            self.MoveF(Move_x, Move_y, random.uniform(1.6, 2.1))
        else:
            self.MoveF(Move_x, Move_y, random.uniform(2.5, 3))
        self.update()

    def HClick(self) -> None:
        py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
        time.sleep(0.1)
        py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
        time.sleep(0.1)
        py.click()
        py.moveRel(random.randint(-2, 2), random.randint(-2, 2), 0.25)
        time.sleep(0.1)
        self.update()

    def Hscroll(self, x) -> None:
        RN = random.randint(1, 3)
        x1 = round(x/RN)
        x2 = x % RN
        py.scroll(x2)
        for _ in range(RN):
            time.sleep(random.uniform(0.7, 1.2))
            py.scroll(x1)
        self.update()


class insidetargetpage(MouseMovements):
    def __init__(self) -> None:
        self.followed=0
        pass

    def ChoosePost(postNum):
        MouseMovements.HMove(800, 782)
        MouseMovements.HClick()
        time.sleep(1)
        for _ in range(postNum):
            time.sleep(random.uniform(0.5, 0.8))
            py.press('Right')
    ########################################################################

    def FollowingPost(self, RemainedFollowed):  # return0 means it fails #end
        # ChangeTheProcessBar('Initiating Following people...')
        Followed = 0
        FlagEndOfPost = 0
        EndOfScroll = None  # ?
        LikeButtomLocation = py.locateOnScreen('images/like_button.png',
                                               region=(700, 800, 600, 400), confidence=0.8)

        if LikeButtomLocation == None:
            # ChangeTheProcessBar('Cannot Recognize The Target Post Page???')
            print('Cannot Recognize The Target Post Page???')
            EnterUrl('www.instagram.com')
            self.error.EFollowin()
            return Followed, 0, FlagEndOfPost
        else:  # start following
            # 6 is number of indivituals in each page
            time.sleep(0.8)
            OpenFollowing = py.locateCenterOnScreen('images/LikeAndCommentShape.png',
                                                    region=(950, 700, 650, 200), confidence=0.7)
            MouseMovements.HMove(OpenFollowing[0], OpenFollowing[1])
            time.sleep(0.8)
            py.moveRel(0, 40, 0.5)
            time.sleep(0.4)
            py.click()
            time.sleep(2)
            # Others = py.locateCenterOnScreen('images/others.png',
            # region=(1000, 800, 600, 200), confidence=0.7)
            # if Others != None and validity.FollowingV() != True:
            #     MouseMovements.HMove(Others[0], Others[1])
            #     py.click()
            #     time.sleep(1)

            # if validity.FollowingV() != True:
            #     # ChangeTheProcessBar('Cannot Recognize The following???')
            #     EnterUrl('www.instagram.com')
            #     return Followed, 'NotDone', FlagEndOfPost
            while Followed < RemainedFollowed:
                time.sleep(0.5)
                FollowButtom = list(py.locateAllOnScreen(
                    'images/FollowButtom.png', region=(700, 300, 500, 500), confidence=0.9))
                time.sleep(random.uniform(0.5, 0.9))
                # start following

                if FollowButtom != None:
                    # ChangeTheProcessBar('Following...')
                    for pos in FollowButtom:
                        C = random.randint(1, 7)
                        if C != 5:
                            pos = py.center(pos)
                            MouseMovements.HMove(pos[0]+random.randint(-15, 15),
                                                 pos[1]+random.randint(-8, 8))
                            time.sleep(random.uniform(0.8, 1))
                            # chime.success()
                            py.click()
                            time.sleep(random.uniform(1.4, 1.8))
                            Followed += 1
                            if Followed >= RemainedFollowed:
                                return Followed, 'Done', FlagEndOfPost
                MouseMovements.HMove(1700+random.randint(-40, 40),
                                     500+random.randint(-20, 20))
                time.sleep(random.uniform(0.8, 1.2))

                im = ImageGrab.grab(bbox=(765, 377, 1130, 755))

                time.sleep(random.uniform(0.8, 1.2))
                MouseMovements.HMove(1000+random.randint(-10, 10),
                                     550+random.randint(-20, 20),)

                time.sleep(random.uniform(0.8, 1.2))
                NowScroll = random.randint(-500, -300)
                MouseMovements.Hscroll(NowScroll)  # 430 scroll kamele

                time.sleep(random.uniform(0.8, 1.2))
                MouseMovements.Hscroll(1700+random.randint(-40, 40),
                                       500+random.randint(-20, 20))

                time.sleep(random.uniform(0.8, 1))
                EndOfScroll = py.locateOnScreen(im, confidence=0.9)

                if EndOfScroll != None:
                    FlagEndOfPost = 1
                    print('End of scroll,lets go to the next post!')
                    # ChangeTheProcessBar(
                    #     'End of scroll,lets go to the next post!')
                    return (Followed, 'Done', FlagEndOfPost)

        py.press("Esc")
        time.sleep(0.2)
        py.press("Esc")
        time.sleep(0.3)
        return (Followed, 'Done', FlagEndOfPost)


if __name__ == "__main__":
    global root
    clear_terminal()
    ProcessBar()
    ChangeTheProcessBar('Cannot Open Following page')

    H_NumberOfFollow = 10
    

    Target1 = PageInformation("mode___rooz")
    instagram = "www.instagram.com"
    TargetPage = "www.instagram.com/"+Target1.name+"/"
    EnterUrl("www.instagram.com")
    followed=0
    while followed < H_NumberOfFollow:
        
    # following
    # opentargetpage
    # page_info = PageInformation(TargetPage)
    # Target = insidetargetpage(postnum)
    # while _follow < NumberOfFOllow:
    #     if FlagEndOfPost == 1:
    #         postnum += 1
    #         Target.ChoosePost(postnum)

    #     cc = NumberOfFOllow - followed_page
    #     followed, followSituation, FlagEndOfPost = insidetargetpage.FollowingPost(
    #         cc)
    # if i == 4:
    #     time.sleep(4)
    #     print('Cannot open following page')
    #     sys.exit()
    # i += 1
    # followed_page = followed + followed_page
    # T = T + followed_page  # total number of follows
    # print("Total Number of followed page is/hour=", T)

    #     FollowFlag = 0
    #     tt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     print('Followed finished at: %s' % tt)
    #     print('Number of followed page hourly: %d' % followed_page)
    #     homebuttom()
    #     _follow+= 1
    # pass

    # OpenTargetpage(page_info)

    # def Post():
    #     ChangeTheProcessBar('Checking validity Of Opened Post')
    #     time.sleep(1)
    #     Homepagevalidity = py.locateCenterOnScreen(
    #         'images/Smaily_face_shape.png', region=(800, 750, 800, 300), confidence=0.8)
    #     if Homepagevalidity == None:
    #         ChangeTheProcessBar('Cannot See the Post')
    #         time.sleep(1)
    #         return False
    #     else:
    #         return True

    # def FollowingV():
    #     ChangeTheProcessBar('Cheking Validity of following...')
    #     time.sleep(1)
    #     Homepagevalidity = py.locateCenterOnScreen(
    #         'images/followingValidity.png', region=(700, 300, 500, 500), confidence=0.9)
    #     if Homepagevalidity == None:
    #         ChangeTheProcessBar('Cannot See The Target Page to follow :(')
    #         time.sleep(1)
    #         return False
    #     else:
    #         return True

    # def StoryV():
    #     ChangeTheProcessBar('Cheking Validity of Story page...')
    #     time.sleep(1)
    #     Homepagevalidity = py.locateCenterOnScreen(
    #         'images/validityStory.png', region=(1700, 95, 220, 80), confidence=0.9)
    #     if Homepagevalidity == None:
    #         ChangeTheProcessBar('Cannot See the Story page????')
    #         time.sleep(1)
    #         return False
    #     else:
    #         return True


# Get the URL of the active tab in Chrome

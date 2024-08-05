from pyscreeze import ImageNotFoundException
import lib_HumanMove as hu
import pyautogui as py
import random
import time
import json
from PIL import ImageGrab  # Required for screen capture
import pyperclip  # Required for clipboard operations
import os
import platform
import pygetwindow as gw
import winsound
import platform
import lib_OpenFollowinPage as openpage


def locateOnScreen(image_path, region=None, confidence=0.7):
    try:
        return py.locateOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


def locateAllOnScreen(image_path, region=None, confidence=0.7):
    try:
        return list(py.locateAllOnScreen(image_path, region=region, confidence=confidence))
    except ImageNotFoundException:
        return []


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
    # start_pos = url.find("https://") + len("https://")
    # end_pos = url.find(".com")

    # # Extract the substring between "https://" and ".com"
    # extracted_part = url[start_pos:end_pos]

    # url = extracted_part
    return url


class Following:
    def __init__(self, RemainedFollowed) -> None:
        self.Followed_temp = 0
        self.Followed = 0
        self.situation = 0
        self.PostBox = (650, 130, 950, 700)
        self.FollowingBox = (700, 350, 600, 450)
        self.followingpage = (850, 127, 500, 200)
        # the box coordinates
        self.bbox = (700, 350, 1200, 800)
        # 0 means it is under process

        # 1 means it is over
        # 3 cannot open followers page
        # 4 end of post
        # 10 means it is ended
        self.PostNum = 1  # 0 means it doesnt need to change the post
        self.EndOfScroll = None
        self.Following_Number = RemainedFollowed
        # self.saved_following = []

        self.initialize()

    def initialize(self):
        if os.path.exists('my_list.json'):
            with open('my_list.json', 'r') as file:
                self.saved_following = json.load(file)
        else:
            self.saved_following = []
        print('Follower list has oppened ...')
        print('Starting Following ...')

    def Finding_follow_buttom(self):

        check = self.CheckValidity()
        if check == 0:
            return

        hu.HumanLikeMove(510+random.randint(-10, 10),
                         400+random.randint(-20, 20),)
        while True:
            time.sleep(random.uniform(0.8, 1))
            FollowButtom = list(locateAllOnScreen(
                r'Main\Images\followbutton2.png', region=self.FollowingBox, confidence=0.9))
            time.sleep(random.uniform(0.5, 0.6))
            # start following

            if len(FollowButtom) != None:
                for pos in FollowButtom:
                    pos = py.center(pos)
                    py.moveTo(py.position()[
                        0], pos[1] + random.randint(-8, 8)-5, duration=random.uniform(0.4, 0.5))
                    # First, move to the x-axis position
                    py.moveTo(pos[0] - 240 + random.randint(-15, 15),
                              py.position()[1], duration=random.uniform(0.4, 0.5))

                    # Then, move to the y-axis position

                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.3, 0.5))
                    py.moveRel(0, -10, 0.3)
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.3, 0.5))
                    py.moveRel(-150, 0, 0.6)
                # ceheck the following is over or not
                if self.Open_pages() == 1:
                    print("Done with following")
                    return
                FollowButtom = []
            time.sleep(1)
            # scroll
            im = ImageGrab.grab(self.bbox)
            # im.save('endofthepost_image__before.jpg')
            time.sleep(random.uniform(0.8, 1.2))
            hu.HumanLikeMove(1000+random.randint(-10, 10),
                             550+random.randint(-20, 20),)
            time.sleep(random.uniform(0.8, 1.2))
            NowScroll = random.randint(-500, -300)
            hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
            time.sleep(random.uniform(0.8, 1.2))
            # im1 = ImageGrab.grab(self.bbox)
            # im1.save('endofthepost_image__after.jpg')
            EndOfScroll = locateOnScreen(im, confidence=0.9)

            if EndOfScroll != None:
                print('End of scroll,lets go to the next post!')
                self.PostNum = self.PostNum+1
                # im1.save('endofthepost_image__after.jpg')
                return

    def Open_pages(self):
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
                with open('my_list.json', 'w') as file:
                    json.dump(self.saved_following, file)
                return 0
            else:
                if username in self.saved_following:
                    time.sleep(random.uniform(0.4, 0.8))
                    py.hotkey('ctrl', 'w')
                else:
                    self.saved_following.append(username)
                    time.sleep(random.uniform(0.5, 0.7))
                    FollowButtom = locateOnScreen(
                        r'Main\Images\followbutton2.png', region=self.PostBox, confidence=0.8)
                    time.sleep(random.uniform(0.5, 0.9))
                    # start following

                    if FollowButtom:
                        print('Following...')
                        hu.HumanLikeMove(FollowButtom[0]+random.randint(25, 35),
                                         FollowButtom[1]+random.randint(10, 15))
                        time.sleep(random.uniform(0.8, 1))
                        # py.click()
                        winsound.Beep(1000, 200)
                        time.sleep(random.uniform(1, 1.4))

                        self.Followed += 1

                        if self.Followed >= self.Following_Number:
                            while True:
                                time.sleep(random.uniform(0.5, 0.7))
                                Name_Of_page = copyurlUrl()
                                time.sleep(random.uniform(0.5, 0.7))
                                if Homepage == Name_Of_page:
                                    with open('my_list.json', 'w') as file:
                                        json.dump(self.saved_following, file)
                                        self.situation = 10
                                        return 1
                                else:
                                    py.hotkey('ctrl', 'w')
                        time.sleep(random.uniform(0.4, 0.8))
                        py.hotkey('ctrl', 'w')
                        time.sleep(random.uniform(0.4, 0.8))

    def CheckValidity(self):
        Flag = 0
        Loop_count = 0
        Situation = "okay"
        time.sleep(random.uniform(0.7, 1))
        Like_image = locateOnScreen(
            r'Main\Images\Validity_following\FollowingPage_LIkeButtom.png', region=self.FollowingBox, confidence=0.8)
        # start following
        if Like_image:
            while Flag != 1:
                Following_image = locateOnScreen(
                    r'Main\Images\Validity_following\Following_buttom.png', region=self.FollowingBox, confidence=0.8)
                Follow_Butt = locateOnScreen(
                    r'Main\Images\Validity_following\Follow_buttom.png', region=self.FollowingBox, confidence=0.8)
                Request_Butt = locateOnScreen(
                    r'Main\Images\Validity_following\requested_Buttom.png', region=self.FollowingBox, confidence=0.8)

                if Following_image is None and Follow_Butt is None and Request_Butt is None:
                    print("Cannot see the page")
                    time.sleep(3)
                    Loop_count = Loop_count+1
                    if Loop_count != 3:
                        Flag = 1
                        Situation = "CannotSeeTheButtoms"
                        print("cannot see the buttoms")
                else:
                    Flag = 1
                    print('done')
                    return 1
        else:
            a = openpage.OpeningFollowingPage()
            a.openfollowingpage()
            print('Not done')
            return 0


# time.sleep(1)
# clear_terminal()

# folowp = Following(5)
# # folowp.CheckValidity()
# folowp.Finding_follow_buttom()

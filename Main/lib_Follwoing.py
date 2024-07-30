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


def locateOnScreen(image_path, region=None, confidence=0.7):
    try:
        return py.locateOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


def locateAllOnScreen(image_path, region=None, confidence=0.7):
    try:
        return py.locateAllOnScreen(image_path, region=region, confidence=confidence)
    except py.ImageNotFoundException:
        return None


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
        print("10")
        while True:
            time.sleep(random.uniform(0.8, 1))
            print("11")
            FollowButtom = list(locateAllOnScreen(
                'images/FollowButtom.png', region=(700, 300, 500, 500), confidence=0.9))
            print("12")
            time.sleep(random.uniform(0.5, 0.9))
            # start following

            if len(FollowButtom) != None:
                for pos in FollowButtom:
                    pos = py.center(pos)
                    hu.HumanLikeMove(pos[0]+random.randint(-15, 15)-240,
                                     pos[1]+random.randint(-8, 8))
                    time.sleep(random.uniform(0.8, 1))
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.5, 0.7))
                    py.moveRel(0, -10, 0.3)
                    with py.hold('ctrl'):
                        py.click()
                    time.sleep(random.uniform(0.8, 1))
                    py.moveRel(-150, 0, 0.6)
                    time.sleep(random.uniform(0.8, 1))
                # ceheck the following is over or not
                if self.Open_pages() == 1:
                    print("222")
                    return

            time.sleep(2)
            # scroll
            im = ImageGrab.grab(bbox=(765, 377, 1130, 755))
            # im.save('endofthepost_image__before.jpg')

            time.sleep(random.uniform(0.8, 1.2))
            print("1")
            hu.HumanLikeMove(1000+random.randint(-10, 10),
                             550+random.randint(-20, 20),)
            print("2")
            time.sleep(random.uniform(0.8, 1.2))
            print("3")
            NowScroll = random.randint(-500, -300)
            print("4")
            hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
            print("5")
            time.sleep(random.uniform(0.8, 1.2))
            print("6")
            im1 = ImageGrab.grab(bbox=(765, 377, 1130, 755))
            print("7")
            im1.save('endofthepost_image__after.jpg')
            print("8")
            EndOfScroll = locateOnScreen(im, confidence=0.9)
            print("9")

            if EndOfScroll != None:
                print('End of scroll,lets go to the next post!')
                # im1.save('endofthepost_image__after.jpg')
                self.situation = 4
                return self.Followed, self.situation

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
            time.sleep(random.uniform(0.5, 0.7))
            Name_Of_page = copyurlUrl()
            time.sleep(random.uniform(0.5, 0.7))
            print(Name_Of_page)
            #
            username = Name_Of_page.split("www.instagram.com/")[-1].rstrip('/')
            # print(username)
            # print(self.saved_following)
            if Homepage == Name_Of_page:
                with open('my_list.json', 'w') as file:
                    json.dump(self.saved_following, file)
                return
            else:
                if username in self.saved_following:
                    time.sleep(random.uniform(0.4, 0.8))
                    py.hotkey('ctrl', 'w')
                else:
                    self.saved_following.append(username)
                    time.sleep(random.uniform(0.5, 0.7))
                    FollowButtom = locateOnScreen(
                        'images/followbutton2.png', region=(650, 100, 800, 150), confidence=0.8)
                    time.sleep(random.uniform(0.5, 0.9))
                    # start following

                    if FollowButtom:
                        print('Following...')
                        hu.HumanLikeMove(FollowButtom[0]+random.randint(25, 35),
                                         FollowButtom[1]+random.randint(10, 15))
                        time.sleep(random.uniform(0.8, 1))
                        py.click()
                        # winsound.Beep(1000, 200)
                        time.sleep(random.uniform(1, 1.4))

                        self.Followed += 1
                        print(self.Followed)
                        print(self.Following_Number)

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


# time.sleep(1)
# clear_terminal()
# folowp = Following(5)

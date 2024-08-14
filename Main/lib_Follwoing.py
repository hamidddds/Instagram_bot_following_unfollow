from PIL import ImageGrab, ImageChops
from datetime import datetime
import lib_HumanMove as hu
import pyautogui as py
import random
import time
import json
import pyperclip  # Required for clipboard operations
import os
import platform
import pygetwindow as gw
import winsound
import lib_OpenFollowinPage as openpage
from Lib_Finding_image_on_screen import find_images


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
        self.Followed = 0
        self.situation = 0
        # self.bbox = self.convertor()
        self.Following_box = (330, 330, 600, 600)

        self.inside_box_pos = (790+random.randint(-10, 10),
                               601+random.randint(-30, -30))

        self.outside_box_pos = (350+random.randint(-10, 10),
                                450+random.randint(-30, -30))

        # 0 means it is under process
        self.im = None
        self.PostNum = 1  # 0 means it doesnt need to change the post
        self.Following_Number = RemainedFollowed
        # self.saved_following = []

        self.initialize()

    def initialize(self):

        if os.path.exists('my_list.json'):
            with open('my_list.json', 'r') as file:
                self.saved_following = json.load(file)
        else:
            self.saved_following = []

        if os.path.exists('Finish_following_posts.json'):
            with open('Finish_following_posts.json', 'r') as file:
                self.finished_following_post = json.load(file)
        else:
            self.finished_following_post = []

        print('Follower list has oppened ...')
        print('Starting Following ...')

    def Finding_follow_buttom(self):

        check = self.CheckValidity()

        if check == 0:
            print("cannot see the following box")
            return 0

        first_iteration = True

        while True:

            if not first_iteration:
                hu.HumanLikeMove(self.inside_box_pos)
                NowScroll = random.randint(-500, -400)
                hu.Humanlikescroll(NowScroll)  # 430 scroll kamele

            first_iteration = False

            a = self.scoroll()
            # move out of box
            hu.HumanLikeMove(self.outside_box_pos)

            if a == 0:  # end of the scroll
                self.PostNum = self.PostNum+1
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
                openeningPages = self.Open_pages()
                if openeningPages == 1:
                    print("Done with following")
                    return 1

                self.im = ImageGrab.grab(self.Following_box)
                # ????

                hu.HumanLikeMove(self.inside_box_pos)
                NowScroll = random.randint(-500, -400)
                hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
                time.sleep(0.5)
                hu.HumanLikeMove(self.outside_box_pos)
                time.sleep(0.5)
                end_scroll = self.EndOfScroll()

                if end_scroll == 1:
                    self.finished_following_post.append(copyurlUrl())

                    with open('finished_following_post.json', 'w') as file:
                        json.dump(self.finished_following_post, file)

                    return 0  # end of scroll

                FollowButtom = []

    def scoroll(self):
        # returning 0 means that we need to go to the next post

        hu.HumanLikeMove(self.inside_box_pos)
        x, y = py.position()

        for _ in range(20):

            # if the cursor move a long disntace

            x1, y1 = py.position()
            if abs(x1-x) > 21 or abs(y1-y) > 21:
                hu.HumanLikeMove([x, y])

            Following_image = []

            Following_image = find_images(
                r'Images\Validity_following\Follow_buttom.png')

            if Following_image == None or len(Following_image) < 3:
                print(self.Following_box)
                self.im = ImageGrab.grab(self.Following_box)
                NowScroll = random.randint(-500, -400)
                hu.Humanlikescroll(NowScroll)  # 430 scroll kamele
                time.sleep(random.uniform(0.5, 0.8))
                end_scroll = self.EndOfScroll()

                if end_scroll == 1:
                    self.finished_following_post.append(copyurlUrl())

                    with open('finished_following_post.json', 'w') as file:
                        json.dump(self.finished_following_post, file)

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
                        time.sleep(random.uniform(1, 1.4))

                        self.Followed += 1
                        print("followed")

                        if self.Followed >= self.Following_Number:
                            while True:
                                time.sleep(random.uniform(0.5, 0.7))
                                Name_Of_page = copyurlUrl()
                                time.sleep(random.uniform(0.5, 0.7))
                                if Homepage == Name_Of_page:
                                    with open('my_list.json', 'w') as file:
                                        json.dump(self.saved_following, file)
                                        self.situation = 10
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
